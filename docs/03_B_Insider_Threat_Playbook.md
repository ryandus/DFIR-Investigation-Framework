# INSIDER THREAT, IP THEFT & DATA EXFILTRATION INVESTIGATION PLAYBOOK
**Document Control ID:** DFIR-PB-002
**Target Standards:** ISO/IEC 27042:2015, NIST SP 800-86, CERT Insider Threat Guide
**Case Identifier:** [INSERT_CASE_NUMBER]
**Lead Examiner:** [INSERT_EXAMINER_NAME] | **Corporate Entity / Agency:** [INSERT_ORGANIZATION]
**Subject Under Investigation:** [INSERT_EMPLOYEE_NAME_AND_USER_ID]
**Investigation Classification:** HIGHLY CONFIDENTIAL // ATTORNEY-CLIENT PRIVILEGED

---

## 1. INTAKE, AUTHORIZATION & PRESERVATION PROTOCOLS

### 1.1 HR & General Counsel Coordination Checklist
* [ ] **Legal Authority Verified:** Written authorization received from Legal Counsel/HR prior to seizing or interrogating employee workstation/accounts.
* [ ] **Preservation Hold Issued:** Legal hold notification served to IT Operations to suspend mailbox retention policies, cloud account auto-purges, and audit log roll-overs.
* [ ] **Silent Account Suspension:** Coordinate timing so Active Directory, SSO (Okta/Entra ID), and VPN access are revoked simultaneously without alerting the subject during physical device acquisition.
* [ ] **Mobile Device & BYOD Assessment:** Identify if company-managed MDM profiles (Intune/Jamf) or MAM containers reside on subject's personal mobile hardware.

---

## 2. REMOVABLE MEDIA & USB ARTIFACT HUNTING GUIDE

To establish physical exfiltration to flash drives, external SSDs, or SD cards, interrogate the following system registry hives and diagnostic logs in chronological sequence:

| Investigative Question | Target Forensic Artifact / Key Path | Expected Value / Forensic Output |
| :--- | :--- | :--- |
| **Was a USB drive connected?** | `HKLM\SYSTEM\CurrentControlSet\Enum\USBSTOR` | Vendor Name, Product Model, Unique Serial Number, Device Class GUID. |
| **First/Last time connected?** | `C:\Windows\INF\setupapi.dev.log` | Exact local hardware installation date, first insert time, and driver initialization. |
| **What drive letter did it get?** | `HKLM\SYSTEM\MountedDevices` | Maps the unique Volume GUID (`\\?\Volume{...}`) to drive letter (e.g., `E:\`). |
| **Which user plugged it in?** | `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\MountPoints2` | Specific user profile registry mapping proving user account active at mount. |
| **Did user browse files on USB?** | `UsrClass.dat` -> `Local Settings\Software\Microsoft\Windows\Shell\Bags` | Shellbags: Proves folder directory traversal and folder viewing on external volumes. |

### 2.1 Removable Media Device Profile Summary Table

| Device Identifier (Make/Model) | Device Serial # | Volume GUID | Assigned Drive Letter | First Insert Timestamp (UTC) | Last Removal Timestamp (UTC) | User Account Active |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `[INSERT_MAKE_MODEL]` | `[INSERT_SERIAL_NUMBER]` | `{[INSERT_VOLUME_GUID]}` | `[INSERT_DRIVE]:\` | `[INSERT_TIMESTAMP]` | `[INSERT_TIMESTAMP]` | `[INSERT_USERNAME]` |

---

## 3. CLOUD STORAGE & WEB-BASED EXFILTRATION TRIAGE

### 3.1 Local Cloud Sync Client Database Inspection
Inspect local client sync SQLite databases to reconstruct batch file syncs prior to employee resignation:

* **Microsoft OneDrive:**
  * SQLite DB Path: `C:\Users\[USERNAME]\AppData\Local\Microsoft\OneDrive\settings\Personal\`
  * Target File: `SyncEngineDatabase.db` / `ClientPolicy.ini`
  * Artifacts: Timestamped record of added files, modified timestamps, sync completion flags.
* **Google Drive for Desktop:**
  * SQLite DB Path: `C:\Users\[USERNAME]\AppData\Local\Google\DriveFS\[USER_ID]\`
  * Target File: `metadata_sqlite_db`
  * Artifacts: Original item names, parent directory ID, cloud sync state, remote download URLs.
* **Dropbox:**
  * SQLite DB Path: `C:\Users\[USERNAME]\AppData\Local\Dropbox\instance1\`
  * Target File: `filecache.db` / `sync_history.db`

### 3.2 Web Browser Exfiltration & Staging Inspection
Search default browser profiles (`Google Chrome`, `Microsoft Edge`, `Mozilla Firefox`) located in `C:\Users\[USERNAME]\AppData\Local\`:

| Browser Artifact | Database / File Location | Target Table / Field | Forensic Significance |
| :--- | :--- | :--- | :--- |
| **Download History** | `...\Default\History` | `downloads` table | Software downloads (e.g., VPNs, compression tools, file transfer agents). |
| **URL Navigation** | `...\Default\History` | `urls` / `visits` table | Access to personal webmail (Gmail/Proton), file drop sites (WeTransfer, Mega, Pastebin). |
| **File Upload Headers** | `...\Default\Network Action Predictor` | Upload action records | Proves browser POST operations containing large payload byte counts to external URLs. |

---

## 4. ARCHIVE CREATION, STAGING & INTELLECTUAL PROPERTY PARSING

### 4.1 Compression & Bulk Staging Tool Artifacts
Departing personnel frequently compress large directory structures (code repositories, CAD drawings, client lists) prior to exfiltration.

* **7-Zip History:** `HKCU\Software\7-Zip\Compression` and `ExtractionPathHistory` (Records target source folders and output archive paths).
* **WinRAR History:** `HKCU\Software\WinRAR\ArcHistory` and `DialogEditHistory\ArcName` (Records recently built `.rar`/`.zip` container names).
* **Target File Knowledge (LNK & Jump Lists):**
  * Path: `C:\Users\[USERNAME]\AppData\Roaming\Microsoft\Windows\Recent\`
  * Parse `.lnk` and `AutomaticDestinations-ms` files for evidence of accessing staged archives or proprietary folders.

### 4.2 Staged & Compromised Intellectual Property Asset Log

| File / Archive Name | Source Path on Host Disk | File Size (Bytes) | SHA-256 Hash | Staged / Exfiltrated To (USB/Cloud/Web) | Timestamp (UTC) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `SourceCode_Master_2026.zip` | `C:\Users\[USER]\Desktop\` | `[INSERT_BYTES]` | `[INSERT_SHA256]` | Drive E: (Sandisk Extreme USB) | `[INSERT_TIMESTAMP]` |
| `Client_Master_Pipeline.xlsx` | `C:\CompanyShare\Sales\` | `[INSERT_BYTES]` | `[INSERT_SHA256]` | WeTransfer Web Upload | `[INSERT_TIMESTAMP]` |

---

## 5. ANTI-FORENSICS & EVIDENCE CONCEALMENT ARTIFACTS

Verify whether intentional evasion, file wiping, or log deletion occurred during the exfiltration window:

* [ ] **Audit Log Deletion:**
  * Windows Security Log Event ID **1102** ("The audit log was cleared").
  * Windows System Log Event ID **104** ("The log file was cleared").
* [ ] **Third-Party Sanitizer Execution:**
  * Check Prefetch (`C:\Windows\Prefetch\*.pf`), Shimcache, and Amcache for execution traces of: `CCLEANER.EXE`, `BLEACHBIT.EXE`, `BCWIPE.EXE`, `ERASER.EXE`, `SDELETE.EXE`.
* [ ] **Volume & Journal Anomalies:**
  * Check NTFS `$UsnJrnl` for massive clusters of `USN_REASON_FILE_DELETE` entries occurring within seconds.
  * Inspect `$MFT` record numbers for anomalous gaps or timestomping indicators (`$STANDARD_INFORMATION` timestamp earlier than `$FILE_NAME` timestamp).

---

## 6. INVESTIGATIVE SUMMARY & CHAIN OF EVIDENCE ATTESTATION

### 6.1 Final Case Assessment & Exfiltration Summary
* **Total Confidential Files Accessed:** `[INSERT_FILE_COUNT]`
* **Total Volume of Data Exfiltrated:** `[INSERT_DATA_VOLUME_MB_OR_GB]`
* **Primary Vector Utilized:** `[ ] USB Mass Storage  [ ] Personal Cloud Sync  [ ] Web Upload / Webmail  [ ] Network Share`
* **Evidence Tampering Detected:** `[ ] YES  [ ] NO`

### 6.2 Examiner Sworn Attestation
I certify that the forensic examination documented in this playbook was executed objectively in accordance with ISO/IEC 27042 standards and peer-accepted digital forensic methodologies. The identified artifacts substantiate the exfiltration vectors and timelines set forth above.

**Lead Forensic Examiner Signature:** _____________________________________________  
**Printed Name:** [INSERT_EXAMINER_NAME], [CREDENTIALS]  
**Title:** [INSERT_TITLE_OR_RANK]  
**Date Completed:** [INSERT_DATE]
