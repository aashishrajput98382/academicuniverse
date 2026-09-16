import xml.etree.ElementTree as ET

ns = {
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'p': 'http://schemas.openxmlformats.org/presentationml/2006/main'
}

print("=== THEME COLOR SCHEME ===")
tree = ET.parse('scratch/theme1.xml')
clrScheme = tree.find('.//a:clrScheme', ns)
if clrScheme is not None:
    print('Name:', clrScheme.attrib.get('name'))
    for elem in clrScheme:
        tag = elem.tag.split('}')[-1]
        colors = []
        for child in elem:
            c_tag = child.tag.split('}')[-1]
            colors.append(f"{c_tag}: {child.attrib}")
        print(f"  {tag}: {', '.join(colors)}")

print("\n=== SLIDE 1 SHAPES & FILLS/COLORS ===")
tree_s1 = ET.parse('scratch/slide1.xml')
for sp in tree_s1.findall('.//p:sp', ns):
    name = sp.find('.//p:cNvPr', ns).attrib.get('name')
    # look for solidFill
    fills = []
    for sf in sp.findall('.//a:solidFill', ns):
        for c in sf:
            fills.append(f"{c.tag.split('}')[-1]}={c.attrib}")
    lines = []
    for ln in sp.findall('.//a:ln', ns):
        for sf in ln.findall('.//a:solidFill', ns):
            for c in sf:
                lines.append(f"{c.tag.split('}')[-1]}={c.attrib}")
    print(f"Shape '{name}': fills={fills}, lines={lines}")

print("\n=== SLIDE 2 SHAPES & FILLS/COLORS ===")
tree_s2 = ET.parse('scratch/slide2.xml')
for sp in tree_s2.findall('.//p:sp', ns):
    name = sp.find('.//p:cNvPr', ns).attrib.get('name')
    fills = []
    for sf in sp.findall('.//a:solidFill', ns):
        for c in sf:
            fills.append(f"{c.tag.split('}')[-1]}={c.attrib}")
    lines = []
    for ln in sp.findall('.//a:ln', ns):
        for sf in ln.findall('.//a:solidFill', ns):
            for c in sf:
                lines.append(f"{c.tag.split('}')[-1]}={c.attrib}")
    print(f"Shape '{name}': fills={fills}, lines={lines}")
