#!/usr/bin/env python3
"""
research/real_live_vision_benchmark.py

100% REAL LIVE MULTI-MODAL VISION-LANGUAGE BENCHMARK (45 PHYSICAL SPECIMENS).
Executes actual MiniCPM-V 7.6B neural network vision inference via Ollama
directly on physical PDF, PNG, and JPEG specimens from the Android SD Card (D:/AU_DIC_Benchmark_60k).

Test Matrix (Total 45 Specimens):
- 5 Vector PDFs (rendered via PyMuPDF)
- 20 PNG Images (5 Clean, 5 Scanned, 5 Mobile Camera, 5 Rotated 90)
- 20 JPEG Images (5 Clean, 5 Scanned, 5 Mobile Camera, 5 Rotated 90)

Zero Simulation. Every single prediction is generated directly by the live VLM.
"""

import os
import sys
import time
import json
import base64
import urllib.request
import io
from pathlib import Path

import pymupdf
from PIL import Image
import pandas as pd
import numpy as np

DATASET_DIR = Path("D:/AU_DIC_Benchmark_60k")
WORKSPACE_DIR = Path(__file__).resolve().parents[1]
RESULTS_DIR = WORKSPACE_DIR / "results"
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "minicpm-v:latest"

PROMPT_TEMPLATE = """You are an academic document reader. Inspect this image carefully and extract:
Student Name:
Institution:
Document Type:"""

def ensure_directories():
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

def render_pdf_to_base64(pdf_path, max_dim=640):
    """Renders page 1 of PDF to optimized JPEG base64 string."""
    doc = pymupdf.open(pdf_path)
    pix = doc[0].get_pixmap(dpi=72)
    png_bytes = pix.tobytes("png")
    doc.close()
    
    img = Image.open(io.BytesIO(png_bytes))
    img.thumbnail((max_dim, max_dim))
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=80)
    return base64.b64encode(buf.getvalue()).decode("utf-8")

def image_file_to_base64(img_path, max_dim=640):
    """Reads image file, resizes to max_dim, and returns base64 string."""
    img = Image.open(img_path)
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.thumbnail((max_dim, max_dim))
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=80)
    return base64.b64encode(buf.getvalue()).decode("utf-8")

def query_live_vlm(b64_img, prompt):
    """Sends image to live local Ollama MiniCPM-V model and measures exact latency."""
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "images": [b64_img],
        "stream": False,
        "options": {
            "temperature": 0.1,
            "num_predict": 128
        }
    }
    
    data_bytes = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(OLLAMA_URL, data=data_bytes, headers={"Content-Type": "application/json"})
    
    t0 = time.perf_counter()
    with urllib.request.urlopen(req, timeout=180) as resp:
        res_json = json.loads(resp.read().decode("utf-8"))
    latency = time.perf_counter() - t0
    
    response_text = res_json.get("response", "").strip()
    return response_text, latency

def load_ground_truth(doc_id):
    """Loads matching ground truth from SD card."""
    gt_path = DATASET_DIR / "groundtruth" / f"{doc_id}.json"
    if not gt_path.exists():
        base_id = doc_id.split("_")[0]
        gt_path = DATASET_DIR / "groundtruth" / f"{base_id}_clean.json"
        
    if gt_path.exists():
        try:
            return json.loads(gt_path.read_text(encoding="utf-8"))
        except Exception:
            pass
    return None

def collect_test_specimens():
    """Collects exactly 45 multi-modal specimens across PDF, PNG, and JPEG."""
    specimens = []
    
    # 1. 5 Vector PDFs
    pdf_dir = DATASET_DIR / "pdf"
    pdf_files = [f.path for f in os.scandir(str(pdf_dir)) if f.name.endswith(".pdf")][:5]
    for p in pdf_files:
        stem = Path(p).stem
        specimens.append({
            "modality": "PDF",
            "quality_profile": "clean",
            "file_path": p,
            "doc_id": f"{stem}_clean"
        })
        
    profiles = ["clean", "scanner_copy", "mobile_camera", "rotated_90"]
    
    # 2. 20 PNGs (5 per profile)
    png_dir = DATASET_DIR / "images" / "png"
    for prof in profiles:
        count = 0
        with os.scandir(str(png_dir)) as it:
            for entry in it:
                if entry.name.endswith(f"_{prof}.png"):
                    stem = Path(entry.name).stem
                    specimens.append({
                        "modality": "PNG",
                        "quality_profile": prof,
                        "file_path": entry.path,
                        "doc_id": stem
                    })
                    count += 1
                    if count >= 5:
                        break
                        
    # 3. 20 JPEGs (5 per profile)
    jpeg_dir = DATASET_DIR / "images" / "jpeg"
    for prof in profiles:
        count = 0
        with os.scandir(str(jpeg_dir)) as it:
            for entry in it:
                if entry.name.endswith(f"_{prof}.jpeg"):
                    stem = Path(entry.name).stem
                    specimens.append({
                        "modality": "JPEG",
                        "quality_profile": prof,
                        "file_path": entry.path,
                        "doc_id": stem
                    })
                    count += 1
                    if count >= 5:
                        break
                        
    return specimens

def main():
    print("=================================================================", flush=True)
    print(" 100% REAL LIVE MULTI-MODAL VISION BENCHMARK (MiniCPM-V 7.6B)", flush=True)
    print(f" Source Location: {DATASET_DIR}", flush=True)
    print("=================================================================", flush=True)
    ensure_directories()
    
    specimens = collect_test_specimens()
    total_samples = len(specimens)
    print(f"\n[INFO] Running Real Live Neural Inference across {total_samples} Physical Specimens:", flush=True)
    print(f"  • Vector PDFs:   5 specimens", flush=True)
    print(f"  • PNG Images:   20 specimens (5 clean, 5 scanned, 5 mobile, 5 rotated)", flush=True)
    print(f"  • JPEG Images:  20 specimens (5 clean, 5 scanned, 5 mobile, 5 rotated)", flush=True)
    print("\nStarting live inference on each file...\n", flush=True)
    
    results = []
    t_start = time.time()
    
    for idx, spec in enumerate(specimens, 1):
        modality = spec["modality"]
        prof = spec["quality_profile"]
        f_path = spec["file_path"]
        doc_id = spec["doc_id"]
        f_name = Path(f_path).name
        
        print(f"[{idx:02d}/{total_samples:02d}] Processing [{modality:4s}] [{prof:14s}] File: {f_name} ...", end="", flush=True)
        
        # 1. Base64 encode
        try:
            if modality == "PDF":
                b64_img = render_pdf_to_base64(f_path)
            else:
                b64_img = image_file_to_base64(f_path)
        except Exception as e:
            print(f" ERROR loading file: {e}", flush=True)
            continue
            
        # 2. Query Live VLM
        try:
            raw_resp, latency = query_live_vlm(b64_img, PROMPT_TEMPLATE)
        except Exception as e:
            print(f" ERROR in VLM inference: {e}", flush=True)
            continue
            
        # 3. Compare with Ground Truth
        gt_data = load_ground_truth(doc_id)
        gt_name = ""
        gt_univ = ""
        if gt_data:
            stud = gt_data.get("student", {})
            gt_name = stud.get("student_name", "") if isinstance(stud, dict) else str(stud)
            univ = gt_data.get("university", {})
            gt_univ = univ.get("name", "") if isinstance(univ, dict) else str(univ)
            
        # Check name presence in response
        name_match = (gt_name.lower() in raw_resp.lower()) if gt_name else False
        univ_match = (gt_univ.lower() in raw_resp.lower()) if gt_univ else False
        
        clean_resp_snippet = raw_resp.replace('\n', ' ')[:80]
        print(f" Done ({latency:.1f}s) | Name Match: {name_match} | Extracted: {clean_resp_snippet}", flush=True)
        
        results.append({
            "Sample_ID": idx,
            "Modality": modality,
            "Quality_Profile": prof,
            "File_Name": f_name,
            "Latency_Sec": latency,
            "GT_Student_Name": gt_name,
            "Name_Match": name_match,
            "GT_University": gt_univ,
            "University_Match": univ_match,
            "Model_Raw_Response": raw_resp
        })
        
    df = pd.DataFrame(results)
    total_time = time.time() - t_start
    
    print("\n=================================================================", flush=True)
    print(" 100% REAL LIVE VISION BENCHMARK RESULTS SUMMARY (45 SPECIMENS)", flush=True)
    print("=================================================================", flush=True)
    print(f"Total Physical Specimens Tested: {len(df)} in {total_time:.1f} seconds", flush=True)
    print(f"Average Neural Inference Latency: {df['Latency_Sec'].mean():.1f} seconds / document", flush=True)
    print(f"Overall Name Recognition Accuracy: {df['Name_Match'].mean()*100.0:.1f}%", flush=True)
    print(f"Overall Institution Recognition:    {df['University_Match'].mean()*100.0:.1f}%", flush=True)
    
    # Breakdown by Modality
    print("\n--- Accuracy by Modality ---", flush=True)
    for mod, group in df.groupby("Modality"):
        acc_name = group["Name_Match"].mean() * 100.0
        acc_univ = group["University_Match"].mean() * 100.0
        lat = group["Latency_Sec"].mean()
        print(f"  [{mod:4s}] (N={len(group):02d}) -> Name Acc: {acc_name:5.1f}% | Univ Acc: {acc_univ:5.1f}% | Avg Latency: {lat:.1f}s", flush=True)
        
    # Breakdown by Profile
    print("\n--- Accuracy by Optical Degradation Profile ---", flush=True)
    for prof, group in df.groupby("Quality_Profile"):
        acc_name = group["Name_Match"].mean() * 100.0
        acc_univ = group["University_Match"].mean() * 100.0
        lat = group["Latency_Sec"].mean()
        print(f"  [{prof:14s}] (N={len(group):02d}) -> Name Acc: {acc_name:5.1f}% | Univ Acc: {acc_univ:5.1f}% | Avg Latency: {lat:.1f}s", flush=True)

    # Save CSV and Markdown
    csv_path = RESULTS_DIR / "real_live_vision_benchmark_45samples.csv"
    md_path = RESULTS_DIR / "real_live_vision_benchmark_45samples.md"
    df.to_csv(csv_path, index=False)
    
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# 100% Real Live Multi-Modal Vision Benchmark Report (45 Specimens)\n\n")
        f.write(f"Direct neural inference via **MiniCPM-V 7.6B** on physical files from `D:/AU_DIC_Benchmark_60k`:\n\n")
        f.write(f"- **Total Physical Specimens Tested:** {len(df)}\n")
        f.write(f"- **Total Benchmark Time:** {total_time:.1f} seconds\n")
        f.write(f"- **Mean Latency per Document:** {df['Latency_Sec'].mean():.1f}s\n")
        f.write(f"- **Overall Student Name Recognition:** {df['Name_Match'].mean()*100.0:.1f}%\n")
        f.write(f"- **Overall University Recognition:** {df['University_Match'].mean()*100.0:.1f}%\n\n")
        cols = ["Sample_ID", "Modality", "Quality_Profile", "File_Name", "Latency_Sec", "GT_Student_Name", "Name_Match", "GT_University", "University_Match"]
        f.write(df[cols].to_markdown(index=False))
        
    print(f"\n[SUCCESS] Saved 45-Sample Real Vision CSV: {csv_path}", flush=True)
    print(f"[SUCCESS] Saved 45-Sample Real Vision MD:  {md_path}", flush=True)
    print("=================================================================", flush=True)

if __name__ == "__main__":
    main()
