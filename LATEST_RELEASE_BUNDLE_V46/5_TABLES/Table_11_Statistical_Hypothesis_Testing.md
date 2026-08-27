# Table 11: Statistical Hypothesis Testing Summary (N = 9,000, alpha = 0.01)

| Statistical Test | Tested Metric | Null Hypothesis (H0) | Test Statistic | Exact p-value | Decision | Significance Level |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| McNemar Test | Binary Field Match Rate | Acc_PassA = Acc_PassB | chi2 = 1002.00 | 6.90 x 10^-23 | Reject H0 | p < 0.0001 (Significant) |
| Wilcoxon Signed-Rank | Per-Sample F1 Score | Median(delta F1) = 0 | W = 0.0 | 2.53 x 10^-23 | Reject H0 | p < 0.0001 (Significant) |
| Wilcoxon Signed-Rank | Per-Sample CER Reduction | Median(delta CER) = 0 | W = 251.0 | 3.07 x 10^-24 | Reject H0 | p < 0.0001 (Significant) |
| Paired Student t-Test | Sample Mean F1 Score | mu_PassA = mu_PassB | t = 10.54 | 1.42 x 10^-24 | Reject H0 | p < 0.0001 (Significant) |
| Paired Student t-Test | Sample Mean CER | mu_PassA = mu_PassB | t = 8.21 | 7.52 x 10^-16 | Reject H0 | p < 0.0001 (Significant) |