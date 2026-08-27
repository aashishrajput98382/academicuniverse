# Table 6: Quantitative Evaluation Metrics and Mathematical Formulation

| Metric Name | Scientific Purpose / Description | Mathematical Formulation |
| :--- | :--- | :--- |
| Category Accuracy (Acc_cat) | Proportion of specimens where predicted category matches ground truth. | Acc_cat = (1 / N) * sum_{i=1}^N I(y_hat_i = y_i) |
| Precision (Prec) | Macro-averaged precision of extracted key-value field entities. | Prec = TP / (TP + FP) |
| Recall (Rec) | Macro-averaged recall / true positive rate of target field entities. | Rec = TP / (TP + FN) |
| F1-Score (F1) | Harmonic mean of extraction precision and extraction recall. | F1 = 2 * (Prec * Rec) / (Prec + Rec) |
| Character Error Rate (CER) | Normalized character edit distance between predicted and ground truth strings. | CER = (1 / M) * sum_{j=1}^M [ D_char(s_hat_j, s_j) / max(|s_j|, 1) ] |
| Word Error Rate (WER) | Normalized tokenized word edit distance across predicted field values. | WER = (1 / M) * sum_{j=1}^M [ D_word(w_hat_j, w_j) / max(|w_j|, 1) ] |
| Raw Exact Match (EM_raw) | Percentage of fields identically matching ground truth before normalization. | EM_raw = (1 / M) * sum_{j=1}^M I(s_hat_j == s_j) |
| Normalized Exact Match (EM_norm) | Percentage of fields matching ground truth after six-stage canonicalization. | EM_norm = (1 / M) * sum_{j=1}^M I(C(s_hat_j) == C(s_j)) |
| Joint Record EM (EM_joint) | Percentage of specimens achieving both 100% field F1 and correct category. | EM_joint = (1 / N) * sum_{i=1}^N I(y_hat_i == y_i AND F1_i == 1.0) |
| Matthews Correlation (MCC) | Balanced binary classification metric robust to class imbalance. | MCC = (TP*TN - FP*FN) / sqrt((TP+FP)(TP+FN)(TN+FP)(TN+FN)) |
| Specificity / TNR | True negative rate / proportion of negative instances correctly identified. | Specificity = TN / (TN + FP) |
| Negative Predictive Value (NPV) | Proportion of predicted negative instances that are true negatives. | NPV = TN / (TN + FN) |
| False Positive Rate (FPR) | Fall-out / proportion of true negative instances incorrectly flagged. | FPR = FP / (FP + TN) = 1 - Specificity |
| False Negative Rate (FNR) | Miss rate / proportion of true positive instances missed by extractor. | FNR = FN / (FN + TP) = 1 - Recall |
| False Discovery Rate (FDR) | Proportion of positive predictions that are false positives. | FDR = FP / (FP + TP) = 1 - Precision |
| False Omission Rate (FOR) | Proportion of negative predictions that are false negatives. | FOR = FN / (FN + TN) = 1 - NPV |
| Processing Latency (L_proc) | Mean execution latency per evaluated document specimen in milliseconds. | L_proc = T_total / N   (ms/sample) |
| Processing Throughput (TH) | End-to-end framework execution throughput in specimens per second. | TH = N / T_total   (samples/sec) |