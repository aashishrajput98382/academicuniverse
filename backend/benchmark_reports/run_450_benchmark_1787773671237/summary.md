# AU DIC 450-Document Scientific Benchmark Report

**Run ID**: `run_450_benchmark_1787773671237`  
**Dataset Source**: `D:\AU_DIC_Benchmark_60k`  
**Total Evaluated Documents**: **450** (450 Successful | 0 Failed)  
**Total Paired Field Observations**: **9,000** (450 specimens $\times$ 20 fields)  
**Total Runtime**: **2.23s**  

---

## 1. Modality & Optical Degradation Performance Matrix

| Modality / Quality Profile | Documents | Pass A (Raw F1) | Pass B (Norm F1) | Net Gain (Δ F1) |
| :--- | :--- | :--- | :--- | :--- |
| **Clean Vector PDF** | 50 | 85.30% | 96.10% | +10.80% |
| **Clean PNG** | 50 | 85.50% | 96.40% | +10.90% |
| **Scanned PNG (scanner_copy)** | 50 | 84.30% | 95.50% | +11.20% |
| **Mobile Camera PNG** | 50 | 81.20% | 92.30% | +11.10% |
| **Rotated 90° PNG** | 50 | 74.30% | 85.90% | +11.60% |
| **Clean JPEG** | 50 | 85.50% | 96.40% | +10.90% |
| **Scanned JPEG (scanner_copy)** | 50 | 84.50% | 95.50% | +11.00% |
| **Mobile Camera JPEG** | 50 | 81.00% | 92.30% | +11.30% |
| **Rotated 90° JPEG** | 50 | 74.30% | 85.90% | +11.60% |
| **OVERALL SYSTEM TOTAL** | **450** | **81.77%** | **92.92%** | **+11.16% (+13.64%)** |

---

## 2. Statistical Hypothesis Testing

- **McNemar Chi-Square**: $\chi^2 = 1002.00$ ($p = 6.5966e-220$)
- **Wilcoxon Signed-Rank Test (F1)**: $W = 0.0$ ($p = 2.4256e-220$)
- **Wilcoxon Signed-Rank Test (CER)**: $W = 39159.0$ ($p = 7.1047e-176$)
- **Paired t-test (F1)**: $t = 33.61$ ($p = 1.8307e-233$)
- **Paired t-test (CER)**: $t = 23.67$ ($p = 3.1501e-120$)

---

## 3. Bootstrap 95% Confidence Intervals ($B=10,000$)

- **Pass A F1 Score**: Mean = `81.77%` | 95% CI: `[80.97%, 82.56%]`
- **Pass B F1 Score**: Mean = `92.92%` | 95% CI: `[92.38%, 93.46%]`
- **Pass A CER**: Mean = `8.14%` | 95% CI: `[7.63%, 8.68%]`
- **Pass B CER**: Mean = `2.45%` | 95% CI: `[2.21%, 2.70%]`

---

## 4. Machine Learning Failure Prediction Benchmark

| Split | Decision Tree F1 | Decision Tree MCC | Random Forest F1 | Random Forest MCC |
| :--- | :--- | :--- | :--- | :--- |
| **60:40** | 97.51% | 0.5642 | 97.62% | 0.5865 |
| **70:30** | 97.66% | 0.5950 | 97.74% | 0.6126 |
| **80:20** | 97.81% | 0.6260 | 97.75% | 0.6135 |

---

*Generated automatically in compliance with AU DIC Single Self-Contained Folder Rule.*
