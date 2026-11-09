# AP Psychology Study Kit (David's format)

Live site: https://dn4563.github.io/AP-Psych-Study-Kit-by-David-/

The content (cards, scenario questions, exam-style questions, chains, tables and watch-out notes) comes from **Phineas's AP Psych study kit** (https://github.com/brother12334/Psych-Unit-1), used with his permission. This repo puts it in the study-kit format David uses for his other classes, and adds one applied question for every card.

Built with the study kit engine by David Noskow (https://github.com/Dn4563/Study-Hub-by-David), MIT license.

`index.html` is **built**. Don't edit it by hand.

## Folders

| Path | What it is |
|---|---|
| `content/course.json` | Course name, colors, Study Hub link, and the list of units |
| `content/unit-00/`, `unit-01/`, `unit-05/`, `perception/` | One folder per unit: `cards.md`, `scenarios.json`, `practice.json`, `guide.json`, `watch.md` (imported) and `asks.json` (our applied questions) |
| `source/phineas-psych-kit.html` | The copy of Phineas's page the content was imported from |
| `scripts/import-phineas.mjs` | The importer (`npm run import`) |
| `scripts/asks-src/` | The applied questions, one file per unit, and `make_asks.py` that checks them and writes `asks.json` |
| `core/` | Copy of the shared engine. Update it with `npm run sync-core`. |

## When Phineas updates his kit

1. Save his page as `source/phineas-psych-kit.html`.
2. `npm run import`. It rewrites the imported files and lists cards that still need an applied question. `asks.json` is never touched.
3. Add the missing applied questions to `scripts/asks-src/<unit>.py` and run `python3 scripts/asks-src/make_asks.py <unit>`.
4. `npm test`.
