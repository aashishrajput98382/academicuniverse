import json

with open('scratch/pptv2_dump.json', encoding='utf-8') as f:
    data = json.load(f)

out_lines = []
for s in data:
    out_lines.append(f"\n==================== SLIDE {s['slide']} ====================")
    for sh in s['shapes']:
        fill = sh.get('fill', 'None')
        line = sh.get('line_color', 'None')
        out_lines.append(f"  Shape {sh['index']} ({sh['name']}) [left={sh['left']}, top={sh['top']}, w={sh['width']}, h={sh['height']}]:")
        out_lines.append(f"     Fill: {fill} | Border: {line}")
        for p in sh.get('paragraphs', []):
            if p['text'].strip():
                runs = [f"{r['text']} (col={r.get('color','default')}, bold={r.get('bold',False)})" for r in p['runs']]
                out_lines.append(f"       P: {' '.join(runs)[:120]}")

with open('scratch/all_slides.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out_lines))
print('Written successfully!')
