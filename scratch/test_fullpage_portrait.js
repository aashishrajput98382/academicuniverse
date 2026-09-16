const { renderMermaidToA4 } = require('./render_a4_mermaid');

const fullPagePortrait = `%%{init: {
  'theme': 'base',
  'themeVariables': {
    'fontSize': '15pt',
    'fontFamily': 'Plus Jakarta Sans, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
    'primaryColor': '#ffffff',
    'primaryTextColor': '#0f172a',
    'primaryBorderColor': '#334155',
    'lineColor': '#1e293b',
    'edgeLabelBackground': '#ffffff',
    'clusterBkg': '#fffde0',
    'clusterBorder': '#b8a83b',
    'tertiaryColor': '#f8fafc'
  },
  'flowchart': {
    'nodeSpacing': 24,
    'rankSpacing': 32,
    'curve': 'basis',
    'padding': 16,
    'useMaxWidth': false
  }
}}%%
flowchart TB

    %% =========================================================================
    %% SUBSYSTEM 1: DATA GENERATION & OPTICAL DEGRADATION BENCHMARK
    %% =========================================================================
    subgraph S1 ["📄 <b>SUBSYSTEM 1 · ACADEMIC DOCUMENT BENCHMARK GENERATOR (ADBG v1.0)</b>"]
        direction TB

        subgraph S1_R1 ["<b>STAGE 1 · DETERMINISTIC CREDENTIAL & VECTOR PDF SYNTHESIS</b>"]
            direction LR
            A["⚙️ <b>Deterministic Seed & Schema Config</b><br/>PRNG Master Seed = 42 · Privacy Entities<br/>Student, Marks, College Registry Schema"]
            B["▦ <b>Typographic Template Engine</b><br/>Typst High-Fidelity Vector Adapter<br/>Certificates · Marksheets · Student ID Cards"]
            C["📄 <b>Vector PDF Compilation (300 DPI)</b><br/>Pixel-Exact Bounding Box Mapping<br/>Canonical Ground-Truth JSON Assembly"]

            A ==>|Entity Synthesis| B ==>|Vector Render| C
        end

        subgraph S1_R2 ["<b>STAGE 2 · HIGH-RESOLUTION RASTERIZATION & PERTURBATION</b>"]
            direction LR
            D["🔍 <b>High-Resolution Rasterization Engine</b><br/>300 DPI RGB Anti-Aliased Rendering<br/>Document Bitmap Tensor Pipeline"]
            E{"⑂ <b>14-Operator Optical Degradation Matrix</b><br/>Controlled Noise Perturbation Bounds<br/>Scanner Artifacts · Mobile Defocus · Affine"}

            D ==>|Tensor Conversion| E
        end

        C ==>|Compiled Documents| D

        subgraph Profiles ["<b>MULTI-MODAL REAL-WORLD QUALITY PROFILES MATRIX</b>"]
            direction LR
            P1["🖥️ <b>Profile 1 · Clean Digital</b><br/>Pristine Electronic PDF Scan<br/>Zero Perception Distortion"]
            P2B["▣ <b>Profile 2B · Scanner Copy</b><br/>Gaussian Noise · Blur Artifacts<br/>Contrast Shift · Threshold Noise"]
            P2A["▤ <b>Profile 2A · Mobile Camera</b><br/>Perspective Skew · Flash Glare<br/>Uneven Illumination · Shadows"]
            P3["↻ <b>Profile 3 · Rotated 90°</b><br/>Geometric 90° Coordinate Flip<br/>Non-Standard Document Flow"]
            P4["🖼️ <b>Profile 4 · Ground Truth</b><br/>Pixel-Exact Annotation Coordinates<br/>Canonical Target Text Keys"]
        end

        E -->|Digital Baseline| P1
        E -->|Scanner Model| P2B
        E -->|Mobile Camera| P2A
        E -->|Orientation Shift| P3
        E -->|Coordinate Maps| P4

        DB[("🗄️ <b>AI UI DC BENCHMARK SUITE REPOSITORY (v1.0)</b><br/>450 Multi-Modal Specimen Documents · 9,000 Paired Evaluation Observations<br/>High-Resolution PNG / PDF Bitmaps + Structured Ground-Truth Annotations · SHA-256 Verified")]

        P1 ==>|Dataset Pack| DB
        P2B ==>|Dataset Pack| DB
        P2A ==>|Dataset Pack| DB
        P3 ==>|Dataset Pack| DB
        P4 ==>|Dataset Pack| DB
    end

    %% INTER-SUBSYSTEM FLOW
    DB ===>|<b>Benchmark Instances + Ground Truth Metadata Stream</b>| F

    %% =========================================================================
    %% SUBSYSTEM 2: AI INFERENCE, NORMALIZATION & DIAGNOSTIC EVALUATION
    %% =========================================================================
    subgraph S2 ["📈 <b>SUBSYSTEM 2 · AI UI EVALUATION & DIAGNOSTIC VERIFICATION SUBSYSTEM</b>"]
        direction TB

        subgraph S2_R1 ["<b>STAGE 3 · MULTIMODAL INFERENCE & PREDICTION HARNESS</b>"]
            direction LR
            F["🎛️ <b>Decoupled Benchmark Controller</b><br/>Stateless Evaluation Harness<br/>Zero Database Mutation · Clean Run"]
            G["🧠 <b>Model Prediction Adapter</b><br/>MiniCPM-V 7.6B Foundation VLM<br/>Local Ollama Q4_0 Engine Runtime"]
            H["{} <b>Raw Model Prediction</b><br/>Extracted Candidate JSON<br/>Raw Key-Value Structured Fields"]

            F ==>|Deploy Specimen| G ==>|Stream Output| H
        end

        subgraph S2_R2 ["<b>STAGE 4 · DUAL-PASS EVALUATION PROTOCOL</b>"]
            direction LR
            I{"☑️ <b>Dual Evaluation Protocol</b><br/>Strict Exact vs. Canonical Normalization"}

            subgraph S2_PASSES ["<b>PARALLEL EVALUATION PASSES</b>"]
                direction LR
                RAW["⚡ <b>Pass A · Raw Mode</b><br/>Direct String Comparison<br/>Unnormalized Character Matching"]
                J["🔽 <b>Pass B · Normalized Mode</b><br/>Six-Stage Semantic Canonicalization<br/>Date · ID · Numeric · Whitespace · Aliases"]
            end

            I ==>|Direct Branch| RAW
            I ==>|Canonical Branch| J
        end

        H ==>|Raw JSON Instance| I

        subgraph S2_R3 ["<b>STAGE 5 · SCORING, METRICS & TAXONOMY CLASSIFICATION</b>"]
            direction LR
            K["⇄ <b>Candidate Comparator & Rules</b><br/>Bilingual Levenshtein Similarity<br/>Field-by-Field Semantic Alignment"]
            L["📊 <b>Evaluation Benchmark Metrics</b><br/>Field Precision · Recall · Field F1<br/>CER / WER · Bootstrap 95% CI · McNemar"]
            M["✅ <b>Inline Nine-Class Diagnostic OCR Error Taxonomy</b><br/>EXACT_MATCH · FORMAT_ERROR · NORMALIZATION_ERROR<br/>OCR_ERROR · FIELD_MISSING · HALLUCINATION · CATEGORY_ERROR"]

            K ==>|Normalized Vectors| L ==>|Diagnostic Triage| M
        end

        RAW ==>|Unprocessed Vector| K
        J ==>|Normalized Vector| K
    end

    %% =========================================================================
    %% A4 FULL-PAGE STYLING SPECIFICATIONS (Strict 15pt Font Size Throughout)
    %% =========================================================================
    classDef systemBlue fill:#e0f2fe,stroke:#0284c7,stroke-width:2.5px,color:#0f172a,font-size:15pt;
    classDef systemPurple fill:#f3e8ff,stroke:#9333ea,stroke-width:2.5px,color:#0f172a,font-size:15pt;
    classDef document fill:#ffffff,stroke:#334155,stroke-width:2px,color:#0f172a,font-size:15pt;
    classDef decision fill:#fef3c7,stroke:#d97706,stroke-width:2.5px,color:#0f172a,font-size:15pt;
    classDef profile fill:#ffffff,stroke:#0284c7,stroke-width:2px,color:#0f172a,font-size:15pt;
    classDef database fill:#dbeafe,stroke:#1d4ed8,stroke-width:3px,color:#0f172a,font-size:16pt;
    classDef normalize fill:#dcfce7,stroke:#16a34a,stroke-width:2.5px,color:#0f172a,font-size:15pt;
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

    style S1 fill:#fefce8,stroke:#ca8a04,stroke-width:3px,color:#713f12,font-size:18pt
    style S2 fill:#f8fafc,stroke:#4f46e5,stroke-width:3px,color:#312e81,font-size:18pt
    style S1_R1 fill:#ffffff,stroke:#94a3b8,stroke-width:1.5px,color:#1e293b,font-size:15pt
    style S1_R2 fill:#ffffff,stroke:#94a3b8,stroke-width:1.5px,color:#1e293b,font-size:15pt
    style Profiles fill:#f1f5f9,stroke:#64748b,stroke-width:1.5px,color:#1e293b,font-size:15pt
    style S2_R1 fill:#ffffff,stroke:#94a3b8,stroke-width:1.5px,color:#1e293b,font-size:15pt
    style S2_R2 fill:#ffffff,stroke:#94a3b8,stroke-width:1.5px,color:#1e293b,font-size:15pt
    style S2_PASSES fill:#f8fafc,stroke:#cbd5e1,stroke-width:1px,color:#1e293b,font-size:15pt
    style S2_R3 fill:#ffffff,stroke:#94a3b8,stroke-width:1.5px,color:#1e293b,font-size:15pt
`;

renderMermaidToA4(fullPagePortrait, 'scratch/full_page_portrait_a4.png', false);
