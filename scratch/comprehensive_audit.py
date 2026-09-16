import docx, re
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl
from docx.text.paragraph import Paragraph
from docx.table import Table

doc = docx.Document('PaperV50.docx')

print("="*80)
print("COMPREHENSIVE AUDIT OF PaperV50.docx")
print("="*80)

# 1. Elements check
print(f"Total paragraphs: {len(doc.paragraphs)}")
print(f"Total tables: {len(doc.tables)}")
assert len(doc.tables) == 14, f"Expected 14 tables, found {len(doc.tables)}"

# 2. Check Table occurrences in text
print("\n--- ALL TABLE MENTIONS IN PARAGRAPHS ---")
table_mentions = []
for i, p in enumerate(doc.paragraphs):
    matches = re.findall(r'\b(?:TABLE|Table)\s*(\d+(?:\.\d+)?)\b', p.text)
    if matches:
        table_mentions.append((i, matches, p.text.strip()))
        print(f"P{i:03d} [{', '.join(matches)}]: {p.text.strip()[:100]}...")

# 3. Check Table occurrences in table cells
print("\n--- ALL TABLE MENTIONS IN TABLE CELLS ---")
cell_mentions = []
for t_idx, tbl in enumerate(doc.tables):
    for r_idx, row in enumerate(tbl.rows):
        for c_idx, cell in enumerate(row.cells):
            matches = re.findall(r'\b(?:TABLE|Table)\s*(\d+(?:\.\d+)?)\b', cell.text)
            if matches:
                cell_mentions.append((t_idx, r_idx, c_idx, matches, cell.text.strip()))
                print(f"T{t_idx} R{r_idx} C{c_idx} [{', '.join(matches)}]: {cell.text.strip()[:70]}")

# 4. Check that Table 14 does NOT exist anywhere
p_t14 = [i for i, p in enumerate(doc.paragraphs) if re.search(r'\bTable\s*14\b', p.text, re.I)]
tbl_t14 = [t for t, tbl in enumerate(doc.tables) if any(re.search(r'\bTable\s*14\b', c.text, re.I) for r in tbl.rows for c in r.cells)]
assert len(p_t14) == 0 and len(tbl_t14) == 0, f"Found Table 14 in P:{p_t14}, T:{tbl_t14}"
print("\nVerified: No mentions of Table 14 exist in the document.")

# 5. Check that dry-run Table 7 does NOT exist anywhere
dry_runs = [i for i, p in enumerate(doc.paragraphs) if re.search(r'dry[- ]run', p.text, re.I)]
assert len(dry_runs) == 0, f"Found dry-run mentions in P:{dry_runs}"
print("Verified: No mentions of dry-run baseline or old Table 7 exist in the document.")

# 6. Check font sizes across all tables
table_sizes = set()
for tbl in doc.tables:
    for r in tbl.rows:
        for c in r.cells:
            for p in c.paragraphs:
                for run in p.runs:
                    table_sizes.add(run.font.size.pt if run.font.size else None)
print(f"\nTable font sizes across all tables: {table_sizes}")
assert table_sizes == {8.0}, f"Unexpected table sizes: {table_sizes}"

# 7. Check asterisks
p_stars = [i for i, p in enumerate(doc.paragraphs) if '*' in p.text]
tbl_stars = [t for t, tbl in enumerate(doc.tables) if any('*' in c.text for r in tbl.rows for c in r.cells)]
print(f"Asterisk count: {len(p_stars) + len(tbl_stars)}")
assert len(p_stars) == 0 and len(tbl_stars) == 0, f"Found asterisks in P:{p_stars}, T:{tbl_stars}"

# 8. Check Conclusion + Future Work word count
c_p = None
f_p = None
for i, p in enumerate(doc.paragraphs):
    if p.text.strip() == '6 CONCLUSION':
        c_p = doc.paragraphs[i + 1]
    elif p.text.strip() == '7 FUTURE WORK':
        f_p = doc.paragraphs[i + 1]

c_words = len(c_p.text.split())
f_words = len(f_p.text.split())
print(f"\nConclusion word count: {c_words}")
print(f"Future Work word count: {f_words}")
print(f"Combined word count: {c_words + f_words}")
assert c_words + f_words == 250, f"Expected 250 words, got {c_words + f_words}"

# 9. Check sequential table captions
print("\n--- ALL TABLE CAPTIONS IN DOCUMENT ---")
for t_idx, tbl in enumerate(doc.tables):
    # Find preceding paragraph
    parent = tbl._element.getparent()
    # Let's inspect preceding elements in parent
    idx_in_parent = parent.index(tbl._element)
    prec_texts = []
    k = idx_in_parent - 1
    while k >= 0 and len(prec_texts) < 2:
        sibling = parent[k]
        if isinstance(sibling, CT_P):
            p = Paragraph(sibling, doc)
            if p.text.strip():
                prec_texts.append(p.text.strip())
        k -= 1
    caption = prec_texts[0] if prec_texts else "UNKNOWN"
    print(f"Table {t_idx}: {caption[:75]}")

print("\n" + "="*80)
print("ALL VERIFICATIONS COMPLETED SUCCESSFULLY WITH ZERO ERRORS!")
print("="*80)
