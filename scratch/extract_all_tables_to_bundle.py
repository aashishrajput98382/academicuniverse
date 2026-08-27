import docx
import csv
from pathlib import Path

workspace = Path(__file__).resolve().parents[1]
bundle_dir = workspace / "LATEST_RELEASE_BUNDLE_V46"
tables_dir = bundle_dir / "5_TABLES"
tables_dir.mkdir(parents=True, exist_ok=True)

docx_path = workspace / "docs" / "paper" / "PaperV46_Ollama_Primary.docx"
doc = docx.Document(docx_path)

table_meta = [
    ("Table_01_Literature_Survey", "Table 1: Structured Literature Survey of Document Intelligence and Academic Credential Research"),
    ("Table_02_Computing_Environment", "Table 2: Experimental Computing Environment"),
    ("Table_03_Dataset_Composition", "Table 3: Multi-Modal Dataset and Benchmark Composition (AU_DIC_Benchmark_v1.0)"),
    ("Table_04_Optical_Degradation_Profiles", "Table 4: Optical Quality Degradation Profiles"),
    ("Table_05_Canonical_Parameters", "Table 5: Canonical Experimental Configuration Parameters"),
    ("Table_06_Mathematical_Metrics", "Table 6: Quantitative Evaluation Metrics and Mathematical Formulation"),
    ("Table_07_Dry_Run_Verification", "Table 7: Framework Verification Metrics (Dry-Run Infrastructure Validation on AU DIC Benchmark v1.0)"),
    ("Table_08_SOTA_Benchmark_Paradigms", "Table 8: State-of-the-Art (SOTA) Empirical Benchmark Across Document Intelligence Paradigms on AU DIC Dataset"),
    ("Table_09_Normalization_Ablation", "Table 9: Empirical Metric Impact of Semantic Canonical Normalization (450 Specimens / 9,000 Fields)"),
    ("Table_10_Normalizer_Rule_Contribution", "Table 10: Mismatch Correction Contribution by Normalizer Rule"),
    ("Table_11_Statistical_Hypothesis_Testing", "Table 11: Statistical Hypothesis Testing Summary (N = 9,000, alpha = 0.01)"),
    ("Table_12_Bootstrap_Confidence_Intervals", "Table 12: Empirical Benchmark Metrics with 95% Bootstrap Confidence Intervals (B = 10,000 Iterations)"),
    ("Table_13_OCR_Error_Taxonomy_Distribution", "Table 13: Nine-Class OCR Error Taxonomy Distribution Before and After Normalization"),
    ("Table_14_Classical_ML_Failure_Prediction", "Table 14: Classical Machine Learning Benchmark Comparison (RF vs. DT Across Train-Test Splits)"),
]

all_md_content = ["# 📊 ALL 14 MANUSCRIPT TABLES: AU DIC BENCHMARK SUITE (V46)", ""]

for idx, tbl in enumerate(doc.tables):
    file_prefix, title = table_meta[idx]
    
    # Extract table rows
    rows_data = []
    for row in tbl.rows:
        row_vals = [c.text.strip().replace('\n', ' ') for c in row.cells]
        rows_data.append(row_vals)
        
    # 1. Save CSV
    csv_file = tables_dir / f"{file_prefix}.csv"
    with open(csv_file, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows_data)
    print(f"[CSV SAVED] {csv_file.name}")
    
    # 2. Save Markdown
    md_file = tables_dir / f"{file_prefix}.md"
    md_lines = [f"# {title}", ""]
    
    if len(rows_data) > 0:
        header = rows_data[0]
        md_lines.append("| " + " | ".join(header) + " |")
        md_lines.append("| " + " | ".join([":---"] * len(header)) + " |")
        for r in rows_data[1:]:
            md_lines.append("| " + " | ".join(r) + " |")
            
    md_content_str = "\n".join(md_lines)
    md_file.write_text(md_content_str, encoding="utf-8")
    print(f"[MD SAVED]  {md_file.name}")
    
    # Add to consolidated document
    all_md_content.append(f"## {title}")
    all_md_content.append("")
    if len(rows_data) > 0:
        header = rows_data[0]
        all_md_content.append("| " + " | ".join(header) + " |")
        all_md_content.append("| " + " | ".join([":---"] * len(header)) + " |")
        for r in rows_data[1:]:
            all_md_content.append("| " + " | ".join(r) + " |")
    all_md_content.append("")
    all_md_content.append("---")
    all_md_content.append("")

# Save Consolidated Markdown
consolidated_file = tables_dir / "ALL_TABLES_CONSOLIDATED.md"
consolidated_file.write_text("\n".join(all_md_content), encoding="utf-8")
print(f"[CONSOLIDATED SAVED] {consolidated_file.name}")

# Update README in LATEST_RELEASE_BUNDLE_V46
readme_path = bundle_dir / "README.md"
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

### 5. `5_TABLES/` (All 14 Manuscript Tables in CSV & Markdown)
* `ALL_TABLES_CONSOLIDATED.md`: Sabhi 14 tables ek single master Markdown document me.
* Individual `.csv` and `.md` files for Table 1 through Table 14:
  - `Table_01_Literature_Survey.csv` / `.md`
  - `Table_02_Computing_Environment.csv` / `.md`
  - `Table_03_Dataset_Composition.csv` / `.md`
  - `Table_04_Optical_Degradation_Profiles.csv` / `.md`
  - `Table_05_Canonical_Parameters.csv` / `.md`
  - `Table_06_Mathematical_Metrics.csv` / `.md`
  - `Table_07_Dry_Run_Verification.csv` / `.md`
  - `Table_08_SOTA_Benchmark_Paradigms.csv` / `.md`
  - `Table_09_Normalization_Ablation.csv` / `.md`
  - `Table_10_Normalizer_Rule_Contribution.csv` / `.md`
  - `Table_11_Statistical_Hypothesis_Testing.csv` / `.md`
  - `Table_12_Bootstrap_Confidence_Intervals.csv` / `.md`
  - `Table_13_OCR_Error_Taxonomy_Distribution.csv` / `.md`
  - `Table_14_Classical_ML_Failure_Prediction.csv` / `.md`

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
readme_path.write_text(readme_content, encoding="utf-8")
print("[SUCCESS] Updated README.md with 5_TABLES section")
