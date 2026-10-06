# Enterprise DFIR Investigation & Incident Response Framework

> Standardized Digital Forensics, Triage, Legal Testimony, and Incident Playbook Suite  
> Aligned with NIST SP 800-61 Rev. 3, ISO/IEC 27037 / 27042, RFC 3227, and Federal Rules of Evidence (FRE 702/901).

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Standards: NIST / ISO](https://img.shields.io/badge/Standards-NIST%20%7C%20ISO-brightgreen.svg)]()
[![Platform: Cross-Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-orange.svg)]()

---

## Executive Overview

The **Enterprise DFIR Framework** is a field-tested, standardized operational toolkit engineered for Digital Forensics and Incident Response (DFIR) examiners, law enforcement detectives, corporate security investigators, and SOC tier-3 analysts.

Navigating high-severity security incidents requires repeatable, defensible, and legally sound methodologies. This framework provides turnkey documentation, triage cheat sheets, step-by-step incident containment workflows, and court-ready legal declarations.

---

## Repository Contents & Modular Components

The source Markdown for each module is in [`docs/`](docs/).

| Module | Filename | Target Standard | Description |
| :--- | :--- | :--- | :--- |
| **00** | [docs/00_Product_Blueprint.md](docs/00_Product_Blueprint.md) | NIST / ISO | Architectural overview, metadata indexing, and procedural design. |
| **01** | [docs/01_Master_DFIR_Investigation_Report.md](docs/01_Master_DFIR_Investigation_Report.md) | ISO/IEC 27042 | Full 10-section forensic investigation template with hex/offset analysis. |
| **02** | [docs/02_Intake_and_Chain_of_Custody_Suite.md](docs/02_Intake_and_Chain_of_Custody_Suite.md) | ISO/IEC 27037 | Physical evidence intake, search warrant logs, and custodial tracking. |
| **03-A** | [docs/03_A_Ransomware_Playbook.md](docs/03_A_Ransomware_Playbook.md) | NIST SP 800-61 | Severity matrix, emergency isolation, and live volatile containment. |
| **03-B** | [docs/03_B_Insider_Threat_Playbook.md](docs/03_B_Insider_Threat_Playbook.md) | CERT / NIST 800-86 | USB/Cloud exfiltration hunting, Shellbags, LNK, and anti-forensics triage. |
| **03-C** | [docs/03_C_Live_Triage_CheatSheet.md](docs/03_C_Live_Triage_CheatSheet.md) | RFC 3227 | Order of volatility execution model, live CLI matrix, and memory capture. |
| **04** | [docs/04_Legal_and_Expert_Witness_Suite.md](docs/04_Legal_and_Expert_Witness_Suite.md) | FRE 702 / FRCP 26 | Daubert checklist, expert affidavits, and Master Services Agreements. |

---

## Pre-Compiled Deliverables

Pre-compiled deliverables are organized under the `dist/` directory:

* **PDFs (`dist/pdf/`)**: Formatted, publication-ready forensic reports and playbooks.
* **Word Documents (`dist/docx/`)**: Fully editable `.docx` templates for active case adaptation.
* **HTML Versions (`dist/html/`)**: Standalone styled reference pages.

---

## Optional: DFIR Copilot (experimental)

`copilot.py` is a command-line assistant. It loads three playbooks from `docs/` (ransomware, insider threat, and live triage) as context and answers investigator questions through Google's Gemini API.

* Setup: `pip install -r Requirements.txt`, then set the `GEMINI_API_KEY` environment variable and run `python copilot.py`.
* **Data warning:** everything you type, plus the playbook text, is sent to Google's Gemini API. Do not enter case details, evidence, or personal information.
* Experimental: it has no tests, and you should confirm the model name set in the script is available to your API key.

---

## License

Distributed under the **MIT License**. See [LICENSE](LICENSE) for details.
