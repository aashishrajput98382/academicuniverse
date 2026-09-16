import xml.etree.ElementTree as ET
ns = {'a': 'http://schemas.openxmlformats.org/drawingml/2006/main', 'p': 'http://schemas.openxmlformats.org/presentationml/2006/main'}
tree = ET.parse('scratch/slide2.xml')
for sp in tree.findall('.//p:sp', ns):
    name = sp.find('.//p:cNvPr', ns).attrib.get('name')
    for elem in sp.findall('.//a:solidFill', ns):
        parent_tag = "unknown"
        for p in sp.iter():
            if elem in list(p):
                parent_tag = p.tag.split('}')[-1]
                break
        clrs = [c.attrib for c in elem]
        print(f"{name}: solidFill inside <{parent_tag}> -> {clrs}")
