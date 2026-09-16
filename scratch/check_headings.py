import docx

doc = docx.Document('PaperV50.docx')
for i, p in enumerate(doc.paragraphs):
    if any(h in p.text for h in ['6 CONCLUSION', '7 FUTURE WORK', 'DECLARATION', 'CODE REPOSITORY', 'REFERENCES']):
        print(f'P{i}: {p.text}')
