# List of Figure Captions

**Manuscript Title:** Smart Academic Document Intelligence System: Automated Extraction, Normalization, and Benchmark Generation  
**Authors:** Kushagra Singh Bhadauria, Aashish Rajput, and Avdesh Kumar Sah  
**Corresponding Author:** Aashish Rajput (`2023329421.aashish@ug.sharda.ac.in`)  
**Target Venue:** IEEE Access / ICDAR 2026  

---

### Figure Captions List (Separate Sheet for Typesetting)

* **Fig. 1.** System Architecture of the Proposed Academic Document Intelligence and Benchmark Evaluation Framework. The architecture decomposes into two decoupled subsystems: (1) Academic Document Benchmark Generator (ADBG v1.0) for vector template compilation and multi-profile optical degradation, and (2) AU DIC Evaluation Subsystem for read-only neural inference ingestion, semantic canonical normalization, and nine-class OCR error taxonomy classification.
* **Fig. 2.** Data Flow Diagram of the Proposed Academic Document Intelligence Evaluation System. Traces the end-to-end multi-level transformation lifecycle across Level 0 (Context Level), Level 1 (Framework Execution Flow), and Level 2 (Diagnostic Error Classification & Evaluation Engine).
* **Fig. 3.** Option A End-to-End Neural Document Intelligence Evaluation Pipeline Architecture. Demonstrates direct image pixel tensor ingestion via Ollama local runtime to MiniCPM-V (7.6B Q4_0) without external OCR pre-segmentation.
* **Fig. 4.** Accuracy Improvement after Semantic Canonical Normalization. Bar chart illustrating field-level accuracy and exact match gains across Certificate, Marksheet, and ID Card document categories before and after normalization.
* **Fig. 5.** Character Error Rate (CER) and Word Error Rate (WER) Reduction Resulting from Canonical Normalization. Visualizes the 90.42% relative reduction in Character Error Rate (from 38.13% to 3.65%) and 90.53% reduction in Word Error Rate (from 285.31% to 27.01%).
* **Fig. 6.** Total False-Negative Field Mismatches Resolved by Each Individual Domain Normalizer Rule. Horizontal distribution of the 2,620 corrected errors across Date, Roll Number, Degree Alias, Numeric, Honorific/Whitespace, and University Alias normalizers.
* **Fig. 7.** Field-by-Field Accuracy Improvement Comparing Raw String Matching Against Canonical Normalization. Detailed multi-field breakdown comparing baseline unnormalized exact match rates against post-canonicalization accuracy.
* **Fig. 8.** Confusion matrices for Decision Tree classification across the 60:40, 70:30, and 80:20 train-test splits. Evaluates the predictability of document extraction failure modes using axis-aligned decision trees (93.69% accuracy, 95.91% F1, 0.8303 MCC).
* **Fig. 9.** Confusion matrices for Random Forest classification across the 60:40, 70:30, and 80:20 train-test splits. Compares ensemble bagging classification across 24,480 observations against decision tree models.
