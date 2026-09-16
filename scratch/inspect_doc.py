import docx

doc = docx.Document(r'c:\github\academicuniverse\ashmitxnaik\Deepfake_Video_Authentication_Updated_Research_Paper_With_Flowchart (1).docx')
# In python-docx, sections correspond to sectPr elements in body
# Let's inspect where sectPr elements appear in doc.element.body
body_elements = list(doc.element.body)
sect_idx = 0
for i, el in enumerate(body_elements):
    tag = el.tag.split('}')[-1]
    text = ""
    if tag == 'p':
        p = docx.text.paragraph.Paragraph(el, doc)
        text = p.text[:40]
    elif tag == 'tbl':
        text = "[TABLE]"
    elif tag == 'sectPr':
        print(f"--- Section boundary {sect_idx} at body index {i} ---")
        sect_idx += 1
        continue
    # check if p has sectPr
    has_sect = el.xpath('./w:pPr/w:sectPr')
    if has_sect:
        print(f"Body element {i} ({tag}): {repr(text)} -> HAS sectPr (Section {sect_idx})")
        sect_idx += 1
    elif 'PROPOSED' in text.upper() or 'INPUT VIDEO' in text.upper():
        print(f"Body element {i} ({tag}): {repr(text)} (Current section {sect_idx})")

