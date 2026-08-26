# PAPER V35 CHANGE AUDIT: SCIENTIFICALLY DEFENSIBLE BASELINE BENCHMARKING

1. **Replaced Over-reaching 'SOTA' Claims**: Rewrote Table 8 title to 'TABLE 8: CONTEXTUAL COMPARISON WITH REPORTED DOCUMENT INTELLIGENCE BASELINES ACROSS EVALUATION PARADIGMS'.
2. **Harmonized Benchmark Badge**: Updated Table 8 proposed system row from 'Live Verified State-of-the-Art' to 'Best performance observed within evaluated AU DIC configuration (+11.00% net gain)'.
3. **Refined Abstract and Results Prose**: Reframed extraction performance claims as superior empirical accuracy on academic records with explicit methodological transparency regarding dataset provenance.
4. **Created Multi-Model Evaluation Harness**: Added `research/evaluate_multi_model_sota_benchmark.py` allowing standardized multi-model evaluation (MiniCPM-V, LLaVA, Donut, PyMuPDF) under identical dataset conditions.
5. **Maintained 100% Statistical Consistency**: McNemar chi2 = 97.01, Wilcoxon W = 0.0, Paired t = 10.54, Pass A F1 [76.89%, 82.22%], Pass B F1 [88.56%, 92.44%], p < 0.0001 across all sections.
6. **Strict Page Budget**: Verified exactly 19 pages (<= 20 pages standard IEEE journal budget).
7. **Frozen Provenance**: Preceding versions V5 through V34 verified 100% frozen and intact.