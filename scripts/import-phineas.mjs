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
// It also writes content/frq/practice.json: his AAQ and EBQ free-response practice (see the end of this file).
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
// ---------- AAQ and EBQ free-response practice (his new sections) ----------
// One practice-only unit, "frq": practice sets and timed sets, his guides, his grading rules and model answers.
// His Gemini settings code isn't copied; the engine has its own optional Gemini grading (js/93-gemini.js).
{
  const fctx = vm.createContext({});
  const fnames = ["AAQ", "AAQ_PARTS", "AAQ_METHODS", "AAQ_WORDS", "EBQ", "EBQ_PARTS", "EBQ_CONCEPTS"];
  vm.runInContext(fnames.map(grab).join("\n") + "\nthis.out = {" + fnames.join(",") + "};", fctx, { timeout: 2000 });
  const F = fctx.out;
  const tpl = (re, what) => {
    const m = re.exec(html);
    if (!m) throw new Error("Could not find " + what + " in " + src);
    return m[1];
  };
  const list = (re, what) => vm.runInContext("(" + tpl(re, what) + ")", vm.createContext({}), { timeout: 1000 });
  const genTopics = list(/const AAQ_GEN_TOPICS\s*=\s*(\[[^\]]*\])/, "AAQ_GEN_TOPICS");
  const frq = {
    aaqParts: F.AAQ_PARTS,
    ebqParts: F.EBQ_PARTS,
    methods: F.AAQ_METHODS,
    words: F.AAQ_WORDS,
    stop: tpl(/const EBQ_STOP\s*=\s*new Set\('([^']*)'/, "EBQ_STOP").split(" "),
    concepts: F.EBQ_CONCEPTS.map(([n, re]) => [n, re.source, re.flags]),
    aaqRubric: tpl(/const AAQ_RUBRIC\s*=\s*`([^`]*)`/, "AAQ_RUBRIC"),
    ebqRubric: tpl(/const EBQ_RUBRIC\s*=\s*`([^`]*)`/, "EBQ_RUBRIC"),
    aaqTopics: genTopics,
    ebqTopics: genTopics.concat(list(/AAQ_GEN_TOPICS\.concat\((\[[^\]]*\])\)/, "EBQ topics")),
  };
  /* His "How the AAQ works" and "How the EBQ works" boxes, word for word, as blocks: {p}, {h}, {rows}, {table}.
     Bold and line breaks are kept; everything else is plain text. */
  const strip = (x) => x.replace(/<(?!\/?b>|br>)[^>]+>/g, "").replace(/\s+/g, " ").trim();
  function guide(title) {
    const i = html.indexOf(">" + title + "</h2>");
    if (i < 0) throw new Error("Could not find the guide " + title);
    const seg = html.slice(i + title.length + 6, html.indexOf("`;", i));
    const blocks = [];
    const re = /<h3>([\s\S]*?)<\/h3>|<p>([\s\S]*?)<\/p>|<div class="rows">([\s\S]*?)(?=<h3>|<p>|$)|<table[^>]*>([\s\S]*?)<\/table>/g;
    let m;
    while ((m = re.exec(seg))) {
      if (m[1]) blocks.push({ h: strip(m[1]) });
      else if (m[2]) blocks.push({ p: strip(m[2]) });
      else if (m[3]) blocks.push({ rows: [...m[3].matchAll(/<div class="t">([\s\S]*?)<\/div><div class="x">([\s\S]*?)<\/div>/g)].map((r) => [strip(r[1]), strip(r[2])]) });
      else if (m[4].indexOf("${AAQ_PARTS") >= 0)
        blocks.push({ table: [["Part", "What it asks", "Task verb", "Pts"]].concat(F.AAQ_PARTS.map((p) => ["<b>" + p.k + "</b> " + p.name, p.tip, p.verb, String(p.pts)])) });
      else blocks.push({ table: [...m[4].matchAll(/<tr>([\s\S]*?)<\/tr>/g)].map((r) => [...r[1].matchAll(/<t[hd]>([\s\S]*?)<\/t[hd]>/g)].map((c) => strip(c[1]))) });
    }
    return blocks;
  }
  const aaqGuide = guide("How the AAQ works"),
    ebqGuide = guide("How the EBQ works");
  const label = "Practice article from Phineas's AP Psych kit (a fictional study written for practice).";
  const aaqSrc = (a) => ({ title: a.title, attr: a.source, label: label, blocks: a.sections.map(([h, p]) => ({ h: h, p: p })), table: [a.table.head].concat(a.table.rows), tableAfter: "Participants" });
  const ebqSrc = (e) => ({ title: e.question, label: "Practice sources from Phineas's AP Psych kit, summarized and simplified.", blocks: e.sources.map((x, i) => ({ h: "Source " + (i + 1) + ": " + x.title, p: x.text })) });
  const aaqQ = (a, pre) => ({ id: pre + a.id, type: "wfr", grader: "aaq", topic: a.topic, title: a.title, src: "a-" + a.id, r: a.r, parts: F.AAQ_PARTS.map((p) => ({ k: p.k, prompt: a.q[p.k], model: a.model[p.k], max: p.pts })) });
  const ebqQ = (e, pre) => ({ id: pre + e.id, type: "wfr", grader: "ebq", topic: e.topic, title: e.title, src: "e-" + e.id, topicWords: e.topicWords || [], parts: F.EBQ_PARTS.map((p) => ({ k: p.k, prompt: p.q, model: e.model[p.k], max: p.pts })) });
  const srcs = (items, key, fn) => Object.fromEntries(items.map((x) => [key + x.id, fn(x)]));
  /* Timed sets: a few spread across the list, so each timed run is a different topic. */
  const spread = (arr, n) => Array.from({ length: n }, (_, i) => arr[Math.floor((i * arr.length) / n)]);
  const tA = spread(F.AAQ, 5),
    tE = spread(F.EBQ, 3);
  const sections = [
    { name: "AAQ practice", mode: "practice", grader: "aaq", guide: aaqGuide, tips: [], sources: srcs(F.AAQ, "a-", aaqSrc), questions: F.AAQ.map((a) => aaqQ(a, "aaq-")) },
    { name: "EBQ practice", mode: "practice", grader: "ebq", guide: ebqGuide, tips: [], sources: srcs(F.EBQ, "e-", ebqSrc), questions: F.EBQ.map((e) => ebqQ(e, "ebq-")) },
    { name: "Timed AAQ (25 min)", mode: "exam", exam: "Timed AAQ", grader: "aaq", guide: aaqGuide, tips: [], examTips: ["Turn the Timer on. The real AAQ is 25 minutes, including a 10-minute reading period.", "Answer every part, then press Check my answers on each article."], sources: srcs(tA, "a-", aaqSrc), questions: tA.map((a) => aaqQ(a, "taaq-")) },
    { name: "Timed EBQ (45 min)", mode: "exam", exam: "Timed EBQ", grader: "ebq", guide: ebqGuide, tips: [], examTips: ["Turn the Timer on. The real EBQ is 45 minutes, including a 15-minute reading period.", "Answer every part, then press Check my answers on each prompt."], sources: srcs(tE, "e-", ebqSrc), questions: tE.map((e) => ebqQ(e, "tebq-")) },
  ];
  const fdir = root + "content/frq/";
  mkdirSync(fdir, { recursive: true });
  writeFileSync(fdir + "practice.json", JSON.stringify({ frq: frq, sections: sections }, null, 1) + "\n");
  report.push("AAQ & EBQ: " + F.AAQ.length + " AAQ articles, " + F.EBQ.length + " EBQ prompts, " + frq.concepts.length + " EBQ concepts");
}
report.forEach((l) => console.log(l));
