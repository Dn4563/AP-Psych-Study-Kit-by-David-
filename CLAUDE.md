# How David wants new units built

These apply to every new unit or chapter in this kit, and to any rework of an old one.

## Learn questions
- Turn on mixed Learn questions for the unit: set `"learnMix": true` on the unit in `content/course.json`.
- Write `asks.json` for the unit with one applied question for every card. Applied questions make you use the idea (for example "Strontium is in group 2. What charge does its ion have?"), not repeat the definition. Every wrong choice gets a `why`, and the right answer is never the longest choice. The build checks this.
- Both kinds of questions stay: Learn picks a definition question or an applied question at random. A missed term comes back 2 or 3 questions later, asked the other way.
- Turn on old unit recall for every unit after the first: set `"recall": true` on the unit in `content/course.json`. Learn then asks at most 1 question from an earlier unit, in about 1 of 3 lessons, never in a deck's first lesson; it never counts against the lesson.
- For history, applied questions lean on cause, effect, comparison, continuity and change, not reciting definitions.

## Cards
- One fact per card. Split cards that pack several items together (for example a card per family or per group charge, not one card for four families).
- Definitions should explain the idea in other words, not repeat the term.

## Old units
- Leave units that classmates have already studied alone unless David asks. Chem Chapter 3 and AP World Unit 2 were brought up to the new Learn style on Nov 12, with David's OK. Review old units again before the midterm, the final, or the AP exam, since those cover everything again. Ask David first.

## Process
- When David sends material for a test, add its date to that unit in the hub's `courses.json` as `"testDate": "YYYY-MM-DD"`. The hub shows "Test on [date]" until that day, then nothing, and lists the course with the soonest test first. Don't add status labels; the hub no longer shows them.
- Don't invent content. Mark anything not in David's sources VERIFY.
- Run `npm test`, show screenshots and examples, and wait for David's OK before pushing to `main`.
- Keep `STATUS.md` in the Study-Hub-by-David repo up to date after every change. Also tell David in the chat, in a few short lines, what changed, which site and file it is in, and what was updated in `STATUS.md`. He does not read the whole status file.
- Before building anything, describe the plan to David in the chat in plain words (what will change, where, and how it will work) and wait for his OK.

## This kit: Phineas's content
- The cards, scenarios, exam questions, chains, tables and watch-out notes come from Phineas's AP Psych kit (his kit at ichbleibhier.github.io/Psych-Unit-1, repo github.com/ichbleibhier/Psych-Unit-1; he changed his username from brother12334 in Nov 2026), used with his permission. Keep his wording; don't split or rewrite his cards. Never edit his repo.
- Re-import only when David says Phineas gave permission again: save Phineas's page as `source/phineas-psych-kit.html`, run `npm run import`, then write applied questions for any cards the importer lists (in `scripts/asks-src/<unit>.py`, then `python3 scripts/asks-src/make_asks.py <unit>`).
- `asks.json` is ours; the importer never touches it.
- `content/<unit>/groups.json` is ours too: it splits Phineas's biggest decks into smaller ones along his section lines (Phineas OK'd regrouping). His card wording and every card id stay the same. After a re-import, the build stops if a section in `groups.json` was renamed; fix the name there.
- Also ours, merged by the importer on every import: `whys.json` (why each wrong choice in his practice questions and scenarios is wrong, keyed by question text and choice), `intros.json` ("Read this first" text per section; a key like `Deck name|Section` beats a plain section name) and `cheat.json` (the unit's cheat sheet). If he rewords a question or a choice, its why stops matching: after a re-import run `python3 scripts/asks-src/check_whys.py` and fill the gaps.
- AAQ & EBQ (unit `frq`): the questions are ours, not Phineas's (David chose this on Nov 26; students who want his shorter practice are pointed to his kit). They are exam-length, fictional studies written to match the released 2025 and 2026 exams, in `scripts/frq-src/items.py`; run `python3 scripts/frq-src/make_frq.py` to check lengths and write `content/frq/fr.json`. Every question needs `r` (what the checker looks for) and model answers that get 7 of 7 from the checker (npm test checks this). Only Phineas's key-word checker comes from him: the importer writes its settings to `content/frq/checker.json`, and the code is ported as is in `kit-core/js/92-frqcheck.js`. The page itself (Practice and the timed Mock exam) is `kit-core/js/94-fr.js`.
- Gemini AI grading is optional and lives in the engine (`kit-core/js/93-gemini.js`). Each student uses their own key, saved only in their browser. Never put a key in the repo.

## Midterms
- Midterm review is on for courses with 2+ units: `"midterm": { "week": "YYYY-MM-DD" (Monday of midterm week), "units": [...] (optional, default all), "mockQs": 40 }` in `content/course.json`. Only "week of Dec 14" came from David; when he sends a course's day, length, format and units, set them there and fit the mock to the real format.
