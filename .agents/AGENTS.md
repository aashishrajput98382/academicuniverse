# Project Rules — AU DIC Benchmark System

## Benchmark Artifact Storage Directive
- **Single Self-Contained Folder Rule**: Every benchmark evaluation run must store all of its artifact files (`metrics.json`, `comparisons.json`, `predictions.json`, `paired_field_observations.csv`, `statistical_results.json`, `summary.md`, `execution.log`) strictly inside its own dedicated run directory under `backend/benchmark_reports/<runId>/`.
- Do NOT scatter benchmark output files randomly across the workspace root or unorganized directories.

## Research Paper Pipeline Versioning Directive
- **New Versioned File Rule**: Whenever executing or modifying the research paper generation pipeline to produce PDF/DOCX/Markdown builds, **NEVER** overwrite existing previous versions in-place. Always create a new file with the incremented/proper version name (e.g., `PaperV13_Ollama_Primary.pdf`, `PaperV13_Ollama_Primary.docx`, `Paper_V13.md`, `PAPER_V13_RELEASE_MANIFEST.md`, `generate_paperv13_pipeline.py`).
- **Frozen History Preservation**: Keep all preceding version artifacts (V4, V5, ..., V12, etc.) completely intact and frozen for provenance and audit tracking.

