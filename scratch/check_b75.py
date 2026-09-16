import docx

doc = docx.Document('PaperV50.docx')
p75 = doc.paragraphs[67] # Wait, let's find the exact paragraph for Body[75]
for i, child in enumerate(doc._body._element):
    if i == 75:
        print('Body[75] xml snippet:')
        print(child.xml[:500])
        print('Has drawing?', 'drawing' in child.xml)
