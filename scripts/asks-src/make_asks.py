# Turns scripts/asks-src/<unit-dir>.py into content/<unit-dir>/asks.json and checks it against cards.md.
#   python3 scripts/asks-src/make_asks.py unit-00 [unit-01 ...]
import json, os, re, sys, runpy

root = os.path.join(os.path.dirname(__file__), "..", "..")
for unit in sys.argv[1:]:
    A = runpy.run_path(os.path.join(os.path.dirname(__file__), unit + ".py"))["A"]
    cards = os.path.join(root, "content", unit, "cards.md")
    terms = []
    for line in open(cards):
        if line.startswith("| ") and not line.startswith("| Term |"):
            cells = re.split(r"(?<!\\)\|", line.strip().strip("|"))
            terms.append(cells[0].strip().replace("\\|", "|"))
    out, bad = {}, []
    for term, q, right, wrong, exp in A:
        if term not in terms:
            bad.append("no such card: " + term)
        if len(wrong) != 3:
            bad.append(term + ": needs 3 wrong choices")
        if len(right) > max(len(w[0]) for w in wrong):
            bad.append(term + ": right answer is the longest (%d vs %d)" % (len(right), max(len(w[0]) for w in wrong)))
        out.setdefault(term, []).append({"q": q, "right": right, "wrong": [list(w) for w in wrong], "exp": exp})
    missing = [t for t in terms if t not in out]
    for b in bad:
        print("  " + b)
    print("%s: %d applied questions, %d cards, %d missing%s" % (unit, len(A), len(terms), len(missing), (": " + "; ".join(missing)) if missing else ""))
    if not bad:
        json.dump(out, open(os.path.join(root, "content", unit, "asks.json"), "w"), indent=1, ensure_ascii=False)
