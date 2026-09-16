const fs = require('fs');
const path = require('path');
const { chromium } = require(path.resolve('backend/node_modules/playwright'));
const { execSync } = require('child_process');

async function renderFlowchart() {
  console.log('Generating Publication-Grade 4K 500-DPI Flowchart (Dense & Crystal Clear)...');

  const htmlContent = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Academic Universe — System Architecture & Usage Flowchart</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;600;700&display=swap');

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      width: 3840px;
      height: 2160px;
      background: radial-gradient(ellipse at 50% -10%, #0d1e38 0%, #060d1a 55%, #02050c 100%);
      color: #f8fafc;
      font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
      overflow: hidden;
      position: relative;
      padding: 28px 40px;
      -webkit-font-smoothing: antialiased;
    }

    /* Architectural Grid Background */
    body::before {
      content: "";
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      background-image: 
        linear-gradient(rgba(56, 189, 248, 0.045) 1px, transparent 1px),
        linear-gradient(90deg, rgba(56, 189, 248, 0.045) 1px, transparent 1px);
      background-size: 60px 60px;
      pointer-events: none;
      z-index: 0;
    }

    .container {
      position: relative;
      z-index: 1;
      width: 100%;
      height: 100%;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 16px;
    }

    /* TOP HEADER */
    .header-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: linear-gradient(135deg, rgba(15, 23, 42, 0.94) 0%, rgba(30, 41, 59, 0.88) 100%);
      border: 1.5px solid rgba(56, 189, 248, 0.4);
      border-radius: 20px;
      padding: 18px 36px;
      box-shadow: 0 16px 40px rgba(0,0,0,0.6), 0 0 35px rgba(56, 189, 248, 0.12);
    }

    .header-left {
      display: flex;
      align-items: center;
      gap: 24px;
    }

    .logo-badge {
      background: linear-gradient(135deg, #10b981 0%, #059669 100%);
      color: white;
      font-weight: 800;
      font-size: 32px;
      padding: 12px 24px;
      border-radius: 16px;
      letter-spacing: 1.5px;
      box-shadow: 0 0 28px rgba(16, 185, 129, 0.45);
      border: 1px solid rgba(255,255,255,0.35);
    }

    .header-titles h1 {
      font-size: 42px;
      font-weight: 800;
      letter-spacing: -0.5px;
      background: linear-gradient(90deg, #ffffff 0%, #cbd5e1 40%, #38bdf8 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      line-height: 1.15;
    }

    .header-titles p {
      font-size: 19px;
      color: #94a3b8;
      margin-top: 4px;
      font-weight: 500;
    }

    .header-meta {
      display: flex;
      gap: 14px;
    }

    .meta-pill {
      background: rgba(15, 23, 42, 0.85);
      border: 1.5px solid rgba(71, 85, 105, 0.7);
      padding: 10px 20px;
      border-radius: 12px;
      font-size: 16px;
      font-weight: 600;
      color: #e2e8f0;
    }
    .meta-pill strong { color: #38bdf8; }
    .meta-pill.emerald strong { color: #34d399; }
    .meta-pill.gold strong { color: #fbbf24; }

    /* PHASE PIPELINE INDICATOR */
    .phase-strip {
      display: grid;
      grid-template-columns: 1fr 1fr 2fr 1fr;
      gap: 14px;
    }

    .phase-chip {
      background: rgba(15, 23, 42, 0.75);
      border: 1px solid rgba(71, 85, 105, 0.55);
      border-radius: 12px;
      padding: 10px 18px;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      font-size: 15px;
      font-weight: 700;
      letter-spacing: 0.5px;
      color: #94a3b8;
      text-transform: uppercase;
    }
    .phase-chip.active-1 { border-color: #06b6d4; color: #38bdf8; background: rgba(6, 182, 212, 0.12); }
    .phase-chip.active-2 { border-color: #8b5cf6; color: #a78bfa; background: rgba(139, 92, 246, 0.12); }
    .phase-chip.active-3 { border-color: #10b981; color: #34d399; background: rgba(16, 185, 129, 0.12); }
    .phase-chip.active-4 { border-color: #f59e0b; color: #fbbf24; background: rgba(245, 158, 11, 0.12); }

    /* MAIN FLOWCHART GRID */
    .main-grid {
      display: grid;
      grid-template-columns: 820px 1fr;
      gap: 20px;
      flex: 1;
      height: 1520px;
    }

    /* LEFT SWIMLANE: ACCESS & DUAL NAVIGATION */
    .left-lane {
      display: flex;
      flex-direction: column;
      gap: 18px;
    }

    /* RIGHT SWIMLANE: 4 PARALLEL OPERATIONAL ENGINES */
    .right-lane {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 18px;
    }

    /* CARD STYLING */
    .card {
      background: rgba(15, 23, 42, 0.85);
      border-radius: 18px;
      border: 1.5px solid rgba(51, 65, 85, 0.85);
      padding: 20px;
      display: flex;
      flex-direction: column;
      box-shadow: 0 16px 40px rgba(0,0,0,0.55);
      backdrop-filter: blur(16px);
      position: relative;
    }

    .card.cyan { border-color: rgba(6, 182, 212, 0.55); }
    .card.indigo { border-color: rgba(99, 102, 241, 0.55); }
    .card.emerald { border-color: rgba(16, 185, 129, 0.55); }
    .card.purple { border-color: rgba(168, 85, 247, 0.55); }
    .card.amber { border-color: rgba(245, 158, 11, 0.55); }
    .card.rose { border-color: rgba(244, 63, 94, 0.55); }

    .card-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-bottom: 12px;
      border-bottom: 1px solid rgba(71, 85, 105, 0.55);
      margin-bottom: 14px;
    }

    .card-header-left {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .card-icon {
      font-size: 26px;
      background: rgba(30, 41, 59, 0.85);
      padding: 6px 10px;
      border-radius: 10px;
      border: 1px solid rgba(255,255,255,0.1);
    }

    .card-title-text {
      font-size: 20px;
      font-weight: 800;
      letter-spacing: -0.2px;
    }
    .card.cyan .card-title-text { color: #38bdf8; }
    .card.indigo .card-title-text { color: #818cf8; }
    .card.emerald .card-title-text { color: #34d399; }
    .card.purple .card-title-text { color: #c084fc; }
    .card.amber .card-title-text { color: #fbbf24; }
    .card.rose .card-title-text { color: #fb7185; }

    .card-badge {
      font-size: 12px;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 8px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    .badge-cyan { background: rgba(6, 182, 212, 0.2); color: #38bdf8; border: 1px solid rgba(6, 182, 212, 0.4); }
    .badge-indigo { background: rgba(99, 102, 241, 0.2); color: #a5b4fc; border: 1px solid rgba(99, 102, 241, 0.4); }
    .badge-emerald { background: rgba(16, 185, 129, 0.2); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.4); }
    .badge-purple { background: rgba(168, 85, 247, 0.2); color: #d8b4fe; border: 1px solid rgba(168, 85, 247, 0.4); }
    .badge-amber { background: rgba(245, 158, 11, 0.2); color: #fde68a; border: 1px solid rgba(245, 158, 11, 0.4); }
    .badge-rose { background: rgba(244, 63, 94, 0.2); color: #fda4af; border: 1px solid rgba(244, 63, 94, 0.4); }

    /* STEP FLOW CONTAINER */
    .steps-container {
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      flex: 1;
      gap: 10px;
    }

    .step-node {
      background: rgba(30, 41, 59, 0.7);
      border: 1px solid rgba(71, 85, 105, 0.6);
      border-radius: 12px;
      padding: 13px 16px;
      position: relative;
    }

    .step-node.active-highlight {
      background: rgba(16, 185, 129, 0.12);
      border-color: rgba(16, 185, 129, 0.55);
      box-shadow: 0 0 16px rgba(16, 185, 129, 0.12);
    }
    .step-node.purple-highlight {
      background: rgba(168, 85, 247, 0.12);
      border-color: rgba(168, 85, 247, 0.55);
    }
    .step-node.amber-highlight {
      background: rgba(245, 158, 11, 0.12);
      border-color: rgba(245, 158, 11, 0.55);
    }
    .step-node.rose-highlight {
      background: rgba(244, 63, 94, 0.12);
      border-color: rgba(244, 63, 94, 0.55);
    }

    .step-node-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 5px;
    }

    .step-label {
      font-size: 12px;
      font-weight: 800;
      color: #94a3b8;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .step-label .dot {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: #38bdf8;
    }

    .step-heading {
      font-size: 17.5px;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 4px;
      line-height: 1.25;
    }

    .step-body {
      font-size: 14px;
      color: #cbd5e1;
      line-height: 1.4;
    }

    .step-footer-meta {
      display: flex;
      gap: 6px;
      margin-top: 6px;
      flex-wrap: wrap;
    }

    .meta-tag {
      font-family: 'JetBrains Mono', monospace;
      font-size: 11.5px;
      padding: 2.5px 7px;
      border-radius: 6px;
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid rgba(71, 85, 105, 0.6);
      color: #38bdf8;
    }
    .meta-tag.green { color: #34d399; border-color: rgba(16, 185, 129, 0.4); }
    .meta-tag.purple { color: #c084fc; border-color: rgba(168, 85, 247, 0.4); }
    .meta-tag.amber { color: #fbbf24; border-color: rgba(245, 158, 11, 0.4); }
    .meta-tag.rose { color: #fb7185; border-color: rgba(244, 63, 94, 0.4); }

    .connector-flow {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      color: #64748b;
      font-size: 11.5px;
      font-weight: 700;
      letter-spacing: 1px;
      margin: -3px 0;
    }
    .connector-flow .arrow {
      color: #38bdf8;
      font-size: 15px;
    }

    /* DUAL NAVIGATION SPECIAL SPLIT */
    .nav-split-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      margin-top: 4px;
    }

    .nav-column-box {
      background: rgba(15, 23, 42, 0.75);
      border: 1px solid rgba(71, 85, 105, 0.6);
      border-radius: 12px;
      padding: 12px;
    }

    .nav-col-header {
      font-size: 13.5px;
      font-weight: 800;
      color: #818cf8;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 8px;
      padding-bottom: 6px;
      border-bottom: 1px solid rgba(71, 85, 105, 0.4);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .nav-item-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    .nav-item-list li {
      font-size: 13.5px;
      color: #e2e8f0;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .nav-item-list li span.route {
      color: #94a3b8;
      font-family: 'JetBrains Mono', monospace;
      font-size: 11.5px;
      margin-left: auto;
    }

    /* BOTTOM CLOUD INFRASTRUCTURE BAR */
    .bottom-infrastructure-strip {
      background: linear-gradient(135deg, rgba(15, 23, 42, 0.96) 0%, rgba(30, 41, 59, 0.9) 100%);
      border: 1.5px solid rgba(16, 185, 129, 0.4);
      border-radius: 20px;
      padding: 16px 32px;
      display: grid;
      grid-template-columns: 320px 1fr 1fr 1fr 1fr;
      gap: 20px;
      align-items: center;
      box-shadow: 0 14px 40px rgba(0,0,0,0.55);
    }

    .infra-title-block h3 {
      font-size: 20px;
      font-weight: 800;
      color: #34d399;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .infra-title-block p {
      font-size: 13px;
      color: #94a3b8;
      margin-top: 3px;
    }

    .infra-box {
      background: rgba(15, 23, 42, 0.75);
      border: 1px solid rgba(71, 85, 105, 0.55);
      border-radius: 12px;
      padding: 12px 16px;
    }

    .infra-box-head {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 4px;
    }

    .infra-box h4 {
      font-size: 15px;
      font-weight: 700;
      color: #f1f5f9;
    }

    .infra-tag {
      font-size: 11px;
      font-weight: 700;
      padding: 2px 6px;
      border-radius: 6px;
      background: rgba(16, 185, 129, 0.2);
      color: #34d399;
      border: 1px solid rgba(16, 185, 129, 0.4);
    }

    .infra-box p {
      font-size: 12.5px;
      color: #94a3b8;
      line-height: 1.35;
    }
  </style>
</head>
<body>

  <div class="container">

    <!-- TOP HEADER -->
    <div class="header-bar">
      <div class="header-left">
        <div class="logo-badge">AU</div>
        <div class="header-titles">
          <h1>ACADEMIC UNIVERSE (AU) — END-TO-END SYSTEM ARCHITECTURE & USAGE FLOW</h1>
          <p>Comprehensive Production Workflow: Institutional OAuth Handshake, Smart Dual Navigation, 4 Core Engines & Distributed Cloud Persistence</p>
        </div>
      </div>
      <div class="header-meta">
        <div class="meta-pill">Lead Developer: <strong>Aashish Rajput</strong> (2023329421)</div>
        <div class="meta-pill emerald">Production URL: <strong>academicuniverse.vercel.app</strong></div>
        <div class="meta-pill gold">Core Stack: <strong>Next.js 16 + Express + Gemini 2.5 Flash</strong></div>
        <div class="meta-pill">Resolution: <strong>4K UHD (3840×2160) • 500 DPI</strong></div>
      </div>
    </div>

    <!-- HIGH-LEVEL PHASES STRIP -->
    <div class="phase-strip">
      <div class="phase-chip active-1">
        <span>🔐 Phase 1: Identity & Authentication Plane</span>
      </div>
      <div class="phase-chip active-2">
        <span>🧭 Phase 2: Deduplicated Navigation Routing</span>
      </div>
      <div class="phase-chip active-3">
        <span>⚡ Phase 3: Four Parallel Autonomous Academic Engines</span>
      </div>
      <div class="phase-chip active-4">
        <span>☁️ Phase 4: Production Cloud Infrastructure & Sync</span>
      </div>
    </div>

    <!-- MAIN BOARD (820px LEFT + 4 EQUAL ENGINE COLUMNS) -->
    <div class="main-grid">

      <!-- LEFT COLUMN: ACCESS & ROUTING -->
      <div class="left-lane">

        <!-- STAGE 1: AUTHENTICATION -->
        <div class="card cyan" style="flex: 1.05;">
          <div class="card-header">
            <div class="card-header-left">
              <span class="card-icon">🔐</span>
              <span class="card-title-text">STAGE 1: AUTHENTICATION & RBAC RESOLUTION</span>
            </div>
            <span class="card-badge badge-cyan">Zero-Trust Identity</span>
          </div>

          <div class="steps-container">
            <div class="step-node">
              <div class="step-node-header">
                <span class="step-label"><span class="dot"></span>STEP 1.1 • ENTRY GATEWAY</span>
                <span class="meta-tag">HTTPS Route</span>
              </div>
              <div class="step-heading">User Lands on /login</div>
              <div class="step-body">Access via browser or university intranet. System detects institutional domains (<span class="meta-tag">@ug.sharda.ac.in</span> / <span class="meta-tag">@fa.sharda.ac.in</span>) and enforces corporate TLS.</div>
            </div>

            <div class="connector-flow">
              <span>SECURITY HANDSHAKE</span>
              <span class="arrow">▼</span>
            </div>

            <div class="step-node active-highlight">
              <div class="step-node-header">
                <span class="step-label"><span class="dot" style="background: #10b981;"></span>STEP 1.2 • OAUTH 2.0 PROTOCOL</span>
                <span class="meta-tag green">Firebase Client</span>
              </div>
              <div class="step-heading">Google OAuth 2.0 Web Client Handshake</div>
              <div class="step-body">OAuth token exchanged with Firebase Auth backend. Sanitized redirect prevents origin mismatch; extracts verified institutional email, avatar, and Google UID.</div>
            </div>

            <div class="connector-flow">
              <span>ROLE VERIFICATION</span>
              <span class="arrow">▼</span>
            </div>

            <div class="step-node">
              <div class="step-node-header">
                <span class="step-label"><span class="dot"></span>STEP 1.3 • TOKEN GENERATION</span>
                <span class="meta-tag">RS256 JWT</span>
              </div>
              <div class="step-heading">MongoDB Atlas User Match & JWT Issuance</div>
              <div class="step-body">Server queries <span class="meta-tag">User</span> collection. Generates signed JWT payload containing RBAC roles: <span class="meta-tag">STUDENT</span>, <span class="meta-tag">FACULTY</span>, or <span class="meta-tag">SUPER_ADMIN</span>.</div>
            </div>

            <div class="connector-flow">
              <span>AUTHORIZED DISPATCH</span>
              <span class="arrow">▼</span>
            </div>

            <div class="step-node">
              <div class="step-node-header">
                <span class="step-label"><span class="dot"></span>STEP 1.4 • SESSION MOUNT</span>
                <span class="meta-tag green">HTTP-Only Cookie</span>
              </div>
              <div class="step-heading">Secure Session & Dashboard Routing</div>
              <div class="step-body">Attaches secure session token; redirects authenticated student directly to personal dashboard portal at <span class="meta-tag">/dashboard/student</span>.</div>
              <div class="step-footer-meta">
                <span class="meta-tag green">✅ Token Verified</span>
                <span class="meta-tag">Role: STUDENT</span>
              </div>
            </div>
          </div>
        </div>

        <!-- STAGE 2: NAVIGATION PLANE -->
        <div class="card indigo" style="flex: 1.15;">
          <div class="card-header">
            <div class="card-header-left">
              <span class="card-icon">🧭</span>
              <span class="card-title-text">STAGE 2: DEDUPLICATED DUAL NAVIGATION</span>
            </div>
            <span class="card-badge badge-indigo">Optimized UX</span>
          </div>

          <div class="step-node" style="margin-bottom: 6px;">
            <div class="step-heading">Clutter-Free Non-Redundant Routing Architecture</div>
            <div class="step-body">To ensure high operational speed, macro-level academic portals live in the <strong>Top Navbar</strong>, while micro-level daily operations are organized in the <strong>Left Dashboard Sidebar</strong>.</div>
          </div>

          <div class="nav-split-grid">
            <div class="nav-column-box">
              <div class="nav-col-header">
                <span>Top Navbar (Global Suite)</span>
                <span class="meta-tag purple">7 Portals</span>
              </div>
              <ul class="nav-item-list">
                <li>📈 <strong>Growth Hub</strong> <span class="route">/growth</span></li>
                <li>💼 <strong>Career Profile</strong> <span class="route">/career</span></li>
                <li>📚 <strong>Presence Central</strong> <span class="route">/attendance</span></li>
                <li>🤖 <strong>Campus AI Bot</strong> <span class="route">/campus-ai</span></li>
                <li>🔬 <strong>Research Wing</strong> <span class="route">/research</span></li>
                <li>💻 <strong>Code Arena</strong> <span class="route">/arena</span></li>
                <li>🚪 <strong>Faculty Cabin</strong> <span class="route">/cabin</span></li>
              </ul>
            </div>

            <div class="nav-column-box">
              <div class="nav-col-header">
                <span>Left Sidebar (Operations)</span>
                <span class="meta-tag purple">9 Modules</span>
              </div>
              <ul class="nav-item-list">
                <li>👤 <strong>Profile Details</strong> <span class="route">/profile</span></li>
                <li>📧 <strong>Gmail Notices</strong> <span class="route">/events</span></li>
                <li>✉️ <strong>Webmail Explorer</strong> <span class="route">/mail</span></li>
                <li>🧠 <strong>Doc Vault Intelligence</strong> <span class="route">/docs</span></li>
                <li>📅 <strong>Weekly Timetable</strong> <span class="route">/schedule</span></li>
                <li>🔄 <strong>E-Zone Sync Engine</strong> <span class="route">/sync</span></li>
                <li>🎯 <strong>Skills Proficiency</strong> <span class="route">/skills</span></li>
                <li>📄 <strong>Placement Resume</strong> <span class="route">/resume</span></li>
                <li>👥 <strong>Overlap Engine</strong> <span class="route">/overlap</span></li>
              </ul>
            </div>
          </div>

          <div class="step-footer-meta" style="margin-top: 8px;">
            <span class="meta-tag green">✅ Zero Redundancy Between Menus</span>
            <span class="meta-tag">Instant Routing without Re-Authentication</span>
          </div>
        </div>

      </div>

      <!-- RIGHT COLUMNS: 4 CORE OPERATIONAL ENGINES (5 STEPS EACH!) -->
      <div class="right-lane">

        <!-- ENGINE A: E-ZONE SYNC -->
        <div class="card emerald">
          <div class="card-header">
            <div class="card-header-left">
              <span class="card-icon">🔄</span>
              <span class="card-title-text">ENGINE A: E-ZONE SYNC</span>
            </div>
            <span class="card-badge badge-emerald">Live Scraper</span>
          </div>

          <div class="steps-container">
            <div class="step-node">
              <div class="step-node-header">
                <span class="step-label"><span class="dot" style="background: #10b981;"></span>STEP A1 • INPUT</span>
                <span class="meta-tag green">Portal Trigger</span>
              </div>
              <div class="step-heading">Student Inputs System ID</div>
              <div class="step-body">Student enters Institutional ID (e.g. <span class="meta-tag">2023329421</span>). Frontend triggers API call to Railway backend scraper microservice.</div>
            </div>

            <div class="connector-flow">
              <span>CHALLENGE VERIFICATION</span>
              <span class="arrow" style="color: #10b981;">▼</span>
            </div>

            <div class="step-node">
              <div class="step-node-header">
                <span class="step-label"><span class="dot" style="background: #10b981;"></span>STEP A2 • 2FA OTP</span>
                <span class="meta-tag">Webmail API</span>
              </div>
              <div class="step-heading">Two-Factor Authentication</div>
              <div class="step-body">University portal transmits 6-digit OTP to student webmail. Student submits OTP to complete session handshake on portal.</div>
            </div>

            <div class="connector-flow">
              <span>HEADLESS SCRAPER RUN</span>
              <span class="arrow" style="color: #10b981;">▼</span>
            </div>

            <div class="step-node active-highlight">
              <div class="step-node-header">
                <span class="step-label"><span class="dot" style="background: #10b981;"></span>STEP A3 • PLAYWRIGHT</span>
                <span class="meta-tag green">DOM Parser</span>
              </div>
              <div class="step-heading">Playwright Automated Scraping</div>
              <div class="step-body">Headless browser accesses timetable & attendance tabs. Extracts subject codes, faculty names, room numbers, and slot timing intervals.</div>
            </div>

            <div class="connector-flow">
              <span>DATA NORMALIZATION</span>
              <span class="arrow" style="color: #10b981;">▼</span>
            </div>

            <div class="step-node">
              <div class="step-node-header">
                <span class="step-label"><span class="dot" style="background: #10b981;"></span>STEP A4 • SANITIZATION</span>
                <span class="meta-tag">JSON Schema</span>
              </div>
              <div class="step-heading">Academic Record Sanitization</div>
              <div class="step-body">Validates period schedules, attendance percentages, and professor contacts against structured TypeScript data models.</div>
            </div>

            <div class="connector-flow">
              <span>DUAL STORAGE PIPELINE</span>
              <span class="arrow" style="color: #10b981;">▼</span>
            </div>

            <div class="step-node">
              <div class="step-node-header">
                <span class="step-label"><span class="dot" style="background: #10b981;"></span>STEP A5 • PERSISTENCE</span>
                <span class="meta-tag green">Atlas + Sheets</span>
              </div>
              <div class="step-heading">Database & Sheet Audit Stream</div>
              <div class="step-body">Saves JSON profile in MongoDB <span class="meta-tag">AcademicSchedule</span> and writes audit row to Google Sheets via Service Account.</div>
              <div class="step-footer-meta">
                <span class="meta-tag green">✅ 12 Weekly Slots Synced</span>
                <span class="meta-tag">Attendance: 84.6%</span>
              </div>
            </div>
          </div>
        </div>

        <!-- ENGINE B: CAMPUS AI ADVISING -->
        <div class="card purple">
          <div class="card-header">
            <div class="card-header-left">
              <span class="card-icon">🤖</span>
              <span class="card-title-text">ENGINE B: CAMPUS AI</span>
            </div>
            <span class="card-badge badge-purple">Gemini 2.5 Flash</span>
          </div>

          <div class="steps-container">
            <div class="step-node">
              <div class="step-node-header">
                <span class="step-label"><span class="dot" style="background: #a855f7;"></span>STEP B1 • QUERY</span>
                <span class="meta-tag purple">Natural Language</span>
              </div>
              <div class="step-heading">Student Query Input</div>
              <div class="step-body">Student asks in chat: <em>"Where is my Research Methodology lecture today and who is the instructor?"</em></div>
            </div>

            <div class="connector-flow">
              <span>SCHEDULE LOOKUP</span>
              <span class="arrow" style="color: #a855f7;">▼</span>
            </div>

            <div class="step-node purple-highlight">
              <div class="step-node-header">
                <span class="step-label"><span class="dot" style="background: #a855f7;"></span>STEP B2 • RETRIEVAL</span>
                <span class="meta-tag purple">Live Context RAG</span>
              </div>
              <div class="step-heading">Real Timetable Data Match</div>
              <div class="step-body">Backend fetches student's active schedule from MongoDB. Identifies Monday Period 2: <span class="meta-tag purple">Room 206 Block 3</span>, Dr. Batri K.</div>
            </div>

            <div class="connector-flow">
              <span>SYSTEM PROMPT INJECTION</span>
              <span class="arrow" style="color: #a855f7;">▼</span>
            </div>

            <div class="step-node">
              <div class="step-node-header">
                <span class="step-label"><span class="dot" style="background: #a855f7;"></span>STEP B3 • GUARDRAILS</span>
                <span class="meta-tag">Zero Hallucination</span>
              </div>
              <div class="step-heading">Prompt Augmentation & Guardrails</div>
              <div class="step-body">Live classroom context + emotional intelligence rules injected into system instructions; prohibits speculative answers.</div>
            </div>

            <div class="connector-flow">
              <span>LLM INFERENCE STREAM</span>
              <span class="arrow" style="color: #a855f7;">▼</span>
            </div>

            <div class="step-node">
              <div class="step-node-header">
                <span class="step-label"><span class="dot" style="background: #a855f7;"></span>STEP B4 • INFERENCE</span>
                <span class="meta-tag purple">Gemini 2.5</span>
              </div>
              <div class="step-heading">Google Gemini 2.5 Generation</div>
              <div class="step-body">Executes low-latency generative completion with grounded room coordinates and friendly, actionable tone.</div>
            </div>

            <div class="connector-flow">
              <span>STREAMED RESPONSE</span>
              <span class="arrow" style="color: #a855f7;">▼</span>
            </div>

            <div class="step-node">
              <div class="step-node-header">
                <span class="step-label"><span class="dot" style="background: #a855f7;"></span>STEP B5 • DELIVERY</span>
                <span class="meta-tag green">Instant UX</span>
              </div>
              <div class="step-heading">Precise Guidance & Support</div>
              <div class="step-body">Returns exact classroom coordinates, teacher name, and subject tips without generic or inaccurate guessing.</div>
              <div class="step-footer-meta">
                <span class="meta-tag green">✅ Verified: Room 206 Block 3</span>
                <span class="meta-tag purple">&lt; 850ms Latency</span>
              </div>
            </div>
          </div>
        </div>

        <!-- ENGINE C: OVERLAP ENGINE -->
        <div class="card amber">
          <div class="card-header">
            <div class="card-header-left">
              <span class="card-icon">👥</span>
              <span class="card-title-text">ENGINE C: OVERLAP PLAN</span>
            </div>
            <span class="card-badge badge-amber">N-Way Match</span>
          </div>

          <div class="steps-container">
            <div class="step-node">
              <div class="step-node-header">
                <span class="step-label"><span class="dot" style="background: #f59e0b;"></span>STEP C1 • HOST RESOLUTION</span>
                <span class="meta-tag amber">Host (You) Card</span>
              </div>
              <div class="step-heading">Active Host Identification</div>
              <div class="step-body">System detects logged-in user (<span class="meta-tag amber">Aashish Rajput • 2023329421</span>) and loads his verified weekly timetable grid.</div>
            </div>

            <div class="connector-flow">
              <span>PEER SELECTION & VALIDATION</span>
              <span class="arrow" style="color: #f59e0b;">▼</span>
            </div>

            <div class="step-node">
              <div class="step-node-header">
                <span class="step-label"><span class="dot" style="background: #f59e0b;"></span>STEP C2 • PEER SEARCH</span>
                <span class="meta-tag amber">1 to 5 Students</span>
              </div>
              <div class="step-heading">Student Directory Lookup</div>
              <div class="step-body">Searches student directory by Name or ID (e.g. <span class="meta-tag amber">Vishal Sharma • 2024427058</span>). Validates real names and <span class="meta-tag green">✅ Synced Schedule</span> badge.</div>
            </div>

            <div class="connector-flow">
              <span>BITMASK MATRIX CREATION</span>
              <span class="arrow" style="color: #f59e0b;">▼</span>
            </div>

            <div class="step-node">
              <div class="step-node-header">
                <span class="step-label"><span class="dot" style="background: #f59e0b;"></span>STEP C3 • 54-SLOT BITMASK</span>
                <span class="meta-tag">6 Days × 9 Slots</span>
              </div>
              <div class="step-heading">Free-Interval Bitmasking</div>
              <div class="step-body">Converts each student's weekly schedule into binary availability masks across 9 daily periods (09:00 - 16:40).</div>
            </div>

            <div class="connector-flow">
              <span>SET-THEORETIC ALGORITHM</span>
              <span class="arrow" style="color: #f59e0b;">▼</span>
            </div>

            <div class="step-node amber-highlight">
              <div class="step-node-header">
                <span class="step-label"><span class="dot" style="background: #f59e0b;"></span>STEP C4 • SET INTERSECTION</span>
                <span class="meta-tag amber">Interval Engine</span>
              </div>
              <div class="step-heading">N-Way Intersection Computation</div>
              <div class="step-body">Executes bitwise logical AND: <span class="meta-tag amber">Free(All) = Free(Host) ∩ ⋂ Free(Peers)</span> to locate mutual leisure windows.</div>
            </div>

            <div class="connector-flow">
              <span>SLOT CLUSTERING & RANKING</span>
              <span class="arrow" style="color: #f59e0b;">▼</span>
            </div>

            <div class="step-node">
              <div class="step-node-header">
                <span class="step-label"><span class="dot" style="background: #f59e0b;"></span>STEP C5 • RANKED SLOTS</span>
                <span class="meta-tag amber">Optimal Booking</span>
              </div>
              <div class="step-heading">Ranked Study Recommendations</div>
              <div class="step-body">Aggregates contiguous periods into 1h/2h study blocks; displays participant count, time ranges, and shareable meet plan.</div>
              <div class="step-footer-meta">
                <span class="meta-tag green">✅ Real Names & IDs Resolved</span>
                <span class="meta-tag amber">9 Time Slots Matched</span>
              </div>
            </div>
          </div>
        </div>

        <!-- ENGINE D: RESEARCH WING -->
        <div class="card rose">
          <div class="card-header">
            <div class="card-header-left">
              <span class="card-icon">🔬</span>
              <span class="card-title-text">ENGINE D: RESEARCH WING</span>
            </div>
            <span class="card-badge badge-rose">5-Stage Pipeline</span>
          </div>

          <div class="steps-container">
            <div class="step-node">
              <div class="step-node-header">
                <span class="step-label"><span class="dot" style="background: #f43f5e;"></span>STEP D1 • TOPIC DISCOVERY</span>
                <span class="meta-tag rose">Literature Gap</span>
              </div>
              <div class="step-heading">1. AI Topic Generation & Scope</div>
              <div class="step-body">Generates novel engineering topics with problem formulation, research objectives, and state-of-the-art gap analysis.</div>
            </div>

            <div class="connector-flow">
              <span>HIERARCHICAL OUTLINING</span>
              <span class="arrow" style="color: #f43f5e;">▼</span>
            </div>

            <div class="step-node">
              <div class="step-node-header">
                <span class="step-label"><span class="dot" style="background: #f43f5e;"></span>STEP D2 • OUTLINE BUILDER</span>
                <span class="meta-tag rose">IEEE Standard</span>
              </div>
              <div class="step-heading">2. Outline & Section Hierarchy</div>
              <div class="step-body">Synthesizes standard multi-tier structure: Abstract, Introduction, System Model, Mathematical Formulations, Experimental Results.</div>
            </div>

            <div class="connector-flow">
              <span>DEEP DRAFTING & LATEX PROSE</span>
              <span class="arrow" style="color: #f43f5e;">▼</span>
            </div>

            <div class="step-node rose-highlight">
              <div class="step-node-header">
                <span class="step-label"><span class="dot" style="background: #f43f5e;"></span>STEP D3 • DRAFT & PROOFREAD</span>
                <span class="meta-tag rose">Iterative Prompting</span>
              </div>
              <div class="step-heading">3. Content Drafting & Polish</div>
              <div class="step-body">Long-form academic synthesis with LaTeX equations, mathematical rigor, and automated grammar polish.</div>
            </div>

            <div class="connector-flow">
              <span>CITATIONS & ABSTRACT COMPILATION</span>
              <span class="arrow" style="color: #f43f5e;">▼</span>
            </div>

            <div class="step-node">
              <div class="step-node-header">
                <span class="step-label"><span class="dot" style="background: #f43f5e;"></span>STEP D4 • CITATIONS & SUMMARY</span>
                <span class="meta-tag rose">BibTeX Formatter</span>
              </div>
              <div class="step-heading">4. Abstract & Citation Indexing</div>
              <div class="step-body">Generates concise executive abstract, relevant IEEE index terms, and rigorously formatted bibliography citations.</div>
            </div>

            <div class="connector-flow">
              <span>MULTI-FORMAT COMPILATION</span>
              <span class="arrow" style="color: #f43f5e;">▼</span>
            </div>

            <div class="step-node">
              <div class="step-node-header">
                <span class="step-label"><span class="dot" style="background: #f43f5e;"></span>STEP D5 • DUAL EXPORT</span>
                <span class="meta-tag green">PDF / DOCX</span>
              </div>
              <div class="step-heading">5. Camera-Ready Artifact Export</div>
              <div class="step-body">Compiles into publication-ready PDF and editable Microsoft Word (.docx) documents; persists draft versions in MongoDB.</div>
              <div class="step-footer-meta">
                <span class="meta-tag green">✅ MongoDB Persistent Drafts</span>
                <span class="meta-tag rose">Camera-Ready Output</span>
              </div>
            </div>
          </div>
        </div>

      </div>

    </div>

    <!-- BOTTOM CLOUD INFRASTRUCTURE BAR -->
    <div class="bottom-infrastructure-strip">
      <div class="infra-title-block">
        <h3><span>☁️</span> CLOUD INFRASTRUCTURE</h3>
        <p>Production Zero-Mock Deployments with Distributed Reliability</p>
      </div>

      <div class="infra-box">
        <div class="infra-box-head">
          <h4>Vercel Edge Platform</h4>
          <span class="infra-tag">Frontend</span>
        </div>
        <p>Next.js 16 App Router with Turbopack. 50 production routes served with global SSL & zero-downtime CI/CD.</p>
      </div>

      <div class="infra-box">
        <div class="infra-box-head">
          <h4>Railway Cloud Container</h4>
          <span class="infra-tag">Backend</span>
        </div>
        <p>Express TypeScript API microservices running headless Playwright browser workers and secure JWT middlewares.</p>
      </div>

      <div class="infra-box">
        <div class="infra-box-head">
          <h4>MongoDB Atlas Enterprise</h4>
          <span class="infra-tag">Persistence</span>
        </div>
        <p>Managed replica set housing User profiles, EzoneAcademicProfiles, AcademicSchedules, and research drafts.</p>
      </div>

      <div class="infra-box">
        <div class="infra-box-head">
          <h4>AI & External API Mesh</h4>
          <span class="infra-tag">Integrations</span>
        </div>
        <p>Google Gemini 2.5 Flash, Firebase Auth 2.0, Google Sheets real-time audit ledger, and Triple-Mirror GitHub remotes.</p>
      </div>
    </div>

  </div>

</body>
</html>`;

  const htmlPath = path.join(process.cwd(), 'scratch', 'flowchart_4k.html');
  fs.writeFileSync(htmlPath, htmlContent, 'utf-8');
  console.log('HTML written to:', htmlPath);

  // Launch Playwright Chromium at 4K viewport
  const browser = await chromium.launch({
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const page = await browser.newPage({
    viewport: { width: 3840, height: 2160 },
    deviceScaleFactor: 1
  });

  await page.goto('file:///' + htmlPath.replace(/\\/g, '/'), { waitUntil: 'networkidle' });
  await page.waitForTimeout(2500); // allow web fonts to fully render

  const rawPngPath = path.join(process.cwd(), 'scratch', 'flowchart_raw_4k.png');
  await page.screenshot({ path: rawPngPath, fullPage: true });
  console.log('4K Screenshot captured at:', rawPngPath);

  await browser.close();

  // Run Python script to set 500 DPI metadata and save final PNG
  const finalPngPath = path.join(process.cwd(), 'Academic_Universe_System_Flowchart_4K_500DPI.png');
  const pyDpiScript = `
from PIL import Image
im = Image.open(r"${rawPngPath.replace(/\\/g, '/')}")
im.save(r"${finalPngPath.replace(/\\/g, '/')}", dpi=(500, 500), compress_level=1)
print(f"Final 4K 500DPI PNG generated successfully: {im.size} at 500 DPI")
`;

  fs.writeFileSync(path.join(process.cwd(), 'scratch', 'set_dpi.py'), pyDpiScript, 'utf-8');
  execSync('python scratch/set_dpi.py', { stdio: 'inherit' });

  console.log('SUCCESS! Flowchart saved at:', finalPngPath);
}

renderFlowchart().catch(err => {
  console.error('Error rendering flowchart:', err);
  process.exit(1);
});
