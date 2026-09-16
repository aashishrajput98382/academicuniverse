const fs = require('fs');
const path = require('path');
const { chromium } = require(path.resolve(__dirname, '../backend/node_modules/playwright'));

async function generateHorizontalFlowchart() {
  console.log('Rendering 4-Stage Horizontal Linear Architecture Flowchart...');

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
      width: 1040px;
      background-color: #ffffff;
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      color: #1e293b;
      padding: 10px;
    }

    .diagram-container {
      width: 100%;
      background: #ffffff;
      border: 1.5px solid #cbd5e1;
      border-radius: 10px;
      padding: 12px 14px;
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.04);
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
      font-size: 16px;
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

    /* 4-Stage Horizontal Row */
    .stages-row {
      display: flex;
      align-items: stretch;
      gap: 8px;
    }

    .arrow-col {
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 18px;
      font-weight: 900;
      color: #64748b;
      user-select: none;
      flex-shrink: 0;
    }

    /* Stage Card */
    .stage-card {
      flex: 1;
      border: 1.5px solid #cbd5e1;
      border-radius: 8px;
      padding: 8px 9px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    .card-1 { border-color: #93c5fd; background: #f0f7ff; }
    .card-2 { border-color: #a5b4fc; background: #f5f3ff; }
    .card-3 { border-color: #fcd34d; background: #fffbeb; }
    .card-4 { border-color: #86efac; background: #f0fdf4; }

    .card-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 7px;
      padding-bottom: 4px;
      border-bottom: 1px dashed rgba(0,0,0,0.12);
    }

    .card-title {
      font-size: 12px;
      font-weight: 800;
      color: #0f172a;
      line-height: 1.2;
    }

    .card-tag {
      font-family: 'JetBrains Mono', monospace;
      font-size: 9px;
      font-weight: 700;
      padding: 1px 5px;
      border-radius: 4px;
      text-transform: uppercase;
      flex-shrink: 0;
    }

    .card-1 .card-tag { background: #dbeafe; color: #1e40af; }
    .card-2 .card-tag { background: #ede9fe; color: #5b21b6; }
    .card-3 .card-tag { background: #fef3c7; color: #92400e; }
    .card-4 .card-tag { background: #dcfce7; color: #166534; }

    /* Steps list */
    .step-list {
      display: flex;
      flex-direction: column;
      gap: 5px;
      flex-grow: 1;
    }

    .step-item {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 5px;
      padding: 5px 6px;
      display: flex;
      flex-direction: column;
      gap: 2px;
    }

    .step-title {
      font-size: 11px;
      font-weight: 700;
      color: #0f172a;
      line-height: 1.2;
    }

    .step-desc {
      font-size: 9.5px;
      color: #64748b;
      line-height: 1.2;
    }

    .sub-code {
      font-family: 'JetBrains Mono', monospace;
      font-size: 9px;
      color: #475569;
      background: #f1f5f9;
      padding: 1px 4px;
      border-radius: 3px;
      align-self: flex-start;
      margin-top: 1px;
    }
  </style>
</head>
<body>

  <div class="diagram-container">
    <div class="diagram-header">
      <div class="diagram-title">System Architecture: Explainable Spatial-Temporal Deepfake Video Authentication</div>
      <div class="diagram-badge">End-to-End Pipeline</div>
    </div>

    <div class="stages-row">
      <!-- Stage 1 -->
      <div class="stage-card card-1">
        <div class="card-header">
          <span class="card-title">Phase 1: Video Ingest</span>
          <span class="card-tag">Stage 1</span>
        </div>
        <div class="step-list">
          <div class="step-item">
            <span class="step-title">Input Video Stream</span>
            <span class="step-desc">Decode & frame sampling</span>
            <span class="sub-code">V = {F₁...F_T}</span>
          </div>
          <div class="step-item">
            <span class="step-title">Face Detection</span>
            <span class="step-desc">Landmark alignment</span>
            <span class="sub-code">MTCNN / RetinaFace</span>
          </div>
          <div class="step-item">
            <span class="step-title">Facial Sequence</span>
            <span class="step-desc">Normalized facial crops</span>
            <span class="sub-code">T × C × H × W</span>
          </div>
        </div>
      </div>

      <div class="arrow-col">→</div>

      <!-- Stage 2 -->
      <div class="stage-card card-2">
        <div class="card-header">
          <span class="card-title">Phase 2: Representation</span>
          <span class="card-tag">Stage 2</span>
        </div>
        <div class="step-list">
          <div class="step-item">
            <span class="step-title">Xception Spatial CNN</span>
            <span class="step-desc">Frame-level visual artifacts</span>
            <span class="sub-code">f_spatial ∈ ℝ^D</span>
          </div>
          <div class="step-item">
            <span class="step-title">Temporal Transformer</span>
            <span class="step-desc">Multi-head self-attention</span>
            <span class="sub-code">f_temporal ∈ ℝ^D</span>
          </div>
          <div class="step-item">
            <span class="step-title">Feature Fusion</span>
            <span class="step-desc">Combined representations</span>
            <span class="sub-code">F_ST = [f_s, f_t]</span>
          </div>
        </div>
      </div>

      <div class="arrow-col">→</div>

      <!-- Stage 3 -->
      <div class="stage-card card-3">
        <div class="card-header">
          <span class="card-title">Phase 3: Decision & XAI</span>
          <span class="card-tag">Stage 3</span>
        </div>
        <div class="step-list">
          <div class="step-item">
            <span class="step-title">Deepfake Classifier</span>
            <span class="step-desc">Binary forgery probability</span>
            <span class="sub-code">P(manipulated | V)</span>
          </div>
          <div class="step-item">
            <span class="step-title">Suspicion Trajectory</span>
            <span class="step-desc">Sequence-level risk profile</span>
            <span class="sub-code">S(t) profile curve</span>
          </div>
          <div class="step-item">
            <span class="step-title">Explainable AI (XAI)</span>
            <span class="step-desc">Spatial & temporal attribution</span>
            <span class="sub-code">Grad-CAM + Attn</span>
          </div>
        </div>
      </div>

      <div class="arrow-col">→</div>

      <!-- Stage 4 -->
      <div class="stage-card card-4">
        <div class="card-header">
          <span class="card-title">Phase 4: Forensic Output</span>
          <span class="card-tag">Stage 4</span>
        </div>
        <div class="step-list">
          <div class="step-item">
            <span class="step-title">Segment Localization</span>
            <span class="step-desc">Suspicious interval bounds</span>
            <span class="sub-code">e.g. 00:03 - 00:05</span>
          </div>
          <div class="step-item">
            <span class="step-title">Authenticity Trust Score</span>
            <span class="step-desc">Calibrated reliability index</span>
            <span class="sub-code">0% – 100% Calibrated</span>
          </div>
          <div class="step-item">
            <span class="step-title">Forensic Dashboard</span>
            <span class="step-desc">Interactive audit interface</span>
            <span class="sub-code">Evidence Visualizer</span>
          </div>
        </div>
      </div>
    </div>
  </div>

</body>
</html>`;

  const outputPath = path.resolve('ashmitxnaik/deepfake_architecture_flowchart_horizontal.png');
  const tempHtmlPath = path.resolve('scratch/temp_horizontal_flowchart.html');
  fs.writeFileSync(tempHtmlPath, html, 'utf8');

  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({
    viewport: { width: 1060, height: 400 },
    deviceScaleFactor: 2.5
  });

  await page.goto('file:///' + tempHtmlPath.replace(/\\/g, '/'), { waitUntil: 'networkidle' });
  const container = await page.$('.diagram-container');
  await container.screenshot({ path: outputPath, omitBackground: false });
  await browser.close();

  console.log('Saved horizontal linear flowchart to:', outputPath);
}

generateHorizontalFlowchart().catch(err => {
  console.error(err);
  process.exit(1);
});
