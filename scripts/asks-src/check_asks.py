# Checks every unit's applied questions: count per card, duplicate questions, repeated choices,
# right answer also listed as wrong, missing whys. Run: python3 scripts/asks-src/check_asks.py
import json, os, re, collections

root = os.path.join(os.path.dirname(__file__), "..", "..")
for unit in ["unit-00", "unit-01", "unit-05", "perception"]:
    asks = json.load(open(os.path.join(root, "content", unit, "asks.json")))
    per = collections.Counter({t: len(v) for t, v in asks.items()})
    stems = collections.Counter(q["q"] for v in asks.values() for q in v)
    problems = []
    for t, v in asks.items():
        for q in v:
            choices = [q["right"]] + [w[0] for w in q["wrong"]]
            if len(set(c.lower() for c in choices)) != len(choices): problems.append(t + ": repeated choice")
            if any(not w[1].strip() for w in q["wrong"]): problems.append(t + ": wrong choice without why")
            if len(q["right"]) > max(len(w[0]) for w in q["wrong"]): problems.append(t + ": right answer longest")
    for s, n in stems.items():
        if n > 1: problems.append("duplicate question: " + s[:70])
    dist = collections.Counter(per.values())
    print(unit, "cards:", len(per), "questions:", sum(per.values()), "per card:", dict(sorted(dist.items())))
    for p in problems: print("  " + p)
