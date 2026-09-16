import docx

doc = docx.Document(r'c:\github\academicuniverse\ashmitxnaik\Deepfake_Video_Authentication_Updated_Research_Paper_With_Flowchart (1)_backup.docx')
for i, p in enumerate(doc.paragraphs):
    sects = p._p.xpath('./w:pPr/w:sectPr')
    brs = p._p.xpath('.//w:br')
    if sects or brs:
        s_types = [s.xpath('./w:type/@w:val') for s in sects]
        b_types = [b.attrib for b in brs]
        safe_text = p.text[:40].encode('ascii', 'replace').decode('ascii')
        print(f"P {i}: sects={s_types}, brs={b_types}, text={repr(safe_text)}")
