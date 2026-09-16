const { renderMermaidToA4 } = require('./render_a4_mermaid');

// 1. A4 Landscape: 6 Balanced Columns across the page
const landscapeMermaid = `%%{init: {
  'theme': 'base',
  'themeVariables': {
    'fontSize': '15pt',
    'fontFamily': 'Plus Jakarta Sans, "Segoe UI", Roboto, Helvetica, Arial, sans-serif',
    'primaryColor': '#ffffff',
    'primaryTextColor': '#0f172a',
    'primaryBorderColor': '#475569',
    'lineColor': '#334155',
    'edgeLabelBackground': '#ffffff',
    'clusterBkg': '#fffde0',
    'clusterBorder': '#b8a83b',
    'tertiaryColor': '#f8fafc'
  },
  'flowchart': {
    'nodeSpacing': 20,
    'rankSpacing': 28,
    'curve': 'basis',
    'padding': 16,
    'useMaxWidth': false
  }
}}%%
flowchart LR

    %% =========================================================================
    %% SUBSYSTEM 1: BENCHMARK GENERATION (LEFT HALF - A4 LANDSCAPE)
    %% =========================================================================
    subgraph S1 ["📄 <b>SUBSYSTEM 1 · ACADEMIC DOCUMENT BENCHMARK GENERATOR (ADBG v1.0)</b>"]
        direction LR

        subgraph S1_COL1 ["<b>1. ENTITY SYNTHESIS</b>"]
            direction TB
            A["⚙️ <b>Deterministic Seed</b><br/>PRNG Master Seed = 42<br/>Fixed Privacy Schema"]
            B["▦ <b>Template Engine</b><br/>Typst Vector Compiler<br/>Certificates · Marksheets · IDs"]
            A ==>|Compile| B
        end

        subgraph S1_COL2 ["<b>2. VECTOR & RASTERIZATION</b>"]
            direction TB
            C["📄 <b>Vector PDFs (300 DPI)</b><br/>Pixel-Exact Bounding Boxes<br/>Ground-Truth JSON Metadata"]
            D["🔍 <b>Rasterization Engine</b><br/>Anti-Aliased 300 DPI Bitmaps<br/>Multi-Format Tensors"]
            E{"⑂ <b>14 Optical Operators</b><br/>Perturbation Matrix<br/>Controlled Degradation"}
            C ==>|Render| D ==>|Perturb| E
        end

        subgraph S1_COL3 ["<b>3. PROFILES & REPOSITORY</b>"]
            direction TB
            subgraph Profiles ["<b>DEGRADATION PROFILES</b>"]
                direction TB
                P1["🖥️ <b>Profile 1</b> · Clean Digital Baseline"]
                P2B["▣ <b>Profile 2B</b> · Scanner Copy Noise"]
                P2A["▤ <b>Profile 2A</b> · Mobile Capture Skew"]
                P3["↻ <b>Profile 3</b> · Heavy Optical Rotation"]
                P4["🖼️ <b>Profile 4</b> · Pixel-Exact Ground Truth"]
            end
            DB[("🗄️ <b>AU DIC Benchmark Suite</b><br/>450 Multi-Modal Specimens<br/>9,000 Paired Field Observations")]
            Profiles ==>|Assemble Suite| DB
        end

        B ==>|Generate| C
        E -->|Profiles 1-4| Profiles
    end

    %% INTER-SUBSYSTEM BRIDGE
    DB ===>|<b>Benchmark Dataset Instances + Metadata JSON</b>| F

    %% =========================================================================
    %% SUBSYSTEM 2: EVALUATION & DIAGNOSTICS (RIGHT HALF - A4 LANDSCAPE)
    %% =========================================================================
    subgraph S2 ["📈 <b>SUBSYSTEM 2 · AI EVALUATION & DIAGNOSTIC VERIFICATION SUBSYSTEM</b>"]
        direction LR

        subgraph S2_COL1 ["<b>4. MODEL INFERENCE</b>"]
            direction TB
            F["🎛️ <b>Decoupled Controller</b><br/>Stateless Benchmark Runner<br/>Zero DB Mutation"]
            G["🧠 <b>Model Adapter</b><br/>MiniCPM-V 7.6B VLM (Q4_0)<br/>Local Ollama Engine"]
            H["{} <b>Raw Prediction</b><br/>Structured Model JSON<br/>Extracted Key-Value Tokens"]
            F ==>|Deploy| G ==>|Inference| H
        end

        subgraph S2_COL2 ["<b>5. DUAL-PASS EVALUATION</b>"]
            direction TB
            I{"☑️ <b>Protocol Selector</b><br/>Raw Match vs. Canonical"}
            
            subgraph PASS_CONTAINER ["<b>EVALUATION PASSES</b>"]
                direction TB
                RAW["⚡ <b>Pass A · Raw Mode</b><br/>Strict Character Matching"]
                J["🔽 <b>Pass B · Normalized Mode</b><br/>Six-Stage Canonical Normalizer<br/>Date · ID · Numeric · Whitespace"]
            end

            K["⇄ <b>Candidate Comparator</b><br/>Levenshtein Fuzzy Metric<br/>Ground Truth vs. Prediction"]
            
            I -->|Pass A| RAW
            I -->|Pass B| J
            RAW --> K
            J --> K
        end

        subgraph S2_COL3 ["<b>6. BENCHMARK METRICS & TAXONOMY</b>"]
            direction TB
            L["📊 <b>Evaluation Metrics</b><br/>Precision · Recall · F1 Score<br/>CER / WER Error Reductions<br/>Statistical Hypothesis Tests"]
            M["✅ <b>9-Class Diagnostic Taxonomy</b><br/>EXACT_MATCH · FORMAT_ERROR<br/>NORMALIZATION_ERROR · OCR_ERROR<br/>FIELD_MISSING · HALLUCINATION"]
            L ==>|Classify Discrepancies| M
        end

        H ==>|Parse JSON| I
        K ==>|Aggregate Stats| L
    end

    %% =========================================================================
    %% STYLING AND THEME (15pt Font Size Throughout)
    %% =========================================================================
    classDef systemBlue fill:#e0f2fe,stroke:#0284c7,stroke-width:2px,color:#0f172a,font-size:15pt;
    classDef systemPurple fill:#f3e8ff,stroke:#9333ea,stroke-width:2px,color:#0f172a,font-size:15pt;
    classDef document fill:#ffffff,stroke:#475569,stroke-width:2px,color:#0f172a,font-size:15pt;
    classDef decision fill:#fef3c7,stroke:#d97706,stroke-width:2px,color:#0f172a,font-size:15pt;
    classDef profile fill:#ffffff,stroke:#0284c7,stroke-width:1.5px,color:#0f172a,font-size:14pt;
    classDef database fill:#dbeafe,stroke:#1d4ed8,stroke-width:2.5px,color:#0f172a,font-size:15pt;
    classDef normalize fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#0f172a,font-size:15pt;
    classDef output fill:#fee2e2,stroke:#dc2626,stroke-width:2.5px,color:#0f172a,font-size:15pt;

    class A,D,F,RAW systemBlue;
    class B,G systemPurple;
    class C,H,K document;
    class E,I decision;
    class P1,P2B,P2A,P3,P4 profile;
    class DB database;
    class J normalize;
    class L document;
    class M output;

    style S1 fill:#fefce8,stroke:#ca8a04,stroke-width:2.5px,color:#854d0e,font-size:17pt
    style S2 fill:#f8fafc,stroke:#4f46e5,stroke-width:2.5px,color:#3730a3,font-size:17pt
    style S1_COL1 fill:#ffffff,stroke:#cbd5e1,stroke-width:1.5px,color:#334155,font-size:15pt
    style S1_COL2 fill:#ffffff,stroke:#cbd5e1,stroke-width:1.5px,color:#334155,font-size:15pt
    style S1_COL3 fill:#ffffff,stroke:#cbd5e1,stroke-width:1.5px,color:#334155,font-size:15pt
    style Profiles fill:#f1f5f9,stroke:#94a3b8,stroke-width:1.5px,color:#334155,font-size:14pt
    style S2_COL1 fill:#ffffff,stroke:#cbd5e1,stroke-width:1.5px,color:#334155,font-size:15pt
    style S2_COL2 fill:#ffffff,stroke:#cbd5e1,stroke-width:1.5px,color:#334155,font-size:15pt
    style S2_COL3 fill:#ffffff,stroke:#cbd5e1,stroke-width:1.5px,color:#334155,font-size:15pt
    style PASS_CONTAINER fill:#ffffff,stroke:#cbd5e1,stroke-width:1px,font-size:14pt
`;

renderMermaidToA4(landscapeMermaid, 'scratch/landscape_a4_test.png', true);
