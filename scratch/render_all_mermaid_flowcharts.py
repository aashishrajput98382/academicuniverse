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
print(" RENDERING PUBLICATION FLOWCHARTS USING MERMAID-PY")
print("==========================================================")

# ----------------------------------------------------------------------
# 1. Figure 1: End-to-End System Architecture (Human-in-the-Loop + ADBG)
# ----------------------------------------------------------------------
fig1_mermaid = """
flowchart TB
    subgraph Subsystem1["SUBSYSTEM I: PRODUCTION HUMAN-IN-THE-LOOP PIPELINE"]
        direction LR
        A1["1. Ingestion\n(Mobile Photo / Scan / PDF)"] --> A2["2. Neural Classification\n(Category ID: 98% Conf)"]
        A2 --> A3["3. Multimodal VLM Parsing\n(MiniCPM-V 7.6B / Zero-Shot)"]
        A3 --> A4["4. 6-Stage Normalizer\n(Dates, Roll No, Aliases)"]
        A4 --> A5["5. Interactive Review UI\n(Human Verification Modal)"]
        A5 --> A6["6. Canonical Database\n(Transcript & CGPA Sync)"]
    end

    subgraph Subsystem2["SUBSYSTEM II: ADBG v1.0 SYNTHETIC BENCHMARK & EVALUATION ENGINE"]
        direction LR
        B1["ADBG Generator\n(360 Vector Docs / Seed 42)"] --> B2["14 Degradation Operators\n(Clean / Scanner / Mobile / Rotated)"]
        B2 --> B3["AU DIC Evaluation Core\n(24,480 Field Observations)"]
        B3 --> B4["9-Class Error Taxonomy\n(2,620 Mismatches Resolved)"]
        B4 --> B5["Statistical Rigor\n(McNemar chi2=2618, p<0.0001)"]
    end

    A4 -.->|"Shared Canonical Rules"| B3
"""

g1 = Graph("SystemArchitecture", fig1_mermaid)
m1 = Mermaid(g1)
fig1_png = out_dir / "figure1_system_architecture_mermaid.png"
m1.to_png(str(fig1_png))
print(f"[SUCCESS] Exported Fig 1 via mermaid-py: {fig1_png.name}")

# ----------------------------------------------------------------------
# 2. Figure 2: Data Flow Diagram (DFD Levels 0, 1, 2)
# ----------------------------------------------------------------------
fig2_mermaid = """
flowchart TD
    subgraph Level0["Level 0: External Interaction Boundaries"]
        U["Student / Evaluator"] -->|"Upload Document / Run Command"| SYS["AU DIC Intelligence System"]
        SYS -->|"Live Transcript / Benchmark Metrics"| U
    end

    subgraph Level1["Level 1: Framework Data Transformation Flow"]
        D_RAW["Raw Document / Image Tensor"] --> CLS["Neural Category Classifier"]
        CLS --> VLM["Multimodal VLM Extractor"]
        VLM --> RAW_JSON["Raw Key-Value Payload"]
        RAW_JSON --> NORM["Six-Stage CanonicalNormalizer"]
        NORM --> CAN_JSON["Normalized Canonical Record"]
    end

    subgraph Level2["Level 2: Error Diagnostics & Persistence Engine"]
        CAN_JSON --> REV["Human Review & Audit"]
        REV -->|"Approve"| DB[("Canonical Database / ERP")]
        CAN_JSON --> TAX["Nine-Class ErrorTaxonomist"]
        TAX --> STATS["Hypothesis Testing & Bootstrap CIs"]
    end

    SYS --> D_RAW
"""

g2 = Graph("DataFlowDiagram", fig2_mermaid)
m2 = Mermaid(g2)
fig2_png = out_dir / "figure2_data_flow_mermaid.png"
m2.to_png(str(fig2_png))
print(f"[SUCCESS] Exported Fig 2 via mermaid-py: {fig2_png.name}")

# ----------------------------------------------------------------------
# 3. Figure 3: Option A Neural Document Intelligence Pipeline
# ----------------------------------------------------------------------
fig3_mermaid = """
flowchart LR
    IMG["Input Image Tensor\n(300 DPI / Degraded)"] --> OLLAMA["Local Ollama Runtime\n(v0.32.14 / CPU-Only)"]
    OLLAMA --> MODEL["MiniCPM-V 7.6B\n(Q4_0 Quantized / Greedy T=0)"]
    MODEL --> JSON_OUT["Structured JSON Extractor\n(12 Subjects / Metadata)"]
    JSON_OUT --> NORM_PASS["Two-Pass Normalizer Engine\n(Pass A Raw vs Pass B Canonical)"]
    NORM_PASS --> EVAL["Multi-Metric Scorer\n(F1: 75.23%, CER: 8.21%)"]
    EVAL --> REPORT["Official Release Manifest\n(24,480 Observations Evaluated)"]
"""

g3 = Graph("OptionAPipeline", fig3_mermaid)
m3 = Mermaid(g3)
fig3_png = out_dir / "figure3_neural_pipeline_mermaid.png"
m3.to_png(str(fig3_png))
print(f"[SUCCESS] Exported Fig 3 via mermaid-py: {fig3_png.name}")

print("==========================================================")
print(" ALL MERMAID-PY FLOWCHARTS COMPILED & EXPORTED SUCCESSFULLY!")
print("==========================================================")
