# PAPER V40 CHANGE AUDIT: DRAW.IO SYSTEM ARCHITECTURE FIGURE REPLACEMENT

1. **Replaced Fig. 1 with draw.io SVG Diagram**: Substituted the previous Mermaid-rendered system architecture with the user-designed `au.drawio.svg` diagram, rendered at 300 DPI and embedded at 3.6 inches width.
2. **Source Artifact**: `docs/figures/au.drawio.svg` (draw.io format, editable in draw.io/diagrams.net).
3. **Rendering Pipeline**: SVG -> 300 DPI PNG (via PyMuPDF) -> Embedded in DOCX paragraph 21 -> PDF export via Word COM.
4. **Preserved All Previous Fixes**: Nuanced FERPA/GDPR privacy statements (V39), synthetic specimen terminology (V38), 100% live SOTA benchmark (V37), and full statistical harmony.
5. **Page Budget**: 20 pages (<= 20 pages IEEE budget).
6. **Frozen Provenance**: Versions V5 through V39 verified 100% frozen and intact.