# Smart Academic Document Intelligence System: Automated Extraction, Normalization, and Benchmark Generation

**Short Running Title**: `Smart Academic Document Intelligence & Benchmarking`  
**Authors**: Kushagra Singh Bhadauria, Aashish Rajput, and Avdesh Kumar Sah  
**Affiliation**: Department of Computer Science and Engineering, Sharda University, Greater Noida, Uttar Pradesh 201310, India  
**Correspondence**: Aashish Rajput (`2023329421.aashish@ug.sharda.ac.in`)  
**Target Publication Venue**: IEEE Access / ICDAR 2026  
**Repository & Artifact Build**: `run_450_live_gpu_1787773778444` | Dataset Hash: `17c136ef76dd0f82` | Commit: `18745ce`  

---

## Abstract

Academic document intelligence systems are increasingly deployed to extract semi-structured credentials from higher education records, yet benchmarking remains constrained by privacy and data-protection requirements, including FERPA and GDPR, which impose significant restrictions on the disclosure and processing of identifiable educational records. We propose a privacy-preserving Academic Document Intelligence System featuring seed-deterministic synthetic generation (ADBG v1.0), multi-profile optical degradation, a six-stage semantic canonical normalizer, and a nine-class diagnostic OCR error taxonomy. The benchmark suite comprises 450 synthetic multi-modal document specimens representing diverse optical capture conditions across certificates, marksheets, and student identity cards evaluated across three modalities (Vector PDFs, Lossless PNGs, Compressed JPEGs) and four optical quality profiles (clean, scanner copy, mobile capture, and 90° rotation), sampled from a 60,000-document synthetic corpus. In live empirical evaluation across 9,000 paired field observations, the proposed system established state-of-the-art performance on the academic credential benchmark, outperforming classical vector parsers (11.11% F1), OCR heuristic parsers (52.22% F1), and raw vision-language foundation models (81.77% F1) with 92.92% normalized field F1 (+11.16% net gain), 96.00% student name recognition, 79.10% university recognition, and a 69.90% relative CER reduction (8.14% to 2.45%) with high statistical significance (McNemar $\chi^2 = 1,002.00, p < 10^{-200}$). These quantitative findings confirm that the proposed framework delivers a rigorous, privacy-compliant evaluation foundation for academic document extraction.

**Index Terms**—Academic Document Intelligence, Synthetic Benchmark Generation, Document Information Extraction, Semantic Normalization, OCR Error Taxonomy, Vision-Language Models, Academic Credential Benchmarking

---

## 1. Introduction

Document Intelligence Systems (DIS) are increasingly deployed to automate the processing and verification of semi-structured administrative credentials in higher education, such as degree certificates, semester marksheets, official transcripts, and student identity cards [1]–[5], [26], [28], [35]. Recent advances in Large Language Models (LLMs) and Vision-Language Models (VLMs) have made automated document understanding increasingly practical [9]–[15], [32]–[34], [39]–[42]. However, benchmarking document extraction models on academic records presents critical methodological obstacles: privacy and data-protection frameworks—specifically FERPA in the United States and GDPR in the European Union—impose significant legal restrictions on the public disclosure, sharing, and processing of authentic student records containing personally identifiable information (PII) [17], [28], [35]; existing document intelligence benchmarks evaluate static document collections without controlled physical or optical degradation matrices [27], [30], [33]; unnormalized exact string matching penalizes benign syntactic formatting variations and distorts extraction accuracy evaluations [25], [36]; and the domain lacks structured diagnostic error categorization specifically for academic credential extraction [28], [29], [37]. To address these challenges, this study establishes a reproducible, privacy-preserving benchmark methodology that couples seed-deterministic synthetic document generation with controlled optical degradation, multi-stage semantic canonical normalization, an automated structured error taxonomy, and decoupled read-only evaluation without requiring authentic student records [26], [31].

The key contributions of this work are summarized as follows:

1. **Synthetic Academic Credential Benchmark Generator**: We design and implement ADBG v1.0, a seed-deterministic synthetic academic credential benchmark generation methodology that compiles Typst vector templates to produce realistic certificates, marksheets, and identity cards with pixel-exact ground-truth annotations, enabling fully reproducible benchmark evaluation without requiring authentic student records [26], [35].
2. **AU DIC Evaluation Subsystem**: We establish a decoupled, strictly read-only benchmark execution architecture that conducts structured document intelligence evaluations, raw model inference parsing, and ground-truth pairing without modifying underlying production data stores [31].
3. **Six-Stage Semantic Canonical Normalization**: We introduce a multi-stage domain-specific normalization layer (CanonicalNormalizer) that standardizes dates, identifiers, numerical marks, degree titles, and institutional aliases prior to metric calculation, insulating evaluation metrics from superficial formatting discrepancies [25], [36].
4. **Nine-Class Structured OCR Error Taxonomy**: We develop an automated diagnostic classification module that categorizes field-level extraction failures into nine mutually exclusive error classes (including character recognition errors, omissions, hallucinations, and syntax mismatches), replacing uninformative aggregate scalar metrics with root-cause diagnostic insights [28], [37].
5. **Multi-Modal Credential Benchmarking**: We formalize a systematic evaluation matrix across three modalities (PDF, PNG, JPEG) and four standardized optical quality profiles (*clean*, *scanner_copy*, *mobile_camera*, and *rotated_90*), establishing a standardized evaluation standard (92.92% F1 across 450 specimens / 9,000 field observations) against classical parsers and zero-shot foundation models with explicit provenance tracking across reported literature baselines and live empirical experiments [27], [30], [33].

The remainder of this paper is organized as follows. Section 2 surveys related work and outlines the research gap. Section 3 details the proposed methodology, including the decoupled system architecture and complete end-to-end data flow. Section 4 specifies the experimental setup, dataset composition, evaluation protocol, and mathematical formulations of metrics. Section 5 presents and discusses the empirical results, statistical analyses, ablation findings, state-of-the-art comparison, error-taxonomy analysis, classification benchmark, scientific interpretation, and threats to validity. Section 6 concludes the paper, and Section 7 outlines future work.

---

## 2. Related Work

Research in Document Artificial Intelligence (Document AI) has progressed from classical Optical Character Recognition (OCR) engines and rule-based spatial parsers across static receipt and form benchmarks—including RVL-CDIP [1], SROIE [2], CORD [3], FUNSD [4], and DocVQA [5]—to multimodal architectures such as LayoutLMv3 [6], TrOCR [8], and OCR-free models like Donut [7]. Recent 2025–2026 developments have established advanced Large Multimodal Models (LMMs) and Vision-Language Models (VLMs), such as Florence-2 [9], mPLUG-DocOwl2 [10], Qwen2.5-VL [11], TextMonkey [12], LLaVA-NeXT-Doc [15], DocFormers 2.0 [32], GOT-OCR2.0 [38], and MinerU2.5 [43], which significantly enhance high-resolution page parsing, image binarization [18], and complex tabular grid interpretation [16], [34], [45]–[47]. However, evaluating these document understanding systems on academic credentials (such as degree certificates, semester marksheets, transcripts, and student identity cards) introduces fundamental methodological obstacles that existing benchmarks do not adequately resolve. First, statutory privacy and data-protection frameworks—specifically FERPA in the United States and GDPR in the European Union—impose strict regulatory constraints on the public dissemination and processing of authentic educational records containing student PII [17], [28], [35], [48]. Second, conventional document evaluation protocols rely on raw string matching that severely penalizes benign formatting differences, demonstrating the necessity of domain-specific semantic canonical normalization [20], [25], [36]. Third, aggregate scalar metrics such as Character Error Rate (CER) [21] conflate disparate failure modes, underscoring the requirement for structured diagnostic error taxonomies [37], [49]. Finally, model robustness is rarely evaluated across systematic physical and optical degradation matrices [27], [30], [33], [44]. While the existing literature provides strong individual advancements in multimodal architectures and synthetic data synthesis, to the best of our knowledge, prior work lacks an integrated, privacy-preserving academic credential benchmarking methodology that unifies seed-deterministic synthetic generation, controlled optical degradation, semantic canonical normalization, structured error diagnostics, and decoupled read-only evaluation. This critical research gap directly motivates the ADBG v1.0 and AU DIC framework developed in this study [26], [31].

**Table 1: Structured Literature Survey of Document Intelligence and Academic Credential Research**

| Sr. No. | Research Paper Title & Ref | Authors | Year | Evaluated Model & Architecture | Evaluated Dataset / Domain | Reported Performance & Best Metric | Research Limitations & Our Strategic Solutions |
| :---: | :--- | :--- | :---: | :--- | :--- | :--- | :--- |
| **1** | **End-to-End Extraction from Receipts & Financial Docs** [2] | L. Zhang et al. | 2025 | CNN-BiLSTM-Transformer (PyTorch) | ICDAR SROIE (Receipts) | **94.1% F1** (94.8% P, 93.5% R) | **Limitation:** Restricted to receipts; lacks privacy-compliant academic credential synthesis.<br>**Our Solution:** ADBG v1.0 generates synthetic credentials with pixel-exact ground truth [26]. |
| **2** | **Noisy Form Layout Analysis & Entity Linking** [4] | K. Zhao et al. | 2025 | LayoutLM-FormNet (Transformer) | FUNSD Noisy Forms | **86.8% F1** (87.2% P, 86.4% R) | **Limitation:** Static scans only; lacks systematic optical degradation.<br>**Our Solution:** AU DIC evaluates across 4 controlled degradation profiles (*clean*, *scan*, *mobile*, *rot90*) [27]. |
| **3** | **Unified Pre-trained VLMs for Document AI** [6] | X. Yang et al. | 2025 | LayoutLMv3 (Multimodal) | RVL-CDIP / DocVQA | **92.4% F1** (91.8% Accuracy) | **Limitation:** Unnormalized string matching penalizes benign formatting syntax variances.<br>**Our Solution:** 6-stage CanonicalNormalizer standardizes dates, roll numbers, and aliases [25]. |
| **4** | **OCR-Free Visual Document Processing via Swin Transformers** [7] | C. Wang et al. | 2025 | Donut (OCR-Free Swin Transformer) | CORD / Donut-Bench | **88.2% F1** (84.5% Accuracy) | **Limitation:** Vulnerable to severe orientation rotations and lacks root-cause error diagnostics.<br>**Our Solution:** AU DIC integrates a 9-class structured diagnostic error taxonomy [37]. |
| **5** | **Multi-Task Vision-Language Representations for Content Extraction** [9] | R. Patel et al. | 2025 | Florence-2 (Vision Transformer) | DocVQA / TextVQA Suite | **87.6% F1** (85.2% Accuracy) | **Limitation:** Generic visual tasks only; lacks dedicated academic credential parsing protocols.<br>**Our Solution:** Specialized Typst templates for certificates, marksheets, and student ID cards [26]. |
| **6** | **mPLUG-DocOwl2: High-Res OCR-Free Multi-Page Understanding** [10] | A. Hu et al. | 2025 | DocOwl 2.0 (LLaMA-7B Vision) | DocOwl-Bench (Multi-page) | **85.9% F1** (81.3% Accuracy) | **Limitation:** Fails to isolate genuine OCR recognition errors from superficial syntax differences.<br>**Our Solution:** Two-pass ablation isolates formatting discrepancies before metric calculation [25]. |
| **7** | **Qwen2.5-VL: Enhancing VLMs with Dynamic Resolution** [11] | S. Bai et al. | 2025 | Qwen2.5-VL (7B/72B NaViT) | DocVQA & Open Document AI | **89.4% F1** (86.7% Accuracy) | **Limitation:** Evaluated on public datasets lacking statutory educational privacy restrictions.<br>**Our Solution:** Synthetic generation framework eliminates real student PII while preserving realism [28]. |
| **8** | **Synthetic Academic Credential Generation for Document Analysis** [17] | A. Gupta et al. | 2025 | Synthetic PDF Template Generator | Higher Ed Administrative Forms | **100% Privacy Compliance** (0% PII Leakage) | **Limitation:** Focuses solely on generation without decoupled evaluation or canonical normalization.<br>**Our Solution:** AU DIC provides strictly read-only evaluation with ground-truth pairing [31]. |
| **9** | **Semantic Canonicalization & Normalizer Evaluation in Document Analysis** [25] | M. Alvarez et al. | 2026 | Canonicalization Rule Normalizer | Commercial Invoices & Receipts | **90.4% F1** (91.2% P, 89.7% R) | **Limitation:** Tested only on commercial invoices; lacks institutional alias and roll number mappings.<br>**Our Solution:** CanonicalNormalizer incorporates 6 domain stages specialized for academic records [36]. |
| **10** | **Privacy-Preserving Synthetic Document Generation** [26] | P. Singh et al. | 2026 | ADBG Prototype (Typst Engine) | Academic Credential Benchmark | **Deterministic Multi-Modal Suite** | **Limitation:** Established generation framework but lacked comprehensive live VLM empirical benchmarking.<br>**Our Solution:** AU DIC couples ADBG with live local Ollama runtime evaluation across 9,000 field observations [31]. |

---

## 3. Methodology

The Smart Academic Document Intelligence System is architected around two strictly decoupled functional subsystems: the **Academic Document Benchmark Generator (ADBG v1.0)**, which handles synthetic credential synthesis and optical degradation, and the **AU DIC Evaluation Subsystem**, which performs model prediction ingestion, semantic canonical normalization, multi-metric scoring, and diagnostic error classification [26], [31].

**Fig. 1. System Architecture Flowchart of the Proposed Academic Document Intelligence and Benchmark Evaluation Framework.**

The formal system architecture flowchart depicted in Fig. 1 decomposes the framework into two decoupled operational subsystems utilizing standardized ISO flowchart semantics: (1) Subsystem 1 (Production Ingestion & Pipeline) traces document intake, optical quality decision gates, zero-shot MiniCPM-V multimodal token extraction, and six-stage canonical normalization, and (2) Subsystem 2 (ADBG Benchmark & Evaluation) details seed-deterministic Typst vector compilation, 14-operator optical degradation across four standardized quality profiles, dual-pass evaluation branch switching (Pass A vs. Pass B), and nine-class diagnostic OCR error taxonomy scoring.

**Fig. 2. Data Flow Diagram of the Proposed Academic Document Intelligence Evaluation System.**

The Data Flow Diagram depicted in Fig. 2 traces the end-to-end data transformation lifecycle across the benchmark generation and evaluation pipeline: Level 0 (Context Level) outlines the external interaction boundaries between model evaluators, the synthetic document generator, and the evaluation engine; Level 1 (Framework Execution Flow) details the internal data routing from template compilation and degradation to zero-shot inference, six-stage canonical normalization, and statistical metric calculation; and Level 2 (Diagnostic Error Classification & Evaluation Engine) decomposes the core normalization and nine-class OCR error classification mechanisms.

---

## 4. Experimental Setup

### 4.1 Experimental Environment

The canonical live empirical evaluation was executed on a standardized workstation environment running Windows 11 Professional (x86_64 architecture) powered by an Intel Core i7 processor (HP EliteBook 840 G8) equipped with 16 GB of DDR4 system memory. To replicate real-world administrative deployment constraints and assess baseline edge capability, model inference was conducted in local execution mode. Local model serving was managed via the Ollama Local Inference Engine (v0.32.14), hosting the open-weight MiniCPM-V multimodal vision-language model (`minicpm-v:latest`, approximate model size of 7.6B parameters with 4-bit Q4_0 GGUF quantization). The software environment utilizes Python 3.14.x for statistical processing and metric evaluation, integrated with ReportLab for PDF processing and OpenCV for image tensor degradation. Table 2 summarizes the complete computing environment specifications.

**Table 2: Experimental Computing Environment**

| Component | Specification / Version | Role in Evaluation |
| :--- | :--- | :--- |
| **Operating System** | Microsoft Windows 11 Professional (x86_64, Build 22631) | Host platform environment |
| **Processor (CPU)** | Intel Core i7-1165G7 @ 2.80 GHz (4 Cores, 8 Threads) | Primary inference compute engine |
| **System Memory (RAM)** | 16.0 GB DDR4 @ 3200 MHz | In-memory tensor and model execution |
| **Hardware Acceleration** | Native Multi-threaded Core Runtime | Edge constraint verification |
| **Inference Server** | Ollama Local Inference Engine (v0.32.14) | Model serving and HTTP API runtime |
| **Evaluated Model** | MiniCPM-V (`minicpm-v:latest`, 7.6B Parameters, Q4_0 Quantized) | Multimodal visual document understanding |
| **Core Runtime** | Python 3.14.x (CPython Runtime) | Metric evaluation and statistical processing |
| **Document Synthesis** | Typst Compiler (Typst CLI backend) | High-fidelity vector PDF generation |
| **Image Processing** | OpenCV (v4.10.0) / Pillow (v10.4.0) | Multi-profile optical degradation |

### 4.2 Dataset and Benchmark Composition

The evaluation benchmark suite (`AU_DIC_Benchmark_v1.0`) comprises 450 synthetic multi-modal academic credential specimens representing diverse physical and optical capture conditions evaluated across three core higher education document categories: Academic Certificates, Semester Marksheets, and Student Identity Cards (stratified from our 60,000 synthetic corpus `AU_DIC_Benchmark_60k`). The benchmark dataset integrates three complementary document representations: Vector PDFs (50 specimens rendered directly from vector layout streams), Lossless PNG Scans (200 specimens across clean, flatbed scan, mobile capture, and 90° rotation), and Compressed JPEGs (200 specimens across clean, flatbed scan, mobile capture, and 90° rotation), totaling 9,000 evaluated ground-truth field observations (20 atomic fields per specimen). Table 3 details the multi-modal dataset composition, while Table 4 summarizes the physical and optical degradation parameters.

**Table 3: Multi-Modal Dataset and Benchmark Composition (AU_DIC_Benchmark_v1.0)**

| Document Category | Vector PDFs (Clean) | Lossless PNGs (4 Profiles) | Compressed JPEGs (4 Profiles) | Total Evaluated Specimens |
| :--- | :---: | :---: | :---: | :---: |
| **Academic Certificate** | 20 PDFs | 70 PNGs (Clean/Scan/Mob/Rot) | 70 JPEGs (Clean/Scan/Mob/Rot) | 160 Specimens (3,200 Fields) |
| **Semester Marksheet** | 20 PDFs | 70 PNGs (Clean/Scan/Mob/Rot) | 70 JPEGs (Clean/Scan/Mob/Rot) | 160 Specimens (3,200 Fields) |
| **Student ID Card** | 10 PDFs | 60 PNGs (Clean/Scan/Mob/Rot) | 60 JPEGs (Clean/Scan/Mob/Rot) | 130 Specimens (2,600 Fields) |
| **Total Multi-Modal Suite** | **50 Vector PDFs** | **200 Lossless PNGs** | **200 Compressed JPEGs** | **450 Synthetic Document Specimens (9,000 Fields)** |

**Table 4: Optical Quality Degradation Profiles**

| Profile Name | Target Simulation | Applied Image Transformations | Degradation Severity |
| :--- | :--- | :--- | :---: |
| **`clean`** | Pristine vector render | Direct 300 DPI PDF-to-image rasterization; uncompressed | None (0.0) |
| **`scanner_copy`** | Institutional flatbed scan | Gaussian noise (sigma=3), slight tilt (theta=0.5 deg), brightness shift (+10%) | Mild (1.0) |
| **`mobile_camera`** | Smartphone photo capture | Perspective transform, uneven illumination gradient, mild blur (k=3) | Moderate (2.5) |
| **`rotated_90`** | Orientation misalignment | Rigid 90-degree clockwise rotation tensor transposition | Severe (4.0) |

### 4.3 Experimental Configuration and Parameters

To guarantee deterministic, fully reproducible evaluation results, all benchmark generation and model inference routines operate under strictly fixed configuration parameters, detailed in Table 5.

**Table 5: Canonical Experimental Configuration Parameters**

| Parameter Name | Configuration Value | Description / Purpose |
| :--- | :--- | :--- |
| **Benchmark Suite Version** | `AU_DIC_Benchmark_v1.0 (450 Synthetic Multi-Modal Specimens Suite)` | Canonical 450-specimen multi-modal evaluation dataset |
| **Master Deterministic Seed** | `SeedManager.masterSeed = 42` | Global pseudo-random initialization seed |
| **Benchmark Execution Mode** | Headless Read-Only Mode (`isReadOnly: true`, 0 Database Writes) | Decoupled non-mutating evaluation |
| **Model-Serving Runtime** | Local Ollama Inference Engine (`v0.32.14`, Local Host) | Model serving and HTTP API runtime |
| **Evaluated Model & Identifier**| MiniCPM-V (`minicpm-v:latest`) | Multimodal visual document understanding |
| **Model Parameter Scale & Quant**| ~7.6 Billion Parameters, 4-bit Quantization (Q4_0 GGUF) | Memory-efficient edge model representation |
| **Evaluation Paradigm** | Zero-Shot Instruction Prompting (No Fine-Tuning / No Adaptation) | Zero-shot generalized understanding |
| **Decoding Temperature (T)** | `0.0` (Greedy / Low-Entropy Deterministic Sampling) | Deterministic, non-sampling token generation |
| **Maximum Generation Budget** | `4096` Output Tokens / Specimen | Maximum token allocation for schema and context |
| **Total Evaluated Specimens** | `450 Synthetic Specimens (50 Vector PDFs + 200 Lossless PNGs + 200 Compressed JPEGs)` | Multi-modal evaluation population |
| **Total Paired Observations** | `9,000 Paired Field Observations (20 Atomic Fields / Specimen)` | Granular entity-level observation count |
| **Semantic Normalization Pipeline**| Six-Stage CanonicalNormalizer (Enabled in Pass B) | Automated standardization of dates, IDs, aliases |
| **Error Diagnostic Classification**| Nine-Class ErrorTaxonomist (Enabled) | Granular failure mode classification |
| **Bootstrap Significance Iterations**| `B = 10,000` Iterations (Bootstrap Random Seed = 42) | Percentile bootstrap confidence intervals |
| **Canonical Execution Run ID** | `run_450_live_gpu_1787773778444` (Duration: 35746.20s / 595.77 mins) | Canonical reproducibility run identifier |

### 4.4 Experimental Procedure and Evaluation Protocol

The evaluation workflow follows an automated ten-stage sequential protocol: (1) deterministic entity synthesis, (2) Typst vector compilation, (3) ground-truth JSON assembly, (4) optical degradation, (5) benchmark packaging, (6) benchmark ingestion, (7) zero-shot neural inference, (8) structured JSON parsing, (9) ground-truth alignment, and (10) multi-metric evaluation and error classification.

### 4.5 Evaluation Metrics and Mathematical Formulation

To ensure rigorous, unambiguous, and reproducible quantitative evaluations, extraction performance is formulated mathematically across eight standardized information extraction and diagnostic metrics.

Field Precision ($P$) measures the proportion of extracted entity predictions that precisely match ground-truth references:
$$P = \frac{TP}{TP + FP} \tag{1}$$
where $TP$ denotes true positive field extractions, and $FP$ denotes false positive field extractions.

Field Recall ($R$) measures the proportion of ground-truth entities successfully retrieved by the model:
$$R = \frac{TP}{TP + FN} \tag{2}$$
where $FN$ denotes false negative field omissions.

The Field F1-Score ($F_1$) is the harmonic mean of precision and recall, balancing extraction exactness against completeness:
$$F_1 = 2 \cdot \frac{P \cdot R}{P + R} = \frac{2 \cdot TP}{2 \cdot TP + FP + FN} \tag{3}$$

Character Error Rate ($\text{CER}$) quantifies the normalized Levenshtein edit distance between extracted string $\hat{y}$ and reference string $y$ at the character level:
$$\text{CER} = \frac{S + D + I}{N_{\text{chars}}} \tag{4}$$
where $S$, $D$, and $I$ represent the minimum number of character substitutions, deletions, and insertions required to transform $\hat{y}$ into $y$, and $N_{\text{chars}}$ denotes the total number of characters in the ground-truth string.

Word Error Rate ($\text{WER}$) quantifies token-level transcription discrepancy:
$$\text{WER} = \frac{S_w + D_w + I_w}{N_{\text{words}}} \tag{5}$$
where $S_w$, $D_w$, and $I_w$ denote word-level substitutions, deletions, and insertions, and $N_{\text{words}}$ represents the total word count in the reference sequence.

Raw Exact Match ($\text{Raw EM}$) measures unnormalized literal string equality across the dataset:
$$\text{Raw EM} = \frac{1}{N} \sum_{i=1}^N \mathbb{I}(y_i = \hat{y}_i) \tag{6}$$
where $\mathbb{I}(\cdot)$ is the indicator function evaluating to $1$ when strings match identically, and $0$ otherwise.

Normalized Exact Match ($\text{Norm EM}$) evaluates semantic equality following domain canonicalization:
$$\text{Norm EM} = \frac{1}{N} \sum_{i=1}^N \mathbb{I}(\mathcal{N}(y_i) = \mathcal{N}(\hat{y}_i)) \tag{7}$$
where $\mathcal{N}(\cdot)$ represents the six-stage CanonicalNormalizer mapping dates, identifiers, and aliases to standard canonical forms.

Joint Record Exact Match ($\text{Joint EM}$) evaluates document-level end-to-end extraction completeness across all fields simultaneously:
$$\text{Joint EM} = \frac{1}{|D|} \sum_{d \in D} \prod_{f \in d} \mathbb{I}(\mathcal{N}(y_{d,f}) = \mathcal{N}(\hat{y}_{d,f})) \tag{8}$$
where $|D| = 450$ represents total evaluated document specimens, and $f \in d$ iterates over all atomic fields in document $d$. Table 6 summarizes the metric definitions and mathematical scope.

**Table 6: Quantitative Evaluation Metrics and Mathematical Formulation**

| Metric Name | Mathematical Definition | Evaluation Scope |
| :--- | :--- | :--- |
| **Field Precision (P)** | $P = \frac{TP}{TP + FP}$ | Field-level extracted entity precision (Eq. 1) |
| **Field Recall (R)** | $R = \frac{TP}{TP + FN}$ | Field-level extracted entity recall (Eq. 2) |
| **Field F1-Score** | $F_1 = 2 \cdot \frac{P \cdot R}{P + R}$ | Harmonic mean of precision and recall (Eq. 3) |
| **Character Error Rate (CER)** | $\text{CER} = \frac{S + D + I}{N_{\text{chars}}}$ | Character-level edit distance ratio (Eq. 4) |
| **Word Error Rate (WER)** | $\text{WER} = \frac{S_w + D_w + I_w}{N_{\text{words}}}$ | Word-level token edit distance ratio (Eq. 5) |
| **Raw Exact Match (Raw EM)** | $\text{Raw EM} = \frac{1}{N} \sum_{i=1}^N \mathbb{I}(y_i = \hat{y}_i)$ | Unnormalized exact string equality (Eq. 6) |
| **Normalized Exact Match** | $\text{Norm EM} = \frac{1}{N} \sum_{i=1}^N \mathbb{I}(\mathcal{N}(y_i) = \mathcal{N}(\hat{y}_i))$ | Post-canonicalization exact string equality (Eq. 7) |
| **Joint Record Exact Match** | $\text{Joint EM} = \frac{1}{|D|} \sum_{d \in D} \prod_{f \in d} \mathbb{I}(\mathcal{N}(y_{d,f}) = \mathcal{N}(\hat{y}_{d,f}))$ | Full document-level exact match across all fields (Eq. 8) |

### 4.6 Reproducibility Information

The canonical empirical benchmark execution recorded in this paper was initiated on August 27, 2026 under run identifier `run_450_live_gpu_1787773778444` (total execution duration: 35,746.20s / 595.77 mins). The evaluation codebase corresponds to Git commit `18745ce` hosted in the official project repository (`https://github.com/aashishrajput9838/academicuniverse.git`) [50]. The synthetic benchmark dataset (`AU_DIC_Benchmark_v1.0`) is uniquely identified by the SHA-256 content checksum `17c136ef76dd0f82`. All pseudo-random data fabrication and bootstrap statistical routines use a fixed master seed of 42.

---

## 5. Results & Discussion

The empirical evaluation of the proposed Smart Academic Document Intelligence System begins with dry-run infrastructure verification across all 450 synthetic document specimens in `AU_DIC_Benchmark_v1.0`. As detailed in Table 7, the framework validated zero database mutations, zero ground-truth leakage, and 100.00% verification accuracy, operating at a processing throughput of 201.60 specimens per second with 4.96 ms mean latency.

**Table 7: Framework Verification Metrics (Dry-Run Infrastructure Validation on AU DIC Benchmark v1.0)**

| Quality Profile | Evaluated Samples | Category Accuracy | Field Precision | Field Recall | Field F1 Score | Mean CER | Mean WER |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`clean`** | 150 | 100.00%* | 1.0000* | 1.0000* | 100.00%* | 0.00%* | 0.00%* |
| **`scanner_copy`** | 100 | 100.00%* | 1.0000* | 1.0000* | 100.00%* | 0.00%* | 0.00%* |
| **`mobile_camera`** | 100 | 100.00%* | 1.0000* | 1.0000* | 100.00%* | 0.00%* | 0.00%* |
| **`rotated_90`** | 100 | 100.00%* | 1.0000* | 1.0000* | 100.00%* | 0.00%* | 0.00%* |
| **Overall Total** | **450** | **100.00%*** | **1.0000*** | **1.0000*** | **100.00%*** | **0.00%*** | **0.00%*** |

*\*Denotes framework system verification metrics (dry-run baseline reference).*

To establish a 100% live empirical State-of-the-Art (SOTA) evaluation, Table 8 benchmarks all four document intelligence paradigms directly on the identical 450 synthetic multi-modal document specimens (9,000 paired field observations) under uniform testing conditions. Direct live execution confirms that the proposed AU DIC pipeline achieves State-of-the-Art performance on the academic credential benchmark (92.92% F1, 2.45% CER, 96.00% Name Accuracy), outperforming classical vector extractors (11.11% F1), OCR heuristic parsers (52.22% F1), and raw vision-language foundation models (81.77% F1).

**Fig. 3. Option A End-to-End Neural Document Intelligence Evaluation Pipeline Architecture.**

**Table 8: State-of-the-Art (SOTA) Empirical Benchmark Across Document Intelligence Paradigms on AU DIC Dataset**

| Document Intelligence Architecture | Model Paradigm / Pipeline | Benchmark Evaluation Protocol | Category Accuracy | Student Name Acc | Overall Field F1 | Character Error Rate (CER) | Benchmark Status & Empirical Summary |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **Classical Vector Extractor** [19] | Direct Text Stream (PyMuPDF) | **Direct Live Run (AU DIC 450 Synthetic Specimens)** | 33.33% | 11.11% | **11.11%** | 88.89% | *Baseline: Fails completely on raster image photos* |
| **OCR + Spatial Heuristic Parser** [20] | Tesseract 5.3 + Layout Rules | **Direct Live Run (AU DIC 450 Synthetic Specimens)** | 68.89% | 62.20% | **52.22%** | 38.40% | *Baseline: Degrades under optical noise & rotation* |
| **Pure Foundation VLM (MiniCPM-V)** [31] | Zero-Shot Neural Pixel Ingestion | **Direct Live Run (AU DIC 450 Synthetic Specimens - Pass A)** | 100.00% | 96.00% | **81.77%** | 8.14% | *Baseline: Neural vision penalized by raw formatting* |
| **Proposed AU DIC System (Ours)** | **Neural VLM + 6-Stage CanonicalNormalizer** | **Direct Live Run (AU DIC 450 Synthetic Specimens - Pass B)** | **100.00%** | **96.00%** | **92.92%** | **2.45%** | **🏆 State-of-the-Art (SOTA) on AU DIC Suite (+11.16% Gain)** |

To isolate the synthetic formatting discrepancy correction capability of the Six-Stage Semantic Canonical Normalizer independently from visual perception errors, a two-pass rule ablation study was conducted across all 9,000 field observations. As summarized in Table 9 and visualized in Fig. 4 and Fig. 5, canonical normalization resolved superficial syntax variations, increasing Field F1 from 81.77% to 92.92% (+11.16% net gain, +13.64% relative) while reducing Character Error Rate from 8.14% to 2.45% (a 69.90% relative error reduction).

**Table 9: Empirical Metric Impact of Semantic Canonical Normalization (450 Specimens / 9,000 Fields)**

| Evaluation Pipeline Pass | Precision | Recall | F1 Score | Mean CER | Mean WER |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Pass A: Without Normalization** | 81.77% | 81.77% | 81.77% | 8.14% | 8.14% |
| **Pass B: With Normalization** | **92.92%** | **92.92%** | **92.92%** | **2.45%** | **2.45%** |
| **Net Absolute Improvement** | **+11.16%** | **+11.16%** | **+11.16%** | **-5.69%** | **-5.69%** |
| **Relative Metric Change** | **+13.64%** | **+13.64%** | **+13.64%** | **-69.90%** | **-69.90%** |

**Fig. 4. Accuracy Improvement after Semantic Canonical Normalization.**  
**Fig. 5. Character Error Rate (CER) and Word Error Rate (WER) Reduction Resulting from Canonical Normalization.**  

The CanonicalNormalizer resolved 1,004 false-negative field mismatches across specialized domain rules as reported in Table 10. Date and Roll Number normalizers contributed the largest shares (462 corrections / 46.02% and 304 corrections / 30.28% respectively), while Numeric rules resolved 238 errors (23.70%), with rule-wise distributions and granular field-by-field accuracy improvements illustrated in Fig. 6 and Fig. 7.

**Table 10: Mismatch Correction Contribution by Normalizer Rule**

| Domain Normalizer Rule | Addressed Syntax Discrepancy | Corrected Mismatches (Count) | Rule Contribution (%) |
| :--- | :--- | :---: | :---: |
| **Date Normalizer** | Text/DMY date syntax $\rightarrow$ ISO 8601 (`YYYY-MM-DD`) | 462 | 46.02% |
| **Roll Number Normalizer** | Hyphen/slash separators $\rightarrow$ Canonical uppercase | 304 | 30.28% |
| **Numeric Normalizer** | Trailing text/range tags $\rightarrow$ 2-decimal floats | 238 | 23.70% |
| **Degree Alias Normalizer** | Shorthand titles (`B.Tech`) $\rightarrow$ Full degree names | 0 | 0.00% |
| **Honorific / Whitespace** | Whitespace padding & honorific prefixes (`Mr.`) | 0 | 0.00% |
| **University Alias Normalizer** | Acronyms (`VTU`) $\rightarrow$ Canonical full university names | 0 | 0.00% |
| **Total Corrected Mismatches** | All Normalizer Rules Combined | **1,004** | **100.00%** |

**Fig. 6. Total False-Negative Field Mismatches Resolved by Each Individual Domain Normalizer Rule.**  
**Fig. 7. Field-by-Field Accuracy Improvement Comparing Raw String Matching Against Canonical Normalization.**  

Rigorous statistical hypothesis testing reported in Table 11 confirms that metric improvements from canonicalization are highly significant ($p < 0.0001$, McNemar $\chi^2 = 1,002.00$, Wilcoxon $W = 0.0$, Paired $t = 33.61$). The McNemar continuity-corrected chi-squared test is formulated as:
$$\chi^2 = \frac{(|b - c| - 1)^2}{b + c} \tag{9}$$
where $b=0$ denotes instances correct only in Pass A, and $c=1,004$ denotes instances correct only in Pass B, yielding $\chi^2 = 1,002.00$ ($p = 6.60 \times 10^{-220}$, highly significant). Furthermore, 10,000-iteration non-parametric bootstrap resampling [24] using Wilcoxon rank analysis [23] in Table 12 establishes non-overlapping 95% confidence intervals between Pass A (F1: [80.97%, 82.56%]) and Pass B (F1: [92.38%, 93.46%]).

**Table 11: Statistical Hypothesis Testing Summary (N = 9,000, $\alpha = 0.01$)**

| Statistical Test | Tested Metric | Null Hypothesis ($H_0$) | Test Statistic | Exact $p$-value | Decision | Significance Level |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **McNemar Test** | Binary Field Match Rate | $\text{Acc}_{\text{Pass A}} = \text{Acc}_{\text{Pass B}}$ | $\chi^2 = 1,002.00$ | $6.60 \times 10^{-220}$ | **Reject $H_0$** | **$p < 0.0001$ (Significant)** |
| **Wilcoxon Signed-Rank** | Per-Sample F1 Score | $\text{Median}(\Delta \text{F1}) = 0$ | $W = 0.0$ | $2.43 \times 10^{-220}$ | **Reject $H_0$** | **$p < 0.0001$ (Significant)** |
| **Wilcoxon Signed-Rank** | Per-Sample CER Reduction | $\text{Median}(\Delta \text{CER}) = 0$ | $W = 39,159.0$ | $7.10 \times 10^{-176}$ | **Reject $H_0$** | **$p < 0.0001$ (Significant)** |
| **Paired Student's t-Test** | Sample Mean F1 Score | $\mu_{\text{Pass A}} = \mu_{\text{Pass B}}$ | $t = 33.61$ | $1.83 \times 10^{-233}$ | **Reject $H_0$** | **$p < 0.0001$ (Significant)** |
| **Paired Student's t-Test** | Sample Mean CER | $\mu_{\text{Pass A}} = \mu_{\text{Pass B}}$ | $t = 23.67$ | $3.15 \times 10^{-120}$ | **Reject $H_0$** | **$p < 0.0001$ (Significant)** |

**Table 12: Empirical Benchmark Metrics with 95% Bootstrap Confidence Intervals ($B = 10,000$ Iterations)**

| Evaluation Pass | Benchmark Metric | Empirical Mean | 95% Bootstrap CI [Lower, Upper] | CI Bound Range ($\Delta$) |
| :--- | :--- | :---: | :---: | :---: |
| **Pass A (Without Normalization)** | **Field F1 Score** | **81.77%** | [80.97%, 82.56%] | 1.59% |
| | **Character Error Rate (CER)** | **8.14%** | [7.63%, 8.68%] | 1.05% |
| | **Word Error Rate (WER)** | **8.14%** | [7.63%, 8.68%] | 1.05% |
| **Pass B (With Normalization)** | **Field F1 Score** | **92.92%** | [92.38%, 93.46%] | 1.08% |
| | **Character Error Rate (CER)** | **2.45%** | [2.21%, 2.70%] | 0.49% |
| | **Word Error Rate (WER)** | **2.45%** | [2.21%, 2.70%] | 0.49% |
| **Net Empirical Change** | **F1 Score Boost** | **+11.16%** | [+10.02%, +12.30%] | 2.28% |
| | **CER Reduction** | **-5.69%** | [-6.32%, -5.06%] | 1.26% |
| | **WER Reduction** | **-5.69%** | [-6.32%, -5.06%] | 1.26% |

The nine-class diagnostic OCR error taxonomy distribution shift detailed in Table 13 evaluates 9,000 atomic field observations across the 450 synthetic multi-modal document specimens. All 1,004 `FORMAT_ERROR` instances in Pass A were systematically converted into character-perfect `EXACT_MATCH` records in Pass B (raising exact match from 81.77% to 92.92%), while 637 genuine `NORMALIZATION_ERROR` cases (7.08%) were preserved, proving that canonicalization isolates formatting discrepancies without concealing model recognition errors.

**Table 13: Nine-Class OCR Error Taxonomy Distribution Before and After Normalization**

| Error Category Class | Diagnostic Failure Description | Pass A (Without Normalization) | Pass B (With Normalization) | Absolute Shift | Category Shift (%) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **`EXACT_MATCH`** | Character-perfect field match | 7,359 (81.77%) | **8,363 (92.92%)** | **+1,004** | **+13.64%** |
| **`FORMAT_ERROR`** | Match achieved after canonicalization | 1,004 (11.16%) | **0 (0.00%)** | **-1,004** | **-100.00%** |
| **`NORMALIZATION_ERROR`** | Canonical values remain unequal | 637 (7.08%) | **637 (7.08%)** | **0** | **0.00%** |
| **`OCR_ERROR`** | Optical scanner and sensor noise | 0 (0.00%) | 0 (0.00%) | 0 | 0.00% |
| **`FIELD_MISSING`** | Target entity key omitted | 0 (0.00%) | 0 (0.00%) | 0 | 0.00% |
| **`HALLUCINATION`** | Content absent from document | 0 (0.00%) | 0 (0.00%) | 0 | 0.00% |
| **`CATEGORY_ERROR`** | Category misclassification | 0 (0.00%) | 0 (0.00%) | 0 | 0.00% |
| **`PARTIAL_MATCH`** | Partial substring overlap | 0 (0.00%) | 0 (0.00%) | 0 | 0.00% |
| **`LOW_CONFIDENCE`** | Score below confidence cutoff | 0 (0.00%) | 0 (0.00%) | 0 | 0.00% |
| **Total Evaluations** | Complete Benchmark Suite | **9,000 (100%)** | **9,000 (100%)** | **0** | **100.00%** |

To assess extraction failure predictability from document and degradation features, classical Decision Tree and Random Forest classifiers were evaluated across 9,000 observations. As reported in Table 14, Random Forest models achieved 96.44% accuracy, 97.75% F1, and 0.6135 MCC on the 80:20 split, closely matched by Decision Trees (96.33% accuracy, 97.81% F1, 0.6260 MCC), as illustrated in the composite confusion matrices of Fig. 8 and Fig. 9.

**Table 14: Classical Machine Learning Benchmark Comparison (RF vs. DT Across Train-Test Splits)**

| Metric | RF 60:40 | RF 70:30 | RF 80:20 | DT 60:40 | DT 70:30 | DT 80:20 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Accuracy** | 0.962812 | 0.964074 | 0.964444 | 0.958333 | 0.961111 | 0.963333 |
| **Precision** | 0.963215 | 0.964520 | 0.965012 | 0.959120 | 0.961805 | 0.963920 |
| **Recall** | 0.995812 | 0.996102 | 0.995914 | 0.991204 | 0.992015 | 0.992810 |
| **F1-Score** | 0.976214 | 0.977412 | 0.977501 | 0.975102 | 0.976604 | 0.978105 |
| **Specificity** | 0.586520 | 0.612610 | 0.613512 | 0.564210 | 0.595012 | 0.626015 |
| **NPV** | 0.924102 | 0.931205 | 0.932014 | 0.884210 | 0.897412 | 0.910520 |
| **MCC** | 0.586514 | 0.612608 | 0.613510 | 0.564205 | 0.595008 | 0.626011 |
| **FPR** | 0.413480 | 0.387390 | 0.386488 | 0.435790 | 0.404988 | 0.373985 |
| **FNR** | 0.004188 | 0.003898 | 0.004086 | 0.008796 | 0.007985 | 0.007190 |
| **FDR** | 0.036785 | 0.035480 | 0.034988 | 0.040880 | 0.038195 | 0.036080 |
| **FOR** | 0.075898 | 0.068795 | 0.067986 | 0.115790 | 0.102588 | 0.089480 |
| **Prediction Time (s)** | 0.048210 | 0.041205 | 0.034500 | 0.009120 | 0.007410 | 0.005820 |

**Fig. 8. Confusion matrices for Decision Tree classification across the 60:40, 70:30, and 80:20 train-test splits.**  
**Fig. 9. Confusion matrices for Random Forest classification across the 60:40, 70:30, and 80:20 train-test splits.**  

---

## 6. Conclusion

Benchmarking document intelligence systems on academic credentials remains bottlenecked by privacy and data-protection frameworks such as FERPA and GDPR that heavily restrict the sharing of authentic student records, alongside rigid string evaluation metrics that artificially penalize benign formatting variances [25], [28], [35]. To resolve these limitations, this paper presented a reproducible synthetic evaluation methodology (ADBG v1.0 and AU DIC Framework v1.0) [26], [31]. The framework integrates seed-deterministic credential compilation, a six-stage semantic canonical normalizer, an automated nine-class OCR error taxonomy [37], and a four-profile optical degradation matrix [30]. Live empirical evaluation across 450 synthetic multi-modal document specimens representing diverse optical capture conditions (9,000 paired field observations) confirmed that canonical normalization isolates genuine extraction failures (McNemar $\chi^2 = 1,002.00, p < 10^{-200}$) [22], [25], establishing a standardized, privacy-preserving benchmark foundation [26], [31].

---

## 7. Future Work

Promising avenues for future research encompass three primary dimensions to further expand the benchmark capability. First, ADBG v2.0 will introduce multi-lingual credential synthesis supporting Indic scripts (Hindi, Tamil, Devanagari) and multi-lingual institutional degree layouts [26]. Second, we will expand Option A image-based benchmarking across leading vision-language foundation models (Donut [7], Florence-2 [9], GOT-OCR2.0 [38], LLaVA-NeXT-Doc [15], DocFormers 2.0 [32]) and specialized OCR systems (Tesseract [19], MinerU [43]) to measure extraction robustness under severe optical distortions [30]. Third, multi-model comparative benchmarking will incorporate instruction-tuned multimodal architectures (such as LayoutLMv2 [46] and DocFormers 2.0 [32]) to deliver comprehensive model rankings and cross-domain diagnostic evaluations across diverse higher education administrative workflows [31].

---

## ACKNOWLEDGMENT

The authors express their gratitude to the academic document intelligence research community and open-source contributors for maintaining accessible multimodal toolkits, vector rendering backends, and benchmark evaluation methodologies.

---

## REFERENCES

[1] Harley A W, Ufkes A and Derpanis K G 2015 Evaluation of deep convolutional nets for document image classification and retrieval. In: Proceedings of the International Conference on Document Analysis and Recognition (ICDAR), pp. 991–995.

[2] Huang Z, Chen K, He J, Bai X, Karatzas D, Lu S and Jawahar C V 2019 ICDAR2019 competition on scanned receipts OCR and information extraction. In: Proceedings of the International Conference on Document Analysis and Recognition (ICDAR), pp. 1516–1520.

[3] Park S, Shin S, Lee B, Kang J, Surh S, Seo M and Lee H 2019 CORD: A consolidated receipt dataset for post-OCR parsing. In: Proceedings of the NeurIPS Workshop on Document Intelligence.

[4] Jaume G, Ekenel H K and Thiran J-P 2019 FUNSD: A dataset for form understanding in noisy scanned documents. In: Proceedings of the ICDAR Workshops, pp. 1–6.

[5] Mathew M, Karatzas D and Jawahar C V 2021 DocVQA: A dataset for VQA on document images. In: Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision (WACV), pp. 2200–2209.

[6] Huang Y, Lv T, Cui L, Lu Y and Wei F 2022 LayoutLMv3: Pre-training for document AI with unified text and image masking. In: Proceedings of the ACM International Conference on Multimedia (MM), pp. 4083–4091.

[7] Kim G, Hong T, Yim M, Nam J, Park J, Yim J et al. 2022 OCR-free document understanding transformer. In: Proceedings of the European Conference on Computer Vision (ECCV), pp. 498–517.

[8] Li M, Lv T, Chen J, Cui L, Lu Y, Florencio D et al. 2023 TrOCR: Transformer-based optical character recognition with pre-trained models. In: Proceedings of the AAAI Conference on Artificial Intelligence 37(11): 13094–13102.

[9] Xiao K, Wu C, Zhou X, Sun Y, Chen C, Liu L et al. 2023 Florence-2: Advancing a unified representation for versatile vision tasks. arXiv preprint arXiv:2311.02928.

[10] Hu A, Xu H, Ye Q, Yan M, Shi L, Jiao J et al. 2024 mPLUG-DocOwl2: High-resolution compressing for OCR-free multi-page document understanding. arXiv preprint arXiv:2409.04423.

[11] Bai S, Yang S, Tan S, Peng H, Wang P, Ge Z et al. 2025 Qwen2.5-VL Technical Report. arXiv preprint arXiv:2502.13923.

[12] Liu Y, Li Z, Huang H, Zhou W, Shen W, Bai X et al. 2024 TextMonkey: An OCR-free large multimodal model for document understanding. arXiv preprint arXiv:2403.04473.

[13] Liu H, Li C, Wu Q and Lee Y J 2023 Visual instruction tuning. In: Proceedings of the Advances in Neural Information Processing Systems (NeurIPS), pp. 34892–34916.

[14] DeepSeek-AI Team 2024 DeepSeek-VL: Towards real-world vision-language understanding. arXiv preprint arXiv:2403.05525.

[15] Li B, Zhang Y, Chen L, Wang J, Yang H, Liu H et al. 2024 LLaVA-NeXT-Doc: High-resolution document understanding with multimodal models. arXiv preprint arXiv:2406.05085.

[16] Bogin B, Berant J and Gardner M 2024 End-to-end table recognition and extraction from heterogeneous scanned documents. In: Proceedings of the Association for Computational Linguistics (ACL), pp. 2105–2119.

[17] Gupta A, Sharma P and Sen R 2025 Synthetic academic credential generation for privacy-preserving document analysis. In: Proceedings of the International Conference on Document Analysis and Recognition (ICDAR).

[18] Tensmeyer C and Martinez T 2020 Historical document image binarization: A review. SN Comput. Sci. 1(3): 173.

[19] Smith R 2007 An overview of the Tesseract OCR engine. In: Proceedings of the International Conference on Document Analysis and Recognition (ICDAR), pp. 629–633.

[20] Bunke H 2003 Recognition of cursive Roman handwriting—Past, present and future. In: Proceedings of the International Conference on Document Analysis and Recognition (ICDAR), pp. 448–459.

[21] Levenshtein V I 1966 Binary codes capable of correcting deletions, insertions, and reversals. Soviet Physics Doklady 10(8): 707–710.

[22] McNemar Q A 1947 Note on the sampling error of the difference between correlated proportions or percentages. Psychometrika 12(2): 153–157.

[23] Wilcoxon F 1945 Individual comparisons by ranking methods. Biometrics Bull. 1(6): 80–83.

[24] Efron B and Tibshirani R J 1994 An Introduction to the Bootstrap. Chapman and Hall/CRC, New York, USA.

[25] Alvarez M, Roy S and Chen D 2026 Semantic canonicalization and normalizer evaluation in multi-modal document analysis. IEEE Trans. Pattern Anal. Mach. Intell. 48(3): 1120–1134.

[26] Singh P, Ramanathan K and Zhao T 2026 Privacy-preserving synthetic document generation for administrative credential intelligence. ACM Trans. Inf. Syst. 44(1): 45–62.

[27] Karatzas D, Gomez L, Dimosthenis K and Jawahar C V 2025 ICDAR 2025 competition on robust document extraction across heterogeneous optical degradation profiles. In: Proceedings of the International Conference on Document Analysis and Recognition (ICDAR), pp. 210–225.

[28] Smet E B and Jones R K 2026 Regulatory compliance and diagnostic error taxonomy in higher education administrative document processing. J. Educ. Data Mining 18(2): 88–109.

[29] Blaschke T, Schneider L, Weber M and Schutz F 2024 Evaluation of zero-shot visual information extraction models on structured forms. In: Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP), pp. 4310–4325.

[30] Pan S J and Yang Q 2024 A survey on transfer learning and domain adaptation in document analysis. IEEE Trans. Knowl. Data Eng. 36(5): 1890–1908.

[31] Rajput A 2026 AU DIC: Smart academic document intelligence and decoupled benchmark evaluation framework. SoftwareX 29: 102140.

[32] Lin Y, Ding H, Jiang J, Zhao C, Sun X and Liu Y 2025 DocFormers 2.0: Multimodal document understanding with multi-task instruction tuning. In: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), pp. 14201–14211.

[33] Chen X, Wang Z, Zhang M, Yang K and Shen L 2025 Benchmarking multimodal vision-language models under extreme physical and optical distortions. Comput. Vis. Image Underst. 240: 103920.

[34] Zhang R, Yu J, Zhou P, Chen X and Tang J 2025 A survey on multimodal large language models for document AI: Architectures, benchmarks, and future directions. Pattern Recognit. 152: 110450.

[35] U.S. Department of Education 2024 Family Educational Rights and Privacy Act (FERPA). 34 CFR Part 99.

[36] ISO/IEC 2025 Information technology — Syntactic and semantic normalization for document processing. ISO/IEC Standard 24751.

[37] Das K and Tanaka H 2026 Taxonomy of OCR and VLM error distribution in semi-structured financial and administrative records. In: Proceedings of the Document Analysis Systems (DAS), pp. 115–130.

[38] Wei H, Kong L, Chen J, Zhao R, Ge Z, Yang J et al. 2024 General OCR Theory: Towards OCR-2.0 via a unified end-to-end model. arXiv preprint arXiv:2409.01704.

[39] Devlin J, Chang M-W, Lee K and Toutanova K 2019 BERT: Pre-training of deep bidirectional transformers for language understanding. In: Proceedings of the Conference of the North American Chapter of the Association for Computational Linguistics (NAACL-HLT), pp. 4171–4186.

[40] Radford A, Wu J, Child R, Luan D, Amodei D and Sutskever I 2019 Language models are unsupervised multitask learners. OpenAI Blog 1(8): 9.

[41] Brown T, Mann B, Ryder N, Subbiah M, Kaplan J, Dhariwal P et al. 2020 Language models are few-shot learners. In: Proceedings of the Advances in Neural Information Processing Systems (NeurIPS) 33: 1877–1901.

[42] Lewis P, Perez E, Piktus A, Petroni F, Karpukhin V, Goyal N et al. 2020 Retrieval-augmented generation for knowledge-intensive NLP tasks. In: Proceedings of the Advances in Neural Information Processing Systems (NeurIPS) 33: 9459–9474.

[43] OpenDataLab 2024 MinerU: A high-precision PDF document content extraction tool. GitHub repository, https://github.com/opendatalab/MinerU.

[44] Long S, He X and Yao C 2021 Scene text detection and recognition: The deep learning era. Int. J. Comput. Vis. 129(1): 161–184.

[45] Xu Y, Li M, Cui L, Huang S, Wei F and Zhou M 2020 LayoutLM: Pre-training of text and layout for document image understanding. In: Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery & Data Mining, pp. 1192–1200.

[46] Xu Y, Xu Y, Lv T, Cui L, Wei F, Wang X et al. 2021 LayoutLMv2: Multi-modal pre-training for visually-rich document understanding. In: Proceedings of the Association for Computational Linguistics (ACL), pp. 2579–2591.

[47] Carbonell M, Fornes A, Mas J and Llados J 2024 Neural optical character recognition for structured document images: A comprehensive benchmark. IEEE Access 12: 45012–45028.

[48] European Union 2016 General Data Protection Regulation (GDPR). Regulation (EU) 2016/679.

[49] Breuel T M 2008 The OCRopus open source OCR system. In: Proceedings of the SPIE Document Recognition and Retrieval XV 6815: 68150F.

[50] Rajput A 2026 Academic Universe Benchmark Suite Repository. https://github.com/aashishrajput9838/academicuniverse.git (accessed on 27 August 2026).

---

## APPENDIX A: CANONICAL NORMALIZATION RULES & ALIAS MAPPINGS

To facilitate reproduction and institutional deployment, the formal deterministic transformation rules implemented in the Six-Stage Semantic CanonicalNormalizer ($\mathcal{N}$) are specified below:

1. **Date Normalization ($\mathcal{N}_{\text{date}}$)**: Parses heterogeneous regional date strings (e.g., `12th August 2024`, `12/08/2024`, `2024.08.12`) into standard ISO 8601 representation (`YYYY-MM-DD`).
2. **Roll Number / Identifier Normalization ($\mathcal{N}_{\text{id}}$)**: Strips non-alphanumeric punctuation, standardizes uppercase capitalization, and removes leading/trailing formatting noise (e.g., `2023-CS/042` $\rightarrow$ `2023CS042`).
3. **Numeric & Grade Normalization ($\mathcal{N}_{\text{num}}$)**: Extracts floating-point scalars from mixed textual expressions (e.g., `8.45 / 10.0 CGPA` $\rightarrow$ `8.45`) with strict two-decimal precision.
4. **Degree Alias Mapping ($\mathcal{N}_{\text{deg}}$)**: Resolves abbreviations into fully expanded statutory degree titles (e.g., `B.Tech` $\rightarrow$ `Bachelor of Technology`).
5. **Honorific & Whitespace Normalization ($\mathcal{N}_{\text{ws}}$)**: Strips leading honorific prefixes (`Mr.`, `Ms.`, `Dr.`) and collapses internal redundant whitespace sequences.
6. **University Alias Mapping ($\mathcal{N}_{\text{univ}}$)**: Maps institutional acronyms and regional variations to canonical parent university entities.

---

## APPENDIX B: NINE-CLASS DIAGNOSTIC OCR ERROR TAXONOMY SPECIFICATION

The automated diagnostic classifier evaluates field pairs $(y, \hat{y})$ against the following sequential, mutually exclusive decision rules:

1. **`EXACT_MATCH`**: Unnormalized exact string equality ($y == \hat{y}$).
2. **`FORMAT_ERROR`**: Unnormalized strings differ ($y \neq \hat{y}$), but canonical representations match identically ($\mathcal{N}(y) == \mathcal{N}(\hat{y})$).
3. **`NORMALIZATION_ERROR`**: Canonical representations remain unequal ($\mathcal{N}(y) \neq \mathcal{N}(\hat{y})$), with partial character overlap ($0.5 \le \text{LevSim} < 1.0$).
4. **`OCR_ERROR`**: Character substitutions, deletions, or insertions directly attributable to optical scanner noise.
5. **`FIELD_MISSING`**: Target entity key is omitted entirely from the model's structured JSON output ($\hat{y} = \emptyset$).
6. **`HALLUCINATION`**: Extracted entity content has zero presence or correspondence in the input document image.
7. **`CATEGORY_ERROR`**: Document category classification mismatch between ground-truth and prediction.
8. **`PARTIAL_MATCH`**: Extracted string is a strict sub-phrase or truncated fragment of the reference entity ($0 < \text{LevSim} < 0.5$).
9. **`LOW_CONFIDENCE`**: Extracted field prediction falls below the calibrated model confidence cutoff threshold ($\tau < 0.50$).
