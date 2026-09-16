import zipfile
import xml.etree.ElementTree as ET

ns = {
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
}

out = []
def log(msg=""):
    out.append(msg)

with zipfile.ZipFile('pptv2.pptx', 'r') as z:
    for idx in range(1, 11):
        slide_xml = z.read(f'ppt/slides/slide{idx}.xml')
        root = ET.fromstring(slide_xml)
        log(f"\n==================== SLIDE {idx} ====================")
        for sp in root.findall('.//p:sp', ns):
            name = sp.find('.//p:cNvPr', ns).attrib.get('name')
            spPr = sp.find('p:spPr', ns)
            
            # Shape fill
            fill_color = "None"
            solidFill = spPr.find('a:solidFill', ns) if spPr is not None else None
            if solidFill is not None:
                clr = solidFill.find('a:srgbClr', ns)
                if clr is not None:
                    fill_color = clr.attrib.get('val')
                else:
                    clr_child = list(solidFill)
                    fill_color = clr_child[0].tag.split('}')[-1] if clr_child else "solid"
            
            # Line
            line_color = "None"
            ln = spPr.find('a:ln', ns) if spPr is not None else None
            if ln is not None:
                ln_fill = ln.find('a:solidFill', ns)
                if ln_fill is not None:
                    clr = ln_fill.find('a:srgbClr', ns)
                    if clr is not None:
                        line_color = clr.attrib.get('val')
            
            log(f"Shape '{name}': fill=#{fill_color}, border=#{line_color}")
            
            txBody = sp.find('p:txBody', ns)
            if txBody is not None:
                for p in txBody.findall('a:p', ns):
                    runs_info = []
                    for r in p.findall('a:r', ns):
                        t = r.find('a:t', ns)
                        text_val = t.text if t is not None else ""
                        rPr = r.find('a:rPr', ns)
                        color = "inherit"
                        bold = "False"
                        sz = "def"
                        if rPr is not None:
                            bold = rPr.attrib.get('b', 'False')
                            sz = str(int(rPr.attrib.get('sz', '0')) / 100) if 'sz' in rPr.attrib else 'def'
                            sf = rPr.find('a:solidFill', ns)
                            if sf is not None:
                                c = sf.find('a:srgbClr', ns)
                                if c is not None:
                                    color = f"#{c.attrib.get('val')}"
                        runs_info.append(f"[{color}, {sz}pt, b={bold}] {text_val}")
                    if runs_info:
                        log(f"    {' '.join(runs_info)[:130]}")

with open('scratch/deep_inspect_output.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))
log("Saved successfully!")
