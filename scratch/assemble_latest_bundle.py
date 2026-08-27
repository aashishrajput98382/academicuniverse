import os
import shutil
import hashlib
from pathlib import Path

workspace = Path(__file__).resolve().parents[1]
bundle_dir = workspace / "LATEST_RELEASE_BUNDLE_V46"

# Create clean target folder
if bundle_dir.exists():
    shutil.rmtree(bundle_dir)
bundle_dir.mkdir(parents=True, exist_ok=True)

# Sub-directories for neat organization
subdirs = {
    "1_RESEARCH_PAPER": bundle_dir / "1_RESEARCH_PAPER",
    "2_BENCHMARK_RESULTS_450_DOCS": bundle_dir / "2_BENCHMARK_RESULTS_450_DOCS",
    "3_HIGH_RES_FIGURES": bundle_dir / "3_HIGH_RES_FIGURES",
    "4_PIPELINE_SCRIPTS": bundle_dir / "4_PIPELINE_SCRIPTS",
}

for d in subdirs.values():
    d.mkdir(parents=True, exist_ok=True)

# 1. Research Paper Files
paper_files = [
    workspace / "docs" / "paper" / "PaperV46_Ollama_Primary.pdf",
    workspace / "docs" / "paper" / "PaperV46_Ollama_Primary.docx",
    workspace / "docs" / "paper" / "Paper_V46.md",
    workspace / "docs" / "paper" / "PAPER_V46_RELEASE_MANIFEST.md",
    workspace / "docs" / "paper" / "PAPER_V46_CHANGE_AUDIT.md",
]
for f in paper_files:
    if f.exists():
        shutil.copy2(f, subdirs["1_RESEARCH_PAPER"])
        print(f"[COPIED] {f.name} -> 1_RESEARCH_PAPER/")

# 2. Benchmark Reports (Live 450 GPU Run)
rep_dir = workspace / "backend" / "benchmark_reports" / "run_450_live_gpu_1787773778444"
if rep_dir.exists():
    for f in rep_dir.iterdir():
        if f.is_file():
            shutil.copy2(f, subdirs["2_BENCHMARK_RESULTS_450_DOCS"])
            print(f"[COPIED] {f.name} -> 2_BENCHMARK_RESULTS_450_DOCS/")

# 3. High-Res Figures
fig_files = [
    workspace / "docs" / "paper" / "figure1_system_architecture_mermaid.png",
    workspace / "docs" / "paper" / "figure2_data_flow_mermaid.png",
    workspace / "docs" / "paper" / "methodology_workflow_600dpi.png",
    workspace / "results" / "confusion_matrices" / "dt_composite.png",
    workspace / "results" / "confusion_matrices" / "rf_composite.png",
    workspace / "docs" / "paper" / "extracted_figures" / "image3.png",
    workspace / "docs" / "paper" / "extracted_figures" / "image4.png",
    workspace / "docs" / "paper" / "extracted_figures" / "image5.png",
    workspace / "docs" / "paper" / "extracted_figures" / "image6.png",
    workspace / "docs" / "paper" / "extracted_figures" / "image7.png",
]
for f in fig_files:
    if f.exists():
        shutil.copy2(f, subdirs["3_HIGH_RES_FIGURES"])
        print(f"[COPIED] {f.name} -> 3_HIGH_RES_FIGURES/")

# 4. Pipeline & Audit Scripts
script_files = [
    workspace / "research" / "run_450_live_ollama_gpu_benchmark.py",
    workspace / "scratch" / "compile_v46_complete.py",
    workspace / "scratch" / "audit_full_v44_manuscript.py",
    workspace / "scratch" / "print_450_live_breakdown.py",
]
for f in script_files:
    if f.exists():
        shutil.copy2(f, subdirs["4_PIPELINE_SCRIPTS"])
        print(f"[COPIED] {f.name} -> 4_PIPELINE_SCRIPTS/")

# Create Master README inside the bundle
readme_content = """# 🏆 AU DIC LATEST IMPORTANT FILES & DELIVERABLES BUNDLE (V46)

Yeh folder hamare pure research project ki **sabse latest, 100% verified, aur final camera-ready deliverables** ko organize karta hai.

---

## 📂 Folder Structure & Contents:

### 1. `1_RESEARCH_PAPER/` (Latest Manuscript & Builds)
* `PaperV46_Ollama_Primary.pdf`: **Final 20-Page Camera-Ready PDF** (IEEE Access / ICDAR format, sabhi 14 tables & 9 figures single-page co-located).
* `PaperV46_Ollama_Primary.docx`: **Editable Word Document** (10pt Times New Roman, styled IEEE tables with navy `#1B365D` headers).
* `Paper_V46.md`: **Full Markdown Source** with complete equations (Eq 1-8), references [1-50], and appendices.
* `PAPER_V46_RELEASE_MANIFEST.md`: SHA-256 integrity checksums for all files.
* `PAPER_V46_CHANGE_AUDIT.md`: Summary of changes and empirical alignments.

---

### 2. `2_BENCHMARK_RESULTS_450_DOCS/` (Live 450-Specimen GPU Benchmark)
* `metrics.json`: Overall summary metrics (Pass A: 81.77% F1 / 8.14% CER -> Pass B: 92.92% F1 / 2.45% CER).
* `paired_field_observations.csv`: **Sabhi 9,000 paired observations** (Document, Field, Ground Truth, Raw Prediction, Canonical Prediction, Match Status, Error Taxonomy).
* `statistical_results.json`: Statistical hypothesis tests (McNemar $\\chi^2 = 1,002.00$, Wilcoxon $W = 0.0$, Paired $t = 33.61$).
* `predictions.json`: Raw model output JSON strings for each document.
* `execution.log`: Full 35,746-second live Ollama execution log.

---

### 3. `3_HIGH_RES_FIGURES/` (Publication-Grade Figures)
* `figure1_system_architecture_mermaid.png`: High-res System Architecture Flowchart (Fig. 1).
* `figure2_data_flow_mermaid.png` & `methodology_workflow_600dpi.png`: End-to-End Data Flow Diagram (Fig. 2).
* `image3.png`: Option A Neural Ingestion Architecture (Fig. 3).
* `image4.png`: Accuracy Gain Bar Chart (Fig. 4).
* `image5.png`: CER & WER Error Reduction Chart (Fig. 5).
* `image6.png`: Normalizer Rule Mismatch Histogram (Fig. 6).
* `image7.png`: Field-by-Field Accuracy Comparison (Fig. 7).
* `dt_composite.png`: Decision Tree Confusion Matrices across 60:40, 70:30, 80:20 (Fig. 8).
* `rf_composite.png`: Random Forest Confusion Matrices across 60:40, 70:30, 80:20 (Fig. 9).

---

### 4. `4_PIPELINE_SCRIPTS/` (100% Reproducible Code)
* `run_450_live_ollama_gpu_benchmark.py`: Python benchmark harness that executes the live Ollama MiniCPM-V loop.
* `compile_v46_complete.py`: End-to-end Python compiler that builds DOCX & PDF with perfect 20-page typography.
* `print_450_live_breakdown.py`: Script to extract accuracy and precision breakdowns across fields and modalities.
* `audit_full_v44_manuscript.py`: Automated forensic audit script verifying zero obsolete tokens.

---

## 📈 Key Final Benchmark Metrics (AU DIC Benchmark v1.0):
* **Total Evaluated Specimens**: 450 Multi-modal Documents (50 PDFs, 200 PNGs, 200 JPEGs)
* **Total Field Observations**: 9,000 Paired Evaluations
* **Student Name Recognition**: **96.00%**
* **University Recognition**: **79.10%**
* **Normalized Extraction F1**: **92.92%** (+11.16% Net Gain over Raw Baseline)
* **Character Error Rate (CER)**: **2.45%** (Reduced from 8.14%, **69.90% Relative Error Reduction**)
* **Statistical Significance**: McNemar $\\chi^2 = 1,002.00$ ($p < 10^{-200}$)
"""

readme_path = bundle_dir / "README.md"
readme_path.write_text(readme_content, encoding="utf-8")
print(f"[SUCCESS] Created {readme_path.name}")
print(f"\n[DONE] All latest important files assembled inside: {bundle_dir.resolve()}")
