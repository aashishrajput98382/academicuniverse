import matplotlib.pyplot as plt
import matplotlib.patches as patches
from pathlib import Path

# Create high-resolution figure (12 x 7 inches at 300 DPI = 3600 x 2100 px)
fig, ax = plt.subplots(figsize=(13, 7.5), dpi=300)
ax.set_xlim(0, 13)
ax.set_ylim(0, 7.5)
ax.axis('off')

# Color palette (modern, professional academic palette)
c_bg = '#F8FAFC'
c_card_bg = '#FFFFFF'
c_blue = '#1E40AF'
c_blue_light = '#EFF6FF'
c_indigo = '#4338CA'
c_purple = '#6D28D9'
c_purple_light = '#F5F3FF'
c_emerald = '#047857'
c_emerald_light = '#ECFDF5'
c_amber = '#B45309'
c_amber_light = '#FFFBEB'
c_border = '#CBD5E1'
c_text_dark = '#0F172A'
c_text_muted = '#475569'

fig.patch.set_facecolor(c_bg)
ax.set_facecolor(c_bg)

# Main Title Header Box
rect_title = patches.FancyBboxPatch((0.5, 6.7), 12.0, 0.65, boxstyle="round,pad=0.08,rounding_size=0.15",
                                    facecolor=c_blue, edgecolor=c_blue, linewidth=1.5)
ax.add_patch(rect_title)
ax.text(6.5, 7.02, "SMART ACADEMIC DOCUMENT INTELLIGENCE & BENCHMARKING SYSTEM",
        ha='center', va='center', fontsize=12, fontweight='bold', color='white', fontfamily='sans-serif')

# -------------------------------------------------------------
# LANE 1: PRODUCTION HUMAN-IN-THE-LOOP DOCUMENT PIPELINE
# -------------------------------------------------------------
# Lane 1 Container
rect_lane1 = patches.FancyBboxPatch((0.5, 3.8), 12.0, 2.7, boxstyle="round,pad=0.1,rounding_size=0.2",
                                    facecolor=c_card_bg, edgecolor='#93C5FD', linewidth=1.5)
ax.add_patch(rect_lane1)

# Lane 1 Title Tag
rect_tag1 = patches.FancyBboxPatch((0.7, 6.15), 4.6, 0.32, boxstyle="round,pad=0.05,rounding_size=0.08",
                                   facecolor=c_blue_light, edgecolor='#3B82F6', linewidth=1)
ax.add_patch(rect_tag1)
ax.text(3.0, 6.31, "SUBSYSTEM I: PRODUCTION HUMAN-IN-THE-LOOP PIPELINE",
        ha='center', va='center', fontsize=8.5, fontweight='bold', color=c_blue, fontfamily='sans-serif')

# Step 1: Ingestion
b1 = patches.FancyBboxPatch((0.7, 4.05), 1.9, 1.9, boxstyle="round,pad=0.08,rounding_size=0.12",
                            facecolor='#F1F5F9', edgecolor=c_border, linewidth=1.2)
ax.add_patch(b1)
ax.text(1.65, 5.7, "1. Ingestion", ha='center', va='center', fontsize=9.5, fontweight='bold', color=c_text_dark)
ax.text(1.65, 5.0, "• Mobile Photos\n• Flatbed Scans\n• Student PDFs\n• Degrees & IDs", ha='center', va='center', fontsize=8, color=c_text_muted)

# Arrow 1->2
ax.annotate('', xy=(2.9, 5.0), xytext=(2.6, 5.0), arrowprops=dict(arrowstyle="-|>", color='#3B82F6', lw=2, mutation_scale=15))

# Step 2: Classifier & VLM
b2 = patches.FancyBboxPatch((3.0, 4.05), 2.1, 1.9, boxstyle="round,pad=0.08,rounding_size=0.12",
                            facecolor='#EFF6FF', edgecolor='#60A5FA', linewidth=1.2)
ax.add_patch(b2)
ax.text(4.05, 5.7, "2. Neural AI Parsing", ha='center', va='center', fontsize=9.5, fontweight='bold', color=c_blue)
ax.text(4.05, 5.0, "• Category Classifier\n  (98%+ Confidence)\n• MiniCPM-V 7.6B\n• Zero-Shot JSON", ha='center', va='center', fontsize=8, color=c_text_muted)

# Arrow 2->3
ax.annotate('', xy=(5.4, 5.0), xytext=(5.1, 5.0), arrowprops=dict(arrowstyle="-|>", color='#3B82F6', lw=2, mutation_scale=15))

# Step 3: Normalizer
b3 = patches.FancyBboxPatch((5.5, 4.05), 2.1, 1.9, boxstyle="round,pad=0.08,rounding_size=0.12",
                            facecolor='#F5F3FF', edgecolor='#A78BFA', linewidth=1.2)
ax.add_patch(b3)
ax.text(6.55, 5.7, "3. 6-Stage Normalizer", ha='center', va='center', fontsize=9.5, fontweight='bold', color=c_purple)
ax.text(6.55, 5.0, "• ISO Date Cleaner\n• Roll No Standardizer\n• Float Normalizer\n• Alias Canonicalizer", ha='center', va='center', fontsize=8, color=c_text_muted)

# Arrow 3->4
ax.annotate('', xy=(7.9, 5.0), xytext=(7.6, 5.0), arrowprops=dict(arrowstyle="-|>", color='#3B82F6', lw=2, mutation_scale=15))

# Step 4: Human-in-the-Loop UI
b4 = patches.FancyBboxPatch((8.0, 4.05), 2.1, 1.9, boxstyle="round,pad=0.08,rounding_size=0.12",
                            facecolor='#FFFBEB', edgecolor='#FCD34D', linewidth=1.2)
ax.add_patch(b4)
ax.text(9.05, 5.7, "4. Verification UI", ha='center', va='center', fontsize=9.5, fontweight='bold', color=c_amber)
ax.text(9.05, 5.0, "• Live Entity Review\n• Editable Grid\n• Human Oversight\n• 1-Click Approval", ha='center', va='center', fontsize=8, color=c_text_muted)

# Arrow 4->5
ax.annotate('', xy=(10.4, 5.0), xytext=(10.1, 5.0), arrowprops=dict(arrowstyle="-|>", color='#3B82F6', lw=2, mutation_scale=15))

# Step 5: Canonical Records
b5 = patches.FancyBboxPatch((10.5, 4.05), 1.8, 1.9, boxstyle="round,pad=0.08,rounding_size=0.12",
                            facecolor='#ECFDF5', edgecolor='#34D399', linewidth=1.2)
ax.add_patch(b5)
ax.text(11.4, 5.7, "5. Transcript & DB", ha='center', va='center', fontsize=9.5, fontweight='bold', color=c_emerald)
ax.text(11.4, 5.0, "• Canonical DB Sync\n• Live Transcripts\n• CGPA Calculation\n• ERP Integration", ha='center', va='center', fontsize=8, color=c_text_muted)

# -------------------------------------------------------------
# LANE 2: ADBG V1.0 SYNTHETIC BENCHMARK & EVALUATION ENGINE
# -------------------------------------------------------------
rect_lane2 = patches.FancyBboxPatch((0.5, 0.4), 12.0, 3.1, boxstyle="round,pad=0.1,rounding_size=0.2",
                                    facecolor=c_card_bg, edgecolor='#C084FC', linewidth=1.5)
ax.add_patch(rect_lane2)

rect_tag2 = patches.FancyBboxPatch((0.7, 3.15), 4.8, 0.32, boxstyle="round,pad=0.05,rounding_size=0.08",
                                   facecolor=c_purple_light, edgecolor='#9333EA', linewidth=1)
ax.add_patch(rect_tag2)
ax.text(3.1, 3.31, "SUBSYSTEM II: ADBG v1.0 SYNTHETIC BENCHMARK & EVALUATION",
        ha='center', va='center', fontsize=8.5, fontweight='bold', color=c_purple, fontfamily='sans-serif')

# Step B1: Generator
b_g1 = patches.FancyBboxPatch((0.7, 0.65), 2.5, 2.3, boxstyle="round,pad=0.08,rounding_size=0.12",
                              facecolor='#F8FAFC', edgecolor=c_border, linewidth=1.2)
ax.add_patch(b_g1)
ax.text(1.95, 2.65, "ADBG Generator (v1.0)", ha='center', va='center', fontsize=9.5, fontweight='bold', color=c_text_dark)
ax.text(1.95, 1.65, "• Master Seed = 42\n• 360 Vector Documents\n• Typst Compilation\n• Exact Ground-Truth JSON\n• 0% Real Student PII Leak", ha='center', va='center', fontsize=8, color=c_text_muted)

# Arrow B1->B2
ax.annotate('', xy=(3.5, 1.8), xytext=(3.2, 1.8), arrowprops=dict(arrowstyle="-|>", color='#9333EA', lw=2, mutation_scale=15))

# Step B2: Degradation
b_g2 = patches.FancyBboxPatch((3.6, 0.65), 2.6, 2.3, boxstyle="round,pad=0.08,rounding_size=0.12",
                              facecolor='#FFF7ED', edgecolor='#FDBA74', linewidth=1.2)
ax.add_patch(b_g2)
ax.text(4.9, 2.65, "Optical Degradation Suite", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#C2410C')
ax.text(4.9, 1.65, "• 14 Physical Operators\n• 4 Standard Quality Profiles:\n   - Clean Vector (0.0)\n   - Scanner Noise (1.0)\n   - Mobile Capture (2.5)\n   - 90° Rotation (4.0)", ha='center', va='center', fontsize=8, color=c_text_muted)

# Arrow B2->B3
ax.annotate('', xy=(6.5, 1.8), xytext=(6.2, 1.8), arrowprops=dict(arrowstyle="-|>", color='#9333EA', lw=2, mutation_scale=15))

# Step B3: Error Taxonomy & Statistical Testing
b_g3 = patches.FancyBboxPatch((6.6, 0.65), 2.7, 2.3, boxstyle="round,pad=0.08,rounding_size=0.12",
                              facecolor='#F5F3FF', edgecolor='#C084FC', linewidth=1.2)
ax.add_patch(b_g3)
ax.text(7.95, 2.65, "9-Class Error Taxonomy", ha='center', va='center', fontsize=9.5, fontweight='bold', color=c_purple)
ax.text(7.95, 1.65, "• ErrorTaxonomist Engine\n• 5,760 Core Metadata Evals\n• 2,620 Format Discrepancies\n  Isolated & Resolved\n• 260 Genuine OCR Errors", ha='center', va='center', fontsize=8, color=c_text_muted)

# Arrow B3->B4
ax.annotate('', xy=(9.6, 1.8), xytext=(9.3, 1.8), arrowprops=dict(arrowstyle="-|>", color='#9333EA', lw=2, mutation_scale=15))

# Step B4: Statistical Rigor
b_g4 = patches.FancyBboxPatch((9.7, 0.65), 2.6, 2.3, boxstyle="round,pad=0.08,rounding_size=0.12",
                              facecolor='#ECFDF5', edgecolor='#6EE7B7', linewidth=1.2)
ax.add_patch(b_g4)
ax.text(11.0, 2.65, "Statistical Verification", ha='center', va='center', fontsize=9.5, fontweight='bold', color=c_emerald)
ax.text(11.0, 1.65, "• McNemar χ² = 2618.00\n• Wilcoxon p < 0.0001\n• 10,000 Bootstrap CIs\n• Decision Tree MCC: 0.8303\n• F1: 50.00% -> 95.49%", ha='center', va='center', fontsize=8, color=c_text_muted)

# Connect Lanes (Cross-Coupling Arrow)
ax.annotate('Canonical Normalizer\nRule Sharing', xy=(6.55, 3.8), xytext=(6.55, 3.1),
            ha='center', va='center', fontsize=7.5, fontweight='bold', color=c_indigo,
            arrowprops=dict(arrowstyle="<|-|>", color=c_indigo, lw=1.5, ls='--'))

plt.tight_layout()
out_fig1 = Path('docs/paper/figure1_system_architecture.png')
plt.savefig(out_fig1, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight')
plt.close()

print(f"[SUCCESS] Generated high-DPI publication architecture diagram at {out_fig1}")
