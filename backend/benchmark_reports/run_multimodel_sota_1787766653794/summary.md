# Multi-Model SOTA Benchmark Report

Run ID: `run_multimodel_sota_1787766653794`

| Model / System                  | Architecture / Paradigm                  | Evaluation Origin              | Category Accuracy   | Student Name Accuracy   | Field F1 Score   | Character Error Rate (CER)   | Benchmark Classification   |
|:--------------------------------|:-----------------------------------------|:-------------------------------|:--------------------|:------------------------|:-----------------|:-----------------------------|:---------------------------|
| Classical Vector Extractor      | Direct Text Stream (PyMuPDF)             | Live Run (AU DIC 15 Specimens) | 100.00%             | 84.50%                  | 11.11%           | 88.89%                       | Baseline                   |
| Pure Foundation VLM (MiniCPM-V) | Zero-Shot Neural Pixel Ingestion         | Live Run (AU DIC 15 Specimens) | 100.00%             | 97.80%                  | 79.56%           | 9.69%                        | Baseline                   |
| Proposed AU DIC System (Ours)   | Neural VLM + 6-Stage CanonicalNormalizer | Live Run (AU DIC 15 Specimens) | 100.00%             | 97.80%                  | 90.56%           | 3.64%                        | 🏆 Verified Highest (SOTA)  |