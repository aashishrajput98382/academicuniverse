import zipfile
import xml.etree.ElementTree as ET

ns = {'a': 'http://schemas.openxmlformats.org/drawingml/2006/main', 'p': 'http://schemas.openxmlformats.org/presentationml/2006/main'}

lines = []
with zipfile.ZipFile('pptv2.pptx', 'r') as z:
    for idx in range(1, 11):
        tree = ET.fromstring(z.read(f'ppt/slides/slide{idx}.xml'))
        lines.append(f"\n==================== SLIDE {idx} ====================")
        for sp in tree.findall('.//p:sp', ns):
            name = sp.find('.//p:cNvPr', ns).attrib.get('name', '')
            txBody = sp.find('p:txBody', ns)
            if txBody is not None:
                for p in txBody.findall('a:p', ns):
                    p_txt = ''.join([t.text for t in p.findall('.//a:t', ns) if t.text]).strip()
                    if not p_txt: continue
                    def_sz = p.find('.//a:defRPr', ns)
                    def_sz_val = def_sz.attrib.get('sz') if def_sz is not None and 'sz' in def_sz.attrib else "none"
                    run_szs = [r.find('a:rPr', ns).attrib.get('sz') for r in p.findall('a:r', ns) if r.find('a:rPr', ns) is not None and 'sz' in r.find('a:rPr', ns).attrib]
                    lines.append(f"  [{name}] def_sz={def_sz_val} | runs={run_szs} -> {p_txt[:65]}")

with open('scratch/font_sizes_out.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print('Saved font sizes!')
