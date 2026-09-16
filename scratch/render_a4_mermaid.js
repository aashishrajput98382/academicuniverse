const path = require('path');
const fs = require('fs');
const { chromium } = require(path.resolve('backend/node_modules/playwright'));

async function renderMermaidToA4(mermaidCode, outImage, isLandscape = false) {
  const width = isLandscape ? 1754 : 1240;
  const height = isLandscape ? 1240 : 1754;

  const browser = await chromium.launch();
  const page = await browser.newPage({
    viewport: { width, height }
  });

  const html = `<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap');
    
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    html, body {
      width: ${width}px;
      height: ${height}px;
      overflow: hidden;
      background: #ffffff;
      font-family: 'Plus Jakarta Sans', sans-serif;
    }
    .page-container {
      width: 100%;
      height: 100%;
      padding: 24px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
    }
    .mermaid {
      width: 100%;
      height: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
    }
    .mermaid svg {
      width: 100% !important;
      height: 100% !important;
      max-width: 100% !important;
      max-height: 100% !important;
    }
  </style>
</head>
<body>
  <div class="page-container">
    <div class="mermaid">
${mermaidCode}
    </div>
  </div>
  <script>
    mermaid.initialize({
      startOnLoad: true,
      securityLevel: 'loose',
      theme: 'base',
      themeVariables: {
        fontSize: '15pt',
        fontFamily: "'Plus Jakarta Sans', sans-serif"
      }
    });
  </script>
</body>
</html>`;

  await page.setContent(html, { waitUntil: 'networkidle' });
  await page.waitForTimeout(1500);

  // Check if svg rendered
  const hasSvg = await page.evaluate(() => !!document.querySelector('.mermaid svg'));
  const errorText = await page.evaluate(() => document.querySelector('.mermaid')?.innerText || '');
  console.log('Render status:', { hasSvg, errorText: hasSvg ? 'OK' : errorText });

  await page.screenshot({ path: outImage, fullPage: false });
  await browser.close();
  console.log(`Saved screenshot to ${outImage}`);
}

module.exports = { renderMermaidToA4 };
