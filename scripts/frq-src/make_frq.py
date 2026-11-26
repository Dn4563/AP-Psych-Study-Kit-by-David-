"""Check our AAQ and EBQ questions (items.py) and write content/frq/fr.json.

Run: python3 scripts/frq-src/make_frq.py
Checks: real-exam length (AAQ article 700 to 950 words; each EBQ source 330 to 720), the four sections,
every part has a question and a model answer, and the checker data (r) has every part.
"""
import json, os, re, sys

sys.path.insert(0, os.path.dirname(__file__))
from items import AAQ, EBQ, EBQ_PARTS, GUIDE, LINKS, AAQ_LABEL, EBQ_LABEL
from aaq_more import AAQ_MORE

AAQ = AAQ + AAQ_MORE
try:
    from ebq_more import EBQ_MORE

    EBQ = EBQ + EBQ_MORE
except ImportError:
    pass
ids = [x["id"] for x in AAQ + EBQ]
if len(ids) != len(set(ids)):
    sys.exit("Two questions share an id")

ROOT = os.path.join(os.path.dirname(__file__), "..", "..")
SECTIONS = ["Introduction", "Participants", "Method", "Results and Discussion"]
# Counted like the released exams (table text included), so lengths compare.
words = lambda t: len(re.findall(r"[A-Za-z0-9][\w'.,%-]*", t))
errors, items, report = [], [], []

for a in AAQ:
    heads = [h for h, _ in a["sections"]]
    if heads != SECTIONS:
        errors.append(f"AAQ {a['id']}: sections must be {SECTIONS}, not {heads}")
    n = sum(words(p) for _, p in a["sections"])
    if not 700 <= n <= 950:
        errors.append(f"AAQ {a['id']}: article is {n} words; real ones are about 750 to 900")
    for k in "ABCDEF":
        if not a["q"].get(k) or not a["model"].get(k):
            errors.append(f"AAQ {a['id']}: part {k} needs a question and a model answer")
        if k not in a["r"]:
            errors.append(f"AAQ {a['id']}: checker data (r) is missing part {k}")
    report.append(f"AAQ {a['id']}: {n} words")
    items.append({
        "id": "aaq-" + a["id"], "type": "wfr", "grader": "aaq", "topic": a["topic"], "title": a["title"], "r": a["r"],
        "source": {"title": a["title"], "label": AAQ_LABEL, "blocks": [{"h": h, "p": p} for h, p in a["sections"]]},
        "parts": [{"k": k, "prompt": a["q"][k], "model": a["model"][k], "max": 2 if k == "F" else 1} for k in "ABCDEF"],
    })

for e in EBQ:
    if len(e["sources"]) != 3:
        errors.append(f"EBQ {e['id']}: needs exactly 3 sources")
    if not e["question"].startswith("Using the sources provided, develop and justify an argument about"):
        errors.append(f"EBQ {e['id']}: the question should use the exam wording")
    counts = []
    for i, (title, text) in enumerate(e["sources"], 1):
        heads = re.findall(r"^## (.+)$", text, flags=re.M)
        if heads != SECTIONS:
            errors.append(f"EBQ {e['id']} source {i}: sections must be {SECTIONS}, not {heads}")
        n = words(re.sub(r"^## .*$", "", text, flags=re.M))
        counts.append(n)
        if not 330 <= n <= 720:
            errors.append(f"EBQ {e['id']} source {i}: {n} words; real ones are about 350 to 700")
    for k, _, _ in EBQ_PARTS:
        if not e["model"].get(k):
            errors.append(f"EBQ {e['id']}: part {k} needs a model answer")
    for k in ("Bi", "Ci"):
        if not re.search(r"Source [123]", e["model"].get(k, "")):
            errors.append(f"EBQ {e['id']}: model answer {k} must cite a source")
    b, c = re.search(r"Source ([123])", e["model"]["Bi"]), re.search(r"Source ([123])", e["model"]["Ci"])
    if b and c and b.group(1) == c.group(1):
        errors.append(f"EBQ {e['id']}: C(i) must use a different source than B(i)")
    report.append(f"EBQ {e['id']}: sources {counts} words")
    items.append({
        "id": "ebq-" + e["id"], "type": "wfr", "grader": "ebq", "topic": e["topic"], "title": e["title"], "topicWords": e["topicWords"],
        "source": {"title": e["question"], "label": EBQ_LABEL, "blocks": [{"h": f"Source {i}: {t}", "p": x} for i, (t, x) in enumerate(e["sources"], 1)]},
        "parts": [{"k": k, "prompt": q, "model": e["model"][k], "max": m} for k, q, m in EBQ_PARTS],
    })

if errors:
    print("\n".join(errors))
    sys.exit(1)
out = os.path.join(ROOT, "content", "frq", "fr.json")
with open(out, "w") as f:
    json.dump({"items": items, "guide": GUIDE, "links": LINKS}, f, indent=1, ensure_ascii=False)
    f.write("\n")
print("\n".join(report))
print(f"Wrote {len(items)} questions to content/frq/fr.json")
