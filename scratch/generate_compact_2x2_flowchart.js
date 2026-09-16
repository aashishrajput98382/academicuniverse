const fs = require('fs');
const path = require('path');
const { chromium } = require(path.resolve(__dirname, '../backend/node_modules/playwright'));

async function generateCompactFlowchart() {
  console.log('Rendering 2x2 Compact Academic Architecture Flowchart...');

  const html = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;600;700&display=swap');

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      width: 980px;
      background-color: #ffffff;
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      color: #1e293b;
      padding: 8px;
    }

    .diagram-container {
      width: 100%;
      background: #ffffff;
      border: 1.5px solid #cbd5e1;
      border-radius: 10px;
      padding: 12px 14px;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
    }

    /* Compact Header */
    .diagram-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-bottom: 8px;
      border-bottom: 1.5px solid #e2e8f0;
      margin-bottom: 10px;
    }

    .diagram-title {
      font-size: 15.5px;
      font-weight: 800;
      color: #0f172a;
      letter-spacing: -0.3px;
    }

    .diagram-badge {
      font-family: 'JetBrains Mono', monospace;
      font-size: 10.5px;
      font-weight: 700;
      letter-spacing: 0.8px;
      text-transform: uppercase;
      color: #1e40af;
      background: #eff6ff;
      border: 1px solid #bfdbfe;
      padding: 2px 8px;
      border-radius: 12px;
    }

    /* 2x2 Grid Layout */
    .grid-2x2 {
      display: grid;
      grid-template-columns: 1fr 28px 1fr;
      grid-template-rows: auto 24px auto;
      align-items: center;
      gap: 0;
    }

    /* Cards */
    .card {
      border: 1.5px solid #cbd5e1;
      border-radius: 8px;
      padding: 9px 10px;
      background: #f8fafc;
    }

    .card-1 { grid-column: 1; grid-row: 1; border-color: #93c5fd; background: #f0f7ff; }
    .card-2 { grid-column: 3; grid-row: 1; border-color: #a5b4fc; background: #f5f3ff; }
    .card-3 { grid-column: 1; grid-row: 3; border-color: #fcd34d; background: #fffbeb; }
    .card-4 { grid-column: 3; grid-row: 3; border-color: #86efac; background: #f0fdf4; }

    .card-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 6px;
      padding-bottom: 4px;
      border-bottom: 1px dashed rgba(0,0,0,0.12);
    }

    .card-title {
      font-size: 12px;
      font-weight: 800;
      color: #0f172a;
    }

    .card-tag {
      font-family: 'JetBrains Mono', monospace;
      font-size: 9.5px;
      font-weight: 700;
      padding: 1px 6px;
      border-radius: 4px;
      text-transform: uppercase;
    }

    .card-1 .card-tag { background: #dbeafe; color: #1e40af; }
    .card-2 .card-tag { background: #ede9fe; color: #5b21b6; }
    .card-3 .card-tag { background: #fef3c7; color: #92400e; }
    .card-4 .card-tag { background: #dcfce7; color: #166534; }

    /* Steps list inside card */
    .step-list {
      display: flex;
      flex-direction: column;
      gap: 4px;
    }

    .step-item {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 5px;
      padding: 4px 7px;
      font-size: 11px;
      color: #334155;
      display: flex;
      align-items: center;
      justify-content: space-between;
      line-height: 1.2;
    }

    .step-item b {
      color: #0f172a;
      font-weight: 700;
    }

    .sub-code {
      font-family: 'JetBrains Mono', monospace;
      font-size: 9.5px;
      color: #64748b;
      background: #f1f5f9;
      padding: 1px 4px;
      border-radius: 3px;
    }

    /* Grid Connectors */
    .connector-h1 {
      grid-column: 2;
      grid-row: 1;
      text-align: center;
      font-size: 16px;
      font-weight: 900;
      color: #64748b;
    }

    .connector-v {
      grid-column: 3;
      grid-row: 2;
      text-align: center;
      font-size: 15px;
      font-weight: 900;
      color: #64748b;
    }

    .connector-h2 {
      grid-column: 2;
      grid-row: 3;
      text-align: center;
      font-size: 16px;
      font-weight: 900;
      color: #64748b;
    }

    .connector-diag {
      grid-column: 1;
      grid-row: 2;
      display: flex;
      justify-content: center;
      align-items: center;
      font-size: 14px;
      font-weight: 900;
      color: #64748b;
    }
  </style>
</head>
<body>

  <div class="diagram-container">
    <div class="diagram-header">
      <div class="diagram-title">System Architecture: Explainable Spatial-Temporal Authentication</div>
      <div class="diagram-badge">End-to-End Pipeline</div>
    </div>

    <div class="grid-2x2">
      <!-- Card 1 -->
      <div class="card card-1">
        <div class="card-header">
          <span class="card-title">Phase 1: Ingest & Preprocessing</span>
          <span class="card-tag">Stage 1</span>
        </div>
        <div class="step-list">
          <div class="step-item"><span><b>Input Video</b> (Decode & Normalize)</span> <span class="sub-code">V = {F₁..F_T}</span></div>
          <div class="step-item"><span><b>Frame Sampling</b> (16 fps clip)</span> <span class="sub-code">Uniform</span></div>
          <div class="step-item"><span><b>Face Detection & Sequence</b></span> <span class="sub-code">Aligned Crops</span></div>
        </div>
      </div>

      <div class="connector-h1">→</div>

      <!-- Card 2 -->
      <div class="card card-2">
        <div class="card-header">
          <span class="card-title">Phase 2: Dual Feature Learning</span>
          <span class="card-tag">Stage 2</span>
        </div>
        <div class="step-list">
          <div class="step-item"><span><b>Xception Spatial Features</b></span> <span class="sub-code">f_spatial</span></div>
          <div class="step-item"><span><b>Temporal Transformer Learning</b></span> <span class="sub-code">Multi-Head Attn</span></div>
          <div class="step-item"><span><b>Spatial-Temporal Fusion</b></span> <span class="sub-code">F_ST = [f_s, f_t]</span></div>
        </div>
      </div>

      <!-- Vertical Transition: From Card 2 down to Card 3 or Card 4 -->
      <!-- Let's do: Card 1 -> Card 2 -> Card 3 -> Card 4 or Card 1 -> Card 2, then down to Card 4, or Card 2 down to Card 3 -->
      <div class="connector-diag">↓</div>
      <div style="grid-column: 2; grid-row: 2;"></div>
      <div class="connector-v">↓</div>

      <!-- Card 3 -->
      <div class="card card-3">
        <div class="card-header">
          <span class="card-title">Phase 3: Decision & Explainability</span>
          <span class="card-tag">Stage 3</span>
        </div>
        <div class="step-list">
          <div class="step-item"><span><b>Deepfake Classification Head</b></span> <span class="sub-code">P(fake | V)</span></div>
          <div class="step-item"><span><b>Temporal Suspicion Analysis</b></span> <span class="sub-code">S(t) profile</span></div>
          <div class="step-item"><span><b>Explainable AI (XAI)</b></span> <span class="sub-code">Grad-CAM + Attn</span></div>
        </div>
      </div>

      <div class="connector-h2">→</div>

      <!-- Card 4 -->
      <div class="card card-4">
        <div class="card-header">
          <span class="card-title">Phase 4: Forensic Localization</span>
          <span class="card-tag">Stage 4</span>
        </div>
        <div class="step-list">
          <div class="step-item"><span><b>Suspicious Segment Localization</b></span> <span class="sub-code">Intervals [t₁, t₂]</span></div>
          <div class="step-item"><span><b>Authenticity Trust Score</b></span> <span class="sub-code">0% – 100%</span></div>
          <div class="step-item"><span><b>Authentication Dashboard</b></span> <span class="sub-code">Forensic UI</span></div>
        </div>
      </div>
    </div>
  </div>

</body>
</html>`;

  const outputPath = path.resolve('ashmitxnaik/deepfake_architecture_flowchart_compact.png');
  const tempHtmlPath = path.resolve('scratch/temp_compact_flowchart.html');
  fs.writeFileSync(tempHtmlPath, html, 'utf8');

  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({
    viewport: { width: 1000, height: 600 },
    deviceScaleFactor: 2.5
  });

  await page.goto('file:///' + tempHtmlPath.replace(/\\/g, '/'), { waitUntil: 'networkidle' });
  const container = await page.$('.diagram-container');
  await container.screenshot({ path: outputPath, omitBackground: false });
  await browser.close();

  console.log('Saved compact 2x2 flowchart to:', outputPath);
}

generateCompactFlowchart().catch(err => {
  console.error(err);
  process.exit(1);
});
