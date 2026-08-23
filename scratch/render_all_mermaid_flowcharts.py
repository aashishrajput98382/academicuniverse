import os
import mermaid as md
from mermaid.graph import Graph
from mermaid import Mermaid
from pathlib import Path
from PIL import Image

workspace = Path.cwd()
out_dir = workspace / "docs" / "paper"
out_dir.mkdir(parents=True, exist_ok=True)

print("==========================================================")
print(" RENDERING BALANCED IEEE PUBLICATION MERMAID FLOWCHARTS")
print("==========================================================")

# ----------------------------------------------------------------------
# 1. Figure 1: System Architecture (Clean 2-Lane Layout)
# ----------------------------------------------------------------------
fig1_mermaid = """
flowchart TB
    subgraph S1["SUBSYSTEM I: PRODUCTION HUMAN-IN-THE-LOOP PIPELINE"]
        direction LR
        A1["1. Document Ingestion\n(Mobile / Scan / PDF)"] --> A2["2. AI Category Classifier\n(98%+ Confidence)"]
        A2 --> A3["3. Multimodal VLM Parsing\n(MiniCPM-V 7.6B)"]
        A3 --> A4["4. 6-Stage Normalizer\n(ISO Dates & Clean Roll No)"]
        A4 --> A5["5. Interactive Review UI\n(Human Verification Modal)"]
        A5 --> A6["6. Canonical DB & Records\n(Live Transcript & CGPA)"]
    end

    subgraph S2["SUBSYSTEM II: ADBG v1.0 SYNTHETIC BENCHMARK & EVALUATION ENGINE"]
        direction LR
        B1["ADBG Generator\n(360 Vector Docs / Typst)"] --> B2["14 Degradation Operators\n(Clean / Scanner / Mobile / Tilt)"]
        B2 --> B3["AU DIC Evaluation Core\n(24,480 Field Observations)"]
        B3 --> B4["9-Class Error Taxonomy\n(2,620 Format Mismatches)"]
        B4 --> B5["Statistical Hypothesis Testing\n(McNemar chi2=2618, p<0.0001)"]
    end

    A4 -.->|"Shared Canonical Rules"| B3
"""

g1 = Graph("SystemArchitecture", fig1_mermaid)
m1 = Mermaid(g1)
fig1_png = out_dir / "figure1_system_architecture_mermaid.png"
m1.to_png(str(fig1_png))
print(f"[SUCCESS] Exported Fig 1: {fig1_png.name}")

# ----------------------------------------------------------------------
# 2. Figure 2: Data Flow Diagram (Balanced 3-Level Layout)
# ----------------------------------------------------------------------
fig2_mermaid = """
flowchart TB
    subgraph L0["Level 0: External Interaction Boundaries"]
        direction LR
        USER["Student / Academic Administrator"] <-->|"Upload Document / Access Transcript"| CORE["AU DIC Intelligence System"]
    end

    subgraph L1["Level 1: Framework Execution Flow"]
        direction LR
        RAW["Raw Document Tensor"] --> CLS["Neural Classifier"] --> VLM["VLM Extractor"] --> NORM["Six-Stage Normalizer"] --> CAN["Canonical Record"]
    end

    subgraph L2["Level 2: Diagnostic Error Classification & Persistence"]
        direction LR
        CAN --> REV["Human Review UI"] --> DB[("Canonical Database / ERP")]
        CAN --> TAX["Nine-Class ErrorTaxonomist"] --> STATS["Statistical Significance Suite"]
    end

    CORE --> RAW
"""

g2 = Graph("DataFlowDiagram", fig2_mermaid)
m2 = Mermaid(g2)
fig2_png = out_dir / "figure2_data_flow_mermaid.png"
m2.to_png(str(fig2_png))
print(f"[SUCCESS] Exported Fig 2: {fig2_png.name}")

# ----------------------------------------------------------------------
# 3. Figure 3: Option A Neural Document Intelligence Pipeline
# ----------------------------------------------------------------------
fig3_mermaid = """
flowchart TB
    subgraph StageA["Input & Inference"]
        direction LR
        IMG["Input Document Tensor\n(300 DPI Degraded Image)"] --> OLLAMA["Local Ollama Runtime\n(v0.32.14 / CPU-Only)"]
        OLLAMA --> VLM_MODEL["MiniCPM-V 7.6B Q4_0\n(Zero-Shot Multimodal Parsing)"]
    end

    subgraph StageB["Normalization & Evaluation"]
        direction LR
        VLM_MODEL --> JSON_DATA["Extracted JSON Payload\n(12 Subjects & Metadata)"]
        JSON_DATA --> CAN_NORM["Two-Pass Normalizer Engine\n(Pass A Raw vs Pass B Canonical)"]
        CAN_NORM --> METRICS["Multi-Metric Scorer\n(F1: 75.23%, CER: 8.21%)"]
    end
"""

g3 = Graph("OptionAPipeline", fig3_mermaid)
m3 = Mermaid(g3)
fig3_png = out_dir / "figure3_neural_pipeline_mermaid.png"
m3.to_png(str(fig3_png))
print(f"[SUCCESS] Exported Fig 3: {fig3_png.name}")

print("==========================================================")
print(" BALANCED MERMAID DIAGRAMS RENDERED SUCCESSFULLY!")
print("==========================================================")
