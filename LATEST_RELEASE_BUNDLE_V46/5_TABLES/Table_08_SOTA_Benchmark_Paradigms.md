# Table 8: State-of-the-Art (SOTA) Empirical Benchmark Across Document Intelligence Paradigms on AU DIC Dataset

| Document Intelligence Architecture | Model Paradigm / Pipeline | Benchmark Evaluation Protocol | Category Accuracy | Student Name Acc | Overall Field F1 | Character Error Rate (CER) | Benchmark Status & Empirical Summary |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Classical Vector Extractor [19] | Direct Text Stream (PyMuPDF) | Direct Live Run (AU DIC 450 Synthetic Specimens) | 33.33% | 11.11% | 11.11% | 88.89% | Baseline: Fails completely on raster image photos |
| OCR + Spatial Parser [20] | Tesseract 5.3 + Layout Rules | Direct Live Run (AU DIC 450 Synthetic Specimens) | 68.89% | 62.20% | 52.22% | 38.40% | Baseline: Degrades under optical noise & rotation |
| Pure Foundation VLM (MiniCPM-V) [31] | Zero-Shot Neural Pixel Ingestion | Direct Live Run (AU DIC 450 Synthetic Specimens - Pass A) | 100.00% | 96.00% | 81.77% | 8.14% | Baseline: Neural vision penalized by raw formatting |
| Proposed AU DIC System (Ours) | Neural VLM + 6-Stage Normalizer | Direct Live Run (AU DIC 450 Synthetic Specimens - Pass B) | 100.00% | 96.00% | 92.92% | 2.45% | State-of-the-Art (SOTA) on AU DIC Suite (+11.16% Gain) |