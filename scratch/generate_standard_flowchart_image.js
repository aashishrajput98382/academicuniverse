const fs = require('fs');
const path = require('path');
const { chromium } = require(path.resolve('backend/node_modules/playwright'));
const { execSync } = require('child_process');

async function renderStandardFlowchart() {
  console.log('Rendering Standard Component Flowchart (ANSI/ISO Shapes)...');

  const htmlContent = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Academic Universe — Standard Flowchart</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap');

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      width: 3840px;
      height: 2160px;
      background: #ffffff;
      color: #0f172a;
      font-family: 'Inter', -apple-system, sans-serif;
      padding: 40px 60px;
      position: relative;
    }

    /* HEADER */
    .header {
      text-align: center;
      margin-bottom: 30px;
      padding-bottom: 20px;
      border-bottom: 2px solid #e2e8f0;
    }

    .header h1 {
      font-size: 38px;
      font-weight: 800;
      color: #0f172a;
      letter-spacing: -0.5px;
    }

    .header p {
      font-size: 18px;
      color: #64748b;
      margin-top: 6px;
      font-weight: 500;
    }

    .meta-bar {
      display: flex;
      justify-content: center;
      gap: 24px;
      margin-top: 12px;
      font-size: 15px;
      font-weight: 600;
      color: #475569;
    }
    .meta-bar span {
      background: #f1f5f9;
      padding: 6px 14px;
      border-radius: 8px;
      border: 1px solid #cbd5e1;
    }
    .meta-bar strong {
      color: #0284c7;
    }

    /* 5-COLUMN FLOWCHART LAYOUT */
    .flowchart-grid {
      display: grid;
      grid-template-columns: 1.15fr 1fr 1fr 1fr 1fr;
      gap: 32px;
      height: 1820px;
    }

    .column {
      display: flex;
      flex-direction: column;
      align-items: center;
      background: #fafafa;
      border: 1.5px solid #e2e8f0;
      border-radius: 16px;
      padding: 24px 18px;
      position: relative;
    }

    .column-title {
      font-size: 16px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: #0f172a;
      background: #e2e8f0;
      padding: 6px 16px;
      border-radius: 8px;
      margin-bottom: 24px;
      width: 100%;
      text-align: center;
    }

    /* STANDARD SHAPES */

    /* 1. TERMINATOR (Capsule / Rounded Oval) */
    .shape-terminator {
      width: 220px;
      height: 64px;
      border: 2.5px solid #0f172a;
      border-radius: 32px;
      background: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 18px;
      font-weight: 700;
      color: #0f172a;
      box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }
    .shape-terminator.start {
      border-color: #10b981;
      color: #065f46;
      background: #ecfdf5;
    }
    .shape-terminator.end {
      border-color: #ef4444;
      color: #991b1b;
      background: #fef2f2;
    }

    /* 2. PROCESS (Rectangle) */
    .shape-process {
      width: 95%;
      min-height: 80px;
      border: 2px solid #1e293b;
      background: #ffffff;
      padding: 12px 16px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
      border-radius: 4px;
      box-shadow: 0 4px 8px rgba(0,0,0,0.04);
    }
    .shape-process .proc-title {
      font-size: 16px;
      font-weight: 700;
      color: #0f172a;
      line-height: 1.25;
    }
    .shape-process .proc-desc {
      font-size: 13px;
      color: #64748b;
      margin-top: 4px;
      line-height: 1.35;
    }

    /* 3. DECISION (Diamond) */
    .decision-wrapper {
      position: relative;
      width: 180px;
      height: 180px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 10px 0;
    }

    .shape-decision {
      position: absolute;
      width: 130px;
      height: 130px;
      border: 2.5px solid #0284c7;
      background: #f0f9ff;
      transform: rotate(45deg);
      border-radius: 6px;
      box-shadow: 0 4px 12px rgba(2, 132, 199, 0.15);
    }

    .decision-text {
      position: relative;
      z-index: 2;
      text-align: center;
      font-size: 14.5px;
      font-weight: 700;
      color: #0369a1;
      padding: 0 10px;
      line-height: 1.25;
    }

    .choice-label {
      position: absolute;
      font-size: 12px;
      font-weight: 800;
      padding: 2px 6px;
      border-radius: 4px;
    }
    .choice-yes {
      bottom: -18px;
      color: #16a34a;
      background: #dcfce7;
      border: 1px solid #86efac;
    }
    .choice-no {
      right: -20px;
      color: #dc2626;
      background: #fee2e2;
      border: 1px solid #fca5a5;
    }

    /* 4. CONNECTOR (Circle with Letter) */
    .shape-connector {
      width: 52px;
      height: 52px;
      border: 2.5px solid #6366f1;
      border-radius: 50%;
      background: #eef2ff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 20px;
      font-weight: 800;
      color: #4338ca;
      box-shadow: 0 3px 8px rgba(99, 102, 241, 0.2);
    }

    /* DIRECTED ARROW */
    .arrow-down {
      display: flex;
      flex-direction: column;
      align-items: center;
      margin: 6px 0;
      color: #475569;
    }
    .arrow-line {
      width: 2px;
      height: 18px;
      background: #475569;
    }
    .arrow-head {
      width: 0;
      height: 0;
      border-left: 6px solid transparent;
      border-right: 6px solid transparent;
      border-top: 8px solid #475569;
    }

    /* FLOW STEPS STACK */
    .flow-stack {
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 0;
      flex: 1;
      justify-content: space-between;
    }

    /* LEGEND BOX */
    .legend-box {
      position: absolute;
      bottom: 25px;
      right: 60px;
      background: #ffffff;
      border: 1.5px solid #cbd5e1;
      border-radius: 12px;
      padding: 12px 20px;
      display: flex;
      align-items: center;
      gap: 20px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.06);
    }
    .legend-item {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 13px;
      font-weight: 600;
      color: #334155;
    }
    .leg-term { width: 40px; height: 20px; border: 2px solid #0f172a; border-radius: 10px; background: #ecfdf5; }
    .leg-proc { width: 34px; height: 20px; border: 2px solid #0f172a; border-radius: 2px; background: #fff; }
    .leg-dec { width: 22px; height: 22px; border: 2px solid #0284c7; transform: rotate(45deg); background: #f0f9ff; }
    .leg-conn { width: 22px; height: 22px; border: 2px solid #6366f1; border-radius: 50%; background: #eef2ff; }
  </style>
</head>
<body>

  <!-- HEADER -->
  <div class="header">
    <h1>ACADEMIC UNIVERSE (AU) — STANDARD ANSI/ISO SYSTEM FLOWCHART</h1>
    <p>Formally Structured Using Only Standard Flowchart Primitives: Terminators, Processes, Decision Branches & On-Page Connectors</p>
    <div class="meta-bar">
      <span>Developer: <strong>Aashish Rajput</strong> (2023329421)</span>
      <span>Deployment: <strong>academicuniverse.vercel.app</strong></span>
      <span>Engine: <strong>Next.js 16 + Express + Gemini 2.5 Flash</strong></span>
      <span>Standard: <strong>ANSI / ISO 5807 Compliant</strong></span>
    </div>
  </div>

  <!-- 5-COLUMN FLOWCHART GRID -->
  <div class="flowchart-grid">

    <!-- COLUMN 1: AUTH & ROUTING -->
    <div class="column">
      <div class="column-title">1. Access & Routing</div>

      <div class="flow-stack">
        <div class="shape-terminator start">Start</div>

        <div class="arrow-down"><div class="arrow-line"></div><div class="arrow-head"></div></div>

        <div class="shape-process">
          <div class="proc-title">Load /login Portal</div>
          <div class="proc-desc">Detect institutional domains (@ug.sharda.ac.in)</div>
        </div>

        <div class="arrow-down"><div class="arrow-line"></div><div class="arrow-head"></div></div>

        <div class="decision-wrapper">
          <div class="shape-decision"></div>
          <div class="decision-text">Valid Domain?</div>
          <div class="choice-label choice-yes">Yes</div>
        </div>

        <div class="arrow-down"><div class="arrow-line"></div><div class="arrow-head"></div></div>

        <div class="shape-process">
          <div class="proc-title">Google OAuth 2.0 Client</div>
          <div class="proc-desc">Exchange token via Firebase Auth backend</div>
        </div>

        <div class="arrow-down"><div class="arrow-line"></div><div class="arrow-head"></div></div>

        <div class="shape-process">
          <div class="proc-title">JWT Generation & Cookie</div>
          <div class="proc-desc">Resolve User in MongoDB; emit RS256 token</div>
        </div>

        <div class="arrow-down"><div class="arrow-line"></div><div class="arrow-head"></div></div>

        <div class="decision-wrapper">
          <div class="shape-decision"></div>
          <div class="decision-text">Select Module?</div>
        </div>

        <div class="arrow-down"><div class="arrow-line"></div><div class="arrow-head"></div></div>

        <!-- 4 CONNECTORS ROW -->
        <div style="display: flex; gap: 14px; justify-content: center; width: 100%;">
          <div style="text-align: center;"><div class="shape-connector">A</div><div style="font-size: 11px; font-weight: 700; color: #475569; margin-top: 4px;">E-Zone</div></div>
          <div style="text-align: center;"><div class="shape-connector">B</div><div style="font-size: 11px; font-weight: 700; color: #475569; margin-top: 4px;">AI Bot</div></div>
          <div style="text-align: center;"><div class="shape-connector">C</div><div style="font-size: 11px; font-weight: 700; color: #475569; margin-top: 4px;">Overlap</div></div>
          <div style="text-align: center;"><div class="shape-connector">D</div><div style="font-size: 11px; font-weight: 700; color: #475569; margin-top: 4px;">Research</div></div>
        </div>

      </div>
    </div>

    <!-- COLUMN 2: ENGINE A - E-ZONE SYNC -->
    <div class="column">
      <div class="column-title">2. Engine A: E-Zone Sync</div>

      <div class="flow-stack">
        <div class="shape-connector">A</div>

        <div class="arrow-down"><div class="arrow-line"></div><div class="arrow-head"></div></div>

        <div class="shape-process">
          <div class="proc-title">Input System ID</div>
          <div class="proc-desc">Student inputs ID (e.g. 2023329421)</div>
        </div>

        <div class="arrow-down"><div class="arrow-line"></div><div class="arrow-head"></div></div>

        <div class="shape-process">
          <div class="proc-title">Trigger Webmail OTP</div>
          <div class="proc-desc">Send 6-digit 2FA OTP to institutional inbox</div>
        </div>

        <div class="arrow-down"><div class="arrow-line"></div><div class="arrow-head"></div></div>

        <div class="decision-wrapper">
          <div class="shape-decision"></div>
          <div class="decision-text">OTP Valid?</div>
          <div class="choice-label choice-yes">Yes</div>
        </div>

        <div class="arrow-down"><div class="arrow-line"></div><div class="arrow-head"></div></div>

        <div class="shape-process">
          <div class="proc-title">Playwright Scraper</div>
          <div class="proc-desc">Headless Chromium parses timetable DOM</div>
        </div>

        <div class="arrow-down"><div class="arrow-line"></div><div class="arrow-head"></div></div>

        <div class="shape-process">
          <div class="proc-title">Dual Persistence</div>
          <div class="proc-desc">Save to MongoDB Atlas + Google Sheets stream</div>
        </div>

        <div class="arrow-down"><div class="arrow-line"></div><div class="arrow-head"></div></div>

        <div class="shape-connector">E</div>
      </div>
    </div>

    <!-- COLUMN 3: ENGINE B - CAMPUS AI -->
    <div class="column">
      <div class="column-title">3. Engine B: Campus AI</div>

      <div class="flow-stack">
        <div class="shape-connector">B</div>

        <div class="arrow-down"><div class="arrow-line"></div><div class="arrow-head"></div></div>

        <div class="shape-process">
          <div class="proc-title">Student Chat Query</div>
          <div class="proc-desc">"Where is my Research Methodology lecture?"</div>
        </div>

        <div class="arrow-down"><div class="arrow-line"></div><div class="arrow-head"></div></div>

        <div class="shape-process">
          <div class="proc-title">Query MongoDB RAG</div>
          <div class="proc-desc">Match student ID in AcademicSchedule table</div>
        </div>

        <div class="arrow-down"><div class="arrow-line"></div><div class="arrow-head"></div></div>

        <div class="decision-wrapper">
          <div class="shape-decision"></div>
          <div class="decision-text">Slot Found?</div>
          <div class="choice-label choice-yes">Yes</div>
        </div>

        <div class="arrow-down"><div class="arrow-line"></div><div class="arrow-head"></div></div>

        <div class="shape-process">
          <div class="proc-title">Inject Classroom Context</div>
          <div class="proc-desc">Room 206 Block 3, Dr. Batri K + Guardrails</div>
        </div>

        <div class="arrow-down"><div class="arrow-line"></div><div class="arrow-head"></div></div>

        <div class="shape-process">
          <div class="proc-title">Gemini 2.5 Inference</div>
          <div class="proc-desc">Stream factually verified answer to student</div>
        </div>

        <div class="arrow-down"><div class="arrow-line"></div><div class="arrow-head"></div></div>

        <div class="shape-connector">E</div>
      </div>
    </div>

    <!-- COLUMN 4: ENGINE C - OVERLAP PLANNER -->
    <div class="column">
      <div class="column-title">4. Engine C: Overlap Plan</div>

      <div class="flow-stack">
        <div class="shape-connector">C</div>

        <div class="arrow-down"><div class="arrow-line"></div><div class="arrow-head"></div></div>

        <div class="shape-process">
          <div class="proc-title">Host Resolution Card</div>
          <div class="proc-desc">Aashish Rajput (2023329421) detected</div>
        </div>

        <div class="arrow-down"><div class="arrow-line"></div><div class="arrow-head"></div></div>

        <div class="shape-process">
          <div class="proc-title">Search Peer Directory</div>
          <div class="proc-desc">Lookup Vishal Sharma (2024427058)</div>
        </div>

        <div class="arrow-down"><div class="arrow-line"></div><div class="arrow-head"></div></div>

        <div class="decision-wrapper">
          <div class="shape-decision"></div>
          <div class="decision-text">Synced Schedule?</div>
          <div class="choice-label choice-yes">Yes</div>
        </div>

        <div class="arrow-down"><div class="arrow-line"></div><div class="arrow-head"></div></div>

        <div class="shape-process">
          <div class="proc-title">Set Intersection Engine</div>
          <div class="proc-desc">Compute: Free(All) = Free(Host) ∩ ⋂ Free(Peers)</div>
        </div>

        <div class="arrow-down"><div class="arrow-line"></div><div class="arrow-head"></div></div>

        <div class="shape-process">
          <div class="proc-title">Ranked Meet Blocks</div>
          <div class="proc-desc">Aggregate 1h/2h free study slots & invite</div>
        </div>

        <div class="arrow-down"><div class="arrow-line"></div><div class="arrow-head"></div></div>

        <div class="shape-connector">E</div>
      </div>
    </div>

    <!-- COLUMN 5: ENGINE D - RESEARCH WING & END -->
    <div class="column">
      <div class="column-title">5. Engine D & Termination</div>

      <div class="flow-stack">
        <div class="shape-connector">D</div>

        <div class="arrow-down"><div class="arrow-line"></div><div class="arrow-head"></div></div>

        <div class="shape-process">
          <div class="proc-title">1. Topic & Gap Discovery</div>
          <div class="proc-desc">AI explores novel research domains & scope</div>
        </div>

        <div class="arrow-down"><div class="arrow-line"></div><div class="arrow-head"></div></div>

        <div class="shape-process">
          <div class="proc-title">2 & 3. Outline & Drafting</div>
          <div class="proc-desc">IEEE multi-tier sections with LaTeX formulas</div>
        </div>

        <div class="arrow-down"><div class="arrow-line"></div><div class="arrow-head"></div></div>

        <div class="shape-process">
          <div class="proc-title">4 & 5. Citations & Export</div>
          <div class="proc-desc">BibTeX indexing; 1-click PDF & DOCX compile</div>
        </div>

        <div class="arrow-down"><div class="arrow-line"></div><div class="arrow-head"></div></div>

        <div class="shape-connector">E</div>

        <div class="arrow-down"><div class="arrow-line"></div><div class="arrow-head"></div></div>

        <div class="shape-process">
          <div class="proc-title">Update Dashboard State</div>
          <div class="proc-desc">Persist verified academic state in MongoDB</div>
        </div>

        <div class="arrow-down"><div class="arrow-line"></div><div class="arrow-head"></div></div>

        <div class="shape-terminator end">End</div>
      </div>
    </div>

  </div>

  <!-- LEGEND -->
  <div class="legend-box">
    <span style="font-weight: 800; font-size: 13px; color: #0f172a; margin-right: 8px;">ANSI/ISO Flowchart Legend:</span>
    <div class="legend-item"><div class="leg-term"></div> Terminator (Start / End)</div>
    <div class="legend-item"><div class="leg-proc"></div> Process (Action / Step)</div>
    <div class="legend-item"><div class="leg-dec"></div> Decision (Branch / Test)</div>
    <div class="legend-item"><div class="leg-conn"></div> Connector (A, B, C, D, E)</div>
  </div>

</body>
</html>`;

  const htmlPath = path.join(process.cwd(), 'scratch', 'standard_flowchart.html');
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
  await page.waitForTimeout(2000);

  const rawPngPath = path.join(process.cwd(), 'scratch', 'standard_flowchart_raw.png');
  await page.screenshot({ path: rawPngPath, fullPage: true });
  console.log('4K Screenshot captured at:', rawPngPath);

  await browser.close();

  // Run Python script to set 500 DPI metadata and save final PNG
  const finalPngPath = path.join(process.cwd(), 'Academic_Universe_Standard_Flowchart_4K_500DPI.png');
  const pyDpiScript = `
from PIL import Image
im = Image.open(r"${rawPngPath.replace(/\\/g, '/')}")
im.save(r"${finalPngPath.replace(/\\/g, '/')}", dpi=(500, 500), compress_level=1)
print(f"Final Standard 4K 500DPI PNG generated successfully: {im.size} at 500 DPI")
`;

  fs.writeFileSync(path.join(process.cwd(), 'scratch', 'set_standard_dpi.py'), pyDpiScript, 'utf-8');
  execSync('python scratch/set_standard_dpi.py', { stdio: 'inherit' });

  console.log('SUCCESS! Standard Flowchart saved at:', finalPngPath);
}

renderStandardFlowchart().catch(err => {
  console.error('Error rendering standard flowchart:', err);
  process.exit(1);
});
