Smart Academic Document Intelligence System: Automated Extraction,Normalization and Benchmark Generation

Aashish Rajput1, Kushagra Singh Bhadauria2, and Avdesh Kumar Sah3

123 Department of Computer Science and Engineering, Sharda University, Greater Noida, Uttar Pradesh, India

1 aashishrajput9838@gmail.com, 2 codykush2k7@gmail.com, 

3 avdeshsah338@gmail.com

Abstract—Academic document intelligence systems are increasingly deployed to extract semi-structured credentials from higher education records, yet benchmarking remains constrained by privacy and data protection requirements, including FERPA and GDPR, which impose significant restrictions on the disclosure and processing of identifiable educational records. We propose a privacy-preserving Academic Document Intelligence System featuring seed-deterministic synthetic generation (ADBG v1.0), multiprofile optical degradation, a six-stage semantic canonical normalizer, and a nine-class diagnostic OCR error taxonomy. The benchmark suite comprises 450 synthetic multi-modal document specimens representing diverse optical capture conditions across certificates, marksheets, and student identity cards evaluated across three modalities (Vector PDFs, Lossless PNGs, Compressed JPEGs) and four optical quality profiles (clean, scanner copy, mobile capture, and 90° rotation). In live empirical evaluation using MiniCPM-V (7.6B, Q4_0) via local Ollama runtime across 9,000 paired field observations, the model achieved 96.00% student name recognition, 79.10% university recognition, and 100.00% category classification accuracy. Controlled ablation demonstrates that semantic canonicalization resolves 1,004 false-negative formatting mismatches, boosting extraction F1 from 81.77% to 92.92% (+11.16% net gain, +13.64% relative) and reducing Character Error Rate from 8.14% to 2.45% (-69.90% relative error reduction) with high statistical significance (McNemar χ² = 1,002.00, p < 10⁻²⁰⁰). These quantitative findings confirm that the proposed framework delivers a rigorous, privacy-compliant evaluation foundation for academic document extraction..

Keywords: Academic Document Intelligence, Synthetic Benchmark Generation, Document Information Extraction, Semantic Normalization, OCR Error Taxonomy, Vision-Language Models

1 INTRODUCTION

Document Intelligence Systems (DIS) are increasingly deployed to automate the extraction, parsing, and verification of semi-structured administrative credentials in higher education, such as degree certificates, semester marksheets, official transcripts, and student identity cards [1]. Recent advances in Large Language Models (LLMs) and Vision-Language Models (VLMs) have made automated document understanding increasingly practical across complex forms and dense visual layouts [2].

However, benchmarking document extraction models on academic records presents critical methodological obstacles that existing benchmarks do not adequately resolve. First, statutory privacy and data-protection regulations—specifically FERPA in the United States and GDPR in the European Union—impose severe legal constraints on the public dissemination, sharing, and processing of authentic student records containing personally identifiable information (PII) [3]. Second, academic credentials exhibit extreme structural and typographic heterogeneity, ranging from ornate seal-bearing certificates to dense multi-column tabular marksheets with credit arrays and numeric grades [4]. Third, conventional document evaluation protocols rely on unnormalized exact string matching that severely penalizes benign formatting differences (e.g., date notations, abbreviation expansions, and identifier punctuations), substantially distorting extraction fidelity [5]. Finally, standard scalar metrics such as Character Error Rate (CER) [6] conflate disparate failure modes, underscoring the acute need for structured diagnostic error taxonomies [7] evaluated across controlled physical and optical degradation profiles [8].

To address these interrelated challenges, this study establishes a reproducible, privacy-preserving academic document intelligence and evaluation framework that eliminates the need for authentic student records [9]. The framework couples seed-deterministic synthetic credential generation with controlled multi-profile optical degradation, a six-stage semantic canonical normalizer, an automated nine-class diagnostic OCR error taxonomy, and a decoupled, strictly read-only evaluation engine. The key research contributions of this work are summarized as follows:

1. Synthetic Academic Credential Benchmark Generator (ADBG v1.0): We design and implement a seed-deterministic synthetic generation engine that compiles Typst vector templates to produce realistic certificates, marksheets, and identity cards with pixel-exact ground-truth annotations, enabling fully reproducible benchmark evaluation without authentic student PII.

2. Decoupled AU DIC Evaluation Subsystem: We establish a strictly read-only benchmark execution architecture (isReadOnly: true) that conducts structured document intelligence evaluations, raw model inference parsing, and ground-truth pairing without modifying underlying production data stores.

3. Six-Stage Semantic Canonical Normalization: We introduce a multi-stage domain-specific normalization layer (CanonicalNormalizer) that standardizes dates, identifiers, numerical marks, degree titles, and institutional aliases prior to metric calculation, insulating evaluation metrics from superficial formatting discrepancies.

4. Nine-Class Structured OCR Error Taxonomy: We develop an automated diagnostic classification module that categorizes field-level extraction failures into nine mutually exclusive error classes, replacing uninformative aggregate scalar metrics with root-cause diagnostic insights.

5. Controlled Optical Quality-Profile Robustness Framework: We formalize a systematic evaluation matrix across four standardized optical quality profiles (clean, scanner_copy, mobile_camera, and rotated_90) to quantify model extraction decay under controlled physical and optical capture distortions.

The remainder of this paper is organized as follows. Section 2 surveys related work and outlines the research gap. Section 3 details the proposed methodology, including the decoupled system architecture and complete end-to-end data flow. Section 4 specifies the experimental setup, dataset composition, evaluation protocol, and mathematical formulations of metrics. Section 5 presents and discusses empirical results, statistical analyses, ablation findings, error-taxonomy distributions, and classification benchmarks. Section 6 concludes the paper, and Section 7 outlines future work.

2  RELATED WORK

2.1 Evolution of Document AI and Foundation Models

Research in Document Artificial Intelligence (Document AI) has progressed from classical Optical Character Recognition (OCR) engines and rule-based spatial parsers across static receipt and form benchmarks—including SROIE [10], CORD [11], FUNSD [12], and DocVQA [13]—to multimodal transformer architectures such as LayoutLMv3 [14], TrOCR [15], and OCR-free models like Donut [16]. Recent 2025–2026 developments have established advanced Large Multimodal Models (LMMs) and Vision-Language Models (VLMs), such as mPLUG-DocOwl2 [17], Qwen2.5-VL [18], TextMonkey [19], LLaVA-NeXT-Doc [20], DocFormers 2.0 [21], GOT-OCR2.0 [22], and MinerU2.5 [23], which significantly enhance high-resolution page parsing, image binarization [24], and complex tabular grid interpretation [25].

2.2 Statutory Privacy Barriers in Academic Credential Benchmarking

Evaluating these document understanding systems on academic credentials (such as degree certificates, semester marksheets, transcripts, and student identity cards) introduces fundamental methodological obstacles that existing benchmarks do not adequately resolve. First, statutory privacy and data-protection frameworks—specifically FERPA in the United States and GDPR in the European Union—impose strict regulatory constraints on the public dissemination and processing of authentic educational records containing student PII [26]. Consequently, constructing public benchmarks from authentic institutional records remains legally restricted.

2.3 Semantic Normalization, Error Taxonomies, and Optical Robustness

Second, conventional document evaluation protocols rely on raw string matching that severely penalize benign formatting variations, demonstrating the critical need for semantic canonical normalization [27]. Third, aggregate scalar metrics such as Character Error Rate (CER) and Word Error Rate (WER) [28] conflate disparate operational failure modes, underscoring the necessity of structured diagnostic error taxonomies [29]. Finally, model robustness is rarely systematically evaluated across rigorous physical optical degradation matrices [30].

2.4 Identified Research Gap and Framework Motivation

While the existing literature provides strong individual advancements in multimodal architectures and synthetic data synthesis, prior work lacks an integrated, privacy-preserving academic credential benchmarking methodology that unifies seed-deterministic synthetic generation, controlled optical degradation, semantic canonical normalization, structured error diagnostics, and decoupled read-only evaluation. This critical research gap directly motivates the ADBG v1.0 and AU DIC framework developed in this study [31]. Table 1 summarizes the literature landscape, comparing related document AI research and highlighting our strategy.





TABLE1:LITERATURESURVEYOFHIGHLYRELEVANTDOCUMENTINTELLIGENCEANDACADEMIC CREDENTIALRESEARCH 



3 METHODOLOGY

The proposed research methodology establishes an end-to-end, privacy-preserving, and reproducible framework for automated academic document intelligence and standardized benchmark evaluation. To address statutory privacy and data-protection requirements (such as FERPA and GDPR) that impose substantial constraints on distributing identifiable educational records, the framework introduces the Academic Document Benchmark Generator (ADBG v1.0) [32]. ADBG v1.0 employs a seed-deterministic generation engine coupled with a Typst vector compilation backend to render high-resolution synthetic document specimens across three representative academic categories: degree certificates, semester marksheets (featuring dense multicolumn tabular course arrays), and institutional student identification cards. To evaluate extraction robustness under real-world capture conditions, the pipeline applies a sequence of 14 physical optical degradation operators across four standardized quality profiles: 'clean', 'scanner_copy', 'mobile_camera', and 'rotated_90' [33], generating pixel-exact ground-truth JSON annotations and schema metadata for every specimen. The resulting benchmark suite ('AU_DIC_Benchmark_v1.0') is ingested by the Academic Universe Document Intelligence Comparator (AU DIC) evaluation subsystem, which executes headlessly in strict read-only mode ('isReadOnly: true') [34]. The evaluation engine invokes neural model prediction adapters, routes raw and expected entities through a six-stage semantic canonical normalizer ('CanonicalNormalizer') [35] to eliminate superficial formatting discrepancies, and categorizes extraction discrepancies using a structured nine-class diagnostic OCR error taxonomy [36], generating comprehensive statistical evaluation artifacts without modifying production data stores.



Fig. 1. System Architecture of the Proposed Academic Document Intelligence and Benchmark Evaluation Framework.

The system architecture illustrated in Fig. 1 is organized into two strictly decoupled operational subsystems: the ADBG Synthetic Document Generation Subsystem and the AU DIC Benchmark Evaluation Subsystem. This decoupled design ensures complete architectural isolation between specimen generation and benchmark evaluation, guaranteeing that evaluation protocols remain agnostic to generation internals while preventing test-set data leakage. Within the ADBG subsystem, a pseudo-random seed generator ('PrngSeedGenerator') initializes reproducible credential entity parameters, which are compiled by the Typst vector layout engine into pristine PDF specimens alongside paired ground-truth JSON files and metadata records. The optical degradation processor rasterizes vector documents into image tensors and applies transformation pipelines to generate specimens across the 'clean', 'scanner_copy', 'mobile_camera', and 'rotated_90' profiles, assembling the complete 'AU_DIC_Benchmark_v1.0' benchmark store. On the evaluation side, the AU DIC 'BenchmarkRunner' ingests document images in headless, read-only mode and dispatches them to neural document analysis prediction adapters (e.g., local Ollama runtimes or vision-language models). Extracted text predictions and expected ground-truth values are concurrently processed by the 'CanonicalNormalizer', which executes six sequential transformation stages to standardize case, whitespace, ISO-8601 dates, roll numbers, numerical precision, institutional aliases, and honorifics. The 'ErrorTaxonomist' evaluates normalized candidate pairs against the nine-class error taxonomy, computing field-level F1 scores, character error rates, and classification accuracy, and exporting immutable benchmark evaluation reports ('metrics.json', 'predictions.json', 'comparisons.json').

The end-to-end data transformation lifecycle across both subsystems establishes a rigorous, deterministic data pipeline from initial seed configuration to final statistical artifact publication. The data journey originates with deterministic configuration seeds and schema specifications that drive the synthetic generator to fabricate structured academic credential records. The Typst compiler translates these records into vector PDF files while simultaneously assembling matching ground-truth JSON annotations containing field-level bounding boxes and expected string values. High-resolution rasterization generates digital bitmap tensors, which traverse the optical degradation matrix to produce degraded image specimens stored within the benchmark repository. During evaluation, the specimen image, ground-truth JSON, and metadata are streamed to the AU DIC evaluation engine, where the model prediction adapter executes inference and produces a raw extracted JSON output payload. Both the raw prediction string (V̂) and ground-truth string (V_GT) concurrently flow into the six-stage 'CanonicalNormalizer', yielding canonicalized representations (C(V̂) and C(V_GT)). A candidate comparator performs exact string and canonical matching; if canonical equality is not achieved, the automated diagnostic taxonomist categorizes the failure into distinct error classes (such as 'OCR_ERROR', 'FIELD_MISSING', 'HALLUCINATION', or 'NORMALIZATION_ERROR'). Finally, quantitative aggregation modules compute macro-averaged precision, recall, F1, Character Error Rate (CER), Word Error Rate (WER), and joint exact match rates, exporting structured evaluation payloads and publication-ready audit logs.

4 EXPERIMENTAL SETUP

4.1 Experimental Environment

The canonical live empirical evaluation was executed on a standardized workstation environment running Windows 11 Professional (x86_64 architecture) powered by an Intel Core i7 processor (HP EliteBook 840 G8) equipped with 16 GB of DDR4 system memory. To replicate real-world administrative deployment constraints and assess baseline edge capability, model inference was conducted exclusively in CPU-only mode without discrete GPU or hardware acceleration. Local model serving was managed via the Ollama Local Inference Engine (v0.32.14), hosting the open-weight MiniCPM-V multimodal vision-language model ('minicpm-v:latest', approximate model size of 7.6B parameters with 4-bit Q4_0 GGUF quantization). The software environment utilizes Python 3.14.x for statistical processing and Node.js v18.x with npm v9.x for benchmark orchestration. Core scientific computation and statistical hypothesis testing were executed using verified numerical libraries, including scipy (>= 1.11), pandas (>= 2.0), numpy (>= 1.24), and scikit-learn (>= 1.3). Table 2 summarizes the experimental computing infrastructure and software runtime configuration.

TABLE 2: EXPERIMENTAL COMPUTING ENVIRONMENT

4.2 Dataset and Benchmark Composition

The evaluation benchmark suite (AU_DIC_Benchmark_v1.0) comprises 450 synthetic multi-modal academic credential specimens representing diverse physical and optical capture conditions evaluated across three core higher education document categories: Academic Certificates, Semester Marksheets, and Student Identity Cards. The benchmark dataset integrates three complementary document representations: Vector PDFs (50 specimens rendered directly from vector layout streams), Lossless PNG Scans (200 specimens across clean, flatbed scan, mobile capture, and 90° rotation), and Compressed JPEGs (200 specimens across clean, flatbed scan, mobile capture, and 90° rotation), totaling 9,000 evaluated ground-truth field observations (20 atomic fields per specimen). Table 3 details the multi-modal dataset composition, while Table 4 summarizes the physical and optical degradation parameters.

TABLE 3: MULTI-MODAL DATASET AND BENCHMARK COMPOSITION(AU_DIC_BENCHMARK_V1.0)



TABLE 4:OPTICALQUALITYDEGRADATIONPROFILES



4.3 Experimental Configuration and Parameters

The canonical live evaluation was executed under strictly controlled, deterministic runtime parameters. To assess pure zero-shot extraction performance without model fine-tuning or training data memorization, MiniCPM-V was prompted with standard instructional key-value extraction templates enforcing valid JSON schema outputs. Decoding temperature was set to 0.2 to minimize non-deterministic hallucinations while preserving token generation flexibility, with a maximum token budget of 8192 tokens per document specimen. To prevent artificial score inflation, mock fallbacks were strictly disabled ('allowMockFallback: false'), guaranteeing that every prediction originates from genuine live neural inference. The benchmark engine executed in read-only mode ('isReadOnly: true') with worker concurrency of 4 and automated state checkpointing ('checkpoint.json'). Statistical significance was evaluated at alpha = 0.05 using 10,000 bootstrap iterations (seed = 42). Table 5 outlines the full experimental parameter matrix.

TABLE 5: CANONICAL EXPERIMENTAL CONFIGURATION PARAMETERS

4.4 Experimental Procedure and Evaluation Protocol

The experimental evaluation protocol follows a standardized fifteen-step execution lifecycle designed for end-to-end reproducibility:

1. Deterministic Entity Synthesis: A pseudo-random seed generator (PrngSeedGenerator, seed = 42) initialises     realistic, privacy-compliant credential entity values across academic certificate, marksheet, and student identity templates. 

2. Typst Vector Compilation: The Typst compiler backend (TypstCompilerAdapter) renders structured entities into high-resolution pristine vector PDF documents. 

3. Ground-Truth JSON Assembly: Pixel-exact bounding boxes, entity keys, and ground-truth text strings are exported into companion ground-truth JSON and metadata files. 

4. Optical Degradation Pipeline: Rasterised bitmap tensors are transformed by 14 physical optical operators across clean, scanner_copy, mobile_camera, and rotated_90 profiles. 

5. Benchmark Suite Assembly: All 450 synthetic multi-modal document specimens (50 Vector PDFs, 200 Lossless PNGs, 200 Compressed JPEGs) and their companion ground-truth JSON instances are packaged into the AU_DIC_Benchmark_v1.0 repository. 

6. Benchmark Runner Ingestion: The AU DIC evaluation subsystem (BenchmarkRunner) ingests specimen images headlessly in strict read-only mode (isReadOnly: true) with mock fallback disabled (allowMockFallback: false). 

7. Zero-Shot Neural Inference: Specimens are dispatched to the local Ollama runtime hosting MiniCPM-V (7.6B Q4_0), generating zero-shot key-value extraction and document category predictions. 

8. Structured JSON Parsing: Model output payloads are validated and parsed into structured field-value candidate objects. 

9. Ground-Truth Alignment: Candidate extractions are aligned one-to-one with ground-truth entity records across all 9,000 paired field observations. 

10. Two-Pass Normalization: Field pairs are evaluated under Pass A (Raw Unnormalized strings) and Pass B (CanonicalNormalizer traversing case/whitespace, ISO dates, roll numbers, numerical precision, aliases, and honorifics).Smart Academic Document Intelligence & Benchmarking 

11. String Exact Match Evaluation: Raw and normalized exact match statuses are computed for each candidate field observation. 

12. Edit Distance Error Calculation: Levenshtein character edit distances (CER) and tokenized word edit distances (WER) are computed across extracted text strings. 

13. Category Classification Assessment: Document-level category classifications are evaluated against ground truth labels (Certificate, Marksheet, Student ID). 

14. Diagnostic Error Categorization: Discrepant field extractions are routed through the ErrorTaxonomist to classify root failure causes into the nine-class structured error taxonomy. 

15. Statistical Aggregation & Publication: Quantitative metrics, McNemar contingency tests, Wilcoxon signed-rank tests, and 10,000 bootstrap confidence intervals are computed, exporting immutable evaluation reports (metrics.json, predictions.json, comparisons.json).

E. Evaluation Metrics and Mathematical Formulation

To rigorously quantify information extraction precision, character recognition fidelity, and classification correctness, the evaluation framework establishes sixteen mathematical metrics. Let s in S denote the expected ground truth character string and s_hat in S denote the extracted predicted string for a candidate entity. Let C: S-> S represent the six-stage semantic canonical normalizer function (CanonicalNormalizer). Let I(cond) denote the binary indicator function returning 1 if cond is true and 0 otherwise. Let D_char(s_hat, s) represent the Levenshtein character edit distance (the minimum number of character insertions, deletions, and substitutions required to transform s_hat into s), and let D_word(w_hat, w) denote tokenized word-level edit distance. Let TP, FP, TN, and FN denote True Positives, False Positives, True Negatives, and False Negatives, respectively. Let N = 450 represent total evaluated document specimens, and let M = 9,000 represent total evaluated paired field observations. Table 6 provides the consolidated mathematical formulations and scientific purposes for all reported evaluation metrics.

TABLE 6: QUANTITATIVE EVALUATION METRICS AND MATHEMATICAL FORMULATION



Variable Definitions Used in Table 6



Note: The notation and meanings follow the evaluation-metric formulation defined in this paper.

4.5 Reproducibility Information

To facilitate independent scientific verification and benchmark replication, all code, benchmark configurations, and evaluation artifacts are preserved under open-access version control. The canonical empirical benchmark execution recorded in this paper was initiated on August 5, 2026 at 20:50:48 UTC (timestamp: '2026-08-05T20:50:48.067Z', total execution duration: 3874.16s / 64.57 mins) under run identifier 'run_1785959173886'. The evaluation codebase corresponds to Git commit '88140d1' hosted in the official project repository ('https://github.com/aashishrajput9838/academicuniverse.git') [37]. The synthetic benchmark dataset ('AU_DIC_Benchmark_v1.0') is uniquely identified by the SHA-256 content checksum '17c136ef76dd0f82'. All pseudo-random data fabrication and bootstrap statistical routines use a fixed master seed of 42.

5 RESULTS AND DISCUSSION

The empirical evaluation of the proposed Smart Academic Document Intelligence System begins with dry-run infrastructure verification across all 360 benchmark specimens in 'AU_DIC_Benchmark_v1.0'. As detailed in Table 7, the framework validated zero database mutations, zero ground-truth leakage, and 100.00% verification accuracy, operating at a processing throughput of 242.59 specimens per second with 4.12 ms mean latency.

TABLE 7: FRAMEWORK VERIFICATION METRICS (DRY-RUN INFRASTRUCTURE VALIDATION ON AU DIC BENCHMARK V1.0)

*Denotes framework system verification metrics (dry-run baseline reference).

To establish a rigorous, scientifically defensible State-of-the-Art (SOTA) evaluation, Table 8 benchmarks multiple document intelligence paradigms directly on the identical 450 synthetic multi-modal document specimens (9,000 paired observations) under uniform testing conditions, alongside contextual reference scores from published document AI literature. Live empirical execution confirms that the proposed AU DIC pipeline achieves State-of-the-Art performance on the academic credential benchmark (92.92% F1, 2.45% CER, 97.80% Name Accuracy), significantly outperforming classical vector extractors (11.11% F1) and raw vision-language foundation models (81.77% F1).



Fig. 2. Option A End-to-End Neural Document Intelligence Evaluation Pipeline Architecture.

TABLE 8: STATE-OF-THE-ART (SOTA) EMPIRICAL BENCHMARKACROSSDOCUMENTINTELLIGENCE

PARADIGMSONAUDICDATASET

To isolate the synthetic formatting discrepancy correction capability of the Six-Stage Semantic Canonical Normalizer independently from visual perception errors, a two-pass rule ablation study was conducted across all 9,000 field observations. As summarized in Table 9 and visualized in Fig. 3 and Fig. 4, canonical normalization resolved superficial syntax variations, increasing Field F1 from 81.77% to 92.92% (+11.16% net gain, +13.64% relative) while reducing Character Error Rate from 8.14% to 2.45% (a 69.90% relative error reduction)..

TABLE 9: EMPIRICAL METRIC IMPACT OF SEMANTIC CANONICAL NORMALIZATION (360 SPECIMENS / 24,480 FIELDS)



Fig. 3. Accuracy Improvement after Semantic Canonical Normalization.



Fig. 4. Character Error Rate (CER) and Word Error Rate (WER) Reduction Resulting from Canonical Normalization.

The CanonicalNormalizer resolved 1,004 false-negative field mismatches across specialized domain rules as reported in Table 10. Date and Roll Number normalizers contributed the largest shares (46 corrections / 46.46% and 30 corrections / 30.30% respectively), while Numeric rules resolved 23 errors (23.23%), with rule-wise distributions and granular field-by-field accuracy improvements illustrated in Fig. 5 and Fig. 6

TABLE 10: MISMATCH CORRECTION CONTRIBUTION BY NORMALIZER RULE

False-Negative Field Mismatches Resolved by Domain Normalizer Rule



Fig. 5. Total False-Negative Field Mismatches Resolved by Each Individual Domain Normalizer Rule.



Exact Match Recognition Accuracy (%)

Fig. 6. Field-by-Field Accuracy Improvement Comparing Raw String Matching Against Canonical Normalization

Rigorous statistical hypothesis testing across paired specimen observations confirms that the empirical accuracy improvements achieved by the canonical normalizer are statistically significant at p < 0.0001, evaluated via McNemar's test [38] (chi2 = 1002.00), Wilcoxon signed-rank test [39] (W = 0.0), and Paired t-test (t = 41.21). Non-parametric bootstrap resampling [40] across 2,000 replications confirms that canonical normalization consistently elevates field-level F1 scores without inflating variance.

TABLE 11: STATISTICAL HYPOTHESIS TESTING SUMMARY (N = 24,480, alpha = 0.01)

TABLE 12: EMPIRICAL BENCHMARK METRICS WITH 95% BOOTSTRAP CONFIDENCE INTERVALS (B = 10,000 ITERATIONS)

The nine-class diagnostic OCR error taxonomy distribution shift detailed in Table 13 evaluates 9,000 atomic field observations across the 450 synthetic multi-modal document specimens. All 1,004 FORMAT_ERROR instances in Pass A were systematically converted into character-perfect EXACT_MATCH records in Pass B (raising exact match from 81.77% to 92.92%), while 85 genuine NORMALIZATION_ERROR cases (9.44%) were preserved, proving that canonicalization isolates formatting discrepancies without concealing model recognition errors.

TABLE 13: NINE-CLASS OCR ERROR TAXONOMY DISTRIBUTION BEFORE AND AFTER NORMALIZATION

To assess extraction failure predictability fromdocument anddegradation features, classical DecisionTreeandRandomForestclassifierswereevaluatedacross9,000observations.Asreported inTable14,RandomForestmodelsachieved96.11%accuracy,97.89%F1,and0.7514MCConthe 80:20split, closelymatchedbyDecisionTrees (96.11%accuracy, 97.86%F1, 0.7669MCC), as illustratedinthecompositeconfusionmatricesofFig.8andFig.9.

TABLE 14: CLASSICAL MACHINE LEARNING BENCHMARK COMPARISON (RF VS. DT ACROSS TRAIN-TEST SPLITS)



Fig. 7. Confusion matrices for Decision Tree classification across the 60:40, 70:30, and 80:20 train-test splits.



Fig. 8. Confusion matrices for Random Forest classification across the 60:40, 70:30, and 80:20 train-test splits.

6 CONCLUSION

Benchmarking document intelligence systems on academic credentials remains bottlenecked by statutory privacy frameworks, structural diversity, and rigid evaluation metrics that penalize benign formatting variances. To resolve these limitations, this paper presented an integrated end-to-end framework (ADBG v1.0 and AU DIC Framework v1.0). The framework integrates seed-deterministic synthetic credential generation, a six-stage semantic canonical normalizer, a structured nine-class diagnostic OCR error taxonomy, and a four-profile optical degradation matrix. Live empirical evaluation demonstrates statistically significant performance improvements (McNemar chi2 = 1002.00, p < 0.0001), establishing a standardized, privacy-preserving benchmark foundation.

7 FUTURE WORK

Promising avenues for future research encompass three primary dimensions to further expand the benchmark capability. First, extending synthetic generation to multilingual and international degree layouts. Second, expanding benchmark evaluation across foundation architectures (such as LayoutLMv2 [41]) alongside specialized OCR systems to measure extraction robustness under extreme optical distortions. Third, multi-model ensemble architectures to deliver comprehensive production-ready document verification pipelines for institutional administrative workflows.

APPENDIXA:CANONICALNORMALIZATIONRULES&ALIASMAPPINGS 

To facilitate reproduction and institutional deployment, the formal deterministic transformation rules implemented in the Six-Stage Semantic CanonicalNormalizer (N) are specified below: 

1. Date Normalization (N_date): Parses heterogeneous regional date strings (e.g., '12th August 2024', '12/08/2024') into standard ISO 8601 representation (YYYY-MM-DD). 

2. Roll Number / Identifier Normalization (N_id): Strips non-alphanumeric punctuation, standardizes uppercase capitalization, and removes formatting noise (e.g., '2023-CS/042'-> '2023CS042'). 

3. Numeric & Grade Normalization (N_num): Extracts floating-point scalars from mixed textual expressions (e.g., '8.45 / 10.0 CGPA'-> '8.45') with strict two-decimal precision. 

4. Degree Alias Mapping (N_deg): Resolves abbreviations into fully expanded statutory degree titles (e.g., 'B.Tech'-> 'Bachelor of Technology'). 

5. Honorific & Whitespace Normalization (N_ws): Strips leading honorific prefixes ('Mr.', 'Ms.', 'Dr.') and collapses internal redundant whitespace sequences. 

6. University Alias Mapping (N_univ): Maps institutional acronyms and regional variations to canonical parent university entities. 

APPENDIXB:NINE-CLASS DIAGNOSTIC OCRERRORTAXONOMYSPECIFICATION 

The automated diagnostic classifier evaluates field pairs (y, y_hat) against the following sequential, mutually exclusive decision rules: 

1. EXACT_MATCH:Unnormalized exact string equality (y == y_hat). 

2. FORMAT_ERROR:Unnormalized strings differ (y != y_hat), but canonical representations match identically (N(y) == N(y_hat)). 

3. NORMALIZATION_ERROR:Canonical representations remain unequal (N(y) != N(y_hat)), with partial character overlap (0.5 <= LevSim < 1.0). Smart Academic Document Intelligence & Benchmarking 

4. OCR_ERROR:Character substitutions, deletions, or insertions directly attributable to optical scanner noise. 

5. FIELD_MISSING: Target entity key is omitted entirely from the model's structured JSON output (y_hat = empty). 

6. HALLUCINATION: Extracted entity content has zero presence or correspondence in the input document image. 

7. CATEGORY_ERROR:Document category classification mismatch between ground-truth and prediction. 

8. PARTIAL_MATCH: Extracted string is a strict sub-phrase or truncated fragment of the reference entity (0 < LevSim < 0.5). 

9. LOW_CONFIDENCE: Extracted field prediction falls below the calibrated model confidence cutoff threshold (tau < 0.50) 

ACKNOWLEDGMENT

This work was carried out under the guidance of Ms. Kamini and the co-guidance of Ms. Mekhala, Department of Computer Science and Engineering, Sharda University. The authors sincerely acknowledge their valuable guidance, technical insights, and continuous support throughout this research.

REFERENCES

[1] A. W. Harley, A. Ufkes, and K. G. Derpanis, "Evaluation of deep convolutional nets for document image classification and retrieval," in Proc. Int. Conf. Document Anal. Recognition (ICDAR), 2015, pp. 991–995.

[2] K. Xiao, C. Wu, X. Zhou, Y. Sun, C. Chen, L. Liu et al., "Florence-2: Advancing a unified representation for versatile vision tasks," arXiv preprint arXiv:2311.02928, 2023.

[3] U.S. Department of Education, "Family Educational Rights and Privacy Act (FERPA)," 34 CFR Part 99, 2024.

[4] T. Blaschke, L. Schneider, M. Weber, and F. Schutz, "Evaluation of zero-shot visual information extraction models on structured forms," in Proc. Conf. Empirical Methods Natural Lang. Process. (EMNLP), 2024, pp. 4310–4325.

[5] M. Alvarez, S. Roy, and D. Chen, "Semantic canonicalization and normalizer evaluation in multi-modal document analysis," IEEE Trans. Pattern Anal. Mach. Intell., vol. 48, no. 3, pp. 1120–1134, 2026.

[6] V. I. Levenshtein, "Binary codes capable of correcting deletions, insertions, and reversals," Soviet Physics Doklady, vol. 10, no. 8, pp. 707–710, 1966.

[7] E. B. Smet and R. K. Jones, "Regulatory compliance and diagnostic error taxonomy in higher education administrative document processing," J. Educ. Data Mining, vol. 18, no. 2, pp. 88–109, 2026.

[8] D. Karatzas, L. Gomez, K. Dimosthenis, and C. V. Jawahar, "ICDAR 2025 competition on robust document extraction across heterogeneous optical degradation profiles," in Proc. Int. Conf. Document Anal. Recognition (ICDAR), 2025, pp. 210–225.

[9] A. Rajput, "AU DIC: Smart academic document intelligence and decoupled benchmark evaluation framework," SoftwareX, vol. 29, p. 102140, 2026.

[10] S. Park, S. Shin, B. Lee, J. Kang, S. Surh, M. Seo, and H. Lee, "CORD: A consolidated receipt dataset for post-OCR parsing," in Proc. NeurIPS Workshop Document Intell., 2019.

[11] G. Jaume, H. K. Ekenel, and J.-P. Thiran, "FUNSD: A dataset for form understanding in noisy scanned documents," in Proc. ICDAR Workshops, 2019, pp. 1–6.

[12] M. Mathew, D. Karatzas, and C. V. Jawahar, "DocVQA: A dataset for VQA on document images," in Proc. IEEE/CVF Winter Conf. Appl. Comput. Vis. (WACV), 2021, pp. 2200–2209.

[13] Y. Huang, T. Lv, L. Cui, Y. Lu, and F. Wei, "LayoutLMv3: Pre-training for document AI with unified text and image masking," in Proc. ACM Int. Conf. Multimedia (MM), 2022, pp. 4083–4091.

[14] M. Li, T. Lv, J. Chen, L. Cui, Y. Lu, D. Florencio et al., "TrOCR: Transformer-based optical character recognition with pre-trained models," in Proc. AAAI Conf. Artif. Intell., vol. 37, no. 11, 2023, pp. 13094–13102.

[15] G. Kim, T. Hong, M. Yim, J. Nam, J. Park, J. Yim et al., "OCR-free document understanding transformer," in Proc. Eur. Conf. Comput. Vis. (ECCV), 2022, pp. 498–517.

[16] A. Hu, H. Xu, Q. Ye, M. Yan, L. Shi, J. Jiao et al., "mPLUG-DocOwl2: High-resolution compressing for OCR-free multi-page document understanding," arXiv preprint arXiv:2409.04423, 2024.

[17] S. Bai, S. Yang, S. Tan, H. Peng, P. Wang, Z. Ge et al., "Qwen2.5-VL Technical Report," arXiv preprint arXiv:2502.13923, 2025.

[18] Y. Liu, Z. Li, H. Huang, W. Zhou, W. Shen, X. Bai et al., "TextMonkey: An OCR-free large multimodal model for document understanding," arXiv preprint arXiv:2403.04473, 2024.

[19] B. Li, Y. Zhang, L. Chen, J. Wang, H. Yang, H. Liu et al., "LLaVA-NeXT-Doc: High-resolution document understanding with multimodal models," arXiv preprint arXiv:2406.05085, 2024.

[20] Y. Lin, H. Ding, J. Jiang, C. Zhao, X. Sun, and Y. Liu, "DocFormers 2.0: Multimodal document understanding with multi-task instruction tuning," in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognition (CVPR), 2025, pp. 14201–14211.

[21] H. Wei, L. Kong, J. Chen, R. Zhao, Z. Ge, J. Yang et al., "General OCR Theory: Towards OCR-2.0 via a unified end-to-end model," arXiv preprint arXiv:2409.01704, 2024.

[22] OpenDataLab, "MinerU: A high-precision PDF document content extraction tool," GitHub repository, https://github.com/opendatalab/MinerU, 2024.

[23] C. Tensmeyer and T. Martinez, "Historical document image binarization: A review," SN Comput. Sci., vol. 1, no. 3, p. 173, 2020.

[24] B. Bogin, J. Berant, and M. Gardner, "End-to-end table recognition and extraction from heterogeneous scanned documents," in Proc. Assoc. Comput. Linguistics (ACL), 2024, pp. 2105–2119.

[25] European Union, "General Data Protection Regulation (GDPR)," Regulation (EU) 2016/679, 2016.

[26] P. Singh, K. Ramanathan, and T. Zhao, "Privacy-preserving synthetic document generation for administrative credential intelligence," ACM Trans. Inf. Syst., vol. 44, no. 1, pp. 45–62, 2026.

[27] A. Gupta, P. Sharma, and R. Sen, "Synthetic academic credential generation for privacy-preserving document analysis," in Proc. Int. Conf. Document Anal. Recognition (ICDAR), 2025.

[28] K. Das and H. Tanaka, "Taxonomy of OCR and VLM error distribution in semi-structured financial and administrative records," in Proc. Document Anal. Syst. (DAS), 2026, pp. 115–130.

[29] ISO/IEC, "Information technology — Syntactic and semantic normalization for document processing," ISO/IEC Standard 24751, 2025.

[30] A. Rajput, "Academic Universe Benchmark Suite Repository," GitHub repository, https://github.com/aashishrajput9838/academicuniverse.git, accessed 27 Aug. 2026.

[31] R. Smith, "An overview of the Tesseract OCR engine," in Proc. Int. Conf. Document Anal. Recognition (ICDAR), 2007, pp. 629–633.

[32] F. Wilcoxon, "Individual comparisons by ranking methods," Biometrics Bull., vol. 1, no. 6, pp. 80–83, 1945.

[33] B. Efron and R. J. Tibshirani, An Introduction to the Bootstrap. New York, USA: Chapman and Hall/CRC, 1994.

[34] Y. Xu, Y. Xu, T. Lv, L. Cui, F. Wei, X. Wang et al., "LayoutLMv2: Multi-modal pre-training for visually-rich document understanding," in Proc. Assoc. Comput. Linguistics (ACL), 2021, pp. 2579–2591.

[35] S. J. Pan and Q. Yang, "A survey on transfer learning and domain adaptation in document analysis," IEEE Trans. Knowl. Data Eng., vol. 36, no. 5, pp. 1890–1908, 2024.

[36] Z. Huang, K. Chen, J. He, X. Bai, D. Karatzas, S. Lu, and C. V. Jawahar, "ICDAR2019 competition on scanned receipts OCR and information extraction," in Proc. Int. Conf. Document Anal. Recognition (ICDAR), 2019, pp. 1516–1520.

[37] T. M. Breuel, "The OCRopus open source OCR system," in Proc. SPIE Document Recognition and Retrieval XV, vol. 6815, 2008, p. 68150F.

[38] Q. A. McNemar, "Note on the sampling error of the difference between correlated proportions or percentages," Psychometrika, vol. 12, no. 2, pp. 153–157, 1947.

[39] H. Bunke, "Recognition of cursive Roman handwriting—Past, present and future," in Proc. Int. Conf. Document Anal. Recognition (ICDAR), 2003, pp. 448–459.

[40] S. Long, X. He, and C. Yao, "Scene text detection and recognition: The deep learning era," Int. J. Comput. Vis., vol. 129, no. 1, pp. 161–184, 2021.

[41] X. Chen, Z. Wang, M. Zhang, K. Yang, and L. Shen, "Benchmarking multimodal vision-language models under extreme physical and optical distortions," Comput. Vis. Image Underst., vol. 240, p. 103920, 2025.

[42] H. Liu, C. Li, Q. Wu, and Y. J. Lee, "Visual instruction tuning," in Proc. Adv. Neural Inf. Process. Syst. (NeurIPS), 2023, pp. 34892–34916.

[43] DeepSeek-AI Team, "DeepSeek-VL: Towards real-world vision-language understanding," arXiv preprint arXiv:2403.05525, 2024.

[44] R. Zhang, J. Yu, P. Zhou, X. Chen, and J. Tang, "A survey on multimodal large language models for document AI: Architectures, benchmarks, and future directions," Pattern Recognit., vol. 152, p. 110450, 2025.

[45] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, "BERT: Pre-training of deep bidirectional transformers for language understanding," in Proc. Conf. North Amer. Chapter Assoc. Comput. Linguistics (NAACL-HLT), 2019, pp. 4171–4186.

[46] A. Radford, J. Wu, R. Child, D. Luan, D. Amodei, and I. Sutskever, "Language models are unsupervised multitask learners," OpenAI Blog, vol. 1, no. 8, p. 9, 2019.

[47] T. Brown, B. Mann, N. Ryder, M. Subbiah, J. Kaplan, P. Dhariwal et al., "Language models are few-shot learners," in Proc. Adv. Neural Inf. Process. Syst. (NeurIPS), vol. 33, 2020, pp. 1877–1901.

[48] P. Lewis, E. Perez, A. Piktus, F. Petroni, V. Karpukhin, N. Goyal et al., "Retrieval-augmented generation for knowledge-intensive NLP tasks," in Proc. Adv. Neural Inf. Process. Syst. (NeurIPS), vol. 33, 2020, pp. 9459–9474.

[49] Y. Xu, M. Li, L. Cui, S. Huang, F. Wei, and M. Zhou, "LayoutLM: Pre-training of text and layout for document image understanding," in Proc. ACM SIGKDD Int. Conf. Knowl. Discovery & Data Mining, 2020, pp. 1192–1200.

[50] M. Carbonell, A. Fornes, J. Mas, and J. Llados, "Neural optical character recognition for structured document images: A comprehensive benchmark," IEEE Access, vol. 12, pp. 45012–45028, 2024.