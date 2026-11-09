// content/<unit>/*.md and *.json -> content/<unit>/data.json
import { parseAll } from "../core/parse-lib.mjs";
for (const line of parseAll(new URL("..", import.meta.url).pathname)) console.log(line);
