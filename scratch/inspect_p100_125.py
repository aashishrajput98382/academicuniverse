import docx

doc = docx.Document('PaperV50.docx')
for i in range(100, 126):
    print(f'P{i}: "{doc.paragraphs[i].text}"')
