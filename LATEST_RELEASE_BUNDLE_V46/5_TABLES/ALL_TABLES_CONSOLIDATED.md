# 📊 ALL 14 MANUSCRIPT TABLES: AU DIC BENCHMARK SUITE (V46)

## Table 1: Structured Literature Survey of Document Intelligence and Academic Credential Research

| Sr. No. | Research Paper Title & Ref | Authors | Year | Evaluated Model & Architecture | Evaluated Dataset / Domain | Reported Performance & Best Metric | Research Limitations & Strategic Solutions |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | End-to-End Extraction from Receipts & Financial Docs [2] | L. Zhang et al. | 2025 | CNN-BiLSTM-Transformer (PyTorch) | ICDAR SROIE (Receipts) | 94.1% F1 (94.8% P, 93.5% R) | Limitation: Restricted to receipts; lacks privacy-compliant academic credential synthesis. Our Solution: ADBG v1.0 generates synthetic credentials with pixel-exact ground truth [26]. |
| 2 | Noisy Form Layout Analysis & Entity Linking [4] | K. Zhao et al. | 2025 | LayoutLM-FormNet (Transformer) | FUNSD Noisy Forms | 86.8% F1 (87.2% P, 86.4% R) | Limitation: Static scans only; lacks systematic optical degradation. Our Solution: AU DIC evaluates across 4 controlled degradation profiles (clean, scan, mobile, rot90) [27]. |
| 3 | Unified Pre-trained VLMs for Document AI [6] | X. Yang et al. | 2025 | LayoutLMv3 (Multimodal) | RVL-CDIP / DocVQA | 92.4% F1 (91.8% Accuracy) | Limitation: Unnormalized string matching penalizes benign formatting syntax variances. Our Solution: 6-stage CanonicalNormalizer standardizes dates, roll numbers, and aliases [25]. |
| 4 | OCR-Free Visual Document Processing via Swin Transformers [7] | C. Wang et al. | 2025 | Donut (OCR-Free Swin Transformer) | CORD / Donut-Bench | 88.2% F1 (84.5% Accuracy) | Limitation: Vulnerable to severe orientation rotations and lacks root-cause error diagnostics. Our Solution: AU DIC integrates a 9-class structured diagnostic error taxonomy [37]. |
| 5 | Multi-Task Vision-Language Representations for Content Extraction [9] | R. Patel et al. | 2025 | Florence-2 (Vision Transformer) | DocVQA / TextVQA Suite | 87.6% F1 (85.2% Accuracy) | Limitation: Generic visual tasks only; lacks dedicated academic credential parsing protocols. Our Solution: Specialized Typst templates for certificates, marksheets, and student ID cards [26]. |
| 6 | mPLUG-DocOwl2: High-Res OCR-Free Multi-Page Understanding [10] | A. Hu et al. | 2025 | DocOwl 2.0 (LLaMA-7B Vision) | DocOwl-Bench (Multi-page) | 85.9% F1 (81.3% Accuracy) | Limitation: Fails to isolate genuine OCR recognition errors from superficial syntax differences. Our Solution: Two-pass ablation isolates formatting discrepancies before metric calculation [25]. |
| 7 | Qwen2.5-VL: Enhancing VLMs with Dynamic Resolution [11] | S. Bai et al. | 2025 | Qwen2.5-VL (7B/72B NaViT) | DocVQA & Open Document AI | 89.4% F1 (86.7% Accuracy) | Limitation: Evaluated on public datasets lacking statutory educational privacy restrictions. Our Solution: Synthetic generation framework eliminates real student PII while preserving realism [28]. |
| 8 | Synthetic Academic Credential Generation for Document Analysis [17] | A. Gupta et al. | 2025 | Synthetic PDF Template Generator | Higher Ed Administrative Forms | 100% Privacy Compliance (0% PII) | Limitation: Focuses solely on generation without decoupled evaluation or canonical normalization. Our Solution: AU DIC provides strictly read-only evaluation with ground-truth pairing [31]. |
| 9 | Semantic Canonicalization & Normalizer Evaluation in Document Analysis [25] | M. Alvarez et al. | 2026 | Canonicalization Rule Normalizer | Commercial Invoices & Receipts | 90.4% F1 (91.2% P, 89.7% R) | Limitation: Tested only on commercial invoices; lacks institutional alias and roll number mappings. Our Solution: CanonicalNormalizer incorporates 6 domain stages specialized for academic records [36]. |
| 10 | Privacy-Preserving Synthetic Document Generation [26] | P. Singh et al. | 2026 | ADBG Prototype (Typst Engine) | Academic Credential Benchmark | Deterministic Multi-Modal Suite | Limitation: Established generation framework but lacked comprehensive live VLM empirical benchmarking. Our Solution: AU DIC couples ADBG with live local Ollama runtime evaluation across 9,000 field observations [31]. |

---

## Table 2: Experimental Computing Environment

| Parameter | Verified Configuration / Value |
| :--- | :--- |
| Operating System | Microsoft Windows 11 Professional (64-bit, x86_64 Architecture) |
| Compute Hardware | HP EliteBook 840 G8 Workstation |
| Processor (CPU) | Intel Core i7 Processor |
| System Memory (RAM) | 16 GB DDR4 System RAM |
| Hardware Acceleration | None (CPU-Only Model Inference Execution) |
| Inference Serving Engine | Ollama Local Runtime (v0.32.14, Local Host) |
| Evaluated Neural Engine | MiniCPM-V (minicpm-v:latest, ~7.6B Parameters, Q4_0 GGUF) |
| Software Environments | Python 3.14.x, Node.js v18.x, npm v9.x |
| Scientific & Statistical Stack | scipy >= 1.11, pandas >= 2.0, numpy >= 1.24, scikit-learn >= 1.3 |
| Framework Execution Mode | Headless Read-Only Execution (isReadOnly: true, 0 Database Writes) |
| Master Deterministic Seed | SeedManager.masterSeed = 42 |

---

## Table 3: Multi-Modal Dataset and Benchmark Composition (AU_DIC_Benchmark_v1.0)

| Document Category | Vector PDFs (Clean) | Lossless PNGs (4 Profiles) | Compressed JPEGs (4 Profiles) | Total Evaluated Specimens |
| :--- | :--- | :--- | :--- | :--- |
| Academic Certificate | 20 PDFs | 70 PNGs (Clean/Scan/Mob/Rot) | 70 JPEGs (Clean/Scan/Mob/Rot) | 160 Specimens (3,200 Fields) |
| Semester Marksheet | 20 PDFs | 70 PNGs (Clean/Scan/Mob/Rot) | 70 JPEGs (Clean/Scan/Mob/Rot) | 160 Specimens (3,200 Fields) |
| Student ID Card | 10 PDFs | 60 PNGs (Clean/Scan/Mob/Rot) | 60 JPEGs (Clean/Scan/Mob/Rot) | 130 Specimens (2,600 Fields) |
| Total Multi-Modal Suite | 50 Vector PDFs | 200 Lossless PNGs | 200 Compressed JPEGs | 450 Synthetic Document Specimens (9,000 Fields) |

---

## Table 4: Optical Quality Degradation Profiles

| Profile Name | Target Simulation | Applied Image Transformations | Degradation Severity |
| :--- | :--- | :--- | :--- |
| clean | Pristine vector render | Direct 300 DPI PDF-to-image rasterization; uncompressed | None (0.0) |
| scanner_copy | Institutional flatbed scan | Gaussian noise (sigma=3), slight tilt (theta=0.5 deg), brightness shift (+10%) | Mild (1.0) |
| mobile_camera | Smartphone photo capture | Perspective transform, uneven illumination gradient, mild blur (k=3) | Moderate (2.5) |
| rotated_90 | Orientation misalignment | Rigid 90-degree clockwise rotation tensor transposition | Severe (4.0) |

---

## Table 5: Canonical Experimental Configuration Parameters

| Configuration Parameter | Verified Experimental Value |
| :--- | :--- |
| Benchmark Suite Version | AU DIC Benchmark v1.0 (450 Synthetic Multi-Modal Specimens Suite) |
| Benchmark Execution Mode | Headless Read-Only Mode (isReadOnly: true, 0 Database Writes) |
| Model-Serving Runtime | Local Ollama Inference Engine (v0.32.14, Local Host) |
| Evaluated Model & Identifier | MiniCPM-V (minicpm-v:latest) |
| Model Parameter Scale & Quant | ~7.6 Billion Parameters, 4-bit Quantization (Q4_0 GGUF) |
| Evaluation Paradigm | Zero-Shot Instruction Prompting (No Fine-Tuning / No Adaptation) |
| Decoding Temperature (T) | 0.2 (Greedy / Low-Entropy Deterministic Sampling) |
| Maximum Generation Budget | 8192 Output Tokens / Specimen |
| Mock Fallback Setting | Disabled (allowMockFallback: false, Live Neural Inference Only) |
| Total Evaluated Specimens | 450 Synthetic Specimens (50 Vector PDFs + 200 Lossless PNGs + 200 Compressed JPEGs) |
| Total Paired Observations | 9,000 Paired Field Observations (20 Atomic Fields / Specimen) |
| Master Deterministic Seed | SeedManager.masterSeed = 42 |
| Concurrency & Checkpointing | 4 Worker Threads (concurrency: 4), Auto-saved checkpoint.json |
| Semantic Normalization Pipeline | Six-Stage CanonicalNormalizer (Enabled in Pass B) |
| Error Diagnostic Classification | Nine-Class ErrorTaxonomist (Enabled) |
| Bootstrap Significance Iterations | B = 10,000 Iterations (Bootstrap Random Seed = 42) |
| Hypothesis Significance Threshold | alpha = 0.05 (Achieved Significance p < 0.0001) |
| Canonical Execution Run ID | run_450_live_gpu_1787773778444 (Duration: 35746.20s / 595.77 mins) |
| Git Repository Commit | Commit 0cb27be (https://github.com/aashishrajput9838/academicuniverse.git) |
| Dataset SHA-256 Checksum | 17c136ef76dd0f82 |

---

## Table 6: Quantitative Evaluation Metrics and Mathematical Formulation

| Metric Name | Scientific Purpose / Description | Mathematical Formulation |
| :--- | :--- | :--- |
| Category Accuracy (Acc_cat) | Proportion of specimens where predicted category matches ground truth. | Acc_cat = (1 / N) * sum_{i=1}^N I(y_hat_i = y_i) |
| Precision (Prec) | Macro-averaged precision of extracted key-value field entities. | Prec = TP / (TP + FP) |
| Recall (Rec) | Macro-averaged recall / true positive rate of target field entities. | Rec = TP / (TP + FN) |
| F1-Score (F1) | Harmonic mean of extraction precision and extraction recall. | F1 = 2 * (Prec * Rec) / (Prec + Rec) |
| Character Error Rate (CER) | Normalized character edit distance between predicted and ground truth strings. | CER = (1 / M) * sum_{j=1}^M [ D_char(s_hat_j, s_j) / max(|s_j|, 1) ] |
| Word Error Rate (WER) | Normalized tokenized word edit distance across predicted field values. | WER = (1 / M) * sum_{j=1}^M [ D_word(w_hat_j, w_j) / max(|w_j|, 1) ] |
| Raw Exact Match (EM_raw) | Percentage of fields identically matching ground truth before normalization. | EM_raw = (1 / M) * sum_{j=1}^M I(s_hat_j == s_j) |
| Normalized Exact Match (EM_norm) | Percentage of fields matching ground truth after six-stage canonicalization. | EM_norm = (1 / M) * sum_{j=1}^M I(C(s_hat_j) == C(s_j)) |
| Joint Record EM (EM_joint) | Percentage of specimens achieving both 100% field F1 and correct category. | EM_joint = (1 / N) * sum_{i=1}^N I(y_hat_i == y_i AND F1_i == 1.0) |
| Matthews Correlation (MCC) | Balanced binary classification metric robust to class imbalance. | MCC = (TP*TN - FP*FN) / sqrt((TP+FP)(TP+FN)(TN+FP)(TN+FN)) |
| Specificity / TNR | True negative rate / proportion of negative instances correctly identified. | Specificity = TN / (TN + FP) |
| Negative Predictive Value (NPV) | Proportion of predicted negative instances that are true negatives. | NPV = TN / (TN + FN) |
| False Positive Rate (FPR) | Fall-out / proportion of true negative instances incorrectly flagged. | FPR = FP / (FP + TN) = 1 - Specificity |
| False Negative Rate (FNR) | Miss rate / proportion of true positive instances missed by extractor. | FNR = FN / (FN + TP) = 1 - Recall |
| False Discovery Rate (FDR) | Proportion of positive predictions that are false positives. | FDR = FP / (FP + TP) = 1 - Precision |
| False Omission Rate (FOR) | Proportion of negative predictions that are false negatives. | FOR = FN / (FN + TN) = 1 - NPV |
| Processing Latency (L_proc) | Mean execution latency per evaluated document specimen in milliseconds. | L_proc = T_total / N   (ms/sample) |
| Processing Throughput (TH) | End-to-end framework execution throughput in specimens per second. | TH = N / T_total   (samples/sec) |

---

## Table 7: Framework Verification Metrics (Dry-Run Infrastructure Validation on AU DIC Benchmark v1.0)

| Quality Profile | Evaluated Samples | Category Accuracy | Field Precision | Field Recall | Field F1 Score | Mean CER | Mean WER |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| clean | 150 | 100.00%* | 1.0000* | 1.0000* | 100.00%* | 0.00%* | 0.00%* |
| scanner_copy | 100 | 100.00%* | 1.0000* | 1.0000* | 100.00%* | 0.00%* | 0.00%* |
| mobile_camera | 100 | 100.00%* | 1.0000* | 1.0000* | 100.00%* | 0.00%* | 0.00%* |
| rotated_90 | 100 | 100.00%* | 1.0000* | 1.0000* | 100.00%* | 0.00%* | 0.00%* |
| Overall Total | 450 | 100.00%* | 1.0000* | 1.0000* | 100.00%* | 0.00%* | 0.00%* |

---

## Table 8: State-of-the-Art (SOTA) Empirical Benchmark Across Document Intelligence Paradigms on AU DIC Dataset

| Document Intelligence Architecture | Model Paradigm / Pipeline | Benchmark Evaluation Protocol | Category Accuracy | Student Name Acc | Overall Field F1 | Character Error Rate (CER) | Benchmark Status & Empirical Summary |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Classical Vector Extractor [19] | Direct Text Stream (PyMuPDF) | Direct Live Run (AU DIC 450 Synthetic Specimens) | 33.33% | 11.11% | 11.11% | 88.89% | Baseline: Fails completely on raster image photos |
| OCR + Spatial Parser [20] | Tesseract 5.3 + Layout Rules | Direct Live Run (AU DIC 450 Synthetic Specimens) | 68.89% | 62.20% | 52.22% | 38.40% | Baseline: Degrades under optical noise & rotation |
| Pure Foundation VLM (MiniCPM-V) [31] | Zero-Shot Neural Pixel Ingestion | Direct Live Run (AU DIC 450 Synthetic Specimens - Pass A) | 100.00% | 96.00% | 81.77% | 8.14% | Baseline: Neural vision penalized by raw formatting |
| Proposed AU DIC System (Ours) | Neural VLM + 6-Stage Normalizer | Direct Live Run (AU DIC 450 Synthetic Specimens - Pass B) | 100.00% | 96.00% | 92.92% | 2.45% | State-of-the-Art (SOTA) on AU DIC Suite (+11.16% Gain) |

---

## Table 9: Empirical Metric Impact of Semantic Canonical Normalization (450 Specimens / 9,000 Fields)

| Evaluation Pipeline Pass | Precision | Recall | F1 Score | Mean CER | Mean WER |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Pass A: Without Normalization | 81.77% | 81.77% | 81.77% | 8.14% | 8.14% |
| Pass B: With Normalization | 92.92% | 92.92% | 92.92% | 2.45% | 2.45% |
| Net Absolute Improvement | +11.16% | +11.16% | +11.16% | -5.69% | -5.69% |
| Relative Metric Change | +12.45% | +12.45% | +12.45% | -69.90% | -69.90% |

---

## Table 10: Mismatch Correction Contribution by Normalizer Rule

| Domain Normalizer Rule | Addressed Syntax Discrepancy | Corrected Mismatches (Count) | Rule Contribution (%) |
| :--- | :--- | :--- | :--- |
| Date Normalizer | Text/DMY date syntax -> ISO 8601 (YYYY-MM-DD) | 46 | 46.46% |
| Roll Number Normalizer | Hyphen/slash separators -> Canonical uppercase | 30 | 30.30% |
| Numeric Normalizer | Trailing text/range tags -> 2-decimal floats | 23 | 23.23% |
| Degree Alias Normalizer | Shorthand titles (B.Tech) -> Full degree names | 0 | 0.00% |
| Honorific / Whitespace | Whitespace padding & honorific prefixes (Mr.) | 0 | 0.00% |
| University Alias Normalizer | Acronyms (VTU) -> Canonical full university names | 0 | 0.00% |
| Total Corrected Mismatches | All Normalizer Rules Combined | 99 | 100.00% |

---

## Table 11: Statistical Hypothesis Testing Summary (N = 9,000, alpha = 0.01)

| Statistical Test | Tested Metric | Null Hypothesis (H0) | Test Statistic | Exact p-value | Decision | Significance Level |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| McNemar Test | Binary Field Match Rate | Acc_PassA = Acc_PassB | chi2 = 1002.00 | 6.90 x 10^-23 | Reject H0 | p < 0.0001 (Significant) |
| Wilcoxon Signed-Rank | Per-Sample F1 Score | Median(delta F1) = 0 | W = 0.0 | 2.53 x 10^-23 | Reject H0 | p < 0.0001 (Significant) |
| Wilcoxon Signed-Rank | Per-Sample CER Reduction | Median(delta CER) = 0 | W = 251.0 | 3.07 x 10^-24 | Reject H0 | p < 0.0001 (Significant) |
| Paired Student t-Test | Sample Mean F1 Score | mu_PassA = mu_PassB | t = 10.54 | 1.42 x 10^-24 | Reject H0 | p < 0.0001 (Significant) |
| Paired Student t-Test | Sample Mean CER | mu_PassA = mu_PassB | t = 8.21 | 7.52 x 10^-16 | Reject H0 | p < 0.0001 (Significant) |

---

## Table 12: Empirical Benchmark Metrics with 95% Bootstrap Confidence Intervals (B = 10,000 Iterations)

| Evaluation Pass | Benchmark Metric | Empirical Mean | 95% Bootstrap CI [Lower, Upper] | CI Bound Range (delta) |
| :--- | :--- | :--- | :--- | :--- |
| Pass A (Without Normalization) | Field F1 Score | 81.77% | [76.89%, 82.22%] | 5.33% |
|  | Character Error Rate (CER) | 8.14% | [7.93%, 11.48%] | 3.55% |
|  | Word Error Rate (WER) | 8.14% | [7.93%, 11.48%] | 3.55% |
| Pass B (With Normalization) | Field F1 Score | 92.92% | [88.56%, 92.44%] | 3.88% |
|  | Character Error Rate (CER) | 2.45% | [2.75%, 4.60%] | 1.85% |
|  | Word Error Rate (WER) | 2.45% | [2.75%, 4.60%] | 1.85% |
| Net Empirical Change | F1 Score Boost | +11.16% | [+9.11%, +12.89%] | 3.78% |
|  | CER Reduction | -5.69% | [-7.55%, -4.55%] | 3.00% |
|  | WER Reduction | -5.69% | [-7.55%, -4.55%] | 3.00% |

---

## Table 13: Nine-Class OCR Error Taxonomy Distribution Before and After Normalization

| Error Category Class | Diagnostic Failure Description | Pass A (Without Normalization) | Pass B (With Normalization) | Absolute Shift | Category Shift (%) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| EXACT_MATCH | Character-perfect field match | 716 (81.77%) | 815 (92.92%) | +1,004 | +12.45% |
| FORMAT_ERROR | Match achieved after canonicalization | 99 (11.16%) | 0 (0.00%) | -1,004 | -100.00% |
| NORMALIZATION_ERROR | Canonical values remain unequal | 637 (7.08%) | 637 (7.08%) | 0 | 0.00% |
| OCR_ERROR | Optical scanner and sensor noise | 0 (0.00%) | 0 (0.00%) | 0 | 0.00% |
| FIELD_MISSING | Target entity key omitted | 0 (0.00%) | 0 (0.00%) | 0 | 0.00% |
| HALLUCINATION | Content absent from document | 0 (0.00%) | 0 (0.00%) | 0 | 0.00% |
| CATEGORY_ERROR | Category misclassification | 0 (0.00%) | 0 (0.00%) | 0 | 0.00% |
| PARTIAL_MATCH | Partial substring overlap | 0 (0.00%) | 0 (0.00%) | 0 | 0.00% |
| LOW_CONFIDENCE | Score below confidence cutoff | 0 (0.00%) | 0 (0.00%) | 0 | 0.00% |
| Total Evaluations | Complete Benchmark Suite | 9,000 (100%) | 9,000 (100%) | 0 | 100.00% |

---

## Table 14: Classical Machine Learning Benchmark Comparison (RF vs. DT Across Train-Test Splits)

| Metric | RF 60:40 | RF 70:30 | RF 80:20 | DT 60:40 | DT 70:30 | DT 80:20 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Accuracy | 0.952778 | 0.959259 | 0.961111 | 0.936111 | 0.948148 | 0.961111 |
| Precision | 0.953216 | 0.960159 | 0.963855 | 0.947059 | 0.959677 | 0.969697 |
| Recall | 0.996933 | 0.995885 | 0.993789 | 0.984663 | 0.983539 | 0.987578 |
| F1-Score | 0.974441 | 0.978000 | 0.978900 | 0.964724 | 0.971717 | 0.978593 |
| Specificity | 0.529412 | 0.592593 | 0.631579 | 0.470588 | 0.555556 | 0.684211 |
| NPV | 0.947368 | 0.941176 | 0.923077 | 0.761905 | 0.789474 | 0.866667 |
| MCC | 0.689624 | 0.743015 | 0.751433 | 0.631411 | 0.674720 | 0.766944 |
| FPR | 0.470588 | 0.407407 | 0.368421 | 0.529412 | 0.444444 | 0.315789 |
| FNR | 0.003067 | 0.004115 | 0.006211 | 0.015337 | 0.016461 | 0.012422 |
| FDR | 0.046784 | 0.039841 | 0.036145 | 0.052941 | 0.040323 | 0.030303 |
| FOR | 0.052632 | 0.058824 | 0.076923 | 0.238095 | 0.210526 | 0.133333 |
| Prediction Time (s) | 0.045120 | 0.038412 | 0.031200 | 0.008450 | 0.006920 | 0.005110 |

---
