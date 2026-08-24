import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Polygon, Circle
from pathlib import Path

workspace = Path(__file__).resolve().parents[1]
fig_dir = workspace / "docs" / "paper" / "extracted_figures"
fig_dir.mkdir(parents=True, exist_ok=True)

plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.family'] = 'sans-serif'

# -------------------------------------------------------------------------
# UTILITY FUNCTIONS FOR DRAWING FORMAL FLOWCHART SHAPES
# -------------------------------------------------------------------------

def draw_oval(ax, x, y, w, h, text, color="#EBF8FF", border="#2B6CB0"):
    """Draws a Start/End terminal oval."""
    box = FancyBboxPatch((x - w/2, y - h/2), w, h,
                         boxstyle=f"round,pad=0.02,rounding_size={h/2}",
                         facecolor=color, edgecolor=border, linewidth=1.5, zorder=3)
    ax.add_patch(box)
    ax.text(x, y, text, ha='center', va='center', fontsize=9, fontweight='bold', color="#1A202C", zorder=4)

def draw_parallelogram(ax, x, y, w, h, text, color="#FEFCBF", border="#D69E2E", skew=0.15):
    """Draws an Input/Output parallelogram."""
    pts = [
        [x - w/2 + skew, y - h/2],
        [x + w/2 + skew, y - h/2],
        [x + w/2 - skew, y + h/2],
        [x - w/2 - skew, y + h/2]
    ]
    poly = Polygon(pts, closed=True, facecolor=color, edgecolor=border, linewidth=1.5, zorder=3)
    ax.add_patch(poly)
    ax.text(x, y, text, ha='center', va='center', fontsize=8.5, fontweight='bold', color="#1A202C", zorder=4)

def draw_rect(ax, x, y, w, h, text, color="#FFFFFF", border="#4A5568", subtitle=None):
    """Draws a standard process rectangle."""
    box = FancyBboxPatch((x - w/2, y - h/2), w, h,
                         boxstyle="square,pad=0.0",
                         facecolor=color, edgecolor=border, linewidth=1.5, zorder=3)
    ax.add_patch(box)
    if subtitle:
        ax.text(x, y + 0.12*h, text, ha='center', va='center', fontsize=9, fontweight='bold', color="#1A202C", zorder=4)
        ax.text(x, y - 0.18*h, subtitle, ha='center', va='center', fontsize=7.5, color="#4A5568", style='italic', zorder=4)
    else:
        ax.text(x, y, text, ha='center', va='center', fontsize=8.5, fontweight='bold', color="#1A202C", zorder=4)

def draw_predefined_process(ax, x, y, w, h, text, color="#EDF2F7", border="#2B6CB0"):
    """Draws a sub-routine rectangle with dual vertical inner bars."""
    draw_rect(ax, x, y, w, h, text, color=color, border=border)
    ax.plot([x - w/2 + 0.12, x - w/2 + 0.12], [y - h/2, y + h/2], color=border, linewidth=1.5, zorder=4)
    ax.plot([x + w/2 - 0.12, x + w/2 - 0.12], [y - h/2, y + h/2], color=border, linewidth=1.5, zorder=4)

def draw_diamond(ax, x, y, w, h, text, color="#FFF5F5", border="#E53E3E"):
    """Draws a decision diamond."""
    pts = [
        [x, y + h/2],
        [x + w/2, y],
        [x, y - h/2],
        [x - w/2, y]
    ]
    poly = Polygon(pts, closed=True, facecolor=color, edgecolor=border, linewidth=1.5, zorder=3)
    ax.add_patch(poly)
    ax.text(x, y, text, ha='center', va='center', fontsize=8.5, fontweight='bold', color="#1A202C", zorder=4)

def draw_connector(ax, x, y, r, label, color="#E2E8F0", border="#4A5568"):
    """Draws a circular on-page connector."""
    circ = Circle((x, y), r, facecolor=color, edgecolor=border, linewidth=1.5, zorder=3)
    ax.add_patch(circ)
    ax.text(x, y, label, ha='center', va='center', fontsize=9, fontweight='bold', color="#2D3748", zorder=4)

def draw_arrow(ax, x1, y1, x2, y2, text=None, text_pos='right', color="#2D3748"):
    """Draws an arrow with optional condition label."""
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(facecolor=color, edgecolor=color, width=1.2, headwidth=6, headlength=7, shrink=0.0),
                zorder=2)
    if text:
        tx = (x1 + x2) / 2
        ty = (y1 + y2) / 2
        offset_x = 0.15 if text_pos == 'right' else (-0.15 if text_pos == 'left' else 0.0)
        offset_y = 0.12 if text_pos == 'top' else (-0.12 if text_pos == 'bottom' else 0.0)
        ax.text(tx + offset_x, ty + offset_y, text, fontsize=7.5, fontweight='bold', color=color,
                ha='center', va='center', bbox=dict(boxstyle='round,pad=0.15', facecolor='white', edgecolor='none', alpha=0.85), zorder=5)

# =========================================================================
# FIGURE 1: FORMAL SYSTEM ARCHITECTURE FLOWCHART (STANDARD SYMBOLS)
# =========================================================================
def generate_formal_figure_1():
    fig, ax = plt.subplots(figsize=(12, 6.2), dpi=300)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6.2)
    ax.axis('off')

    # Subsystem background containers
    box_sub1 = FancyBboxPatch((0.4, 0.4), 5.3, 5.4, boxstyle="round,pad=0.1", facecolor="#F7FAFC", edgecolor="#CBD5E0", linewidth=1.2, linestyle="--")
    ax.add_patch(box_sub1)
    ax.text(3.05, 5.55, "SUBSYSTEM 1: PRODUCTION INGESTION & PIPELINE", fontsize=9.5, fontweight='bold', color="#2B6CB0", ha='center')

    box_sub2 = FancyBboxPatch((6.3, 0.4), 5.3, 5.4, boxstyle="round,pad=0.1", facecolor="#F7FAFC", edgecolor="#CBD5E0", linewidth=1.2, linestyle="--")
    ax.add_patch(box_sub2)
    ax.text(8.95, 5.55, "SUBSYSTEM 2: ADBG BENCHMARK & EVALUATION", fontsize=9.5, fontweight='bold', color="#C53030", ha='center')

    # Left Pipeline: Subsystem 1
    draw_oval(ax, 3.05, 4.9, 2.2, 0.5, "Start: Document Intake", color="#C6F6D5", border="#22543D")
    draw_arrow(ax, 3.05, 4.65, 3.05, 4.25)

    draw_parallelogram(ax, 3.05, 3.95, 3.2, 0.55, "Input Document (PDF / Image)", color="#FEFCBF", border="#B7791F")
    draw_arrow(ax, 3.05, 3.67, 3.05, 3.25)

    draw_diamond(ax, 3.05, 2.8, 2.6, 0.8, "Doc Quality OK?", color="#ED8936", border="#C05621")
    draw_arrow(ax, 3.05, 2.4, 3.05, 1.95, "Yes (Valid)", text_pos='right')
    
    # Error branch
    draw_arrow(ax, 1.75, 2.8, 1.0, 2.8, "No", text_pos='top')
    draw_rect(ax, 1.0, 2.1, 1.4, 0.5, "Request Rescan", color="#FED7D7", border="#E53E3E")
    ax.plot([1.0, 1.0], [2.8, 2.35], color="#E53E3E", linewidth=1.2)

    draw_rect(ax, 3.05, 1.65, 3.4, 0.55, "Zero-Shot MiniCPM-V (7.6B)", subtitle="Multimodal Visual Token Extraction")
    draw_arrow(ax, 3.05, 1.37, 3.05, 0.95)

    draw_predefined_process(ax, 3.05, 0.7, 3.6, 0.5, "6-Stage Semantic Normalizer", color="#EBF8FF", border="#2B6CB0")

    # Right Pipeline: Subsystem 2 (Benchmark & Evaluation)
    draw_oval(ax, 8.95, 4.9, 2.4, 0.5, "Start: ADBG Generation", color="#FED7E2", border="#97266D")
    draw_arrow(ax, 8.95, 4.65, 8.95, 4.25)

    draw_rect(ax, 8.95, 3.95, 3.4, 0.55, "Seed-Deterministic Typst Compiler", subtitle="45 Specimens across 3 Categories")
    draw_arrow(ax, 8.95, 3.67, 8.95, 3.25)

    draw_rect(ax, 8.95, 2.95, 3.4, 0.55, "14-Operator Optical Degradation", subtitle="Clean, Scanner, Mobile, Rotated_90")
    draw_arrow(ax, 8.95, 2.67, 8.95, 2.25)

    draw_diamond(ax, 8.95, 1.8, 2.8, 0.8, "Pass A or Pass B?", color="#ED8936", border="#C05621")
    
    draw_arrow(ax, 7.55, 1.8, 6.9, 1.8, "Pass A (Raw)", text_pos='top')
    draw_rect(ax, 6.9, 1.1, 1.6, 0.5, "Raw String EM", color="#EDF2F7", border="#4A5568")
    ax.plot([6.9, 6.9], [1.8, 1.35], color="#4A5568", linewidth=1.2)

    draw_arrow(ax, 10.35, 1.8, 11.0, 1.8, "Pass B (Norm)", text_pos='top')
    draw_rect(ax, 11.0, 1.1, 1.6, 0.5, "9-Class Taxonomy", color="#EBF8FF", border="#2B6CB0")
    ax.plot([11.0, 11.0], [1.8, 1.35], color="#2B6CB0", linewidth=1.2)

    # Final Output Sync
    draw_oval(ax, 8.95, 0.7, 2.6, 0.45, "Verified State-of-the-Art", color="#C6F6D5", border="#22543D")
    draw_arrow(ax, 6.9, 0.85, 7.65, 0.7)
    draw_arrow(ax, 11.0, 0.85, 10.25, 0.7)

    plt.tight_layout()
    fig1_out = fig_dir / "image1.png"
    plt.savefig(fig1_out, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"[SUCCESS] Generated formal IEEE Flowchart 1: {fig1_out.name}")

# =========================================================================
# FIGURE 2: FORMAL DATA FLOW DIAGRAM (DFD LEVEL 0, 1, 2)
# =========================================================================
def generate_formal_figure_2():
    fig, ax = plt.subplots(figsize=(12, 6.2), dpi=300)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6.2)
    ax.axis('off')

    # DFD Level 0: Context Level
    box_lvl0 = FancyBboxPatch((0.4, 4.3), 11.2, 1.6, boxstyle="round,pad=0.08", facecolor="#F7FAFC", edgecolor="#CBD5E0", linewidth=1.2)
    ax.add_patch(box_lvl0)
    ax.text(0.7, 5.65, "LEVEL 0: CONTEXT LEVEL DFD", fontsize=9, fontweight='bold', color="#2B6CB0")

    draw_rect(ax, 1.8, 4.95, 1.8, 0.6, "System Evaluator", color="#EDF2F7", border="#2B6CB0")
    draw_arrow(ax, 2.7, 4.95, 4.4, 4.95, "Run Benchmark Config")

    draw_oval(ax, 5.8, 4.95, 2.8, 0.7, "0.0 Academic Universe\nDocument Engine", color="#EBF8FF", border="#2B6CB0")

    draw_arrow(ax, 7.2, 4.95, 8.9, 4.95, "Audit Reports & Metrics")
    draw_rect(ax, 10.0, 4.95, 2.0, 0.6, "Persistent Storage\n& Analytics", color="#EDF2F7", border="#2B6CB0")

    # DFD Level 1: Framework Execution Flow
    box_lvl1 = FancyBboxPatch((0.4, 2.2), 11.2, 1.9, boxstyle="round,pad=0.08", facecolor="#F7FAFC", edgecolor="#CBD5E0", linewidth=1.2)
    ax.add_patch(box_lvl1)
    ax.text(0.7, 3.85, "LEVEL 1: FRAMEWORK EXECUTION FLOW", fontsize=9, fontweight='bold', color="#2F855A")

    draw_oval(ax, 1.8, 3.0, 1.8, 0.6, "1.0 Synthetic\nCompilation", color="#E6FFFA", border="#234E52")
    draw_arrow(ax, 2.7, 3.0, 3.7, 3.0, "Vector PDF")

    draw_oval(ax, 4.7, 3.0, 2.0, 0.6, "2.0 Optical\nDegradation", color="#E6FFFA", border="#234E52")
    draw_arrow(ax, 5.7, 3.0, 6.7, 3.0, "4 Quality Profiles")

    draw_oval(ax, 7.7, 3.0, 2.0, 0.6, "3.0 Zero-Shot\nVLM Inference", color="#E6FFFA", border="#234E52")
    draw_arrow(ax, 8.7, 3.0, 9.7, 3.0, "Raw JSON Output")

    draw_oval(ax, 10.5, 3.0, 1.6, 0.6, "4.0 Canonical\nNormalizer", color="#E6FFFA", border="#234E52")

    # DFD Level 2: Diagnostic Evaluation Engine
    box_lvl2 = FancyBboxPatch((0.4, 0.3), 11.2, 1.7, boxstyle="round,pad=0.08", facecolor="#F7FAFC", edgecolor="#CBD5E0", linewidth=1.2)
    ax.add_patch(box_lvl2)
    ax.text(0.7, 1.75, "LEVEL 2: DIAGNOSTIC ERROR CLASSIFICATION & EVALUATION ENGINE", fontsize=9, fontweight='bold', color="#C53030")

    draw_oval(ax, 2.2, 0.95, 2.4, 0.6, "4.1 Ground-Truth\nJSON Alignment", color="#FFF5F5", border="#742A2A")
    draw_arrow(ax, 3.4, 0.95, 4.4, 0.95, "Field Pairs")

    draw_oval(ax, 5.6, 0.95, 2.4, 0.6, "4.2 Six-Stage Semantic\nRule Normalizer", color="#FFF5F5", border="#742A2A")
    draw_arrow(ax, 6.8, 0.95, 7.8, 0.95, "Standardized Fields")

    draw_oval(ax, 9.0, 0.95, 2.4, 0.6, "4.3 9-Class OCR Error\nTaxonomy Classifier", color="#FFF5F5", border="#742A2A")
    draw_arrow(ax, 10.2, 0.95, 11.0, 0.95)

    draw_connector(ax, 11.3, 0.95, 0.25, "RES", color="#FEFCBF", border="#B7791F")

    plt.tight_layout()
    fig2_out = fig_dir / "image2.png"
    plt.savefig(fig2_out, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"[SUCCESS] Generated formal IEEE Flowchart 2: {fig2_out.name}")

# =========================================================================
# FIGURE 3: OPTION A INFERENCE PIPELINE FLOWCHART
# =========================================================================
def generate_formal_figure_3():
    fig, ax = plt.subplots(figsize=(12, 6.2), dpi=300)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6.2)
    ax.axis('off')

    box_main = FancyBboxPatch((0.4, 0.4), 11.2, 5.4, boxstyle="round,pad=0.1", facecolor="#F7FAFC", edgecolor="#CBD5E0", linewidth=1.2)
    ax.add_patch(box_main)
    ax.text(6.0, 5.55, "OPTION A END-TO-END MULTIMODAL VLM INFERENCE & SCORING PIPELINE", fontsize=10, fontweight='bold', color="#2B6CB0", ha='center')

    # Row 1 (Left to Right)
    draw_oval(ax, 1.8, 4.6, 2.0, 0.5, "Start: Ingest Specimen", color="#C6F6D5", border="#22543D")
    draw_arrow(ax, 2.8, 4.6, 3.8, 4.6)

    draw_parallelogram(ax, 5.0, 4.6, 2.4, 0.55, "Load Document Tensor\n(PDF / PNG / JPEG)", color="#FEFCBF", border="#B7791F")
    draw_arrow(ax, 6.2, 4.6, 7.2, 4.6)

    draw_rect(ax, 8.4, 4.6, 2.4, 0.55, "Resolution Normalization\n(300 DPI Grid Resize)", color="#FFFFFF", border="#4A5568")
    draw_arrow(ax, 9.6, 4.6, 10.6, 4.6)

    draw_connector(ax, 10.9, 4.6, 0.25, "1", color="#E2E8F0", border="#4A5568")

    # Row 2 (Right to Left)
    draw_connector(ax, 10.9, 3.1, 0.25, "1", color="#E2E8F0", border="#4A5568")
    draw_arrow(ax, 10.65, 3.1, 9.6, 3.1)

    draw_rect(ax, 8.4, 3.1, 2.4, 0.55, "Zero-Shot Prompt Inject\n(Academic Schema Target)", color="#FFFFFF", border="#4A5568")
    draw_arrow(ax, 7.2, 3.1, 6.2, 3.1)

    draw_predefined_process(ax, 5.0, 3.1, 2.4, 0.55, "MiniCPM-V 7.6B VLM\n(Local Ollama Engine)", color="#EBF8FF", border="#2B6CB0")
    draw_arrow(ax, 3.8, 3.1, 2.8, 3.1)

    draw_rect(ax, 1.8, 3.1, 2.0, 0.55, "Structured JSON\nParser & Validator", color="#FFFFFF", border="#4A5568")
    draw_arrow(ax, 1.8, 2.82, 1.8, 2.0)

    # Row 3 (Left to Right)
    draw_diamond(ax, 1.8, 1.6, 2.2, 0.8, "JSON Valid?", color="#ED8936", border="#C05621")
    draw_arrow(ax, 2.9, 1.6, 4.0, 1.6, "Yes (Valid)", text_pos='top')
    
    # Retry branch
    draw_arrow(ax, 1.8, 1.2, 1.8, 0.65, "No", text_pos='right')
    draw_rect(ax, 2.8, 0.65, 1.6, 0.4, "Schema Repair", color="#FED7D7", border="#E53E3E")
    ax.plot([1.8, 2.0], [0.65, 0.65], color="#E53E3E", linewidth=1.2)

    draw_predefined_process(ax, 5.2, 1.6, 2.4, 0.55, "6-Stage Semantic\nCanonicalNormalizer", color="#EBF8FF", border="#2B6CB0")
    draw_arrow(ax, 6.4, 1.6, 7.4, 1.6)

    draw_rect(ax, 8.5, 1.6, 2.2, 0.55, "9-Class Error Taxonomy\n& Statistical Scoring", color="#FFFFFF", border="#4A5568")
    draw_arrow(ax, 9.6, 1.6, 10.4, 1.6)

    draw_oval(ax, 10.9, 1.6, 1.0, 0.5, "End", color="#C6F6D5", border="#22543D")

    plt.tight_layout()
    fig3_out = fig_dir / "image3.png"
    plt.savefig(fig3_out, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"[SUCCESS] Generated formal IEEE Flowchart 3: {fig3_out.name}")

if __name__ == "__main__":
    generate_formal_figure_1()
    generate_formal_figure_2()
    generate_formal_figure_3()
    print("[ALL DONE] Generated all 3 formal IEEE flowcharts with standard symbols!")
