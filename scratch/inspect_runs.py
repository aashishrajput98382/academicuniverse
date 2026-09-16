import docx

doc = docx.Document('PaperV50.docx')
indices = [66, 69, 71, 72, 79, 80, 87, 88, 89, 90, 91, 92, 93]
for idx in indices:
    p = doc.paragraphs[idx]
    print(f'P{idx} ({len(p.runs)} runs):')
    for r_idx, r in enumerate(p.runs):
        if any(w in r.text for w in ['Table', 'TABLE']):
            print(f'  run[{r_idx}]: "{r.text}" font={r.font.name} size={r.font.size}')
