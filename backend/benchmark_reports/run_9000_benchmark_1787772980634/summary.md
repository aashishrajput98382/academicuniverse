# AU DIC 9,000-Document Scientific Benchmark Report

**Run ID**: `run_9000_benchmark_1787772980634`  
**Dataset Source**: `D:\AU_DIC_Benchmark_60k`  
**Total Evaluated Documents**: **9,000** (9,000 Successful | 0 Failed)  
**Total Paired Field Observations**: **180,000**  
**Total Runtime**: **79.21s**  

---

## 1. Modality & Optical Degradation Performance Matrix

| Modality / Quality Profile | Documents | Pass A (Raw F1) | Pass B (Norm F1) | Net Gain (Δ F1) |
| :--- | :--- | :--- | :--- | :--- |
| **Clean Vector PDF** | 1,000 | 85.34% | 96.23% | +10.88% |
| **Clean PNG** | 1,000 | 85.38% | 96.29% | +10.91% |
| **Scanned PNG (scanner_copy)** | 1,000 | 83.21% | 94.22% | +11.01% |
| **Mobile Camera PNG** | 1,000 | 80.06% | 91.17% | +11.11% |
| **Rotated 90° PNG** | 1,000 | 74.37% | 85.83% | +11.47% |
| **Clean JPEG** | 1,000 | 85.37% | 96.29% | +10.92% |
| **Scanned JPEG (scanner_copy)** | 1,000 | 83.23% | 94.22% | +10.99% |
| **Mobile Camera JPEG** | 1,000 | 80.06% | 91.17% | +11.11% |
| **Rotated 90° JPEG** | 1,000 | 74.36% | 85.83% | +11.48% |
| **OVERALL SYSTEM TOTAL** | **9,000** | **81.26%** | **92.36%** | **+11.10% (+13.66%)** |

---

## 2. Statistical Hypothesis Testing

- **McNemar Chi-Square**: $\chi^2 = 19975.00$ ($p = 0.0000e+00$)
- **Wilcoxon Signed-Rank Test (F1)**: $W = 0.0$ ($p = 0.0000e+00$)
- **Wilcoxon Signed-Rank Test (CER)**: $W = 10807368.0$ ($p = 0.0000e+00$)
- **Paired t-test (F1)**: $t = 149.90$ ($p = 0.0000e+00$)
- **Paired t-test (CER)**: $t = 108.83$ ($p = 0.0000e+00$)

---

## 3. Bootstrap 95% Confidence Intervals ($B=10,000$)

- **Pass A F1 Score**: Mean = `81.26%` | 95% CI: `[80.51%, 82.03%]`
- **Pass B F1 Score**: Mean = `92.36%` | 95% CI: `[91.83%, 92.87%]`
- **Pass A CER**: Mean = `8.13%` | 95% CI: `[7.64%, 8.63%]`
- **Pass B CER**: Mean = `2.42%` | 95% CI: `[2.20%, 2.64%]`

---

## 4. Machine Learning Failure Prediction Benchmark

| Split | Decision Tree F1 | Decision Tree MCC | Random Forest F1 | Random Forest MCC |
| :--- | :--- | :--- | :--- | :--- |
| **60:40** | 97.43% | 0.5854 | 97.41% | 0.5819 |
| **70:30** | 97.44% | 0.5880 | 97.42% | 0.5848 |
| **80:20** | 97.43% | 0.5864 | 97.42% | 0.5842 |

---

*Generated automatically in compliance with AU DIC Single Self-Contained Folder Rule.*
