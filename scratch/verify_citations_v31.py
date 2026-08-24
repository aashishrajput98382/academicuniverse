import re
from pathlib import Path

workspace = Path(__file__).resolve().parents[1]
v31_md_path = workspace / "docs" / "paper" / "Paper_V31.md"
content = v31_md_path.read_text(encoding="utf-8")

# Extract References section
prose, refs_section = content.split("## REFERENCES")

# Find all citations in prose
citations = re.findall(r'\[(\d+(?:[–\-,\s]+\d+)*)\]', prose)
print(f"Total citation groups found in prose: {len(citations)}")

cited_nums = set()
for c in citations:
    parts = re.split(r'[,–\-]', c)
    for p in parts:
        p = p.strip()
        if p.isdigit():
            cited_nums.add(int(p))

print(f"Cited reference numbers: {sorted(list(cited_nums))}")
print(f"Total unique references cited: {len(cited_nums)} / 50")

missing_citations = [i for i in range(1, 51) if i not in cited_nums]
print(f"Missing in-text citations (if any): {missing_citations}")
