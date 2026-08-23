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
print(" RENDERING COMPACT BALANCED CLASSIC ENGINEERING FLOWCHARTS")
print("==========================================================")

# ----------------------------------------------------------------------
# 1. Figure 1: Classic System Architecture Flowchart
# ----------------------------------------------------------------------
fig1_classic_mermaid = """
flowchart LR
    S(["Start"]) --> IN1[/"1. Ingestion: Upload Marksheet / PDF"/]
    IN1 --> P1["2. AI Category Classifier\n(98%+ Confidence)"]
    P1 --> D1{"Category Valid?"}
    D1 -- No --> F1["Route to Manual Review"] --> E_FAIL(["End: Rejected"])
    D1 -- Yes --> P2["3. Zero-Shot VLM Engine\n(MiniCPM-V 7.6B)"]
    P2 --> P3["4. 6-Stage Semantic Normalizer\n(Dates, Roll No, Aliases)"]
    P3 --> D2{"Data Verified?"}
    D2 -- No --> P4["OCR Error Taxonomist\n& Benchmark Scoring"] --> E_BENCH(["End: Benchmark Done"])
    D2 -- Yes --> OUT1[/"5. Review UI Candidate Table"/]
    OUT1 --> D3{"Human Approved?"}
    D3 -- No --> P5["Inline Field Editor"] --> OUT1
    D3 -- Yes --> P6["6. Canonical DB Sync\n& Multi-Semester Transcript"]
    P6 --> OUT2[/"7. Live Student Profile & CGPA"/]
    OUT2 --> E_SUCC(["End: Record Synced"])
"""

g_f1 = Graph("SystemArchitectureFlowchart", fig1_classic_mermaid)
m_f1 = Mermaid(g_f1)
f1_png = out_dir / "figure1_system_architecture_mermaid.png"
m_f1.to_png(str(f1_png))
print(f"[SUCCESS] Exported Fig 1: {f1_png.name}")

# ----------------------------------------------------------------------
# 2. Figure 2: Classic Data Flow Diagram (DFD) Flowchart
# ----------------------------------------------------------------------
fig2_classic_mermaid = """
flowchart LR
    subgraph S1["Data Ingestion & Extraction"]
        direction TB
        START(["Start"]) --> I1[/"Upload Document (Image/PDF)"/]
        I1 --> P_OCR["OCR Preprocessing & Normalization"]
        P_OCR --> P_VLM["Multimodal VLM Neural Extraction"]
    end

    subgraph S2["Canonical Normalization & Review"]
        direction TB
        P_VLM --> P_CAN["Six-Stage CanonicalNormalizer"]
        P_CAN --> D_CONF{"Confidence >= 90%?"}
        D_CONF -- No --> P_REV_REQ["Flag for Manual Inspection"]
        D_CONF -- Yes --> I_PREV[/"Structured Preview UI"/]
    end

    subgraph S3["Database Persistence & Output"]
        direction TB
        I_PREV --> D_APP{"Human Approved?"}
        D_APP -- Reject --> P_DRAFT["Save Draft / Re-upload"]
        D_APP -- Approve --> P_DB[("Write Canonical Records")]
        P_DB --> P_TRANS["Compute CGPA & Transcript"]
        P_TRANS --> END_OK(["End: Sync Complete"])
    end

    P_REV_REQ --> I_PREV
"""

g_f2 = Graph("DataFlowDiagramFlowchart", fig2_classic_mermaid)
m_f2 = Mermaid(g_f2)
f2_png = out_dir / "figure2_data_flow_mermaid.png"
m_f2.to_png(str(f2_png))
print(f"[SUCCESS] Exported Fig 2: {f2_png.name}")

print("==========================================================")
