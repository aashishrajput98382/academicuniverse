import docx, re
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl
from docx.text.paragraph import Paragraph
from docx.table import Table

def test_remove_table_7():
    doc = docx.Document('PaperV50.docx')
    print('Original tables:', len(doc.tables))
    print('Original paragraphs:', len(doc.paragraphs))

    # Identify Table 7 and its surrounding paragraphs P63, P64, P65
    p63 = doc.paragraphs[63]
    p64 = doc.paragraphs[64]
    tbl7 = doc.tables[7]
    p65 = doc.paragraphs[65]

    print(f'P63 text: {p63.text[:60]}...')
    print(f'P64 text: {p64.text[:60]}...')
    print(f'Tbl7 rows: {len(tbl7.rows)}')
    print(f'P65 text: {p65.text[:60]}...')

    # Check that they match our expectations
    assert 'Table 7' in p63.text
    assert 'TABLE 7' in p64.text
    assert 'Denotes framework system verification' in p65.text

    # Remove P63, P64, Tbl7, P65 from XML
    p63._p.getparent().remove(p63._p)
    p64._p.getparent().remove(p64._p)
    tbl7._element.getparent().remove(tbl7._element)
    p65._p.getparent().remove(p65._p)

    print('After removal: tables =', len(doc.tables), ', paragraphs =', len(doc.paragraphs))

    # Now renumber remaining tables and references (Table 8->7, Table 9->8, ..., Table 14->13)
    # Let's inspect all paragraphs and replace
    renumber_map = [
        # (old, new)
        ('TABLE 14', 'TABLE 13'),
        ('Table 14', 'Table 13'),
        ('TABLE 13', 'TABLE 12'),
        ('Table 13', 'Table 12'),
        ('TABLE 12', 'TABLE 11'),
        ('Table 12', 'Table 11'),
        ('TABLE 11', 'TABLE 10'),
        ('Table 11', 'Table 10'),
        ('TABLE 10', 'TABLE 9'),
        ('Table 10', 'Table 9'),
        ('TABLE 9', 'TABLE 8'),
        ('Table 9', 'Table 8'),
        ('TABLE 8', 'TABLE 7'),
        ('Table 8', 'Table 7'),
    ]

    for p in doc.paragraphs:
        for old_str, new_str in renumber_map:
            if old_str in p.text:
                # Replace in runs
                for r in p.runs:
                    if old_str in r.text:
                        r.text = r.text.replace(old_str, new_str)

    # Also check table cells just in case
    for t in doc.tables:
        for row in t.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    for old_str, new_str in renumber_map:
                        if old_str in p.text:
                            for r in p.runs:
                                if old_str in r.text:
                                    r.text = r.text.replace(old_str, new_str)

    doc.save('PaperV50_test.docx')
    print('Saved test docx successfully!')

test_remove_table_7()
