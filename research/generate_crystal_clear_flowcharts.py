#!/usr/bin/env python3
"""
research/generate_crystal_clear_flowcharts.py

Generates gorgeous, publication-ready, horizontal crystal-clear flowcharts:
- Fig 1: System Architecture Diagram (Production Subsystem + Benchmark Subsystem)
- Fig 2: Data Flow Diagram (DFD Levels 0, 1, 2)
- Fig 3: Option A End-to-End Neural Inference Pipeline
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib as mpl
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[1]
FIG_DIR = WORKSPACE / "docs" / "paper" / "extracted_figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']

def create_fig1():
    """Fig 1: System Architecture Diagram (Clean, Horizontal Layout)"""
    fig, ax = plt.subplots(figsize=(12, 6.5), dpi=300)
    ax.set_xlim(0, 120)
    ax.set_ylim(0, 65)
    ax.axis('off')
    
    # Title Box
    title_box = patches.FancyBboxPatch((2, 57), 116, 6, boxstyle="round,pad=0.5", ec="#1B365D", fc="#1B365D")
    ax.add_patch(title_box)
    ax.text(60, 60, "SMART ACADEMIC DOCUMENT INTELLIGENCE SYSTEM ARCHITECTURE", ha="center", va="center", color="white", fontsize=11, fontweight="bold")
    
    # Subsystem 1: Production System (Left Side, Blue Theme)
    sub1_bg = patches.FancyBboxPatch((3, 4), 54, 50, boxstyle="round,pad=0.8", ec="#2B6CB0", fc="#EBF8FF", lw=1.5)
    ax.add_patch(sub1_bg)
    ax.text(30, 51, "SUBSYSTEM 1: PRODUCTION INFERENCE & VERIFICATION", ha="center", va="center", color="#2B6CB0", fontsize=9.5, fontweight="bold")
    
    steps_s1 = [
        ("1. Multi-Format Ingestion", "(PDFs, PNGs, JPEGs, Scans)", 43),
        ("2. Document Category Classifier", "(Certificate / Marksheet / ID Card)", 34),
        ("3. Multimodal VLM Extractor", "(Zero-Shot MiniCPM-V 7.6B Engine)", 25),
        ("4. 6-Stage Semantic Normalizer", "(Dates, Roll Nos, Numeric, Aliases)", 16),
        ("5. Canonical Database & CGPA Engine", "(Multi-Semester Transcript Compilation)", 7)
    ]
    
    for title, sub, y in steps_s1:
        box = patches.FancyBboxPatch((6, y-3), 48, 6, boxstyle="round,pad=0.4", ec="#2B6CB0", fc="white", lw=1.0)
        ax.add_patch(box)
        ax.text(30, y+0.8, title, ha="center", va="center", color="#1A365D", fontsize=8.5, fontweight="bold")
        ax.text(30, y-1.4, sub, ha="center", va="center", color="#4A5568", fontsize=7.2)
        if y > 10:
            ax.annotate('', xy=(30, y-3.2), xytext=(30, y-4.8), arrowprops=dict(facecolor='#2B6CB0', edgecolor='#2B6CB0', width=1.5, headwidth=6, shrink=0.05))

    # Subsystem 2: Benchmark Generator (Right Side, Green Theme)
    sub2_bg = patches.FancyBboxPatch((63, 4), 54, 50, boxstyle="round,pad=0.8", ec="#2F855A", fc="#F0FFF4", lw=1.5)
    ax.add_patch(sub2_bg)
    ax.text(90, 51, "SUBSYSTEM 2: ADBG BENCHMARK & EVALUATION ENGINE", ha="center", va="center", color="#2F855A", fontsize=9.5, fontweight="bold")
    
    steps_s2 = [
        ("1. Seed-Deterministic Synthesis", "(PrngSeedGenerator, seed = 42)", 43),
        ("2. Typst Vector Engine & Ground-Truth", "(High-Res Vector PDFs + JSON Annotations)", 34),
        ("3. 14-Operator Degradation Matrix", "(Clean, Scanner, Mobile, 90° Rotated)", 25),
        ("4. Read-Only Benchmark Runner", "(Strict Read-Only Mode, Zero Data Mutation)", 16),
        ("5. 9-Class Taxonomy & Statistical Engine", "(Bootstrap CI, McNemar, Wilcoxon Tests)", 7)
    ]
    
    for title, sub, y in steps_s2:
        box = patches.FancyBboxPatch((66, y-3), 48, 6, boxstyle="round,pad=0.4", ec="#2F855A", fc="white", lw=1.0)
        ax.add_patch(box)
        ax.text(90, y+0.8, title, ha="center", va="center", color="#1C4532", fontsize=8.5, fontweight="bold")
        ax.text(90, y-1.4, sub, ha="center", va="center", color="#4A5568", fontsize=7.2)
        if y > 10:
            ax.annotate('', xy=(90, y-3.2), xytext=(90, y-4.8), arrowprops=dict(facecolor='#2F855A', edgecolor='#2F855A', width=1.5, headwidth=6, shrink=0.05))

    # Decoupled Isolation Channel
    ax.annotate('', xy=(62, 25), xytext=(58, 25), arrowprops=dict(facecolor='#C53030', edgecolor='#C53030', width=1.5, headwidth=6))
    ax.text(60, 29, "DECOUPLED READ-ONLY EVALUATION", ha="center", va="center", color="#C53030", fontsize=7.5, fontweight="bold", rotation=90)
    
    plt.tight_layout()
    out_path = FIG_DIR / "image1.png"
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[SUCCESS] Saved Fig 1 -> {out_path}")

def create_fig2():
    """Fig 2: Data Flow Diagram (DFD Levels 0, 1, 2 in Clean Horizontal Flow)"""
    fig, ax = plt.subplots(figsize=(12, 6.5), dpi=300)
    ax.set_xlim(0, 120)
    ax.set_ylim(0, 65)
    ax.axis('off')
    
    # Title Box
    title_box = patches.FancyBboxPatch((2, 57), 116, 6, boxstyle="round,pad=0.5", ec="#4C51BF", fc="#4C51BF")
    ax.add_patch(title_box)
    ax.text(60, 60, "DATA FLOW DIAGRAM: END-TO-END BENCHMARK & EXTRACTION FLOW", ha="center", va="center", color="white", fontsize=11, fontweight="bold")
    
    # Block 1: Input Data & Generation (Left)
    b1 = patches.FancyBboxPatch((4, 8), 24, 45, boxstyle="round,pad=0.6", ec="#D69E2E", fc="#FEFCBF", lw=1.2)
    ax.add_patch(b1)
    ax.text(16, 50, "1. SPECIMEN CREATION", ha="center", va="center", color="#744210", fontsize=8.5, fontweight="bold")
    
    steps_b1 = [("Prng Seed (42)", 42), ("Typst Compiler", 33), ("45 Physical Files", 24), ("Ground Truth JSON", 15)]
    for txt, y in steps_b1:
        box = patches.FancyBboxPatch((6, y-2.5), 20, 5, boxstyle="round,pad=0.3", ec="#B7791F", fc="white")
        ax.add_patch(box)
        ax.text(16, y, txt, ha="center", va="center", color="#2D3748", fontsize=7.5, fontweight="bold")
        if y > 16:
            ax.annotate('', xy=(16, y-2.7), xytext=(16, y-4.8), arrowprops=dict(arrowstyle="->", color="#B7791F", lw=1.2))

    # Block 2: Neural Inference Engine (Center-Left)
    b2 = patches.FancyBboxPatch((32, 8), 26, 45, boxstyle="round,pad=0.6", ec="#3182CE", fc="#EBF8FF", lw=1.2)
    ax.add_patch(b2)
    ax.text(45, 50, "2. ZERO-SHOT INFERENCE", ha="center", va="center", color="#2B6CB0", fontsize=8.5, fontweight="bold")
    
    steps_b2 = [("Image Tensor Pipeline", 42), ("MiniCPM-V (7.6B Q4_0)", 33), ("Structured JSON Parser", 24), ("Raw String Extractions", 15)]
    for txt, y in steps_b2:
        box = patches.FancyBboxPatch((34, y-2.5), 22, 5, boxstyle="round,pad=0.3", ec="#3182CE", fc="white")
        ax.add_patch(box)
        ax.text(45, y, txt, ha="center", va="center", color="#2D3748", fontsize=7.5, fontweight="bold")
        if y > 16:
            ax.annotate('', xy=(45, y-2.7), xytext=(45, y-4.8), arrowprops=dict(arrowstyle="->", color="#3182CE", lw=1.2))

    # Block 3: Canonical Normalization (Center-Right)
    b3 = patches.FancyBboxPatch((62, 8), 26, 45, boxstyle="round,pad=0.6", ec="#38A169", fc="#F0FFF4", lw=1.2)
    ax.add_patch(b3)
    ax.text(75, 50, "3. CANONICAL NORMALIZATION", ha="center", va="center", color="#276749", fontsize=8.5, fontweight="bold")
    
    steps_b3 = [("Date Normalizer (ISO)", 42), ("Roll No Normalizer", 33), ("Numeric Precision", 24), ("Degree / Univ Aliases", 15)]
    for txt, y in steps_b3:
        box = patches.FancyBboxPatch((64, y-2.5), 22, 5, boxstyle="round,pad=0.3", ec="#38A169", fc="white")
        ax.add_patch(box)
        ax.text(75, y, txt, ha="center", va="center", color="#2D3748", fontsize=7.5, fontweight="bold")
        if y > 16:
            ax.annotate('', xy=(75, y-2.7), xytext=(75, y-4.8), arrowprops=dict(arrowstyle="->", color="#38A169", lw=1.2))

    # Block 4: Multi-Metric Evaluation & Diagnostics (Right)
    b4 = patches.FancyBboxPatch((92, 8), 24, 45, boxstyle="round,pad=0.6", ec="#805AD5", fc="#FAF5FF", lw=1.2)
    ax.add_patch(b4)
    ax.text(104, 50, "4. EVALUATION & AUDIT", ha="center", va="center", color="#553C9A", fontsize=8.5, fontweight="bold")
    
    steps_b4 = [("Exact Match Scoring", 42), ("CER & WER Edit Distance", 33), ("9-Class Error Taxonomy", 24), ("Statistical Hypotheses", 15)]
    for txt, y in steps_b4:
        box = patches.FancyBboxPatch((94, y-2.5), 20, 5, boxstyle="round,pad=0.3", ec="#805AD5", fc="white")
        ax.add_patch(box)
        ax.text(104, y, txt, ha="center", va="center", color="#2D3748", fontsize=7.5, fontweight="bold")
        if y > 16:
            ax.annotate('', xy=(104, y-2.7), xytext=(104, y-4.8), arrowprops=dict(arrowstyle="->", color="#805AD5", lw=1.2))

    # Connecting Flow Arrows between Blocks
    ax.annotate('', xy=(32, 33), xytext=(28, 33), arrowprops=dict(facecolor='#2D3748', edgecolor='#2D3748', width=2.0, headwidth=7))
    ax.annotate('', xy=(62, 33), xytext=(58, 33), arrowprops=dict(facecolor='#2D3748', edgecolor='#2D3748', width=2.0, headwidth=7))
    ax.annotate('', xy=(92, 33), xytext=(88, 33), arrowprops=dict(facecolor='#2D3748', edgecolor='#2D3748', width=2.0, headwidth=7))

    plt.tight_layout()
    out_path = FIG_DIR / "image2.png"
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[SUCCESS] Saved Fig 2 -> {out_path}")

def create_fig3():
    """Fig 3: Option A End-to-End Neural Inference Pipeline"""
    fig, ax = plt.subplots(figsize=(12, 5.5), dpi=300)
    ax.set_xlim(0, 120)
    ax.set_ylim(0, 50)
    ax.axis('off')
    
    # Title Box
    title_box = patches.FancyBboxPatch((2, 42), 116, 6, boxstyle="round,pad=0.5", ec="#2D3748", fc="#2D3748")
    ax.add_patch(title_box)
    ax.text(60, 45, "OPTION A: END-TO-END ZERO-SHOT VLM INFERENCE PIPELINE", ha="center", va="center", color="white", fontsize=11, fontweight="bold")
    
    blocks = [
        ("1. Input Document Specimen", "(Vector PDF / PNG / JPEG Scan)", 14, "#3182CE", "#EBF8FF"),
        ("2. Vision-Language Encoder", "(MiniCPM-V 7.6B Q4_0 GGUF)", 45, "#DD6B20", "#FEEBC8"),
        ("3. JSON Structured Parser", "(Key-Value Extraction Schema)", 76, "#38A169", "#F0FFF4"),
        ("4. Canonical Normalizer", "(6-Stage Domain Standardization)", 107, "#805AD5", "#FAF5FF")
    ]
    
    for title, sub, x, ec, fc in blocks:
        box = patches.FancyBboxPatch((x-11, 10), 22, 26, boxstyle="round,pad=0.6", ec=ec, fc=fc, lw=1.5)
        ax.add_patch(box)
        ax.text(x, 26, title, ha="center", va="center", color=ec, fontsize=8.5, fontweight="bold")
        ax.text(x, 18, sub, ha="center", va="center", color="#4A5568", fontsize=7.5)
        
        if x < 100:
            ax.annotate('', xy=(x+13, 23), xytext=(x+11, 23), arrowprops=dict(facecolor='#2D3748', edgecolor='#2D3748', width=2.0, headwidth=7))
            
    plt.tight_layout()
    out_path = FIG_DIR / "image3.png"
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[SUCCESS] Saved Fig 3 -> {out_path}")

def main():
    print("=================================================================")
    print(" GENERATING CRYSTAL-CLEAR HORIZONTAL PUBLICATION FLOWCHARTS")
    print("=================================================================")
    create_fig1()
    create_fig2()
    create_fig3()
    print("=================================================================")
    print(" ALL 3 FLOWCHARTS GENERATED SUCCESSFULLY!")
    print("=================================================================")

if __name__ == "__main__":
    main()
