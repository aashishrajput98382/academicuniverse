const fs = require('fs');
const path = require('path');
const { chromium } = require(path.resolve(__dirname, '../backend/node_modules/playwright'));

async function generateFlowchart() {
  console.log('Rendering Deepfake Video Authentication Architecture Flowchart...');

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
      padding: 16px;
    }

    /* Diagram Outer Container */
    .diagram-container {
      width: 100%;
      background: #ffffff;
      border: 2px solid #cbd5e1;
      border-radius: 14px;
      padding: 22px 20px;
      box-shadow: 0 4px 16px -2px rgba(0, 0, 0, 0.05);
    }

    /* Header Banner */
    .diagram-header {
      text-align: center;
      padding-bottom: 16px;
      border-bottom: 2px solid #e2e8f0;
      margin-bottom: 18px;
    }

    .diagram-badge {
      display: inline-block;
      font-family: 'JetBrains Mono', monospace;
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 1.2px;
      text-transform: uppercase;
      color: #1e40af;
      background: #eff6ff;
      border: 1px solid #bfdbfe;
      padding: 3px 12px;
      border-radius: 20px;
      margin-bottom: 6px;
    }

    .diagram-title {
      font-size: 22px;
      font-weight: 800;
      color: #0f172a;
      letter-spacing: -0.4px;
      line-height: 1.25;
    }

    .diagram-subtitle {
      font-size: 13.5px;
      color: #64748b;
      margin-top: 4px;
      font-weight: 500;
    }

    /* Pipeline Flow */
    .pipeline {
      display: flex;
      flex-direction: column;
      gap: 12px;
      position: relative;
    }

    /* Stage Card */
    .stage-card {
      background: #f8fafc;
      border: 2px solid #e2e8f0;
      border-radius: 12px;
      padding: 14px 16px;
      position: relative;
    }

    /* Stage specific colors */
    .stage-1 {
      border-color: #93c5fd;
      background: #f0f7ff;
    }
    .stage-2 {
      border-color: #a5b4fc;
      background: #f5f3ff;
    }
    .stage-3 {
      border-color: #fcd34d;
      background: #fffbeb;
    }
    .stage-4 {
      border-color: #86efac;
      background: #f0fdf4;
    }

    .stage-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 12px;
      padding-bottom: 6px;
      border-bottom: 1.5px dashed rgba(0,0,0,0.1);
    }

    .stage-pill {
      font-family: 'JetBrains Mono', monospace;
      font-size: 11.5px;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 6px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .stage-1 .stage-pill { background: #dbeafe; color: #1e40af; border: 1px solid #bfdbfe; }
    .stage-2 .stage-pill { background: #ede9fe; color: #5b21b6; border: 1px solid #ddd6fe; }
    .stage-3 .stage-pill { background: #fef3c7; color: #92400e; border: 1px solid #fde68a; }
    .stage-4 .stage-pill { background: #dcfce7; color: #166534; border: 1px solid #bbf7d0; }

    .stage-name {
      font-size: 15px;
      font-weight: 700;
      color: #0f172a;
    }

    /* Node Grid inside stage */
    .node-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
    }

    .node-box {
      flex: 1;
      background: #ffffff;
      border: 1.5px solid #cbd5e1;
      border-radius: 8px;
      padding: 10px 8px;
      text-align: center;
      min-height: 74px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
    }

    .node-title {
      font-size: 13.5px;
      font-weight: 700;
      color: #0f172a;
      line-height: 1.25;
      margin-bottom: 3px;
    }

    .node-desc {
      font-size: 11.5px;
      color: #64748b;
      font-weight: 500;
      line-height: 1.2;
    }

    /* Flow Connectors */
    .arrow-right {
      color: #64748b;
      font-size: 18px;
      font-weight: 800;
      user-select: none;
      flex-shrink: 0;
    }

    .arrow-down-sub {
      display: flex;
      justify-content: center;
      align-items: center;
      color: #3b82f6;
      font-size: 16px;
      font-weight: 800;
      margin: 4px 0;
    }

    .arrow-down-container {
      display: flex;
      justify-content: center;
      align-items: center;
      margin: -6px 0;
    }

    .arrow-down-badge {
      background: #ffffff;
      border: 2px solid #cbd5e1;
      color: #334155;
      width: 28px;
      height: 28px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 15px;
      font-weight: 800;
      box-shadow: 0 2px 4px rgba(0,0,0,0.06);
      z-index: 2;
    }

    /* Key Output Highlights */
    .highlight-badge {
      display: inline-block;
      margin-top: 3px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 10px;
      font-weight: 600;
      padding: 1px 5px;
      border-radius: 4px;
      background: #f1f5f9;
      color: #475569;
    }
  </style>
</head>
<body>

  <div class="diagram-container">
    <div class="diagram-header">
      <div class="diagram-badge">SYSTEM ARCHITECTURE WORKFLOW</div>
      <h1 class="diagram-title">Explainable Spatial-Temporal Deepfake Video Authentication Framework</h1>
      <p class="diagram-subtitle">Integrated pipeline from raw video ingest to forensic temporal localization and trust scoring</p>
    </div>

    <div class="pipeline">
      <!-- STAGE 1 -->
      <div class="stage-card stage-1">
        <div class="stage-header">
          <span class="stage-name">Phase 1: Video Ingest & Facial Sequence Preprocessing</span>
          <span class="stage-pill">Preprocessing</span>
        </div>
        
        <!-- Row 1: Ingest & Frame Sampling -->
        <div class="node-row" style="margin-bottom: 6px;">
          <div class="node-box" style="border-left: 4px solid #3b82f6;">
            <div class="node-title">Input Video (V)</div>
            <div class="node-desc">Raw video stream ingest</div>
            <span class="highlight-badge">V = {F₁, ..., F_T}</span>
          </div>
          <div class="arrow-right">→</div>
          <div class="node-box">
            <div class="node-title">Video Preprocessing</div>
            <div class="node-desc">Decoding & color normalization</div>
          </div>
          <div class="arrow-right">→</div>
          <div class="node-box">
            <div class="node-title">Frame Sampling</div>
            <div class="node-desc">Uniform temporal rate sampling</div>
            <span class="highlight-badge">16 frames / clip</span>
          </div>
        </div>

        <div class="arrow-down-sub">↓</div>

        <!-- Row 2: Face Detection & Sequence Construction -->
        <div class="node-row">
          <div class="node-box">
            <div class="node-title">Face Detection & Alignment</div>
            <div class="node-desc">Facial landmark extraction & pose normalization</div>
          </div>
          <div class="arrow-right">→</div>
          <div class="node-box" style="border-right: 4px solid #3b82f6;">
            <div class="node-title">Facial Sequence Construction</div>
            <div class="node-desc">Aligned face crops formatted for spatio-temporal modeling</div>
            <span class="highlight-badge">T × C × H × W</span>
          </div>
        </div>
      </div>

      <!-- DOWN CONNECTOR -->
      <div class="arrow-down-container">
        <div class="arrow-down-badge">↓</div>
      </div>

      <!-- STAGE 2 -->
      <div class="stage-card stage-2">
        <div class="stage-header">
          <span class="stage-name">Phase 2: Dual Spatial-Temporal Feature Learning</span>
          <span class="stage-pill">Representation Learning</span>
        </div>
        <div class="node-row">
          <div class="node-box" style="border-left: 4px solid #6366f1;">
            <div class="node-title">Xception Spatial Feature Extraction</div>
            <div class="node-desc">Frame-level visual artifacts & warping boundaries</div>
            <span class="highlight-badge">f_spatial ∈ ℝ^D</span>
          </div>
          <div class="arrow-right">→</div>
          <div class="node-box">
            <div class="node-title">Temporal Transformer Learning</div>
            <div class="node-desc">Multi-head self-attention models temporal continuity</div>
            <span class="highlight-badge">f_temporal ∈ ℝ^D</span>
          </div>
          <div class="arrow-right">→</div>
          <div class="node-box" style="border-right: 4px solid #6366f1;">
            <div class="node-title">Spatial-Temporal Feature Fusion</div>
            <div class="node-desc">Unified representation joining spatial & temporal cues</div>
            <span class="highlight-badge">F_ST = [f_s, f_t]</span>
          </div>
        </div>
      </div>

      <!-- DOWN CONNECTOR -->
      <div class="arrow-down-container">
        <div class="arrow-down-badge">↓</div>
      </div>

      <!-- STAGE 3 -->
      <div class="stage-card stage-3">
        <div class="stage-header">
          <span class="stage-name">Phase 3: Decision Classification & Explainable AI (XAI)</span>
          <span class="stage-pill">Inference & Explainability</span>
        </div>
        <div class="node-row">
          <div class="node-box" style="border-left: 4px solid #f59e0b;">
            <div class="node-title">Deepfake Classification</div>
            <div class="node-desc">Calibrated prediction head yields binary probability</div>
            <span class="highlight-badge">P(manipulated)</span>
          </div>
          <div class="arrow-right">→</div>
          <div class="node-box">
            <div class="node-title">Temporal Suspicion Analysis</div>
            <div class="node-desc">Frame-by-frame anomaly curve evaluation</div>
            <span class="highlight-badge">S(t) profile</span>
          </div>
          <div class="arrow-right">→</div>
          <div class="node-box" style="border-right: 4px solid #f59e0b;">
            <div class="node-title">Explainable AI (XAI)</div>
            <div class="node-desc">Grad-CAM heatmaps & attention weight attribution</div>
            <span class="highlight-badge">Spatial + Temporal XAI</span>
          </div>
        </div>
      </div>

      <!-- DOWN CONNECTOR -->
      <div class="arrow-down-container">
        <div class="arrow-down-badge">↓</div>
      </div>

      <!-- STAGE 4 -->
      <div class="stage-card stage-4">
        <div class="stage-header">
          <span class="stage-name">Phase 4: Forensic Localization & Authentication Dashboard</span>
          <span class="stage-pill">Forensic Output</span>
        </div>
        <div class="node-row">
          <div class="node-box" style="border-left: 4px solid #10b981;">
            <div class="node-title">Suspicious Segment Localization</div>
            <div class="node-desc">Pinpoints anomalous intervals with timestamps</div>
            <span class="highlight-badge">e.g. 00:03 - 00:05</span>
          </div>
          <div class="arrow-right">→</div>
          <div class="node-box">
            <div class="node-title">Authenticity Trust Score</div>
            <div class="node-desc">Confidence-calibrated forensic trust metric</div>
            <span class="highlight-badge">0% - 100% Calibrated</span>
          </div>
          <div class="arrow-right">→</div>
          <div class="node-box" style="border-right: 4px solid #10b981;">
            <div class="node-title">Authentication Dashboard</div>
            <div class="node-desc">Interactive forensic interface for evidence review</div>
            <span class="highlight-badge">Forensic Audit UI</span>
          </div>
        </div>
      </div>
    </div>
  </div>

</body>
</html>`;

  const outputPath = path.resolve('ashmitxnaik/deepfake_architecture_flowchart.png');
  const tempHtmlPath = path.resolve('scratch/temp_deepfake_flowchart.html');
  fs.writeFileSync(tempHtmlPath, html, 'utf8');

  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({
    viewport: { width: 1020, height: 1300 },
    deviceScaleFactor: 2.5 // Crisp 300+ DPI output
  });

  await page.goto('file:///' + tempHtmlPath.replace(/\\/g, '/'), { waitUntil: 'networkidle' });
  const container = await page.$('.diagram-container');
  await container.screenshot({ path: outputPath, omitBackground: false });
  await browser.close();

  console.log('Saved high-res flowchart to:', outputPath);
}

generateFlowchart().catch(err => {
  console.error('Error generating flowchart:', err);
  process.exit(1);
});
