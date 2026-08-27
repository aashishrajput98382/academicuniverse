# Table 5: Canonical Experimental Configuration Parameters

| Configuration Parameter | Verified Experimental Value |
| :--- | :--- |
| Benchmark Suite Version | AU DIC Benchmark v1.0 (450 Synthetic Multi-Modal Specimens Suite) |
| Benchmark Execution Mode | Headless Read-Only Mode (isReadOnly: true, 0 Database Writes) |
| Model-Serving Runtime | Local Ollama Inference Engine (v0.32.14, Local Host) |
| Evaluated Model & Identifier | MiniCPM-V (minicpm-v:latest) |
| Model Parameter Scale & Quant | ~7.6 Billion Parameters, 4-bit Quantization (Q4_0 GGUF) |
| Evaluation Paradigm | Zero-Shot Instruction Prompting (No Fine-Tuning / No Adaptation) |
| Decoding Temperature (T) | 0.2 (Greedy / Low-Entropy Deterministic Sampling) |
| Maximum Generation Budget | 8192 Output Tokens / Specimen |
| Mock Fallback Setting | Disabled (allowMockFallback: false, Live Neural Inference Only) |
| Total Evaluated Specimens | 450 Synthetic Specimens (50 Vector PDFs + 200 Lossless PNGs + 200 Compressed JPEGs) |
| Total Paired Observations | 9,000 Paired Field Observations (20 Atomic Fields / Specimen) |
| Master Deterministic Seed | SeedManager.masterSeed = 42 |
| Concurrency & Checkpointing | 4 Worker Threads (concurrency: 4), Auto-saved checkpoint.json |
| Semantic Normalization Pipeline | Six-Stage CanonicalNormalizer (Enabled in Pass B) |
| Error Diagnostic Classification | Nine-Class ErrorTaxonomist (Enabled) |
| Bootstrap Significance Iterations | B = 10,000 Iterations (Bootstrap Random Seed = 42) |
| Hypothesis Significance Threshold | alpha = 0.05 (Achieved Significance p < 0.0001) |
| Canonical Execution Run ID | run_450_live_gpu_1787773778444 (Duration: 35746.20s / 595.77 mins) |
| Git Repository Commit | Commit 0cb27be (https://github.com/aashishrajput9838/academicuniverse.git) |
| Dataset SHA-256 Checksum | 17c136ef76dd0f82 |