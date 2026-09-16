import docx
import pymupdf
import win32com.client, os

doc_path = r'c:\github\academicuniverse\scratch\test_applied_paper.docx'
test_fix_path = r'c:\github\academicuniverse\scratch\test_fix_flow.docx'
test_fix_pdf = r'c:\github\academicuniverse\scratch\test_fix_flow.pdf'

doc = docx.Document(doc_path)

# 1. Remove column break at Batch size: 16
for p in doc.paragraphs:
    if 'Batch size' in p.text:
        col_brs = p._p.xpath('.//w:br[@w:type="column"]')
        for b in col_brs:
            b.getparent().remove(b)
        print("Removed column break from 'Batch size'")

# 2. Change Section 9 start_type to CONTINUOUS
s9 = doc.sections[9]
s9.start_type = docx.enum.section.WD_SECTION_START.CONTINUOUS
# Ensure w:type continuous is present in sectPr
type_els = s9._sectPr.xpath('./w:type')
if type_els:
    type_els[0].set(docx.oxml.ns.qn('w:val'), 'continuous')
else:
    t = docx.oxml.OxmlElement('w:type')
    t.set(docx.oxml.ns.qn('w:val'), 'continuous')
    s9._sectPr.insert(0, t)

print("Set Section 9 to CONTINUOUS")

doc.save(test_fix_path)

# Convert to PDF
word = win32com.client.Dispatch('Word.Application')
word.Visible = False
d = word.Documents.Open(os.path.abspath(test_fix_path))
d.SaveAs(os.path.abspath(test_fix_pdf), FileFormat=17)
d.Close()
word.Quit()

# Render pages 3 and 4
pdf = pymupdf.open(test_fix_pdf)
print(f"Total pages in fixed doc: {len(pdf)}")
for pno in range(min(len(pdf), 5)):
    pix = pdf[pno].get_pixmap(dpi=150)
    pix.save(f"scratch/fixed_page_{pno+1}.png")
    print(f"Saved scratch/fixed_page_{pno+1}.png")
