// Run with: npm test   (builds first)
import { clickthrough } from "../core/test-lib.mjs";
const r = await clickthrough(new URL("../index.html", import.meta.url).pathname).catch((e) => {
  console.error("FAIL: " + e.message);
  process.exit(1);
});
console.log(`PASS: ${r.passed} checks across units ${r.units.join(", ")}`);
