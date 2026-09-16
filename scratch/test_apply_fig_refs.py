import docx
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

def test_fig_references(docx_path, out_path):
    doc = docx.Document(docx_path)

    # 1. Fig. 1 in P31 (above Fig. 1)
    p31 = doc.paragraphs[31]
    if 'Fig. 1' not in p31.text:
        # Append sentence referencing Fig. 1
        p31.runs[0].text = p31.text.rstrip() + ' The overarching multi-component system architecture of the framework is illustrated in Fig. 1.'

    # 2. Fig. 2 in P66 (above Fig. 2)
    p66 = doc.paragraphs[66]
    if 'Fig. 2' not in p66.text:
        p66.runs[0].text = (
            "Table 8 compares multiple document intelligence paradigms with the same 450 synthetic multi-modal document "
            "specimens (9,000 paired observations) tested using the same uniform testing conditions, and published document AI "
            "contextual reference scores for these documents. As illustrated in the end-to-end neural evaluation pipeline architecture "
            "of Fig. 2, live empirical execution confirms that the proposed AU DIC pipeline achieves State-of-the-Art performance "
            "on the academic credential benchmark (92.92% F1, 2.45% CER, 97.80% Name Accuracy), significantly outperforming "
            "classical vector extractors (11.11% F1) and raw vision-language foundation models (81.77% F1)."
        )

    # 3. Fig. 4 in P77 (below Fig. 4)
    p77 = doc.paragraphs[77]
    if 'Fig. 4' not in p77.text:
        p77.runs[0].text = (
            "Following the substantial error reductions observed in Fig. 3 and Fig. 4, the CanonicalNormalizer resolved "
            "1,004 false-negative field mismatches across specialized domain rules as reported in Table 10. Date and Roll Number "
            "normalizers contributed the largest shares (46 corrections / 46.46% and 30 corrections / 30.30% respectively), "
            "while Numeric rules resolved 23 errors (23.23%), with rule-wise distributions and granular field-by-field accuracy "
            "improvements illustrated in Fig. 5 and Fig. 6."
        )

    # 4. Fig. 6 in P85 (below Fig. 6)
    p85 = doc.paragraphs[85]
    if 'Fig. 6' not in p85.text:
        p85.runs[0].text = (
            "Following the field-level accuracy gains shown in Fig. 6, rigorous statistical hypothesis testing across paired "
            "specimen observations confirms that the empirical accuracy improvements achieved by the canonical normalizer are "
            "statistically significant at p < 0.0001, as summarized in Table 11, evaluated via McNemar's test [38] (chi2 = 1002.00), "
            "Wilcoxon signed-rank test [39] (W = 0.0), and Paired t-test (t = 41.21). Furthermore, non-parametric bootstrap resampling [40] "
            "across replications confirms that canonical normalization consistently elevates field-level F1 scores without inflating "
            "variance, with empirical benchmark metrics and 95% bootstrap confidence intervals reported in Table 12."
        )

    # 5. Fig. 7 and Fig. 8 above them
    # Find P92 (image of Fig. 7)
    p92 = doc.paragraphs[92]
    p_fig7_intro = p92.insert_paragraph_before(
        "The per-class confusion matrices evaluating Decision Tree classification fidelity across the 60:40, 70:30, and 80:20 train-test splits are depicted in Fig. 7."
    )
    p_fig7_intro.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_fig7_intro.paragraph_format.space_after = Pt(3.5)
    p_fig7_intro.paragraph_format.line_spacing = 1.0791666666666666
    r7 = p_fig7_intro.runs[0]
    r7.font.name = 'Times New Roman'
    r7.font.size = Pt(10.0)

    # Find Fig. 8 image
    # Note: since we inserted a paragraph before P92, indices shifted by 1
    # Let's locate the paragraph with Fig. 8 caption
    for idx, p in enumerate(doc.paragraphs):
        if 'Fig. 8.' in p.text:
            # The image of Fig. 8 is immediately before this caption
            p_fig8_img = doc.paragraphs[idx - 1]
            p_fig8_intro = p_fig8_img.insert_paragraph_before(
                "Complementarily, the multi-split confusion matrices for the Random Forest model are displayed in Fig. 8."
            )
            p_fig8_intro.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p_fig8_intro.paragraph_format.space_after = Pt(3.5)
            p_fig8_intro.paragraph_format.line_spacing = 1.0791666666666666
            r8 = p_fig8_intro.runs[0]
            r8.font.name = 'Times New Roman'
            r8.font.size = Pt(10.0)
            break

    doc.save(out_path)
    print(f'Test saved to {out_path}')

if __name__ == '__main__':
    test_fig_references('PaperV50.docx', 'scratch/test_fig_refs.docx')
