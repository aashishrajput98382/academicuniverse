import docx

doc = docx.Document("docs/paper/PaperV30_Ollama_Primary.docx")
print("All paragraphs:")
for idx, p in enumerate(doc.paragraphs):
    txt = p.text.strip()
    if txt.upper() in ["ACKNOWLEDGMENT", "ACKNOWLEDGEMENTS", "REFERENCES", "7. FUTURE WORK"] or txt.startswith("[1]") or txt.startswith("[50]"):
        print(f"Index {idx}: {repr(txt[:60])}")
