import json

with open('scratch/pptv2_dump.json', encoding='utf-8') as f:
    data = json.load(f)

for s in data:
    print(f"=== Slide {s['slide']} ===")
    for sh in s['shapes']:
        fill = sh.get('fill', 'None')
        line = sh.get('line_color', 'None')
        texts = [p['text'] for p in sh.get('paragraphs', []) if p['text'].strip()]
        first_txt = texts[0][:50] if texts else ''
        runs_colors = set()
        for p in sh.get('paragraphs', []):
            for r in p.get('runs', []):
                if 'color' in r:
                    runs_colors.add(r['color'])
        print(f"  Shape {sh['index']}: {sh['name']} | fill={fill} | line={line} | font={list(runs_colors)} | txt='{first_txt}'")
