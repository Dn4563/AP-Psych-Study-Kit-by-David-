// Copies the shared engine from the Study Hub repo (cloned next to this one) into core/.
import { cpSync, rmSync, existsSync } from "node:fs";
const src = new URL("../../study-hub-by-david/kit-core/", import.meta.url);
const alt = new URL("../../Study-Hub-by-David/kit-core/", import.meta.url);
const from = existsSync(src) ? src : alt;
if (!existsSync(from)) {
  console.error("Could not find kit-core. Clone Study-Hub-by-David into the same folder as this repo.");
  process.exit(1);
}
const to = new URL("../core/", import.meta.url);
rmSync(to, { recursive: true, force: true });
cpSync(from, to, { recursive: true });
console.log("core/ now matches " + from.pathname);
