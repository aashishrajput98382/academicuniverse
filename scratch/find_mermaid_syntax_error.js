const path = require('path');
const { chromium } = require(path.resolve('backend/node_modules/playwright'));

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  
  const originalCode = `flowchart LR
    %% =========================
    %% Subsystem 1
    %% =========================
    subgraph S1["📄 SUBSYSTEM 1 · ACADEMIC DOCUMENT BENCHMARK GENERATOR"]
        direction TB

        A["⚙️ <b>Deterministic Seed &<br/>Schema Configuration</b>"]
        B["▦ <b>Typographic Template<br/>Compilation Engine</b>"]
        C["📄 <b>Vector PDFs · 300 DPI</b><br/>Certificates · Handouts · ID Cards"]
        D["🔍 <b>High-Resolution<br/>Rasterization Engine</b>"]
        E{"⑂ <b>14 Operator Optical<br/>Degradation Profiles</b>"}

        A --> B --> C --> D --> E

        subgraph Profiles[""]
            direction LR
            P4["🖼️ <b>Profile 4</b><br/>Pixel-Exact Ground Truth"]
            P3["↻ <b>Profile 3</b><br/>VB · Rotation"]
            P2A["▤ <b>Profile 2</b><br/>Modal Canvas"]
            P2B["▣ <b>Profile 2</b><br/>Scanner Copy"]
            P1["🖥️ <b>Profile 1</b><br/>Clean Digital"]
        end

        E -->|<b>Profiles</b>| P1

        DB[("🗄️ <b>AI UI DC Benchmark Suite</b><br/>JSON + rendered models + PDF files")]

        P4 --> DB
        P3 --> DB
        P2A --> DB
        P2B --> DB
        P1 --> DB
    end

    %% =========================
    %% Subsystem 2
    %% =========================
    subgraph S2["📈 SUBSYSTEM 2 · AI UI EVALUATION & DIAGNOSTIC SUBSYSTEM"]
        direction TB

        F["🎛️ <b>Decoupled Benchmark<br/>Controller</b><br/>Schema-only · no live DB mutation"]
        G["🧠 <b>Model Prediction Adapter</b><br/>MiniCPM-V · 7B · Q4 · local runtime"]
        H["{} <b>Raw Model Prediction</b><br/>JSON"]
        I{"☑️ <b>Evaluation Protocol</b><br/>Exact Match"}

        F --> G --> H --> I

        J["🔽 <b>Pass B · Normalized Mode</b><br/>Site-stage semantic canonicalization<br/>Grade · UI Damage · Log noise<br/>Whitespace · Unicode · layout variance"]
        K["⇄ <b>Candidate Comparator<br/>& Rule Tables</b>"]
        L["📊 <b>Metrics</b><br/>Pass / Fail<br/>Accuracy · F1"]
        M["✅ <b>Inline CAS-OR Error Taxonomy · Exact Match · Format Error · OCR Error</b>"]

        I -->|<b>Pass B</b>| J
        I -->|<b>Pass A</b>| K
        J --> K --> L --> M
    end

    DB -->|<b>Benchmark JSON + assets</b>| F

    %% =========================
    %% Styles
    %% =========================
    classDef systemBlue fill:#e8f0f7,stroke:#617a91,color:#000,stroke-width:1px;
    classDef systemPurple fill:#eadcff,stroke:#8b6ec8,color:#000,stroke-width:1px;
    classDef document fill:#ffffff,stroke:#617a91,color:#000,stroke-width:1px;
    classDef decision fill:#fff0c9,stroke:#bf8530,color:#000,stroke-width:1px;
    classDef profile fill:#ffffff,stroke:#617a91,color:#000,stroke-width:1px;
    classDef database fill:#dcecf7,stroke:#3f7192,color:#000,stroke-width:1px;
    classDef normalize fill:#d9f3df,stroke:#42936a,color:#000,stroke-width:1px;
    classDef output fill:#ffd9d9,stroke:#d45555,color:#000,stroke-width:1px;

    class A,D,F systemBlue;
    class B,G systemPurple;
    class C,H,K,L document;
    class E,I decision;
    class P1,P2A,P2B,P3,P4 profile;
    class DB database;
    class J normalize;
    class M output;

    style S1 fill:#fffde0,stroke:#b8a83b,stroke-width:1px
    style S2 fill:#fbf8ff,stroke:#8b6ec8,stroke-width:1px
    style Profiles fill:transparent,stroke:transparent`;

  const html = `<!DOCTYPE html><html><body>
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
    <script>
      window.testCode = async (code) => {
        try {
          await mermaid.parse(code);
          return { ok: true };
        } catch (e) {
          return { ok: false, error: e.message, str: e.str };
        }
      };
    </script>
  </body></html>`;

  await page.setContent(html, { waitUntil: 'networkidle' });
  const res = await page.evaluate((code) => window.testCode(code), originalCode);
  console.log('Result:', JSON.stringify(res, null, 2));
  await browser.close();
})();
