# AP Psychology Study Kit by David

Live site: https://dn4563.github.io/AP-Psych-Study-Kit-by-David-/

David's AP Psych study kit. It started from **Phineas's AP Psych study kit** (https://github.com/ichbleibhier/Psych-Unit-1; his username was brother12334 until Nov 2026), used with his permission: his cards, scenario questions, exam-style questions, chains, tables and watch-out notes were the starting point. Since then David has rebuilt and expanded it: applied questions for every card, why each wrong choice is wrong, section intros, cheat sheets, extra practice exams, exam-length AAQ & EBQ practice with a timed mock, smaller decks, the Start screen, study plan, focus timer and midterm review.

Built with the study kit engine by David Noskow (https://github.com/Dn4563/Study-Hub-by-David), MIT license.

`index.html` is **built**. Don't edit it by hand.

## Folders

| Path | What it is |
|---|---|
| `content/course.json` | Course name, colors, Study Hub link, and the list of units |
| `content/frq/fr.json` | AAQ & EBQ questions (ours, exam-length, fictional studies), written by `python3 scripts/frq-src/make_frq.py` from `scripts/frq-src/items.py`; `checker.json` next to it is Phineas's checker settings (imported) |
| `content/unit-00/`, `unit-01/`, `unit-05/`, `perception/` | One folder per unit: `cards.md`, `scenarios.json`, `practice.json`, `guide.json`, `watch.md` (imported); `asks.json` (our applied questions), `whys.json` (why each wrong choice is wrong), `intros.json` (section intros) and `cheat.json` (cheat sheet) are ours and survive re-imports |
| `source/phineas-psych-kit.html` | The copy of Phineas's page the content was imported from |
| `scripts/import-phineas.mjs` | The importer (`npm run import`) |
| `scripts/asks-src/` | The applied questions, one file per unit, and `make_asks.py` that checks them and writes `asks.json` |
| `core/` | Copy of the shared engine. Update it with `npm run sync-core`. |

## When Phineas updates his kit

1. Save his page as `source/phineas-psych-kit.html`.
2. `npm run import`. It rewrites the imported files and lists cards that still need an applied question. `asks.json`, `whys.json`, `intros.json` and `cheat.json` are never touched. Then run `python3 scripts/asks-src/check_whys.py` to find any wrong choices that lost their why.
3. Add the missing applied questions to `scripts/asks-src/<unit>.py` and run `python3 scripts/asks-src/make_asks.py <unit>`.
4. `npm test`.

## Move your progress from Phineas's kit

1. On Phineas's site, open **Settings** and press **Download backup**. It saves a `.json` file.
2. On this kit's home page (the list of units), press **Restore from backup** and choose that file.
3. Cards you marked known there become "got it" here, in the right unit, and terms you missed come up more in Learn. His lesson numbers and quiz answers don't carry over (the lessons and question sets are different).

The card map is `content/import-map.json`, rebuilt by `npm run import`.

## AI grading with Gemini (optional, free)

Every AAQ and EBQ is graded by the built-in checker (Phineas's key-word checker) with no setup. To also have answers graded like an AP reader would, and to make unlimited new practice articles and prompts:

1. Go to https://aistudio.google.com and sign in with a Google account. School accounts and accounts for students under 18 may be blocked; a personal account usually works (ask a parent if you need to).
2. Click **Get API key**, then **Create API key**. If you don't see those buttons, look for **API keys** in the menu on the left. Google may make a project for you; that's fine.
3. Copy the key (a long code that starts with `AIza`).
4. On the site, open the **AAQ & EBQ** unit, press the gear (Settings), paste the key into **Gemini AI grading**, press **Save**, then **Test**.

Good to know: it's free with daily limits. The key is saved only in that browser and is never part of the site; your answers go only to Google's Gemini service. On a shared computer, press **Remove key** when you're done. AI can make mistakes, so compare with the model answer.
