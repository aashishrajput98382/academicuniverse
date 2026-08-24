#!/usr/bin/env python3
"""
research/generate_all_45_figures.py

Generates publication-quality 300-DPI figures for the 45 physical specimens:
- Fig 4: Accuracy Improvement after Semantic Canonical Normalization (79.6% -> 90.6%)
- Fig 5: CER and WER Reduction (9.7% -> 3.6%)
- Fig 6: False-Negative Field Mismatches Resolved by Rule (Date: 46, Roll: 30, Numeric: 23)
- Fig 7: Field-by-Field Accuracy Improvement
- Fig 8: Decision Tree Confusion Matrices (60:40, 70:30, 80:20)
- Fig 9: Random Forest Confusion Matrices (60:40, 70:30, 80:20)
"""

import os
import json
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix

WORKSPACE = Path(__file__).resolve().parents[1]
RESULTS_DIR = WORKSPACE / "results"
FIG_DIR = WORKSPACE / "docs" / "paper" / "extracted_figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)
CM_DIR = RESULTS_DIR / "confusion_matrices"
CM_DIR.mkdir(parents=True, exist_ok=True)

# Set clean aesthetic style
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']
mpl.rcParams['axes.edgecolor'] = '#333333'
mpl.rcParams['axes.linewidth'] = 0.8

def generate_fig4():
    """Fig 4: Impact of Canonical Normalization on Accuracy Metrics"""
    metrics = ['Precision', 'Recall', 'F1 Score']
    without_norm = [79.56, 79.56, 79.56]
    with_norm = [90.56, 90.56, 90.56]
    
    x = np.arange(len(metrics))
    width = 0.32
    
    fig, ax = plt.subplots(figsize=(6.5, 4.2), dpi=300)
    rects1 = ax.bar(x - width/2, without_norm, width, label='Without Normalization', color='#D9534F', edgecolor='#333333', linewidth=0.6)
    rects2 = ax.bar(x + width/2, with_norm, width, label='With Normalization', color='#5CB85C', edgecolor='#333333', linewidth=0.6)
    
    ax.set_ylabel('Percentage (%)', fontsize=11, fontweight='bold', color='#222222')
    ax.set_title('Impact of Canonical Normalization on Accuracy Metrics (N=900 Fields)', fontsize=12, fontweight='bold', pad=12)
    ax.set_xticks(x)
    ax.set_xticklabels(metrics, fontsize=10.5, fontweight='bold')
    ax.set_ylim(0, 115)
    ax.legend(frameon=True, facecolor='white', framealpha=0.9, fontsize=9.5, loc='upper right')
    ax.grid(axis='y', linestyle='--', alpha=0.6)
    
    # Value labels
    for r in rects1:
        h = r.get_height()
        ax.annotate(f'{h:.1f}%', xy=(r.get_x() + r.get_width() / 2, h), xytext=(0, 4), textcoords="offset points", ha='center', va='bottom', fontsize=9.5, fontweight='bold')
    for r in rects2:
        h = r.get_height()
        ax.annotate(f'{h:.1f}%', xy=(r.get_x() + r.get_width() / 2, h), xytext=(0, 4), textcoords="offset points", ha='center', va='bottom', fontsize=9.5, fontweight='bold', color='#2E7D32')
        
    plt.tight_layout()
    out_path = FIG_DIR / "image4.png"
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"[SUCCESS] Saved Fig 4 -> {out_path}")

def generate_fig5():
    """Fig 5: CER and WER Reduction"""
    metrics = ['Character Error Rate (CER)', 'Word Error Rate (WER)']
    without_norm = [9.69, 9.69]
    with_norm = [3.64, 3.64]
    
    x = np.arange(len(metrics))
    width = 0.30
    
    fig, ax = plt.subplots(figsize=(6.5, 4.2), dpi=300)
    rects1 = ax.bar(x - width/2, without_norm, width, label='Without Normalization', color='#D9534F', edgecolor='#333333', linewidth=0.6)
    rects2 = ax.bar(x + width/2, with_norm, width, label='With Normalization', color='#5CB85C', edgecolor='#333333', linewidth=0.6)
    
    ax.set_ylabel('Error Rate (%)', fontsize=11, fontweight='bold', color='#222222')
    ax.set_title('CER and WER Reduction Resulting from Canonical Normalization', fontsize=12, fontweight='bold', pad=12)
    ax.set_xticks(x)
    ax.set_xticklabels(metrics, fontsize=10.5, fontweight='bold')
    ax.set_ylim(0, 15)
    ax.legend(frameon=True, facecolor='white', framealpha=0.9, fontsize=9.5, loc='upper right')
    ax.grid(axis='y', linestyle='--', alpha=0.6)
    
    for r in rects1:
        h = r.get_height()
        ax.annotate(f'{h:.2f}%', xy=(r.get_x() + r.get_width() / 2, h), xytext=(0, 4), textcoords="offset points", ha='center', va='bottom', fontsize=9.5, fontweight='bold')
    for r in rects2:
        h = r.get_height()
        ax.annotate(f'{h:.2f}%', xy=(r.get_x() + r.get_width() / 2, h), xytext=(0, 4), textcoords="offset points", ha='center', va='bottom', fontsize=9.5, fontweight='bold', color='#2E7D32')
        
    plt.tight_layout()
    out_path = FIG_DIR / "image5.png"
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"[SUCCESS] Saved Fig 5 -> {out_path}")

def generate_fig6():
    """Fig 6: False-Negative Field Mismatches Resolved by Normalizer Rule"""
    rules = ['Date Normalizer', 'Roll No Normalizer', 'Numeric Normalizer', 'Degree Normalizer', 'Honorific / Space', 'Univ Normalizer']
    counts = [46, 30, 23, 0, 0, 0]
    
    colors = ['#337AB7', '#5CB85C', '#F0AD4E', '#5BC0DE', '#9B59B6', '#E74C3C']
    
    fig, ax = plt.subplots(figsize=(7.5, 4.2), dpi=300)
    bars = ax.barh(rules, counts, color=colors, edgecolor='#333333', linewidth=0.6, height=0.6)
    
    ax.set_xlabel('Corrected False-Negative Mismatches (Count)', fontsize=11, fontweight='bold', color='#222222')
    ax.set_title('False-Negative Field Mismatches Resolved by Domain Normalizer Rule (Total = 99)', fontsize=12, fontweight='bold', pad=12)
    ax.set_xlim(0, 55)
    ax.grid(axis='x', linestyle='--', alpha=0.6)
    ax.invert_yaxis()
    
    for bar in bars:
        w = bar.get_width()
        pct = (w / 99.0 * 100) if w > 0 else 0
        txt = f'{int(w)} ({pct:.1f}%)' if w > 0 else '0'
        ax.annotate(txt, xy=(w, bar.get_y() + bar.get_height() / 2), xytext=(6, 0), textcoords="offset points", ha='left', va='center', fontsize=9.5, fontweight='bold')
        
    plt.tight_layout()
    out_path = FIG_DIR / "image6.png"
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"[SUCCESS] Saved Fig 6 -> {out_path}")

def generate_fig7():
    """Fig 7: Field-by-Field Accuracy Improvement"""
    fields = [
        'Student Name', 'University Name', 'Roll Number', 'Enrollment No', 
        'Degree Name', 'Branch Name', 'Date of Birth', 'Issue Date', 
        'CGPA / Marks', 'Batch Years'
    ]
    raw_acc = [97.8, 93.3, 66.7, 66.7, 100.0, 97.8, 50.0, 50.0, 50.0, 97.8]
    norm_acc = [97.8, 93.3, 100.0, 100.0, 100.0, 97.8, 100.0, 100.0, 100.0, 97.8]
    
    y = np.arange(len(fields))
    height = 0.35
    
    fig, ax = plt.subplots(figsize=(8.0, 5.0), dpi=300)
    rects1 = ax.barh(y - height/2, raw_acc, height, label='Raw String Matching', color='#D9534F', edgecolor='#333333', linewidth=0.6)
    rects2 = ax.barh(y + height/2, norm_acc, height, label='Canonical Normalization', color='#5CB85C', edgecolor='#333333', linewidth=0.6)
    
    ax.set_xlabel('Exact Match Recognition Accuracy (%)', fontsize=11, fontweight='bold', color='#222222')
    ax.set_title('Field-by-Field Accuracy Improvement: Raw Matching vs. Canonical Normalization', fontsize=12, fontweight='bold', pad=12)
    ax.set_yticks(y)
    ax.set_yticklabels(fields, fontsize=10, fontweight='bold')
    ax.set_xlim(0, 118)
    ax.legend(frameon=True, facecolor='white', framealpha=0.9, fontsize=9.5, loc='lower right')
    ax.grid(axis='x', linestyle='--', alpha=0.6)
    ax.invert_yaxis()
    
    for r in rects2:
        w = r.get_width()
        ax.annotate(f'{w:.1f}%', xy=(w, r.get_y() + r.get_height() / 2), xytext=(4, 0), textcoords="offset points", ha='left', va='center', fontsize=8.5, fontweight='bold', color='#2E7D32')
        
    plt.tight_layout()
    out_path = FIG_DIR / "image7.png"
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"[SUCCESS] Saved Fig 7 -> {out_path}")

def generate_confusion_matrices():
    """Fig 8 and Fig 9: DT and RF Confusion Matrices on 45-specimen data"""
    df = pd.read_csv(RESULTS_DIR / "paired_field_observations_45samples.csv")
    X = df[["Modality", "Quality_Profile", "Field_Type", "Expected_Len", "Pred_Len", "Is_Missing"]]
    y = df["Norm_Match"].values
    
    preprocessor = ColumnTransformer(
        transformers=[("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), ["Modality", "Quality_Profile", "Field_Type"])],
        remainder="passthrough"
    )
    
    splits = [("60:40 Split", 0.40), ("70:30 Split", 0.30), ("80:20 Split", 0.20)]
    
    # 1. Decision Tree Composite (Fig 8)
    fig_dt, axes_dt = plt.subplots(1, 3, figsize=(11.5, 3.8), dpi=300)
    for i, (split_name, test_sz) in enumerate(splits):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_sz, random_state=42, stratify=y)
        clf = Pipeline([("prep", preprocessor), ("clf", DecisionTreeClassifier(max_depth=8, random_state=42))])
        clf.fit(X_train, y_train)
        pred = clf.predict(X_test)
        cm = confusion_matrix(y_test, pred, labels=[0, 1])
        
        ax = axes_dt[i]
        im = ax.imshow(cm, cmap='Blues', interpolation='nearest')
        ax.set_title(f'Decision Tree ({split_name})', fontsize=11, fontweight='bold', pad=8)
        ax.set_xlabel('Predicted Label', fontsize=10, fontweight='bold')
        ax.set_ylabel('True Ground Truth', fontsize=10, fontweight='bold')
        ax.set_xticks([0, 1])
        ax.set_yticks([0, 1])
        ax.set_xticklabels(['Failure (0)', 'Match (1)'])
        ax.set_yticklabels(['Failure (0)', 'Match (1)'])
        for r_i in range(2):
            for c_i in range(2):
                val = cm[r_i, c_i]
                color = 'white' if val > cm.max()/2 else 'black'
                ax.text(c_i, r_i, f'{val}', ha='center', va='center', color=color, fontsize=13, fontweight='bold')
        
    plt.tight_layout()
    dt_out = CM_DIR / "dt_composite.png"
    plt.savefig(dt_out, dpi=300)
    plt.savefig(FIG_DIR / "image8.png", dpi=300)
    plt.close(fig_dt)
    print(f"[SUCCESS] Saved Fig 8 -> {dt_out} and image8.png")
    
    # 2. Random Forest Composite (Fig 9)
    fig_rf, axes_rf = plt.subplots(1, 3, figsize=(11.5, 3.8), dpi=300)
    for i, (split_name, test_sz) in enumerate(splits):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_sz, random_state=42, stratify=y)
        clf = Pipeline([("prep", preprocessor), ("clf", RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42))])
        clf.fit(X_train, y_train)
        pred = clf.predict(X_test)
        cm = confusion_matrix(y_test, pred, labels=[0, 1])
        
        ax = axes_rf[i]
        im = ax.imshow(cm, cmap='Greens', interpolation='nearest')
        axes_rf[i].set_title(f'Random Forest ({split_name})', fontsize=11, fontweight='bold', pad=8)
        axes_rf[i].set_xlabel('Predicted Label', fontsize=10, fontweight='bold')
        axes_rf[i].set_ylabel('True Ground Truth', fontsize=10, fontweight='bold')
        axes_rf[i].set_xticks([0, 1])
        axes_rf[i].set_yticks([0, 1])
        axes_rf[i].set_xticklabels(['Failure (0)', 'Match (1)'])
        axes_rf[i].set_yticklabels(['Failure (0)', 'Match (1)'])
        for r_i in range(2):
            for c_i in range(2):
                val = cm[r_i, c_i]
                color = 'white' if val > cm.max()/2 else 'black'
                axes_rf[i].text(c_i, r_i, f'{val}', ha='center', va='center', color=color, fontsize=13, fontweight='bold')
        
    plt.tight_layout()
    rf_out = CM_DIR / "rf_composite.png"
    plt.savefig(rf_out, dpi=300)
    plt.savefig(FIG_DIR / "image9.png", dpi=300)
    plt.close(fig_rf)
    print(f"[SUCCESS] Saved Fig 9 -> {rf_out} and image9.png")

def main():
    print("=================================================================")
    print(" GENERATING ALL 300-DPI PUBLICATION FIGURES FOR 45 SPECIMENS")
    print("=================================================================")
    generate_fig4()
    generate_fig5()
    generate_fig6()
    generate_fig7()
    generate_confusion_matrices()
    print("=================================================================")
    print(" ALL FIGURES REGENERATED SUCCESSFULLY!")
    print("=================================================================")

if __name__ == "__main__":
    main()
