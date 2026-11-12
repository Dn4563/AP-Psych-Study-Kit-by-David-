# Lists wrong choices in Phineas's practice questions and scenarios that have no "why" yet
# (for example after a re-import where he reworded a question). Run: python3 scripts/asks-src/check_whys.py
# Fill gaps in content/<unit>/whys.json ({question text: {choice text: why}}), then run npm run import.
import json, os
root = os.path.join(os.path.dirname(__file__), "..", "..")
for unit in ["unit-00", "unit-01", "unit-05", "perception"]:
    d = os.path.join(root, "content", unit)
    gaps = []
    for it in json.load(open(os.path.join(d, "scenarios.json"))):
        w = it.get("why") or [""] * len(it["opts"])
        gaps += [(it["q"], o) for i, o in enumerate(it["opts"]) if i != it["ans"] and not w[i]]
    for s in json.load(open(os.path.join(d, "practice.json")))["sections"]:
        for q in s["questions"]:
            if q.get("type") == "mcq":
                gaps += [(q["stem"], o) for i, o in enumerate(q["options"]) if i != q["ans"] and not (q.get("why") or [""] * 4)[i]]
    gaps = sorted(set(gaps))
    print(unit, "wrong choices without a why:", len(gaps))
    for g in gaps[:40]:
        print("   ", g[0][:70], "|", g[1])
