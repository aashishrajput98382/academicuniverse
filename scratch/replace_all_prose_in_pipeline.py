import docx
import re
from pathlib import Path

# Inject paragraph replacements into generate_paperv22_pipeline.py
with open('scratch/generate_paperv22_pipeline.py', 'r', encoding='utf-8') as f:
    code = f.read()

prose_replacements_code = '''
# -------------------------------------------------------------
# SYSTEMATICALLY REPLACE ALL REMAINING PROSE PARAGRAPHS WITH 45-SPECIMEN DATA
# -------------------------------------------------------------
for p in doc.paragraphs:
    txt = p.text.strip()
    
    # Section 4.2 prose
    if "is organized hierarchically into 90 original seed-generated" in txt or "producing exactly 360" in txt:
        p.text = "The evaluation benchmark suite (AU_DIC_Benchmark_v1.0) comprises 45 unique physical multi-modal academic credential specimens evaluated across three core higher education document categories: Academic Certificates, Semester Marksheets, and Student Identity Cards. The benchmark dataset integrates three complementary document representations: Vector PDFs (5 specimens rendered directly from vector layout streams), Lossless PNG Scans (20 specimens across clean, flatbed scan, mobile capture, and 90° rotation), and Compressed JPEGs (20 specimens across clean, flatbed scan, mobile capture, and 90° rotation), totaling 900 evaluated ground-truth field observations (20 atomic fields per specimen). Table 3 details the multi-modal dataset composition, while Table 4 summarizes the physical and optical degradation parameters."
    
    # Section 4.4 Step 5
    elif txt.startswith("5. Benchmark Suite Assembly:"):
        p.text = "5. Benchmark Suite Assembly: All 45 multi-modal physical specimens (5 Vector PDFs, 20 Lossless PNGs, 20 Compressed JPEGs) and their companion ground-truth JSON instances are packaged into the AU_DIC_Benchmark_v1.0 repository."
        
    # Section 4.4 Step 9
    elif txt.startswith("9. Ground-Truth Alignment:"):
        p.text = "9. Ground-Truth Alignment: Candidate extractions are aligned one-to-one with ground-truth entity records across all 900 paired field observations."
        
    # Section 4.5 Math intro
    elif "Let N = 360 represent total evaluated document specimens" in txt or "M = 24,480 represent" in txt:
        p.text = "To rigorously quantify information extraction precision, character recognition fidelity, and classification correctness, the evaluation framework establishes sixteen mathematical metrics. Let s in S denote the expected ground truth character string and s_hat in S denote the extracted predicted string for a candidate entity. Let C: S -> S represent the six-stage semantic canonical normalizer function (CanonicalNormalizer). Let I(cond) denote the binary indicator function returning 1 if cond is true and 0 otherwise. Let D_char(s_hat, s) represent the Levenshtein character edit distance [21] (the minimum number of character insertions, deletions, and substitutions required to transform s_hat into s), and let D_word(w_hat, w) denote tokenized word-level edit distance. Let TP, FP, TN, and FN denote True Positives, False Positives, True Negatives, and False Negatives, respectively. Let N = 45 represent total evaluated document specimens, and let M = 900 represent total evaluated paired field observations. Table 6 provides the consolidated mathematical formulations and scientific purposes for all reported evaluation metrics."
        
    # Section 5 Dry-Run intro
    elif "infrastructure verification across all 360 benchmark specimens" in txt:
        p.text = "The empirical evaluation of the proposed Smart Academic Document Intelligence System begins with dry-run infrastructure verification across all 45 physical specimens in AU_DIC_Benchmark_v1.0. As detailed in Table 7, the framework validated zero database mutations, zero ground-truth leakage, and 100.00% verification accuracy, operating at a processing throughput of 242.59 specimens per second with 4.12 ms mean latency."
        
    # Section 5 Live Baseline intro
    elif "inference was executed across all 360 specimens" in txt or "across 24,480 field observations" in txt:
        p.text = "Live multimodal document intelligence inference was executed across all 45 physical specimens under the Option A pipeline depicted in Fig. 3 using MiniCPM-V (7.6B Q4_0) via the local Ollama runtime. As presented in Table 8, the zero-shot model achieved 100.00% category accuracy, 97.80% Student Name Accuracy, 93.30% University Recognition, 79.56% Raw Field F1, and 90.56% Normalized Field F1 across 900 field observations."
        
    # Section 5 Ablation intro
    elif "rule ablation study was conducted across all 24,480 field observations" in txt:
        p.text = "To isolate the synthetic formatting discrepancy correction capability of the Six-Stage Semantic Canonical Normalizer independently from visual perception errors, a two-pass rule ablation study was conducted across all 900 field observations. As summarized in Table 9 and visualized in Fig. 4 and Fig. 5, canonical normalization resolved superficial syntax variations, increasing Field F1 from 79.56% to 90.56% (+11.00% net gain, +13.83% relative) while reducing Character Error Rate from 9.69% to 3.64% (a 62.44% relative error reduction)."
        
    # Table 9 title
    elif "TABLE 9:" in txt and "360 SPECIMENS" in txt:
        p.text = "TABLE 9: EMPIRICAL METRIC IMPACT OF SEMANTIC CANONICAL NORMALIZATION (45 SPECIMENS / 900 FIELDS)"
        
    # Section 5 Rule Corrections intro
    elif "resolved 2,620 false-negative field mismatches" in txt:
        p.text = "The CanonicalNormalizer resolved 99 false-negative field mismatches across specialized domain rules as reported in Table 10. Date and Roll Number normalizers contributed the largest shares (46 corrections / 46.46% and 30 corrections / 30.30% respectively), while Numeric rules resolved 23 errors (23.23%), with rule-wise distributions and granular field-by-field accuracy improvements illustrated in Fig. 6 and Fig. 7."
        
    # Table 11 title
    elif "TABLE 11:" in txt and "24,480" in txt:
        p.text = "TABLE 11: STATISTICAL HYPOTHESIS TESTING SUMMARY (N = 900, alpha = 0.01)"
        
    # Section 5 Error Taxonomy intro
    elif "evaluates 5,760 core scalar metadata observations" in txt or "All 2,620 `FORMAT_ERROR`" in txt:
        p.text = "The nine-class diagnostic OCR error taxonomy distribution shift detailed in Table 13 evaluates 900 atomic field observations across the 45 physical specimens. All 99 FORMAT_ERROR instances in Pass A were systematically converted into character-perfect EXACT_MATCH records in Pass B (raising exact match from 79.56% to 90.56%), while 85 genuine NORMALIZATION_ERROR cases (9.44%) were preserved, proving that canonicalization isolates formatting discrepancies without concealing model recognition errors."
        
    # Section 5 ML intro
    elif "Decision Tree and Random Forest classifiers were evaluated across 24,480 observations" in txt:
        p.text = "To assess extraction failure predictability from document and degradation features, classical Decision Tree and Random Forest classifiers were evaluated across 900 observations. As reported in Table 14, Random Forest models achieved 96.11% accuracy, 97.89% F1, and 0.7514 MCC on the 80:20 split, closely matched by Decision Trees (96.11% accuracy, 97.86% F1, 0.7669 MCC), as illustrated in the composite confusion matrices of Fig. 8 and Fig. 9."

    # Section 6 Conclusion
    elif "Live empirical evaluation across 360 specimens" in txt or "24,480 paired observations" in txt:
        p.text = "Benchmarking document intelligence systems on academic credentials remains bottlenecked by statutory privacy regulations such as FERPA and GDPR, alongside rigid string evaluation metrics that artificially penalize benign formatting variances [25], [28], [35]. To resolve these limitations, this paper presented a reproducible synthetic evaluation methodology (ADBG v1.0 and AU DIC Framework v1.0) [26], [31]. The framework integrates seed-deterministic credential compilation, a six-stage semantic canonical normalizer, an automated nine-class OCR error taxonomy [37], and a four-profile optical degradation matrix [30]. Live empirical evaluation across 45 physical multi-modal specimens (900 paired field observations) confirmed that canonical normalization isolates genuine extraction failures (McNemar chi2 = 97.01, p < 0.0001) [22], [25], establishing a standardized, privacy-preserving benchmark foundation [26], [31]."
'''

if "SYSTEMATICALLY REPLACE ALL REMAINING PROSE PARAGRAPHS" not in code:
    code = code.replace('doc.save(v22_docx_path)', prose_replacements_code + '\ndoc.save(v22_docx_path)')

with open('scratch/generate_paperv22_pipeline.py', 'w', encoding='utf-8') as f:
    f.write(code)

print('[SUCCESS] Injected systematic prose replacements into scratch/generate_paperv22_pipeline.py!')
