const { renderMermaidToA4 } = require('./render_a4_mermaid');

const portraitMermaidCode = `%%{init: {
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
    'nodeSpacing': 28,
    'rankSpacing': 36,
    'curve': 'basis',
    'padding': 18,
    'useMaxWidth': false
  }
}}%%
flowchart TB

    %% =========================================================================
    %% SUBSYSTEM 1: SYNTHETIC DATA & OPTICAL DEGRADATION BENCHMARK PIPELINE
    %% =========================================================================
    subgraph S1 ["📄 <b>SUBSYSTEM 1 · ACADEMIC DOCUMENT BENCHMARK GENERATOR (ADBG v1.0)</b>"]
        direction TB

        subgraph S1_STAGE1 ["<b>STAGE 1 · DETERMINISTIC TEMPLATE & PDF SYNTHESIS</b>"]
            direction LR
            A["⚙️ <b>Deterministic Seed Generator</b><br/>PRNG Master Seed = 42<br/>Fixed Entity Schema Rules"]
            B["▦ <b>Typographic Template Adapter</b><br/>Typst Vector Compiler<br/>Certificates · Marksheets · ID Cards"]
            C["📄 <b>Vector PDF Compilation (300 DPI)</b><br/>Pixel-Exact Bounding Boxes<br/>Ground-Truth JSON Metadata"]
            
            A ==>|Compile Templates| B ==>|Synthesize Documents| C
        end

        subgraph S1_STAGE2 ["<b>STAGE 2 · OPTICAL DEGRADATION & BENCHMARK SUITE COMPILATION</b>"]
            direction TB
            D["🔍 <b>High-Resolution Rasterization Engine</b><br/>Bitmap Tensor Conversion · Anti-Aliased 300 DPI Rendering"]
            E{"⑂ <b>14-Operator Optical Degradation Engine</b><br/>Controlled Perturbation Matrix & Parameter Space"}

            D ==>|Rasterize PDF Tensors| E

            subgraph Profiles ["<b>MULTI-MODAL OPTICAL DEGRADATION PROFILES MATRIX</b>"]
                direction LR
                P1["🖥️ <b>Profile 1: Clean Digital</b><br/>Pristine Vector Rendering<br/>Zero Distortion Baseline"]
                P2B["▣ <b>Profile 2B: Scanner Copy</b><br/>Gaussian Blur · Pixel Noise<br/>Brightness & Contrast Drift"]
                P2A["▤ <b>Profile 2A: Mobile Capture</b><br/>Perspective Skew · Shadows<br/>Uneven Flash Illumination"]
                P3["↻ <b>Profile 3: Heavy Degraded</b><br/>Motion Blur · Artifacts<br/>Vignetting · 90° Rotation"]
                P4["🖼️ <b>Profile 4: Ground Truth</b><br/>Character-Level Coordinates<br/>Canonical Target References"]
            end

            E -->|Digital Profile| P1
            E -->|Scanner Profile| P2B
            E -->|Camera Profile| P2A
            E -->|Degraded Profile| P3
            E -->|Ground Truth Data| P4
        end

        C ==>|Render Bitmaps| D

        DB[("🗄️ <b>AU DIC BENCHMARK SUITE DATASET REPOSITORY (v1.0)</b><br/>450 Multi-Modal Academic Specimens · 9,000 Paired Evaluation Observations · Cryptographic SHA-256 Checksum")]

        P1 ==>|Artifact Pack| DB
        P2B ==>|Artifact Pack| DB
        P2A ==>|Artifact Pack| DB
        P3 ==>|Artifact Pack| DB
        P4 ==>|Artifact Pack| DB
    end

    %% INTER-SUBSYSTEM DUAL BUS ARROW
    DB ===>|<b>Benchmark Dataset Instances + Metadata JSON</b>| F

    %% =========================================================================
    %% SUBSYSTEM 2: MULTI-MODAL INFERENCE, NORMALIZATION & DIAGNOSTIC EVALUATION
    %% =========================================================================
    subgraph S2 ["📈 <b>SUBSYSTEM 2 · AI EVALUATION & DIAGNOSTIC VERIFICATION SUBSYSTEM</b>"]
        direction TB

        subgraph S2_STAGE1 ["<b>STAGE 3 · MULTIMODAL INFERENCE & RAW PREDICTION PIPELINE</b>"]
            direction LR
            F["🎛️ <b>Decoupled Benchmark Controller</b><br/>Stateless Orchestrator<br/>Zero DB Mutation · Isolated Run"]
            G["🧠 <b>Model Prediction Adapter</b><br/>MiniCPM-V 7.6B VLM (Q4_0)<br/>Local Ollama Runtime Engine"]
            H["{} <b>Raw Model Extraction Output</b><br/>Unparsed Structured JSON<br/>Atomic Key-Value Pairs"]

            F ==>|Deploy Specimen| G ==>|Stream Inference| H
        end

        I{"☑️ <b>Dual-Mode Evaluation Protocol Selector</b><br/>Branching Exact Match vs. Semantic Canonicalization"}

        H ==>|Raw JSON Extracted| I

        subgraph S2_STAGE2 ["<b>STAGE 4 · DUAL-PASS SEMANTIC VERIFICATION & COMPARISON</b>"]
            direction LR
            
            subgraph BRANCH_A ["<b>PASS A · RAW EVALUATION</b>"]
                direction TB
                RAW_MODE["⚡ <b>Raw String Direct Matching</b><br/>Literal Strict Character Comparison<br/>Without Semantic Normalization"]
            end

            subgraph BRANCH_B ["<b>PASS B · CANONICAL NORMALIZED EVALUATION</b>"]
                direction TB
                J["🔽 <b>Six-Stage Semantic Canonical Normalizer</b><br/>Date (YYYY-MM-DD) · ID / Roll Number Cleaning<br/>Numeric & Grade Float · Institutional Aliases<br/>Honorific & Whitespace Strip · Layout Syntax"]
            end

            K["⇄ <b>Candidate Comparator & Rule Evaluation Engine</b><br/>Bilingual Levenshtein Similarity Metric · Field Alignment<br/>Ground Truth vs. Canonical Extracted Entity Matching"]
        end

        I ==>|Pass A: Direct Mode| RAW_MODE
        I ==>|Pass B: Normalized Mode| J
        RAW_MODE ==>|Raw Comparison Vector| K
        J ==>|Standardized Entity Vector| K

        subgraph S2_STAGE3 ["<b>STAGE 5 · BENCHMARK METRICS & NINE-CLASS ERROR TAXONOMY</b>"]
            direction LR
            L["📊 <b>Quantitative Performance Metrics</b><br/>Field Precision · Recall · Field F1 Score<br/>Character Error Rate (CER) · Word Error Rate (WER)<br/>Statistical Significance (McNemar · Wilcoxon · t-test)"]
            
            M["✅ <b>Structured Nine-Class Diagnostic OCR Error Taxonomy</b><br/>1. EXACT_MATCH · 2. FORMAT_ERROR · 3. NORMALIZATION_ERROR<br/>4. OCR_ERROR · 5. FIELD_MISSING · 6. HALLUCINATION<br/>7. CATEGORY_ERROR · 8. PARTIAL_MATCH · 9. LOW_CONFIDENCE"]

            L ==>|Classify Discrepancies| M
        end

        K ==>|Aggregate Evaluation Records| L
    end

    %% =========================================================================
    %% STYLING AND THEME SPECIFICATIONS (15pt Font Size Throughout)
    %% =========================================================================
    classDef systemBlue fill:#e0f2fe,stroke:#0284c7,stroke-width:2px,color:#0f172a,font-size:15pt;
    classDef systemPurple fill:#f3e8ff,stroke:#9333ea,stroke-width:2px,color:#0f172a,font-size:15pt;
    classDef document fill:#ffffff,stroke:#475569,stroke-width:2px,color:#0f172a,font-size:15pt;
    classDef decision fill:#fef3c7,stroke:#d97706,stroke-width:2.5px,color:#0f172a,font-size:15pt;
    classDef profile fill:#ffffff,stroke:#0284c7,stroke-width:2px,color:#0f172a,font-size:15pt;
    classDef database fill:#dbeafe,stroke:#1d4ed8,stroke-width:2.5px,color:#0f172a,font-size:15pt;
    classDef normalize fill:#dcfce7,stroke:#16a34a,stroke-width:2.5px,color:#0f172a,font-size:15pt;
    classDef output fill:#fee2e2,stroke:#dc2626,stroke-width:2.5px,color:#0f172a,font-size:15pt;
    classDef subHeader fill:#f8fafc,stroke:#94a3b8,stroke-width:1.5px,color:#1e293b,font-size:15pt;

    class A,D,F,RAW_MODE systemBlue;
    class B,G systemPurple;
    class C,H,K document;
    class E,I decision;
    class P1,P2B,P2A,P3,P4 profile;
    class DB database;
    class J normalize;
    class L subHeader;
    class M output;

    style S1 fill:#fefce8,stroke:#ca8a04,stroke-width:2.5px,color:#854d0e,font-size:17pt
    style S2 fill:#f8fafc,stroke:#4f46e5,stroke-width:2.5px,color:#3730a3,font-size:17pt
    style S1_STAGE1 fill:#ffffff,stroke:#cbd5e1,stroke-width:1.5px,color:#334155,font-size:15pt
    style S1_STAGE2 fill:#ffffff,stroke:#cbd5e1,stroke-width:1.5px,color:#334155,font-size:15pt
    style Profiles fill:#f1f5f9,stroke:#94a3b8,stroke-width:1.5px,color:#334155,font-size:15pt
    style S2_STAGE1 fill:#ffffff,stroke:#cbd5e1,stroke-width:1.5px,color:#334155,font-size:15pt
    style S2_STAGE2 fill:#ffffff,stroke:#cbd5e1,stroke-width:1.5px,color:#334155,font-size:15pt
    style BRANCH_A fill:#f0f9ff,stroke:#7dd3fc,stroke-width:1.5px,color:#0369a1,font-size:15pt
    style BRANCH_B fill:#f0fdf4,stroke:#86efac,stroke-width:1.5px,color:#15803d,font-size:15pt
    style S2_STAGE3 fill:#ffffff,stroke:#cbd5e1,stroke-width:1.5px,color:#334155,font-size:15pt
`;

renderMermaidToA4(portraitMermaidCode, 'scratch/portrait_a4_test.png', false);
