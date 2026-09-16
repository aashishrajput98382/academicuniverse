const { renderMermaidToA4 } = require('./render_a4_mermaid');

const balancedA4Landscape = `%%{init: {
  'theme': 'base',
  'themeVariables': {
    'fontSize': '15pt',
    'fontFamily': 'Plus Jakarta Sans, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif',
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
    'nodeSpacing': 22,
    'rankSpacing': 28,
    'curve': 'basis',
    'padding': 16,
    'useMaxWidth': false
  }
}}%%
flowchart LR

    %% =========================================================================
    %% SUBSYSTEM 1: DATASET & BENCHMARK SYNTHESIS (LEFT 50% OF PAGE)
    %% =========================================================================
    subgraph S1 ["📄 <b>SUBSYSTEM 1 · ACADEMIC DOCUMENT BENCHMARK GENERATOR (ADBG v1.0)</b>"]
        direction TB

        subgraph S1_STAGE1 ["<b>1. ENTITY SYNTHESIS & VECTOR COMPILATION</b>"]
            direction LR
            A["⚙️ <b>Deterministic Seed Generator</b><br/>PRNG Master Seed = 42<br/>Fixed Privacy-Compliant Schema"]
            B["▦ <b>Typographic Template Engine</b><br/>Typst High-Fidelity Vector Compiler<br/>Certificates · Marksheets · ID Cards"]
            A ==>|Entity Rules| B
        end

        subgraph S1_STAGE2 ["<b>2. VECTOR PDFS & RASTERIZATION PIPELINE</b>"]
            direction LR
            C["📄 <b>Vector PDFs (300 DPI)</b><br/>Pixel-Exact Bounding Boxes<br/>Ground-Truth JSON Metadata"]
            D["🔍 <b>Rasterization Engine</b><br/>300 DPI Anti-Aliased Bitmaps<br/>Tensor Image Conversion"]
            C ==>|Render Bitmaps| D
        end

        B ==>|Compile Documents| C

        subgraph S1_STAGE3 ["<b>3. OPTICAL DEGRADATION & REAL-WORLD PROFILES</b>"]
            direction TB
            E["⑂ <b>14-Operator Optical Degradation Engine</b><br/>Controlled Perturbation Matrix & Parameter Space Bounds"]
            
            subgraph Profiles ["<b>MULTI-MODAL QUALITY DEGRADATION PROFILES MATRIX</b>"]
                direction LR
                subgraph PROF_COL1 [" "]
                    direction TB
                    P1["🖥️ <b>Profile 1 · Clean Digital</b><br/>Pristine Electronic PDF Baseline"]
                    P2B["▣ <b>Profile 2B · Scanner Copy</b><br/>Gaussian Noise · Blur & Dust Drift"]
                end
                subgraph PROF_COL2 [" "]
                    direction TB
                    P2A["▤ <b>Profile 2A · Mobile Camera</b><br/>Perspective Skew · Flash Glare"]
                    P3["↻ <b>Profile 3 · Rotated 90°</b><br/>Geometric 90° Coordinate Flip"]
                end
                subgraph PROF_COL3 [" "]
                    direction TB
                    P4["🖼️ <b>Profile 4 · Ground Truth</b><br/>Character-Level Target Coordinates"]
                end
            end

            E -->|Digital| P1
            E -->|Scanner| P2B
            E -->|Mobile| P2A
            E -->|Rotation| P3
            E -->|Ground Truth| P4
        end

        D ==>|Bitmap Tensors| E

        DB[("🗄️ <b>AU DIC BENCHMARK SUITE REPOSITORY (v1.0)</b><br/>450 Multi-Modal Specimen Documents · 9,000 Paired Evaluation Observations<br/>High-Resolution PNG / PDF Bitmaps + Structured Ground-Truth Annotations · SHA-256 Verified")]

        P1 ==>|Dataset Pack| DB
        P2B ==>|Dataset Pack| DB
        P2A ==>|Dataset Pack| DB
        P3 ==>|Dataset Pack| DB
        P4 ==>|Dataset Pack| DB
    end

    %% INTER-SUBSYSTEM DUAL-BUS BRIDGE
    DB ===>|<b>Benchmark Dataset Stream<br/>JSON Annotations + Specimen Images</b>| F

    %% =========================================================================
    %% SUBSYSTEM 2: AI INFERENCE, NORMALIZATION & EVALUATION (RIGHT 50% OF PAGE)
    %% =========================================================================
    subgraph S2 ["📈 <b>SUBSYSTEM 2 · AI EVALUATION & DIAGNOSTIC SUBSYSTEM</b>"]
        direction TB

        subgraph S2_STAGE1 ["<b>4. DECOUPLED HARNESS & MODEL INFERENCE</b>"]
            direction LR
            F["🎛️ <b>Decoupled Benchmark Controller</b><br/>Stateless Orchestrator<br/>Zero Database Mutation · Clean Run"]
            G["🧠 <b>Model Prediction Adapter</b><br/>MiniCPM-V 7.6B Foundation VLM<br/>Local Ollama Q4_0 Engine Runtime"]
            F ==>|Deploy Specimen| G
        end

        subgraph S2_STAGE2 ["<b>5. RAW PREDICTION & DUAL EVALUATION PROTOCOL</b>"]
            direction LR
            H["{} <b>Raw Model Extraction Output</b><br/>Structured JSON Prediction Stream<br/>Atomic Key-Value Field Instances"]
            I["☑️ <b>Dual Evaluation Protocol</b><br/>Branching Exact Match vs.<br/>Semantic Canonical Normalization"]
            H ==>|Parse JSON| I
        end

        G ==>|Inference Output| H

        subgraph S2_STAGE3 ["<b>6. DUAL-PASS VERIFICATION & CANONICALIZATION</b>"]
            direction TB
            subgraph S2_PASSES ["<b>PARALLEL EVALUATION PASSES</b>"]
                direction LR
                RAW["⚡ <b>Pass A · Raw Mode</b><br/>Direct Strict Character Matching<br/>Unnormalized Baseline Score"]
                J["🔽 <b>Pass B · Normalized Mode</b><br/>Six-Stage Semantic Canonicalization<br/>Date · ID · Numeric · Whitespace · Aliases"]
            end
            K["⇄ <b>Candidate Comparator & Rule Matching Engine</b><br/>Bilingual Levenshtein Similarity · Field-by-Field Semantic Alignment<br/>Ground Truth vs. Canonical Extracted Entity Verification"]
            RAW ==>|Raw Score Vector| K
            J ==>|Normalized Vector| K
        end

        I ==>|Pass A: Direct| RAW
        I ==>|Pass B: Canonical| J

        subgraph S2_STAGE4 ["<b>7. QUANTITATIVE METRICS & ERROR TAXONOMY</b>"]
            direction TB
            L["📊 <b>Quantitative Evaluation Benchmark Metrics</b><br/>Field Precision · Recall · Field F1 Score · CER / WER Error Reductions<br/>Statistical Significance Testing (McNemar · Wilcoxon Signed-Rank · Paired t-test)"]
            M["✅ <b>Inline Nine-Class Diagnostic OCR Error Taxonomy</b><br/>1. EXACT_MATCH · 2. FORMAT_ERROR · 3. NORMALIZATION_ERROR · 4. OCR_ERROR<br/>5. FIELD_MISSING · 6. HALLUCINATION · 7. CATEGORY_ERROR · 8. PARTIAL_MATCH · 9. LOW_CONFIDENCE"]
            L ==>|Classify Discrepancies| M
        end

        K ==>|Aggregate Evaluation Records| L
    end

    %% =========================================================================
    %% STYLING & 15PT FONT SPECIFICATION
    %% =========================================================================
    classDef systemBlue fill:#e0f2fe,stroke:#0284c7,stroke-width:2.5px,color:#0f172a,font-size:15pt;
    classDef systemPurple fill:#f3e8ff,stroke:#9333ea,stroke-width:2.5px,color:#0f172a,font-size:15pt;
    classDef document fill:#ffffff,stroke:#334155,stroke-width:2px,color:#0f172a,font-size:15pt;
    classDef decision fill:#fef3c7,stroke:#d97706,stroke-width:2.5px,color:#0f172a,font-size:15pt;
    classDef profile fill:#ffffff,stroke:#0284c7,stroke-width:2px,color:#0f172a,font-size:14pt;
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
    style S1_STAGE1 fill:#ffffff,stroke:#94a3b8,stroke-width:1.5px,color:#1e293b,font-size:15pt
    style S1_STAGE2 fill:#ffffff,stroke:#94a3b8,stroke-width:1.5px,color:#1e293b,font-size:15pt
    style S1_STAGE3 fill:#ffffff,stroke:#94a3b8,stroke-width:1.5px,color:#1e293b,font-size:15pt
    style Profiles fill:#f1f5f9,stroke:#64748b,stroke-width:1.5px,color:#1e293b,font-size:14pt
    style PROF_COL1 fill:transparent,stroke:transparent
    style PROF_COL2 fill:transparent,stroke:transparent
    style PROF_COL3 fill:transparent,stroke:transparent
    style S2_STAGE1 fill:#ffffff,stroke:#94a3b8,stroke-width:1.5px,color:#1e293b,font-size:15pt
    style S2_STAGE2 fill:#ffffff,stroke:#94a3b8,stroke-width:1.5px,color:#1e293b,font-size:15pt
    style S2_STAGE3 fill:#ffffff,stroke:#94a3b8,stroke-width:1.5px,color:#1e293b,font-size:15pt
    style S2_PASSES fill:#f8fafc,stroke:#cbd5e1,stroke-width:1px,color:#1e293b,font-size:14pt
    style S2_STAGE4 fill:#ffffff,stroke:#94a3b8,stroke-width:1.5px,color:#1e293b,font-size:15pt
`;

renderMermaidToA4(balancedA4Landscape, 'scratch/balanced_landscape_a4.png', true);
