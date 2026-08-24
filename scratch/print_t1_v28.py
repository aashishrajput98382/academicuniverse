import docx

doc = docx.Document('docs/paper/PaperV28_Ollama_Primary.docx')
t = doc.tables[0]
print(f"Table 1 Dimensions: {len(t.rows)} rows, {len(t.columns)} cols")
for i, r in enumerate(t.rows):
    print(f"Row {i}: {[c.text.strip().replace('\n', ' ') for c in r.cells]}")
