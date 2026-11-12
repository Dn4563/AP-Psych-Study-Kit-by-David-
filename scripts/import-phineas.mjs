// Imports Phineas's AP Psych study kit (one HTML page) into this kit's content/ folders.
//
//   npm run import                      (reads source/phineas-psych-kit.html)
//   npm run import -- path/to/page.html
//
// Writes, for each unit: cards.md, scenarios.json, practice.json, guide.json, watch.md.
// Merges our own files if present: whys.json (why each wrong choice is wrong, keyed by question text and choice),
// intros.json ("Read this first" text per section), cheat.json (cheat sheet). It never writes those or asks.json.
// Never touches asks.json (our applied questions). At the end it lists cards that have no applied question
// yet, and applied questions whose card no longer exists, so they can be written or removed.
// Phineas's content is copied as is. Cards he hides (the named-phobia cards) stay out.
import { readFileSync, writeFileSync, existsSync, mkdirSync } from "node:fs";
import vm from "node:vm";

const root = new URL("..", import.meta.url).pathname;
/* Small seeded random number generator (mulberry32 over a string hash), so imports are repeatable. */
function rng(seedText) {
  let h = 1779033703;
  for (const ch of seedText) h = Math.imul(h ^ ch.charCodeAt(0), 3432918353), (h = (h << 13) | (h >>> 19));
  let a = h >>> 0;
  return () => {
    a = (a + 0x6d2b79f5) >>> 0;
    let t = a;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}
const src = process.argv[2] || root + "source/phineas-psych-kit.html";
const html = readFileSync(src, "utf8");

/* Pull one top-level `const NAME = ...;` declaration out of the page's script. Data literals only. */
function grab(name) {
  const start = html.indexOf("const " + name + " = ");
  if (start < 0) throw new Error("Could not find " + name + " in " + src);
  const open = html.indexOf(/[\[{]/.exec(html.slice(start))[0], start);
  let depth = 0, inStr = null, i = open;
  for (; i < html.length; i++) {
    const ch = html[i];
    if (inStr) {
      if (ch === "\\") i++;
      else if (ch === inStr) inStr = null;
      continue;
    }
    if (ch === "/" && html[i + 1] === "/") {
      i = html.indexOf("\n", i);
      continue;
    }
    if (ch === "/" && html[i + 1] === "*") {
      i = html.indexOf("*/", i) + 1;
      continue;
    }
    if (ch === "'" || ch === '"' || ch === "`") inStr = ch;
    else if (ch === "[" || ch === "{") depth++;
    else if (ch === "]" || ch === "}") {
      depth--;
      if (depth === 0) break;
    }
  }
  return html.slice(start, i + 1) + ";";
}
const names = ["DECKS", "UNITS", "RAW", "CHAINS", "WATCH", "COMPARE_NT", "TABLES", "SCEN", "EXAM"];
const code = names.map(grab).join("\n") + "\n" + html.slice(html.indexOf("const HIDDEN = "), html.indexOf(";", html.indexOf("const HIDDEN = ")) + 1);
const ctx = vm.createContext({ Set });
vm.runInContext(code + "\nthis.out = {" + names.join(",") + ", HIDDEN};", ctx, { timeout: 2000 });
const { DECKS, UNITS, RAW, CHAINS, WATCH, TABLES, SCEN, EXAM, HIDDEN } = ctx.out;

/* Our units, in Phineas's order. His "Other" group (Perception) becomes its own unit. */
const OURS = {
  u0: { id: "u0", dir: "unit-00", label: "Unit 0", title: "Perspectives, Research & Statistics" },
  u1: { id: "u1", dir: "unit-01", label: "Unit 1", title: "Neuroscience, Senses, Sleep & Drugs" },
  u5: { id: "u5", dir: "unit-05", label: "Unit 5", title: "Health, Disorders & Treatment" },
  u2: { id: "per", dir: "perception", label: "Perception", title: "Perception" },
};
const cell = (t) => String(t || "").replace(/\|/g, "\\|").replace(/\s*\n\s*/g, " ").trim();
const report = [];

UNITS.forEach((U, ui) => {
  const ours = OURS[U.id];
  if (!ours) throw new Error("New unit in Phineas's kit: " + U.id + " (" + U.name + "). Add it to OURS.");
  const dir = root + "content/" + ours.dir + "/";
  mkdirSync(dir, { recursive: true });
  // Our own overlays (never written by this importer): whys for his wrong choices, section intros, a cheat sheet.
  const ownJSON = (f, empty) => (existsSync(dir + f) ? JSON.parse(readFileSync(dir + f, "utf8")) : empty);
  const WHYS = ownJSON("whys.json", {}),
    INTROS = ownJSON("intros.json", {}),
    CHEAT = ownJSON("cheat.json", []);
  const whyFor = (stem, options, ans) => options.map((o, k) => (k === ans ? "" : (WHYS[stem] || {})[o] || ""));
  // Optional decks go last, as in his deck view.
  const decks = U.decks.map((id) => DECKS.find((d) => d.id === id)).sort((a, b) => !!a.opt - !!b.opt);
  const num = {};
  decks.forEach((d, i) => (num[d.id] = i + 1));

  // cards.md
  let md = "";
  const terms = [];
  decks.forEach((d) => {
    const name = d.name.replace(/^Optional:\s*/, "");
    md += "# Deck " + num[d.id] + ": " + name + (d.opt ? " (optional)" : "") + "\n\n";
    if (d.sub) md += "> " + cell(d.sub).replace(/\\\|/g, "|") + "\n\n";
    const rows = RAW.filter((r) => r[0] === d.id && !HIDDEN.has(r[0] + "|" + r[2]));
    const secs = [];
    rows.forEach((r) => secs.indexOf(r[1]) < 0 && secs.push(r[1]));
    secs.forEach((s) => {
      md += "## " + s + "\n\n" + (INTROS[name + "|" + s] || INTROS[s] ? "> " + cell(INTROS[name + "|" + s] || INTROS[s]) + "\n\n" : "") + "| Term | Definition | Hook |\n|---|---|---|\n";
      rows.filter((r) => r[1] === s).forEach((r) => {
        md += "| " + cell(r[2]) + " | " + cell(r[3]) + " | " + cell(r[4]) + " |\n";
        terms.push(r[2]);
      });
      md += "\n";
    });
  });
  writeFileSync(dir + "cards.md", md);

  // scenarios.json (Learn checkpoints and Quiz scenarios)
  const sq = SCEN.filter((s) => num[s[0]]).map((s, i) => {
    const o = { id: "SQ" + (i + 1), deck: num[s[0]], q: s[1], opts: s[2], ans: s[3], exp: s[4] };
    const w = whyFor(s[1], s[2], s[3]);
    if (w.some((x) => x)) o.why = w;
    return o;
  });
  writeFileSync(dir + "scenarios.json", JSON.stringify(sq, null, 1) + "\n");

  // practice.json: his exam-style questions, one practice set per deck, plus a mock exam drawn evenly across decks.
  const exam = EXAM.filter((e) => num[e[0]]);
  // Phineas lists the right answer first almost every time. Each set gets its right answers spread evenly across
  // the letters, in a fixed random order (same seed every import), with the wrong choices kept in his order.
  // We reorder his choices, so an explanation that points to a choice by letter or position ("so B is a trap",
  // "the second option") would point to the wrong one. Those references are replaced with the choice's own text.
  const ORD = { first: 0, second: 1, third: 2, fourth: 3 };
  const fixRefs = (exp, opts) =>
    String(exp || "")
      .replace(/\b([A-D]) is (a|the) trap\b/g, (m, l, a) => (opts["ABCD".indexOf(l)] ? '"' + opts["ABCD".indexOf(l)] + '" is ' + a + " trap" : m))
      .replace(/\b[Tt]he (first|second|third|fourth) option\b/g, (m, w) => (opts[ORD[w]] ? '"' + opts[ORD[w]] + '"' : m));
  const toSet = (list, idOf, seed) => {
    const rnd = rng(seed);
    const slots = list.map((_, i) => i % 4);
    for (let i = slots.length - 1; i > 0; i--) {
      const j = Math.floor(rnd() * (i + 1));
      [slots[i], slots[j]] = [slots[j], slots[i]];
    }
    return list.map((e, i) => {
      const right = e[2][e[3]],
        wrong = e[2].filter((_, k) => k !== e[3]);
      const at = slots[i] % e[2].length;
      const options = wrong.slice(0, at).concat([right], wrong.slice(at));
      return { id: idOf(i), type: "mcq", topic: decks.find((d) => d.id === e[0]).name.replace(/^Optional:\s*/, ""), stem: e[1], options, ans: at, exp: fixRefs(e[4], e[2]), why: whyFor(e[1], options, at) };
    });
  };
  const sections = [];
  decks.forEach((d) => {
    const qs = exam.filter((e) => e[0] === d.id);
    if (!qs.length) return;
    sections.push({
      name: d.name.replace(/^Optional:\s*/, ""),
      mode: "practice",
      tips: ["Exam-style questions from Phineas's kit for this deck. Read every choice before you pick: the wrong ones are common mix-ups."],
      questions: toSet(qs, (i) => "q" + num[d.id] + "-" + (i + 1), ours.id + ":" + d.id),
    });
  });
  const core = decks.filter((d) => !d.opt);
  const per = Math.max(1, Math.ceil(30 / Math.max(1, core.length)));
  const mock = [];
  core.forEach((d) => exam.filter((e) => e[0] === d.id).slice(0, per).forEach((e) => mock.push(e)));
  if (mock.length)
    sections.push({
      name: "Mock exam",
      mode: "exam",
      exam: "Mock exam",
      examTips: ["Turn the Timer on and answer every question without looking anything up.", "Aim for about one minute per question. Flag hard ones and come back."],
      tips: ["A mix of exam-style questions from every deck in this unit."],
      questions: toSet(mock.slice(0, 30), (i) => "qM" + (i + 1), ours.id + ":mock"),
    });
  // Our own extra sets (written by scripts/asks-src/practice_extra.py) are kept across re-imports.
  if (existsSync(dir + "practice-extra.json")) JSON.parse(readFileSync(dir + "practice-extra.json", "utf8")).sections.forEach((s) => sections.push(s));
  writeFileSync(dir + "practice.json", JSON.stringify({ sections }, null, 1) + "\n");

  // guide.json: his chains and tables.
  const flows = [];
  decks.forEach((d) => (CHAINS[d.id] || []).forEach((c, i) => flows.push({ id: "F" + num[d.id] + "-" + (i + 1), title: c.label, deck: num[d.id], steps: c.steps })));
  const tables = [];
  Object.keys(TABLES).forEach((k) => {
    const [deckId, title] = k.split("|");
    if (!num[deckId]) return;
    const t = TABLES[k];
    const rows = typeof t.rows === "function" ? t.rows() : t.rows;
    tables.push({ title, rows: [t.head].concat(rows) });
  });
  writeFileSync(dir + "guide.json", JSON.stringify(CHEAT.length ? { flows, tables, cheat: CHEAT } : { flows, tables }, null, 1) + "\n");

  // watch.md
  let w = "# Watch out\n\nNotes from Phineas's kit on things that are easy to mix up or where the slides need care. Each starts with the deck it belongs to.\n\n";
  decks.forEach((d) => (WATCH[d.id] || []).forEach((n) => (w += "- (deck " + num[d.id] + ") " + n.replace(/\s*\n\s*/g, " ") + "\n")));
  writeFileSync(dir + "watch.md", w);

  // Applied questions: report what still needs writing (asks.json itself is never changed here).
  const asks = existsSync(dir + "asks.json") ? JSON.parse(readFileSync(dir + "asks.json", "utf8")) : {};
  const missing = terms.filter((t) => !asks[t]);
  const orphan = Object.keys(asks).filter((t) => terms.indexOf(t) < 0);
  report.push(ours.label + ": " + terms.length + " cards, " + sq.length + " scenarios, " + exam.length + " exam questions; " + missing.length + " cards need an applied question" + (orphan.length ? "; " + orphan.length + " applied questions have no card: " + orphan.join(", ") : ""));
});

// Card map for bringing progress over from Phineas's backup file (read by the engine's Restore from backup).
// His card ids are "<deck>-<position in RAW>"; ours are found by unit and term.
const unitOf = {};
UNITS.forEach((U) => U.decks.forEach((d) => (unitOf[d] = OURS[U.id].id)));
const cards = {};
RAW.forEach((r, i) => {
  if (HIDDEN.has(r[0] + "|" + r[2]) || !unitOf[r[0]]) return;
  cards[r[0] + "-" + i] = [unitOf[r[0]], r[2]];
});
writeFileSync(root + "content/import-map.json", JSON.stringify({ app: "psych-unit-1", name: "Phineas's kit", known: "ps1-known", miss: "ps1-miss", cards }, null, 1) + "\n");
report.push("Progress map: " + Object.keys(cards).length + " of Phineas's card ids");
report.forEach((l) => console.log(l));
