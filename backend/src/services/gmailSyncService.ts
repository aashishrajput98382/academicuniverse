import { google } from 'googleapis';
import User from '../models/User';
import { getOAuth2Client, getStoredGmailTokens, refreshAccessToken } from './gmailAuthService';
import { firebaseFirestore } from '../config/firebaseAdmin';

const TARGET_KEYWORDS = [
    'hackathon', 'coding competition', 'tech event', 'workshop',
    'bootcamp', 'seminar', 'developer meetup', 'tech fest',
    'exam', 'examination', 'mid-semester', 'end-semester', 'quiz', 'assessment'
];

const SPAM_KEYWORDS = [
    'sale', 'discount', 'amazon', 'bank', 'otp', 'shopping',
    'promotion', 'newsletter'
];

export const syncGmailEvents = async (userId: string, fallbackFirebaseUid?: string) => {
    console.log("[GMAIL_SYNC_TRACE] Starting sync for mongo userId:", userId);

    let user = await User.findById(userId);
    if (!user) {
        console.log("[GMAIL_SYNC_TRACE] User not found!");
        throw new Error('User not found');
    }

    const targetFirebaseUid = user.firebaseUid || fallbackFirebaseUid || String(userId);
    console.log("[GMAIL_SYNC_TRACE] Found user, firebaseUid:", user.firebaseUid, "targetFirebaseUid:", targetFirebaseUid);

    // If user document didn't have firebaseUid but we have one from token, persist it
    if (!user.firebaseUid && targetFirebaseUid && targetFirebaseUid !== String(userId)) {
        try {
            user.firebaseUid = targetFirebaseUid;
            await user.save();
        } catch (saveUidErr) {
            console.warn('[GMAIL_SYNC] Could not persist firebaseUid to user:', saveUidErr);
        }
    }

    if (!user.gmailTokens) {
        console.log("[GMAIL_SYNC_TRACE] Gmail not connected!");
        throw new Error('Gmail account not connected');
    }

    const storedTokens = await getStoredGmailTokens(userId);

    // Check if token is expired or about to expire (5 minutes buffer)
    const now = Date.now();
    const isExpired = !storedTokens.expiryDate || storedTokens.expiryDate < now + 5 * 60 * 1000;

    if (isExpired) {
        console.log("[GMAIL_SYNC_TRACE] Refreshing expired Gmail token...");
        try {
            await refreshAccessToken(userId);
            // Refresh user object from DB to get new tokens
            user = await User.findById(userId);
            if (!user) throw new Error('User not found after token refresh');
            if (!user.gmailTokens) throw new Error('Gmail tokens missing after refresh');
        } catch (refreshError) {
            // If refresh fails, clear invalid tokens and throw error
            const currentUser = await User.findById(userId);
            if (currentUser) {
                currentUser.gmailTokens = undefined;
                await currentUser.save();
            }
            throw new Error('Gmail connection expired. Please reconnect your Gmail account.');
        }
    }

    // Ensure we have tokens
    const resolvedTokens = await getStoredGmailTokens(userId);

    const oauth2Client = getOAuth2Client();
    oauth2Client.setCredentials({
        access_token: resolvedTokens.accessToken,
        refresh_token: resolvedTokens.refreshToken,
        expiry_date: resolvedTokens.expiryDate,
    });

    const gmail = google.gmail({ version: 'v1', auth: oauth2Client });

    // Fetch latest 50 emails that might be related to events or exams
    const gmailQuery = 'hackathon OR "coding competition" OR "tech event" OR workshop OR bootcamp OR seminar OR "developer meetup" OR "tech fest" OR exam OR examination OR "mid-semester" OR "end-semester" OR quiz';
    console.log("[GMAIL_SYNC_TRACE] Calling Gmail API with query:", gmailQuery);
    console.log("[GMAIL_SYNC_TRACE] Gmail API params: maxResults=50");

    let response;
    try {
        response = await gmail.users.messages.list({
            userId: 'me',
            maxResults: 50,
            q: gmailQuery,
        });
    } catch (listErr: any) {
        console.error('[GMAIL_SYNC_TRACE] Failed to list messages from Gmail API:', listErr);
        const errMsg = listErr?.message || '';
        if (
            errMsg.includes('invalid_grant') || 
            errMsg.includes('Invalid Credentials') || 
            errMsg.includes('unauthorized') || 
            errMsg.includes('Insufficient Permission')
        ) {
            throw new Error('Gmail authorization expired or missing permissions. Please reconnect your Gmail account.');
        }
        throw new Error(`Gmail API error: ${errMsg || 'Failed to list messages'}`);
    }

    const messages = response.data.messages || [];
    console.log("[GMAIL_SYNC_TRACE] Gmail API returned", messages.length, "messages");
    console.log("[GMAIL_SYNC_TRACE] Next page token exists:", !!response.data.nextPageToken);

    let newEventsCount = 0;
    let processedCount = 0;
    let duplicateCount = 0;
    let spamCount = 0;
    let notEventCount = 0;

    for (const message of messages) {
        processedCount++;
        if (!message.id) continue;

        try {
            console.log("[GMAIL_SYNC_TRACE] Processing message ID:", message.id);
            const msgData = await gmail.users.messages.get({
                userId: 'me',
                id: message.id,
                format: 'full',
            });

            const headers = msgData.data.payload?.headers || [];
            const subjectHeader = headers.find(h => h.name?.toLowerCase() === 'subject');
            const fromHeader = headers.find(h => h.name?.toLowerCase() === 'from');
            const dateHeader = headers.find(h => h.name?.toLowerCase() === 'date');
            const internalDate = msgData.data.internalDate;

            const subject = subjectHeader?.value || '';
            const from = fromHeader?.value || 'Unknown Organizer';

            let emailDateIso = new Date().toISOString();
            try {
                if (dateHeader?.value) {
                    const parsed = new Date(dateHeader.value);
                    if (!isNaN(parsed.getTime())) {
                        emailDateIso = parsed.toISOString();
                    }
                } else if (internalDate) {
                    const parsed = new Date(Number(internalDate));
                    if (!isNaN(parsed.getTime())) {
                        emailDateIso = parsed.toISOString();
                    }
                }
            } catch {
                emailDateIso = new Date().toISOString();
            }

            const snippet = msgData.data.snippet || '';
            
            const payload = msgData.data.payload;
            const getEmailBody = (p: any): string => {
                let body = '';
                if (!p) return body;
                if (p.body && p.body.data) {
                    const base64 = p.body.data.replace(/-/g, '+').replace(/_/g, '/');
                    body += Buffer.from(base64, 'base64').toString('utf-8') + ' ';
                }
                if (p.parts && p.parts.length > 0) {
                    for (const part of p.parts) {
                        body += getEmailBody(part);
                    }
                }
                return body;
            };
            const bodyText = getEmailBody(payload);

            const searchText = `${subject} ${snippet} ${bodyText}`.toLowerCase();

            // Check spam first
            const isSpam = SPAM_KEYWORDS.some(keyword => searchText.includes(keyword.toLowerCase()));
            if (isSpam) {
                spamCount++;
                console.log("[GMAIL_SYNC_TRACE] Skipping message (spam):", subject);
                continue;
            }

            // Check target keywords
            const isEvent = TARGET_KEYWORDS.some(keyword => searchText.includes(keyword.toLowerCase()));
            if (!isEvent) {
                notEventCount++;
                continue;
            }

            // Check if already exists in Firestore
            let isDuplicate = false;
            if (firebaseFirestore && typeof firebaseFirestore.collection === 'function' && targetFirebaseUid) {
                try {
                    const existingRef = await firebaseFirestore
                        .collection('detected_events')
                        .where('emailId', '==', message.id)
                        .where('userId', '==', targetFirebaseUid)
                        .get();

                    if (existingRef && !existingRef.empty) {
                        isDuplicate = true;
                    }
                } catch (firestoreErr) {
                    console.warn(`[GMAIL_SYNC] Firestore duplicate check warning for ${message.id}:`, firestoreErr);
                }
            }

            if (isDuplicate) {
                duplicateCount++;
                console.log("[GMAIL_SYNC_TRACE] Skipping message (duplicate):", subject);
                continue;
            }

            const eventData = {
                userId: targetFirebaseUid,
                mongoUserId: userId,
                emailId: message.id,
                title: subject || 'Untitled Event',
                date: emailDateIso,
                location: 'See Email',
                registrationLink: `https://mail.google.com/mail/u/0/#inbox/${message.id}`,
                organizer: from.replace(/<.*>/, '').trim() || 'Unknown Organizer',
                emailSource: 'Gmail',
                detectedAt: new Date().toISOString(),
            };

            console.log("[GMAIL_SYNC_TRACE] Saving new event for subject:", subject);
            if (firebaseFirestore && typeof firebaseFirestore.collection === 'function') {
                try {
                    await firebaseFirestore.collection('detected_events').add(eventData);
                    newEventsCount++;
                } catch (saveErr) {
                    console.error(`[GMAIL_SYNC] Failed to save detected event ${message.id} to Firestore:`, saveErr);
                }
            }
        } catch (msgErr) {
            console.error(`[GMAIL_SYNC] Error processing message ${message.id}:`, msgErr);
            continue;
        }
    }

    console.log("[GMAIL_SYNC_TRACE] Sync completed! processedCount:", processedCount, "spamCount:", spamCount, "notEventCount:", notEventCount, "duplicateCount:", duplicateCount, "newEventsCount:", newEventsCount);
    return { success: true, newEventsCount };
};
