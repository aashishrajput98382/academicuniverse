import re

def renumber_tables(text):
    def repl(match):
        prefix = match.group(1)
        num = int(match.group(2))
        if 8 <= num <= 14:
            return f"{prefix}{num - 1}"
        return match.group(0)
    return re.sub(r'\b(TABLE\s*|Table\s*)(\d+)\b', repl, text)

test_strings = [
    "Table 8 compares multiple paradigms",
    "TABLE 8: STATE-OF-THE-ART",
    "As summarized in Table 9 and visualized",
    "TABLE 9: EMPIRICAL METRIC",
    "reported in Table 10.",
    "TABLE 10: MISMATCH CORRECTION",
    "summarized in Table 11, and reported in Table 12.",
    "TABLE 11: STATISTICAL HYPOTHESIS",
    "TABLE 12: EMPIRICAL BENCHMARK",
    "reported in Table 12 and detailed in Table 13.",
    "TABLE 13: NINE-CLASS",
    "As reported in Table 14, Random Forest",
    "TABLE 14: CLASSICAL MACHINE LEARNING",
    "Table 6 and Table 1 and Table 2 and Table 3 and Table 4 and Table 5",
]

for s in test_strings:
    res = renumber_tables(s)
    print(f"'{s}' -> '{res}'")
