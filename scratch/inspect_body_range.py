import docx

doc = docx.Document('PaperV50.docx')
for i, child in enumerate(doc._body._element):
    tag = child.tag.split('}')[-1]
    txt = ''.join(child.itertext()).strip()
    if 65 <= i <= 82:
        print(f'Body[{i}] ({tag}): {txt[:80]}')
