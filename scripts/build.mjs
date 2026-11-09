// Parses the content, then builds the single self-contained index.html.
import { parseAll } from "../core/parse-lib.mjs";
import { buildKit } from "../core/build-lib.mjs";
const root = new URL("..", import.meta.url).pathname;
parseAll(root).forEach((l) => console.log(l));
const r = buildKit({ root, coreDir: root + "core" });
console.log(`Built index.html (${Math.round(r.bytes / 1024)} KB)`);
