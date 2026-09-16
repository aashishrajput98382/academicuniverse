import zipfile
import xml.etree.ElementTree as ET

ns = {
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'p': 'http://schemas.openxmlformats.org/presentationml/2006/main'
}

lines = []
def plog(s=""):
    lines.append(s)

with zipfile.ZipFile('pptv2.pptx', 'r') as z:
    for idx in range(1, 11):
        tree = ET.fromstring(z.read(f'ppt/slides/slide{idx}.xml'))
        plog(f"\n--- SLIDE {idx} ---")
        for sp in tree.findall('.//p:sp', ns):
            name = sp.find('.//p:cNvPr', ns).attrib.get('name')
            
            # shape fill
            spPr = sp.find('p:spPr', ns)
            if spPr is not None:
                sf = spPr.find('a:solidFill/a:srgbClr', ns)
                if sf is not None:
                    plog(f"  ShapeFill [{name}]: #{sf.attrib.get('val')}")
                ln = spPr.find('a:ln/a:solidFill/a:srgbClr', ns)
                if ln is not None:
                    plog(f"  Border [{name}]: #{ln.attrib.get('val')}")
            
            # text fills
            txBody = sp.find('p:txBody', ns)
            if txBody is not None:
                for p in txBody.findall('a:p', ns):
                    p_text = "".join([t.text for t in p.findall('.//a:t', ns) if t.text])
                    p_sf = p.find('a:pPr/a:defRPr/a:solidFill/a:srgbClr', ns)
                    p_clr = f"defRPr:#{p_sf.attrib.get('val')}" if p_sf is not None else ""
                    
                    runs_clrs = []
                    for r in p.findall('a:r', ns):
                        r_t = r.find('a:t', ns)
                        t_str = r_t.text if r_t is not None else ""
                        r_sf = r.find('a:rPr/a:solidFill/a:srgbClr', ns)
                        if r_sf is not None:
                            runs_clrs.append(f"#{r_sf.attrib.get('val')}:'{t_str[:25]}'")
                    
                    runs_str = " | ".join(runs_clrs)
                    if p_text.strip():
                        plog(f"    Text [{name}]: {p_clr} {runs_str} -> '{p_text[:50]}'")

with open('scratch/color_map_out.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print('Saved map!')
