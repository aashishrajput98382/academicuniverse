import pandas as pd

df = pd.read_csv('backend/benchmark_reports/run_450_live_gpu_1787773778444/paired_field_observations.csv')
print("Total Paired Field Observations:", len(df))
print("\n================== OVERALL METRICS ==================")
print(f"Pass A (Raw Unnormalized): Exact Match / Precision = {df['Raw_Match'].mean()*100:.2f}% | CER = {df['CER_A'].mean()*100:.2f}% | WER = {df['WER_A'].mean()*100:.2f}%")
print(f"Pass B (Canonical Normal):  Exact Match / Precision = {df['Norm_Match'].mean()*100:.2f}% | CER = {df['CER_B'].mean()*100:.2f}% | WER = {df['WER_B'].mean()*100:.2f}%")
print(f"Net Canonical Gain:         +{ (df['Norm_Match'].mean() - df['Raw_Match'].mean())*100:.2f}% (+{ ((df['Norm_Match'].mean() - df['Raw_Match'].mean()) / df['Raw_Match'].mean())*100:.2f}% relative)")

print("\n================== BY FIELD CATEGORY ==================")
for f_type, group in df.groupby('Field_Type'):
    acc_a = group['Raw_Match'].mean() * 100
    acc_b = group['Norm_Match'].mean() * 100
    gain = acc_b - acc_a
    print(f"  {f_type:20s} (N={len(group)}) -> Pass A: {acc_a:5.1f}% | Pass B: {acc_b:5.1f}% | Gain: +{gain:4.1f}%")

print("\n================== BY MODALITY ==================")
for mod, group in df.groupby('Modality'):
    acc_a = group['Raw_Match'].mean() * 100
    acc_b = group['Norm_Match'].mean() * 100
    print(f"  {mod:10s} (N={len(group)}) -> Pass A: {acc_a:5.1f}% | Pass B: {acc_b:5.1f}%")

print("\n================== BY OPTICAL DEGRADATION ==================")
for prof, group in df.groupby('Quality_Profile'):
    acc_a = group['Raw_Match'].mean() * 100
    acc_b = group['Norm_Match'].mean() * 100
    print(f"  {prof:15s} (N={len(group)}) -> Pass A: {acc_a:5.1f}% | Pass B: {acc_b:5.1f}%")
