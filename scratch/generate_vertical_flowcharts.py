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
print(" RENDERING CLEAN VERTICAL ISO ENGINEERING FLOWCHARTS")
print("==========================================================")

# ----------------------------------------------------------------------
# 1. Figure 1: Vertical Classic System Architecture Flowchart (Top-to-Bottom)
# ----------------------------------------------------------------------
fig1_vertical_mermaid = """
flowchart TD
    START(["Start: Document Ingestion"]) --> IN1[/"Input: Upload Marksheet / Certificate (PDF/Image)"/]
    
    IN1 --> P1["Neural AI Category Classification\n(Format Preprocessing & Confidence Score)"]
    
    P1 --> D1{"Category Confirmed\n(Confidence >= 90%)?"}
    
    D1 -- No --> F1["Route to Human Audit Queue"]
    F1 --> D1_HUMAN{"Manual Category\nAssigned?"}
    D1_HUMAN -- No --> E_FAIL(["End: Document Rejected"])
    D1_HUMAN -- Yes --> P2
    
    D1 -- Yes --> P2["Multimodal VLM Zero-Shot Extraction Engine\n(Local Ollama MiniCPM-V 7.6B)"]
    
    P2 --> P3["Six-Stage Semantic Canonical Normalization\n(Dates, Roll Numbers, Numeric Aliases)"]
    
    P3 --> D2{"Exact Format\nValidated?"}
    
    D2 -- No --> P4["Route to 9-Class OCR Error Taxonomist\n& Benchmark Scoring"]
    P4 --> E_BENCH(["End: Benchmark Report Generated"])
    
    D2 -- Yes --> OUT1[/"Output: Render Structured Candidate Preview Table"/]
    
    OUT1 --> D3{"Human Verification:\nApprove Extracted Data?"}
    
    D3 -- Reject / Edit --> P5["Inline Field Editor / Save Draft"]
    P5 --> OUT1
    
    D3 -- Approve --> P6["Commit to Canonical Database Collections\n(Academic Records, Growth Hub, Career Profile)"]
    
    P6 --> P7["Calculate Multi-Semester SGPA, Cumulative CGPA\n& Total Earned Credits"]
    
    P7 --> OUT2[/"Output: Render Live Student Transcript\n& Verified Academic Profile"/]
    
    OUT2 --> E_SUCC(["End: Academic Sync Successfully Completed"])
"""

g_f1 = Graph("VerticalSystemArchitectureFlowchart", fig1_vertical_mermaid)
m_f1 = Mermaid(g_f1)
f1_png = out_dir / "figure1_system_architecture_mermaid.png"
m_f1.to_png(str(f1_png))
print(f"[SUCCESS] Exported Fig 1 (Vertical): {f1_png.name}")

# ----------------------------------------------------------------------
# 2. Figure 2: Vertical Classic Data Flow Diagram (DFD)
# ----------------------------------------------------------------------
fig2_vertical_mermaid = """
flowchart TD
    S(["Start: Data Flow Lifecycle"]) --> I1[/"Level 0: User Ingestion (PDF / Mobile Scan)"/]
    
    I1 --> P1["Level 1: Multimodal OCR & VLM Neural Extraction"]
    
    P1 --> P2["Level 1: Six-Stage Semantic Canonicalization Engine"]
    
    P2 --> D1{"Confidence Score\n>= 90%?"}
    
    D1 -- No --> P_FLAG["Flag for Manual Inspection & Review"]
    P_FLAG --> I2[/"Level 2: Structured Review UI Modal"/]
    
    D1 -- Yes --> I2
    
    I2 --> D2{"Human Reviewer\nApproval?"}
    
    D2 -- Reject --> P_REJ["Save Draft / Request Re-upload"] --> S_END(["End: Draft Saved"])
    
    D2 -- Approve --> P_COMMIT["Level 2: Write to Canonical Database Collections"]
    
    P_COMMIT --> P_CALC["Calculate CGPA, Multi-Semester SGPA & Transcripts"]
    
    P_CALC --> OUT_FINAL[/"Level 2 Output: Live Student Profile Dashboard"/]
    
    OUT_FINAL --> E_FINAL(["End: Data Flow Complete"])
"""

g_f2 = Graph("VerticalDataFlowDiagram", fig2_vertical_mermaid)
m_f2 = Mermaid(g_f2)
f2_png = out_dir / "figure2_data_flow_mermaid.png"
m_f2.to_png(str(f2_png))
print(f"[SUCCESS] Exported Fig 2 (Vertical): {f2_png.name}")

print("==========================================================")
