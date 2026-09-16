import zipfile
import xml.etree.ElementTree as ET
from collections import defaultdict

ns = {
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'p': 'http://schemas.openxmlformats.org/presentationml/2006/main'
}

color_usage = defaultdict(lambda: defaultdict(int))

with zipfile.ZipFile('pptv2.pptx', 'r') as z:
    for name in z.namelist():
        if name.startswith('ppt/slides/slide') and name.endswith('.xml'):
            slide_num = name.split('slide')[-1].replace('.xml', '')
            tree = ET.fromstring(z.read(name))
            for elem in tree.iter():
                tag = elem.tag.split('}')[-1]
                if tag == 'srgbClr':
                    val = elem.attrib.get('val')
                    # find context
                    color_usage[val][f"slide_{slide_num}"] += 1

print("All unique srgbClr in pptv2.pptx:")
for color, occurrences in sorted(color_usage.items()):
    total = sum(occurrences.values())
    slides = sorted(occurrences.keys(), key=lambda x: int(x.split('_')[1]))
    print(f"#{color} (total={total}): slides {', '.join(slides)}")
