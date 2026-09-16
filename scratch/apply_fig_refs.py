import docx
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

def apply_all_figure_references(docx_path):
    doc = docx.Document(docx_path)

    # 1. Fig. 1 in P31 (above Fig. 1)
    p31 = doc.paragraphs[31]
    if 'Fig. 1' not in p31.text:
        p31.runs[0].text = p31.text.rstrip() + ' The overarching multi-component system architecture of the framework is illustrated in Fig. 1.'

    # 2. Fig. 2 in P66 (above Fig. 2)
    p66 = doc.paragraphs[66]
    p66.runs[0].text = (
        "Table 8 compares multiple document intelligence paradigms with the same 450 synthetic multi-modal document "
        "specimens (9,000 paired observations) tested using the same uniform testing conditions, and published document AI "
        "contextual reference scores for these documents. As illustrated in the end-to-end neural evaluation pipeline architecture "
        "of Fig. 2, live empirical execution confirms that the proposed AU DIC pipeline achieves State-of-the-Art performance "
        "on the academic credential benchmark (92.92% F1, 2.45% CER, 97.80% Name Accuracy), significantly outperforming "
        "classical vector extractors (11.11% F1) and raw vision-language foundation models (81.77% F1)."
    )

    # 3. Fig. 3: Insert introductory sentence before Fig. 3 image
    # Locate Fig. 3 caption
    p_fig3_cap = None
    for idx, p in enumerate(doc.paragraphs):
        if p.text.strip().startswith('Fig. 3.'):
            p_fig3_cap = p
            p_fig3_img = doc.paragraphs[idx - 1]
            break
    
    assert p_fig3_cap is not None, 'Fig. 3 caption not found!'
    p_fig3_intro = p_fig3_img.insert_paragraph_before(
        "The comparative field accuracy improvements attained across document categories following semantic canonical normalization are plotted in Fig. 3."
    )
    p_fig3_intro.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_fig3_intro.paragraph_format.space_after = Pt(3.5)
    p_fig3_intro.paragraph_format.line_spacing = 1.0791666666666666
    r3 = p_fig3_intro.runs[0]
    r3.font.name = 'Times New Roman'
    r3.font.size = Pt(10.0)

    # 4. Fig. 4: Insert introductory sentence before Fig. 4 image
    # Locate Fig. 4 caption
    p_fig4_cap = None
    for idx, p in enumerate(doc.paragraphs):
        if p.text.strip().startswith('Fig. 4.'):
            p_fig4_cap = p
            p_fig4_img = doc.paragraphs[idx - 1]
            break

    assert p_fig4_cap is not None, 'Fig. 4 caption not found!'
    p_fig4_intro = p_fig4_img.insert_paragraph_before(
        "The corresponding reductions in Character Error Rate (CER) and Word Error Rate (WER) resulting from canonical normalization are illustrated in Fig. 4."
    )
    p_fig4_intro.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_fig4_intro.paragraph_format.space_after = Pt(3.5)
    p_fig4_intro.paragraph_format.line_spacing = 1.0791666666666666
    r4 = p_fig4_intro.runs[0]
    r4.font.name = 'Times New Roman'
    r4.font.size = Pt(10.0)

    # Also update P77 (which shifts down by 2 paragraphs) to reference Fig. 4
    for idx, p in enumerate(doc.paragraphs):
        if 'The CanonicalNormalizer resolved 1,004 false-negative' in p.text:
            p.runs[0].text = (
                "Following the substantial error reductions observed in Fig. 3 and Fig. 4, the CanonicalNormalizer resolved "
                "1,004 false-negative field mismatches across specialized domain rules as reported in Table 10. Date and Roll Number "
                "normalizers contributed the largest shares (46 corrections / 46.46% and 30 corrections / 30.30% respectively), "
                "while Numeric rules resolved 23 errors (23.23%), with rule-wise distributions and granular field-by-field accuracy "
                "improvements illustrated in Fig. 5 and Fig. 6."
            )
            break

    # 5. Fig. 5: Update P79 (chart title before Fig. 5 image) into full descriptive sentence
    for idx, p in enumerate(doc.paragraphs):
        if 'False-Negative Field Mismatches Resolved by Domain Normalizer Rule' in p.text and not p.text.strip().startswith('Fig.'):
            p.runs[0].text = "The total number of false-negative field mismatches resolved by each individual domain normalizer rule is illustrated in Fig. 5."
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p.paragraph_format.space_after = Pt(3.5)
            p.paragraph_format.line_spacing = 1.0791666666666666
            for r in p.runs[1:]:
                r.text = ''
            p.runs[0].font.name = 'Times New Roman'
            p.runs[0].font.size = Pt(10.0)
            p.runs[0].bold = None
            break

    # 6. Fig. 6: Update P83 (chart title before Fig. 6 caption) into full descriptive sentence
    for idx, p in enumerate(doc.paragraphs):
        if 'Exact Match Recognition Accuracy (%)' in p.text:
            p.runs[0].text = "The field-by-field exact match recognition accuracy comparing raw extraction against canonical normalization is presented in Fig. 6."
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p.paragraph_format.space_after = Pt(3.5)
            p.paragraph_format.line_spacing = 1.0791666666666666
            for r in p.runs[1:]:
                r.text = ''
            p.runs[0].font.name = 'Times New Roman'
            p.runs[0].font.size = Pt(10.0)
            p.runs[0].bold = None
            break

    # Also update paragraph below Fig. 6 (Rigorous statistical hypothesis testing...)
    for idx, p in enumerate(doc.paragraphs):
        if 'Rigorous statistical hypothesis testing' in p.text:
            p.runs[0].text = (
                "Following the field-level accuracy gains shown in Fig. 6, rigorous statistical hypothesis testing across paired "
                "specimen observations confirms that the empirical accuracy improvements achieved by the canonical normalizer are "
                "statistically significant at p < 0.0001, as summarized in Table 11, evaluated via McNemar's test [38] (chi2 = 1002.00), "
                "Wilcoxon signed-rank test [39] (W = 0.0), and Paired t-test (t = 41.21). Furthermore, non-parametric bootstrap resampling [40] "
                "across replications confirms that canonical normalization consistently elevates field-level F1 scores without inflating "
                "variance, with empirical benchmark metrics and 95% bootstrap confidence intervals reported in Table 12."
            )
            break

    # 7. Fig. 7: Insert introductory sentence before Fig. 7 image
    p_fig7_cap = None
    for idx, p in enumerate(doc.paragraphs):
        if p.text.strip().startswith('Fig. 7.'):
            p_fig7_cap = p
            p_fig7_img = doc.paragraphs[idx - 1]
            break

    assert p_fig7_cap is not None, 'Fig. 7 caption not found!'
    p_fig7_intro = p_fig7_img.insert_paragraph_before(
        "The per-class confusion matrices evaluating Decision Tree classification fidelity across the 60:40, 70:30, and 80:20 train-test splits are depicted in Fig. 7."
    )
    p_fig7_intro.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_fig7_intro.paragraph_format.space_after = Pt(3.5)
    p_fig7_intro.paragraph_format.line_spacing = 1.0791666666666666
    r7 = p_fig7_intro.runs[0]
    r7.font.name = 'Times New Roman'
    r7.font.size = Pt(10.0)

    # 8. Fig. 8: Insert introductory sentence before Fig. 8 image
    p_fig8_cap = None
    for idx, p in enumerate(doc.paragraphs):
        if p.text.strip().startswith('Fig. 8.'):
            p_fig8_cap = p
            p_fig8_img = doc.paragraphs[idx - 1]
            break

    assert p_fig8_cap is not None, 'Fig. 8 caption not found!'
    p_fig8_intro = p_fig8_img.insert_paragraph_before(
        "Complementarily, the multi-split confusion matrices for the Random Forest model are displayed in Fig. 8, demonstrating consistent classification stability."
    )
    p_fig8_intro.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_fig8_intro.paragraph_format.space_after = Pt(3.5)
    p_fig8_intro.paragraph_format.line_spacing = 1.0791666666666666
    r8 = p_fig8_intro.runs[0]
    r8.font.name = 'Times New Roman'
    r8.font.size = Pt(10.0)

    doc.save(docx_path)
    print(f'Successfully applied all figure references to {docx_path}!')

if __name__ == '__main__':
    apply_all_figure_references('PaperV50.docx')
