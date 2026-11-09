// Imports Phineas's AP Psych study kit (one HTML page) into this kit's content/ folders.
//
//   npm run import                      (reads source/phineas-psych-kit.html)
//   npm run import -- path/to/page.html
//
// Writes, for each unit: cards.md, scenarios.json, practice.json, guide.json, watch.md.
// Never touches asks.json (our applied questions). At the end it lists cards that have no applied question
// yet, and applied questions whose card no longer exists, so they can be written or removed.
// Phineas's content is copied as is. Cards he hides (the named-phobia cards) stay out.
import { readFileSync, writeFileSync, existsSync, mkdirSync } from "node:fs";
import vm from "node:vm";

const root = new URL("..", import.meta.url).pathname;
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
      md += "## " + s + "\n\n| Term | Definition | Hook |\n|---|---|---|\n";
      rows.filter((r) => r[1] === s).forEach((r) => {
        md += "| " + cell(r[2]) + " | " + cell(r[3]) + " | " + cell(r[4]) + " |\n";
        terms.push(r[2]);
      });
      md += "\n";
    });
  });
  writeFileSync(dir + "cards.md", md);

  // scenarios.json (Learn checkpoints and Quiz scenarios)
  const sq = SCEN.filter((s) => num[s[0]]).map((s, i) => ({ id: "SQ" + (i + 1), deck: num[s[0]], q: s[1], opts: s[2], ans: s[3], exp: s[4] }));
  writeFileSync(dir + "scenarios.json", JSON.stringify(sq, null, 1) + "\n");

  // practice.json: his exam-style questions, one practice set per deck, plus a mock exam drawn evenly across decks.
  const exam = EXAM.filter((e) => num[e[0]]);
  const toQ = (e, id) => ({ id, type: "mcq", topic: decks.find((d) => d.id === e[0]).name.replace(/^Optional:\s*/, ""), stem: e[1], options: e[2], ans: e[3], exp: e[4], why: e[2].map(() => "") });
  const sections = [];
  decks.forEach((d) => {
    const qs = exam.filter((e) => e[0] === d.id);
    if (!qs.length) return;
    sections.push({
      name: d.name.replace(/^Optional:\s*/, ""),
      mode: "practice",
      tips: ["Exam-style questions from Phineas's kit for this deck. Read every choice before you pick: the wrong ones are common mix-ups."],
      questions: qs.map((e, i) => toQ(e, num[d.id] + "-" + (i + 1))),
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
      questions: mock.slice(0, 30).map((e, i) => toQ(e, "M" + (i + 1))),
    });
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
  writeFileSync(dir + "guide.json", JSON.stringify({ flows, tables }, null, 1) + "\n");

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

report.forEach((l) => console.log(l));
