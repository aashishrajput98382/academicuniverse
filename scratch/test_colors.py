import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon, Circle

def test_colors():
    for arrow_color in ["#E53E3E", "#2D3748"]:
        fig, ax = plt.subplots(figsize=(12, 6.2), dpi=300)
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 6.2)
        ax.axis('off')

        box_main = FancyBboxPatch((0.4, 0.4), 11.2, 5.4, boxstyle="round,pad=0.1", facecolor="#F7FAFC", edgecolor="#CBD5E0", linewidth=1.2)
        ax.add_patch(box_main)
        ax.text(6.0, 5.55, "OPTION A END-TO-END MULTIMODAL VLM INFERENCE & SCORING PIPELINE", fontsize=10, fontweight='bold', color="#2B6CB0", ha='center')

        def draw_oval(ax, x, y, w, h, text, color="#EBF8FF", border="#2B6CB0"):
            box = FancyBboxPatch((x - w/2, y - h/2), w, h, boxstyle=f"round,pad=0.02,rounding_size={h/2}", facecolor=color, edgecolor=border, linewidth=1.5, zorder=3)
            ax.add_patch(box)
            ax.text(x, y, text, ha='center', va='center', fontsize=9, fontweight='bold', color="#1A202C", zorder=4)

        def draw_parallelogram(ax, x, y, w, h, text, color="#FEFCBF", border="#D69E2E", skew=0.15):
            pts = [[x - w/2 + skew, y - h/2], [x + w/2 + skew, y - h/2], [x + w/2 - skew, y + h/2], [x - w/2 - skew, y + h/2]]
            poly = Polygon(pts, closed=True, facecolor=color, edgecolor=border, linewidth=1.5, zorder=3)
            ax.add_patch(poly)
            ax.text(x, y, text, ha='center', va='center', fontsize=8.5, fontweight='bold', color="#1A202C", zorder=4)

        def draw_rect(ax, x, y, w, h, text, color="#FFFFFF", border="#4A5568", subtitle=None):
            box = FancyBboxPatch((x - w/2, y - h/2), w, h, boxstyle="square,pad=0.0", facecolor=color, edgecolor=border, linewidth=1.5, zorder=3)
            ax.add_patch(box)
            if subtitle:
                ax.text(x, y + 0.12*h, text, ha='center', va='center', fontsize=9, fontweight='bold', color="#1A202C", zorder=4)
                ax.text(x, y - 0.18*h, subtitle, ha='center', va='center', fontsize=7.5, color="#4A5568", style='italic', zorder=4)
            else:
                ax.text(x, y, text, ha='center', va='center', fontsize=8.5, fontweight='bold', color="#1A202C", zorder=4)

        def draw_predefined_process(ax, x, y, w, h, text, color="#EDF2F7", border="#2B6CB0"):
            draw_rect(ax, x, y, w, h, text, color=color, border=border)
            ax.plot([x - w/2 + 0.12, x - w/2 + 0.12], [y - h/2, y + h/2], color=border, linewidth=1.5, zorder=4)
            ax.plot([x + w/2 - 0.12, x + w/2 - 0.12], [y - h/2, y + h/2], color=border, linewidth=1.5, zorder=4)

        def draw_diamond(ax, x, y, w, h, text, color="#FFF5F5", border="#E53E3E"):
            pts = [[x, y + h/2], [x + w/2, y], [x, y - h/2], [x - w/2, y]]
            poly = Polygon(pts, closed=True, facecolor=color, edgecolor=border, linewidth=1.5, zorder=3)
            ax.add_patch(poly)
            ax.text(x, y, text, ha='center', va='center', fontsize=8.5, fontweight='bold', color="#1A202C", zorder=4)

        def draw_arrow(ax, x1, y1, x2, y2, text=None, text_pos='right', color="#2D3748"):
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

        # Row 1
        draw_oval(ax, 1.8, 4.6, 2.0, 0.5, "Start: Ingest Specimen", color="#C6F6D5", border="#22543D")
        draw_arrow(ax, 2.8, 4.6, 3.8, 4.6)
        draw_parallelogram(ax, 5.0, 4.6, 2.4, 0.55, "Load Document Tensor\n(PDF / PNG / JPEG)", color="#FEFCBF", border="#B7791F")
        draw_arrow(ax, 6.2, 4.6, 7.2, 4.6)
        draw_rect(ax, 8.4, 4.6, 2.4, 0.55, "Resolution Normalization\n(300 DPI Grid Resize)", color="#FFFFFF", border="#4A5568")

        # Row 1 to Row 2 connection
        ax.plot([9.6, 10.9], [4.6, 4.6], color="#2D3748", linewidth=1.2, zorder=2)
        draw_arrow(ax, 10.9, 4.6, 10.9, 3.8)
        ax.plot([10.9, 10.9], [3.8, 3.1], color="#2D3748", linewidth=1.2, zorder=2)
        draw_arrow(ax, 10.9, 3.1, 9.6, 3.1)

        # Row 2
        draw_rect(ax, 8.4, 3.1, 2.4, 0.55, "Zero-Shot Prompt Inject\n(Academic Schema Target)", color="#FFFFFF", border="#4A5568")
        draw_arrow(ax, 7.2, 3.1, 6.2, 3.1)
        draw_predefined_process(ax, 5.0, 3.1, 2.4, 0.55, "MiniCPM-V 7.6B VLM\n(Local Ollama Engine)", color="#EBF8FF", border="#2B6CB0")
        draw_arrow(ax, 3.8, 3.1, 2.8, 3.1)
        draw_rect(ax, 1.8, 3.1, 2.0, 0.55, "Structured JSON\nParser & Validator", color="#FFFFFF", border="#4A5568")
        draw_arrow(ax, 1.8, 2.82, 1.8, 2.0)

        # Row 3
        draw_diamond(ax, 1.8, 1.6, 2.2, 0.8, "JSON Valid?", color="#ED8936", border="#C05621")
        draw_arrow(ax, 2.9, 1.6, 4.0, 1.6, "Yes (Valid)", text_pos='top')
        
        # Retry branch
        draw_arrow(ax, 1.8, 1.2, 1.8, 0.65, "No", text_pos='right')
        draw_rect(ax, 2.8, 0.65, 1.6, 0.4, "Schema Repair", color="#FED7D7", border="#E53E3E")
        ax.plot([1.8, 2.0], [0.65, 0.65], color="#E53E3E", linewidth=1.2)

        # Connect Schema Repair to End
        ax.plot([3.6, 10.9], [0.65, 0.65], color=arrow_color, linewidth=1.2, zorder=2)
        draw_arrow(ax, 10.9, 0.65, 10.9, 1.35, color=arrow_color)

        draw_predefined_process(ax, 5.2, 1.6, 2.4, 0.55, "6-Stage Semantic\nCanonicalNormalizer", color="#EBF8FF", border="#2B6CB0")
        draw_arrow(ax, 6.4, 1.6, 7.4, 1.6)
        draw_rect(ax, 8.5, 1.6, 2.2, 0.55, "9-Class Error Taxonomy\n& Statistical Scoring", color="#FFFFFF", border="#4A5568")
        draw_arrow(ax, 9.6, 1.6, 10.4, 1.6)
        draw_oval(ax, 10.9, 1.6, 1.0, 0.5, "End", color="#C6F6D5", border="#22543D")

        plt.tight_layout()
        tag = "red" if arrow_color == "#E53E3E" else "dark"
        plt.savefig(f"scratch/fig2_schema_{tag}.png", bbox_inches='tight', dpi=300)
        plt.close()
        print(f"Generated scratch/fig2_schema_{tag}.png")

test_colors()
