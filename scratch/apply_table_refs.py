import docx
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

def update_table_references(docx_path, output_path):
    doc = docx.Document(docx_path)

    # 1. Update P43 (immediately above Table 4)
    p43 = doc.paragraphs[43]
    p43.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p43.paragraph_format.space_after = Pt(3.5)
    if len(p43.runs) == 0:
        r43 = p43.add_run()
    else:
        r43 = p43.runs[0]
        for r in p43.runs[1:]:
            r.text = ''
    r43.text = 'The specific transformation operators, parameter bounds, and optical degradation profiles applied to synthesize real-world capture noise are detailed in Table 4.'
    r43.font.name = 'Times New Roman'
    r43.font.size = Pt(10.0)
    r43.bold = None
    r43.italic = None

    # Format Table 4 caption spacing in P44
    p44 = doc.paragraphs[44]
    p44.runs[0].text = 'TABLE 4: OPTICAL QUALITY DEGRADATION PROFILES'
    for r in p44.runs[1:]:
        r.text = ''
    p44.runs[0].font.name = 'Times New Roman'
    p44.runs[0].font.size = Pt(10.0)
    p44.runs[0].bold = True

    # 2. Update P59 (immediately below Variable Definitions Table for Table 6)
    p59 = doc.paragraphs[59]
    p59.runs[0].text = 'Note: The notation and mathematical variable definitions cataloged in the table above follow the evaluation-metric formulation defined in Table 6 and throughout this paper.'
    p59.runs[0].font.name = 'Times New Roman'
    p59.runs[0].font.size = Pt(10.0)
    for r in p59.runs[1:]:
        r.text = ''

    # 3. Update P85 (immediately above Table 11 & Table 12)
    p85 = doc.paragraphs[85]
    p85.runs[0].text = (
        "Rigorous statistical hypothesis testing across paired specimen observations confirms "
        "that the empirical accuracy improvements achieved by the canonical normalizer are "
        "statistically significant at p < 0.0001, as summarized in Table 11, evaluated via "
        "McNemar's test [38] (chi2 = 1002.00), Wilcoxon signed-rank test [39] (W = 0.0), "
        "and Paired t-test (t = 41.21). Furthermore, non-parametric bootstrap resampling [40] "
        "across replications confirms that canonical normalization consistently elevates "
        "field-level F1 scores without inflating variance, with empirical benchmark metrics "
        "and 95% bootstrap confidence intervals reported in Table 12."
    )
    p85.runs[0].font.name = 'Times New Roman'
    p85.runs[0].font.size = Pt(10.0)
    for r in p85.runs[1:]:
        r.text = ''

    # 4. Update P88 (immediately below Table 12, and immediately above Table 13)
    p88 = doc.paragraphs[88]
    p88.runs[0].text = (
        "As evidenced by the narrow 95% bootstrap confidence intervals across all primary evaluation metrics "
        "reported in Table 12, the framework demonstrates consistent statistical reproducibility. "
        "The nine-class diagnostic OCR error taxonomy distribution shift detailed in Table 13 evaluates "
        "9,000 atomic field observations across the 450 synthetic multi-modal document specimens. "
        "All 1,004 FORMAT_ERROR instances in Pass A were systematically converted into character-perfect "
        "EXACT_MATCH records in Pass B (raising exact match from 81.77% to 92.92%), while 85 genuine "
        "NORMALIZATION_ERROR cases (9.44%) were preserved, proving that canonicalization isolates "
        "formatting discrepancies without concealing model recognition errors."
    )
    p88.runs[0].font.name = 'Times New Roman'
    p88.runs[0].font.size = Pt(10.0)
    for r in p88.runs[1:]:
        r.text = ''

    # 5. Update P90 (immediately above Table 14)
    p90 = doc.paragraphs[90]
    p90.runs[0].text = (
        "To assess extraction failure predictability from document and degradation features, "
        "classical Decision Tree and Random Forest classifiers were evaluated across 9,000 observations. "
        "As reported in Table 14, Random Forest models achieved 96.11% accuracy, 97.89% F1, "
        "and 0.7514 MCC on the 80:20 split, closely matched by Decision Trees (96.11% accuracy, "
        "97.86% F1, 0.7669 MCC), as illustrated in the composite confusion matrices of Fig. 7 and Fig. 8."
    )
    p90.runs[0].font.name = 'Times New Roman'
    p90.runs[0].font.size = Pt(10.0)
    for r in p90.runs[1:]:
        r.text = ''

    doc.save(output_path)
    print(f'Saved successfully to {output_path}')

if __name__ == '__main__':
    update_table_references('PaperV50.docx', 'PaperV50.docx')
