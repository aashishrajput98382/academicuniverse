import docx, os

doc = docx.Document('PaperV50.docx')

for i, p in enumerate(doc.paragraphs):
    if 'Fig. 2' in p.text:
        print(f"P{i}: {p.text}")
        # Look at p and preceding paragraph
        for offset in [-1, 0, 1]:
            target_p = doc.paragraphs[i + offset]
            xml = target_p._element.xml
            if 'blip' in xml:
                import xml.etree.ElementTree as ET
                root = ET.fromstring(xml)
                for elem in root.iter():
                    if elem.tag.endswith('blip'):
                        rId = elem.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
                        print(f"Found blip in P{i+offset}, rId: {rId}")
                        target_part = doc.part.related_parts[rId]
                        print(f"Target part: {target_part.partname}")
                        os.makedirs('scratch/extracted_images', exist_ok=True)
                        out_path = os.path.join('scratch/extracted_images', os.path.basename(target_part.partname))
                        with open(out_path, 'wb') as f:
                            f.write(target_part.blob)
                        print(f"Saved to {out_path} ({len(target_part.blob)} bytes)")
