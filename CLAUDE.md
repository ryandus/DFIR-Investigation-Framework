## Minimal Code
- Write the shortest solution that fully meets the stated requirement. YAGNI: no features, options, or config not asked for.
- Python stdlib first. Add a third-party dependency only when stdlib would take substantially more code or be less reliable, and say why in one line.
- No new classes, abstraction layers, factories, or helper modules unless the same logic is needed in 3+ places.
- No speculative error handling for situations that can't realistically happen. Let unexpected errors raise.
- Edit existing code in place with minimal diffs. Don't refactor, rename, or reformat code outside the task.
- No boilerplate docstrings or comments that restate the code. Comment only non-obvious "why".
- Don't generate tests, READMEs, or example files unless asked.
- Keep explanations short: what changed and why.

## Evidence Handling: never minimize
This is forensic tooling. If minimal code conflicts with defensibility in court, defensibility wins.
- SHA-256 hash verification before and after any read, copy, or transform of evidence. Don't add MD5 or SHA-1 unless asked (e.g., to match a legacy acquisition record).
- Never modify source evidence files.
- Chain-of-custody logging: timestamps, tool version, operator, input/output hashes.
- Validate evidence input and fail explicitly. Never silently skip or swallow errors on evidence data.
- Output must be deterministic and reproducible.
- No real case data in this repo. Samples and tests use synthetic data only.
