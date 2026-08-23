# List of Symbols & Mathematical Notation (Nomenclature)

**Manuscript Title:** Smart Academic Document Intelligence System: Automated Extraction, Normalization, and Benchmark Generation  
**Authors:** Kushagra Singh Bhadauria, Aashish Rajput, and Avdesh Kumar Sah  
**Corresponding Author:** Aashish Rajput (`2023329421.aashish@ug.sharda.ac.in`)  
**Target Venue:** IEEE Access / ICDAR 2026  

---

### List of Mathematical Symbols & Notations

| Symbol | Mathematical / Technical Meaning | Unit / Domain |
| :--- | :--- | :--- |
| $P$ | Field-level entity Precision ($P = \frac{TP}{TP + FP}$) | Percentage / Ratio $[0, 1]$ |
| $R$ | Field-level entity Recall ($R = \frac{TP}{TP + FN}$) | Percentage / Ratio $[0, 1]$ |
| $F_1$ | Harmonic mean of Precision and Recall ($F_1 = 2 \cdot \frac{P \cdot R}{P + R}$) | Percentage $[0, 100\%]$ |
| $\text{CER}$ | Character Error Rate ($\frac{S + D + I}{N_{\text{chars}}}$ via Levenshtein distance) | Percentage $[0, 100\%]$ |
| $\text{WER}$ | Word Error Rate ($\frac{S_w + D_w + I_w}{N_{\text{words}}}$) | Percentage $[0, \infty)$ |
| $\text{Raw EM}$ | Raw Exact Match rate ($\frac{1}{N} \sum \mathbb{I}(y_i = \hat{y}_i)$) | Percentage $[0, 100\%]$ |
| $\text{Norm EM}$ | Normalized Exact Match rate ($\frac{1}{N} \sum \mathbb{I}(\mathcal{N}(y_i) = \mathcal{N}(\hat{y}_i))$) | Percentage $[0, 100\%]$ |
| $\text{Joint EM}$ | Document-level Joint Record Exact Match | Percentage $[0, 100\%]$ |
| $y_i$ | Ground-truth reference string for field observation $i$ | Text String |
| $\hat{y}_i$ | Extracted model prediction string for field observation $i$ | Text String |
| $\mathcal{N}(\cdot)$ | Six-stage semantic canonicalization operator | String Transformation Function |
| $\mathbb{I}(\cdot)$ | Indicator function (evaluates to 1 if condition holds, 0 otherwise) | Binary $\{0, 1\}$ |
| $TP$ | True Positive count (correctly extracted field entity) | Integer $\ge 0$ |
| $FP$ | False Positive count (erroneously extracted or hallucinated field entity) | Integer $\ge 0$ |
| $FN$ | False Negative count (omitted or format-mismatched field entity) | Integer $\ge 0$ |
| $S, D, I$ | Substitutions, Deletions, and Insertions in Levenshtein character alignment | Integer counts $\ge 0$ |
| $N_{\text{chars}}$ | Total reference character count in ground truth | Integer $> 0$ |
| $N_{\text{words}}$ | Total reference word count in ground truth | Integer $> 0$ |
| $\chi^2$ | McNemar's chi-squared test statistic for paired binary proportions | Statistical Test Statistic |
| $W$ | Wilcoxon signed-rank test statistic for paired non-parametric differences | Statistical Test Statistic |
| $t$ | Paired Student's $t$-test statistic | Statistical Test Statistic |
| $p$ | Statistical significance probability ($p$-value) | Probability $[0, 1]$ |
| $\alpha$ | Hypothesis rejection significance threshold ($\alpha = 0.01$ or $0.05$) | Significance Level |
| $B$ | Number of non-parametric bootstrap resampling iterations ($B = 10,000$) | Integer Count |
| $\mu$ | Empirical sample mean of metric distribution | Scalar Point Estimate |
| $\Delta$ | Absolute difference or confidence interval bound range | Metric Delta |
| $\sigma$ | Standard deviation of Gaussian noise perturbation | Degradation Parameter |
| $\theta$ | Angular tilt rotation angle | Degrees ($^\circ$) |
| $k$ | Gaussian kernel blur filter window size | Pixels |
| $N$ | Total evaluated field observations ($N = 24,480$) | Integer Count |
| $|D|$ | Total evaluated document specimens ($|D| = 360$) | Integer Count |

---

### Abbreviations & Acronyms

* **ADBG:** Academic Document Benchmark Generator
* **AU DIC:** Academic Universe Document Intelligence Core / Subsystem
* **CER:** Character Error Rate
* **WER:** Word Error Rate
* **EM:** Exact Match
* **FERPA:** Family Educational Rights and Privacy Act (US)
* **GDPR:** General Data Protection Regulation (EU)
* **LLM:** Large Language Model
* **MCC:** Matthews Correlation Coefficient
* **OCR:** Optical Character Recognition
* **PII:** Personally Identifiable Information
* **VLM:** Vision-Language Model
