import docx

doc = docx.Document(r'c:\github\academicuniverse\ashmitxnaik\Deepfake_Video_Authentication_Updated_Research_Paper_With_Flowchart (1)_backup.docx')
for s_idx in range(5, 12):
    s = doc.sections[s_idx]
    cols = s._sectPr.xpath('.//w:col')
    print(f"Section {s_idx}: start_type={s.start_type}, cols_count={len(cols)}")
    print(f"  page_w={s.page_width.pt}, page_h={s.page_height.pt}, margins: t={s.top_margin.pt}, b={s.bottom_margin.pt}")
