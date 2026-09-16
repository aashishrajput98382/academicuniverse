# Academic Universe (AU) — All 16 Modules Mermaid Flowcharts
Standard ISO/ANSI Flowchart Structure: `([Start])`, `[Process]`, `{Decision?}`, `([End])`.
Copy-paste directly into draw.io (`+` -> `Advanced` -> `Mermaid`).

---

## 1. Profile Module
```mermaid
flowchart TD
    Start([Start]) --> P1[Navigate to Student Profile Page]
    P1 --> P2[Fetch Personal & Academic Data from MongoDB]
    P2 --> D1{Edit Profile Details?}
    D1 -->|No| P3[View Academic Information & ID]
    D1 -->|Yes| P4[Update Bio, Skills, and Avatar]
    P4 --> D2{Valid Input?}
    D2 -->|No| P4
    D2 -->|Yes| P5[Save Updated Profile to MongoDB Atlas]
    P3 --> EndNode([End])
    P5 --> EndNode
```

---

## 2. Events from Gmail Module
```mermaid
flowchart TD
    Start([Start]) --> P1[Open Gmail Events Scanner]
    P1 --> P2[Connect University Email via Google API]
    P2 --> D1{New Campus Circulars Found?}
    D1 -->|No| P3[Display 'No New Events Found']
    D1 -->|Yes| P4[Parse Notice Dates, Venue & Subject]
    P4 --> P5[Auto-Sync to Student Academic Calendar]
    P5 --> P6[Set Event Reminders & Notification Alert]
    P3 --> EndNode([End])
    P6 --> EndNode
```

---

## 3. Mail Explorer Module
```mermaid
flowchart TD
    Start([Start]) --> P1[Open Webmail Explorer]
    P1 --> P2[Authenticate Secure IMAP/Webmail Session]
    P2 --> D1{Mailbox Connected?}
    D1 -->|No| P_Err[Show Connection Error & Retry]
    P_Err --> P2
    D1 -->|Yes| P3[Fetch & Filter Institutional Emails]
    P3 --> P4[Search by Faculty, Department or Keyword]
    P4 --> P5[Read Notices, Download Attachments or Reply]
    P5 --> EndNode([End])
```

---

## 4. Academic Universe (Timetable & Schedule) Module
```mermaid
flowchart TD
    Start([Start]) --> P1[Open Weekly Academic Schedule]
    P1 --> P2[Load Synced Class Schedule from MongoDB]
    P2 --> D1{Classes Scheduled Today?}
    D1 -->|No| P3[Display 'No Classes Today - Enjoy Free Time']
    D1 -->|Yes| P4[Display Daily Timeline: Periods 1 to 9]
    P4 --> P5[Highlight Current Class, Room & Faculty Name]
    P3 --> EndNode([End])
    P5 --> EndNode
```

---

## 5. Sync College Profile (E-Zone Sync Engine)
```mermaid
flowchart TD
    Start([Start]) --> P1[Enter Institutional System ID]
    P1 --> P2[Trigger 2FA OTP to University Webmail]
    P2 --> D1{OTP Valid & Verified?}
    D1 -->|No| P_Err[Display Invalid OTP Alert]
    P_Err --> P1
    D1 -->|Yes| P3[Launch Headless Playwright Browser Worker]
    P3 --> P4[Scrape Timetable Grid & Attendance Data]
    P4 --> P5[Save in MongoDB Atlas & Append Audit to Google Sheets]
    P5 --> EndNode([End])
```

---

## 6. Skill Tracker Module
```mermaid
flowchart TD
    Start([Start]) --> P1[Open Skills Competency Dashboard]
    P1 --> P2[Load Enrolled Technical & Core Skills]
    P2 --> D1{Log New Skill or Project?}
    D1 -->|No| P3[View Proficiency Radar Chart]
    D1 -->|Yes| P4[Submit Completed Problem / Certificate Link]
    P4 --> D2{Verified Assessment?}
    D2 -->|No| P5[Mark as In-Progress]
    D2 -->|Yes| P6[Increment Skill Level to Advanced]
    P3 --> EndNode([End])
    P5 --> EndNode
    P6 --> EndNode
```

---

## 7. Resume Builder Module
```mermaid
flowchart TD
    Start([Start]) --> P1[Launch Resume Builder Engine]
    P1 --> P2[Auto-Fetch Synced Profile, CGPA & Skills]
    P2 --> P3[Select ATS-Optimized Resume Template]
    P3 --> D1{Edit Content or Projects?}
    D1 -->|Yes| P4[Update Work Experience & Objective]
    D1 -->|No| P5[Run Real-time ATS Formatting Check]
    P4 --> P5
    P5 --> D2{ATS Score > 80%?}
    D2 -->|No| P6[Suggest Keyword & Layout Improvements]
    P6 --> P4
    D2 -->|Yes| P7[Export One-Click PDF & Editable Word DOCX]
    P7 --> EndNode([End])
```

---

## 8. Overlap Engine Module
```mermaid
flowchart TD
    Start([Start]) --> P1[Detect Host Student Profile]
    P1 --> P2[Search Peer Students by Name or ID]
    P2 --> D1{Peer Timetable Synced?}
    D1 -->|No| P3[Send Sync Invitation Link to Peer]
    P3 --> EndNode([End])
    D1 -->|Yes| P4[Convert Weekly Schedules to 54-Slot Bitmasks]
    P4 --> P5[Compute Set Intersection: Free Host ∩ Free Peers]
    P5 --> P6[Rank Contiguous 1h/2h Free Study Windows]
    P6 --> P7[Display Availability Matrix & Share Booking Link]
    P7 --> EndNode
```

---

## 9. Growth Hub Module
```mermaid
flowchart TD
    Start([Start]) --> P1[Open Growth Hub Dashboard]
    P1 --> P2[Aggregate Semester Attendance & Internal Marks]
    P2 --> P3[Compute Predictive Academic Performance Metric]
    P3 --> D1{Performance On Track?}
    D1 -->|No| P4[Trigger Low-Attendance / Grade Warning Alert]
    D1 -->|Yes| P5[Display Commendation & Growth Badges]
    P4 --> P6[Suggest Remedial Action & Revision Resources]
    P5 --> EndNode([End])
    P6 --> EndNode
```

---

## 10. Certificates (Doc Vault Intelligence) Module
```mermaid
flowchart TD
    Start([Start]) --> P1[Open Certificate Vault]
    P1 --> P2[Upload Certificate File PDF/Image]
    P2 --> P3[Execute OCR Text & Metadata Extraction]
    P3 --> D1{Valid Institutional Credential?}
    D1 -->|No| P4[Flag for Manual Review]
    D1 -->|Yes| P5[Attach Verified Credential Badge]
    P5 --> P6[Store Encrypted in MongoDB Atlas GridFS]
    P4 --> EndNode([End])
    P6 --> EndNode
```

---

## 11. Centralized Presence (Attendance Monitoring) Module
```mermaid
flowchart TD
    Start([Start]) --> P1[Open Centralized Presence Portal]
    P1 --> P2[Fetch Real Attendance Percentage from Database]
    P2 --> P3[Calculate Subject-wise Attendance Breakdown]
    P3 --> D1{Attendance >= 75% Threshold?}
    D1 -->|No| P4[Calculate Exact Classes Needed to Reach 75%]
    D1 -->|Yes| P5[Display Safe Attendance Status & Buffer Days]
    P4 --> P6[Send Low-Attendance Alert to Student]
    P5 --> EndNode([End])
    P6 --> EndNode
```

---

## 12. AI Chatbot (Campus AI Advisor) Module
```mermaid
flowchart TD
    Start([Start]) --> P1[Student Submits Chat Query]
    P1 --> P2[Query MongoDB for Student Today's Timetable]
    P2 --> D1{Classroom Context Found?}
    D1 -->|Yes| P3[Inject Real Coordinates: Room 206 Block 3]
    D1 -->|No| P4[Inject General Campus Guidelines]
    P3 --> P5[Apply Zero-Hallucination Guardrails]
    P4 --> P5
    P5 --> P6[Google Gemini 2.5 Flash Generates Response]
    P6 --> P7[Stream Verified Actionable Guidance to Student]
    P7 --> EndNode([End])
```

---

## 13. Research Wing Module
```mermaid
flowchart TD
    Start([Start]) --> P1[Enter Research Domain or Problem Statement]
    P1 --> P2[Stage 1: AI Literature Gap & Topic Discovery]
    P2 --> P3[Stage 2: Synthesize IEEE Multi-Tier Outline]
    P3 --> P4[Stage 3: Deep Drafting with LaTeX Math & Formulas]
    P4 --> P5[Stage 4: Format BibTeX Indexing & Abstract]
    P5 --> D1{Proofreading Quality Passed?}
    D1 -->|No| P4
    D1 -->|Yes| P6[Stage 5: Dual Export to Camera-Ready PDF & DOCX]
    P6 --> EndNode([End])
```

---

## 14. Code Arena Module
```mermaid
flowchart TD
    Start([Start]) --> P1[Select DSA Problem Challenge]
    P1 --> P2[Write Code in Interactive Web IDE]
    P2 --> P3[Submit Solution to Execution Engine]
    P3 --> D1{All Test Cases Passed?}
    D1 -->|No| P4[Display Failed Test Cases & Error Trace]
    P4 --> P2
    D1 -->|Yes| P5[Update User Score & Global Leaderboard Rank]
    P5 --> EndNode([End])
```

---

## 15. Soft Skills Lab Module
```mermaid
flowchart TD
    Start([Start]) --> P1[Select Soft Skills / Interview Scenario]
    P1 --> P2[AI Generates Dynamic Situational Question]
    P2 --> P3[Record Student Verbal or Text Response]
    P3 --> P4[Analyze Tone, Vocabulary, Grammar & Confidence]
    P4 --> D1{Score Meets Threshold?}
    D1 -->|No| P5[Provide Corrective Tips & Re-attempt]
    P5 --> P2
    D1 -->|Yes| P6[Award Completion Badge & Progress Report]
    P6 --> EndNode([End])
```

---

## 16. Sign In / Sign Up Module
```mermaid
flowchart TD
    Start([Start]) --> P1[Open /login Authentication Gateway]
    P1 --> P2[Enter Institutional Email ID]
    P2 --> D1{Domain is @ug.sharda.ac.in?}
    D1 -->|No| P_Err1[Display Domain Restriction Notice]
    P_Err1 --> P1
    D1 -->|Yes| P3[Initiate Google OAuth 2.0 Web Client]
    P3 --> D2{OAuth Verified by Firebase?}
    D2 -->|No| P_Err2[Display Auth Handshake Error]
    P_Err2 --> P1
    D2 -->|Yes| P4[Match User in MongoDB & Issue RS256 JWT]
    P4 --> P5[Mount Secure Cookie & Dispatch to /dashboard]
    P5 --> EndNode([End])
```
