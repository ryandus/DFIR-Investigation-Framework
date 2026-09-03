# DIGITAL EVIDENCE INTAKE, ACQUISITION & CUSTODY SUITE
**Document Control ID:** DFIR-MOD-01  
**Compliance Standards:** ISO/IEC 27037:2012, NIST SP 800-86, NIST SP 800-88 Rev. 1, Federal Rules of Evidence (FRE 901)  
**Classification:** STRICTLY CONFIDENTIAL // EVIDENCE RECORD  

---

## PART 1: MASTER DIGITAL EVIDENCE CHAIN OF CUSTODY (CoC) LOG

### 1.1 Administrative Case Header

| Field Name | Investigative Detail |
| :--- | :--- |
| **Laboratory / Agency Case ID:** | `[INSERT_CASE_NUMBER]` |
| **External Agency Reference ID:** | `[INSERT_EXTERNAL_AGENCY_REF]` |
| **Primary Forensic Examiner:** | `[INSERT_PRIMARY_EXAMINER_NAME]`, `[BADGE/ID_NUMBER]` |
| **Requesting Agency / Retaining Client:** | `[INSERT_CLIENT_OR_AGENCY_NAME]` |
| **Investigation Title / Matter:** | `[INSERT_CASE_MATTER_NAME]` |
| **Subject / Target Identifier:** | `[INSERT_TARGET_NAME_OR_IDENTIFIER]` |
| **Secure Vault Storage Location:** | `[INSERT_VAULT_NUMBER / SHELF / LOCKER_ID]` |

---

### 1.2 Digital Physical Evidence Master Inventory Table

| Item # | Complete Item Description (Make, Model, Color, Condition) | Serial Number / IMEI / MAC | Storage Media Type & Capacity | Tamper-Evident Bag Seal # |
| :--- | :--- | :--- | :--- | :--- |
| **Item 01** | `[INSERT_MAKE_MODEL_DESCRIPTION_01]` | `[INSERT_SERIAL_OR_IMEI_01]` | `[e.g., NVMe M.2 SSD - 1TB]` | `[INSERT_SEAL_NUM_01]` |
| **Item 02** | `[INSERT_MAKE_MODEL_DESCRIPTION_02]` | `[INSERT_SERIAL_OR_IMEI_02]` | `[e.g., SATA 3.5 HDD - 4TB]` | `[INSERT_SEAL_NUM_02]` |
| **Item 03** | `[INSERT_MAKE_MODEL_DESCRIPTION_03]` | `[INSERT_SERIAL_OR_IMEI_03]` | `[e.g., iPhone 15 Pro - 256GB]` | `[INSERT_SEAL_NUM_03]` |
| **Item 04** | `[INSERT_MAKE_MODEL_DESCRIPTION_04]` | `[INSERT_SERIAL_OR_IMEI_04]` | `[e.g., USB Flash Drive - 64GB]` | `[INSERT_SEAL_NUM_04]` |

---

### 1.3 Custodial Transfer & Tracking Log Table

> **MANDATORY PROTOCOL:** Every physical or digital movement of evidence items must be logged below immediately upon transfer. No transfer is legally valid without both releasing and receiving party signatures.

| Item #(s) | Date & Time (Local / UTC) | Released By (Print & Sign) | Received By (Print & Sign) | Transfer Location | Purpose of Transfer |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **01, 02** | `[INSERT_DATETIME_1]` | `[RELEASING_PARTY_1]` | `[RECEIVING_PARTY_1]` | `[LOCATION_1]` | Evidence intake and secure vault logging |
| **01** | `[INSERT_DATETIME_2]` | `[RELEASING_PARTY_2]` | `[RECEIVING_PARTY_2]` | Forensic Lab Station 03 | Physical write-blocked bit-stream acquisition |
| **01** | `[INSERT_DATETIME_3]` | `[RELEASING_PARTY_3]` | `[RECEIVING_PARTY_3]` | Evidence Vault Locker A | Return to secure long-term evidence storage |
| `[ITEM_#]` | `[INSERT_DATETIME_4]` | `[RELEASING_PARTY_4]` | `[RECEIVING_PARTY_4]` | `[LOCATION_4]` | `[PURPOSE_4]` |

---

## PART 2: DIGITAL EVIDENCE ACQUISITION & INTAKE WORKSHEET

### 2.1 Physical & Environmental Assessment Upon Seizure
* **Item Number:** `[INSERT_ITEM_NUMBER]`
* **Power State Upon Arrival:**
  * [ ] Powered Off (Cold)
  * [ ] Powered On / Unlocked (Live Screen State)
  * [ ] Powered On / Screen Locked (PIN / Password Unknown)
  * [ ] Sleep / Hibernation State
* **Isolation Applied Immediately:**
  * [ ] Faraday Bag / RF Shielding Container (Seal #: `[INSERT_FARADAY_SEAL]`)
  * [ ] Airplane Mode Toggled ON (Physical interaction verified)
  * [ ] SIM Card Removed (ICCID: `[INSERT_SIM_ICCID]`)
  * [ ] Network Interface Physically Disconnected / Disabled
* **Physical Condition Observations:** `[INSERT_PHYSICAL_NOTES: e.g., Minor chassis casing scratch; ports intact; water immersion indicator white/untriggered.]`

### 2.2 Forensic Write-Blocker & Tool Calibration
* **Hardware Write-Blocker:** `[INSERT_WRITE_BLOCKER_MAKE_AND_MODEL]`
* **Serial Number:** `[INSERT_BLOCKER_SERIAL_NUMBER]` | **Firmware:** `[INSERT_BLOCKER_FIRMWARE]`
* **Validation Check:**
  * [ ] Hardware Write-Protect switch engaged and verified via OS read-only mount test.
  * [ ] Passed laboratory calibration cycle (Calibration Date: `[INSERT_CAL_DATE]`).

### 2.3 Acquisition Methodology & Specifications
* **Forensic Software Engine:** `[INSERT_SOFTWARE_E.G., FTK IMAGER / MAGNET AXIOM / X-WAYS / GUYMAGER]` (Version: `[INSERT_VERSION]`)
* **Acquisition Type:**
  * [ ] Physical Raw Bit-Stream (`.dd` / `.raw` / `.img`)
  * [ ] Expert Witness Compression Format (`.E01` / `.Ex01` - Segment Size: `[2048 MB]`)
  * [ ] Advanced Forensic Format (`.AFF4`)
  * [ ] Logical File Extraction / Targeted Container (`.L01` / `.AD1`)
* **Destination Storage Drive:** Drive Serial `[INSERT_DESTINATION_DRIVE_SERIAL]`, Path `[INSERT_OUTPUT_PATH]`

### 2.4 Cryptographic Verification Hashes

| Hash Algorithm | Source Pre-Acquisition Value | Output Post-Acquisition Value | Match Status |
| :--- | :--- | :--- | :--- |
| **MD5** | `[INSERT_SOURCE_MD5_HASH]` | `[INSERT_VERIFICATION_MD5_HASH]` | **VERIFIED BIT-FOR-BIT MATCH** |
| **SHA-256** | `[INSERT_SOURCE_SHA256_HASH]` | `[INSERT_VERIFICATION_SHA256_HASH]` | **VERIFIED BIT-FOR-BIT MATCH** |

---

## PART 3: EVIDENCE RETURN, DESTRUCTION & SANITIZATION AGREEMENT

### 3.1 Authorization for Final Disposition
The undersigned client / retaining counsel hereby authorizes `[INSERT_LAB_OR_AGENCY_NAME]` to execute the final disposition of evidence media listed below in compliance with **NIST SP 800-88 Rev. 1 Guidelines for Media Sanitization**.

| Item # | Serial Number | Requested Action (Return / Sanitize / Destroy) | Sanitization Method Applied |
| :--- | :--- | :--- | :--- |
| **Item 01** | `[INSERT_SERIAL_01]` | `[ ] RETURN TO CLIENT  [ ] SANITIZE & RELEASE  [ ] SECURE DESTRUCTION` | `[e.g., NIST Clear / Purge / Physical Shred]` |
| **Item 02** | `[INSERT_SERIAL_02]` | `[ ] RETURN TO CLIENT  [ ] SANITIZE & RELEASE  [ ] SECURE DESTRUCTION` | `[e.g., NIST Clear / Purge / Physical Shred]` |

### 3.2 Certificate of Sanitization / Destruction
* **Sanitization Software / Tool:** `[INSERT_WIPE_TOOL_NAME]` (Version: `[VERSION]`)
* **Sanitization Verification:** Post-wipe hex inspection verified 100% zero-byte / random fill pattern across all LBA blocks.
* **Date Action Completed:** `[INSERT_DATE]` | **Technician Name:** `[INSERT_TECHNICIAN_NAME]`

### 3.3 Liability Release & Custody Relinquishment
Client acknowledges that upon execution of this return or destruction order, `[INSERT_LAB_OR_AGENCY_NAME]` is fully released from all future custodial liability and data preservation obligations regarding the listed media.

**Client / Retaining Counsel Signature:** _______________________________________ **Date:** `[INSERT_DATE]`  
**Forensic Custodian Signature:** _______________________________________________ **Date:** `[INSERT_DATE]`  

---

## PART 4: CONSENT TO SEARCH & DIGITAL EXTRACTION AUTHORIZATION

### 4.1 Voluntary Consent & Authorization
I, `[INSERT_CONSENTING_PARTY_NAME]`, hereby certify that I am the legal owner, authorized corporate representative, or lawful custodian of the electronic devices and accounts described below. I freely and voluntarily grant permission to `[INSERT_LAB_OR_COMPANY_NAME]` to conduct a digital forensic examination, extraction, and technical analysis.

### 4.2 Authorized Devices & Scope Limitations

| Device Description | Serial Number / IMEI | Permitted Scope / Investigative Restrictions |
| :--- | :--- | :--- |
| `[INSERT_DEVICE_01]` | `[INSERT_SERIAL_01]` | `[e.g., Limited to corporate email and file activity between Jan 1 - Mar 30, 2026]` |
| `[INSERT_DEVICE_02]` | `[INSERT_SERIAL_02]` | `[e.g., Full bit-stream acquisition and forensic artifact analysis]` |

### 4.3 Explicit Authorization Terms
1. **Non-Destructive Testing:** Forensic examination will be performed on write-blocked bit-stream copies whenever technically feasible.
2. **Credential & Decryption Access:** I authorize the forensic team to bypass, reset, or extract access credentials and encryption keys strictly necessary to execute the agreed scope.
3. **Privilege & Confidentiality:** All recovered data shall remain strictly confidential subject to attorney-client privilege or applicable non-disclosure agreements.

**Consenting Party Printed Name:** `[INSERT_NAME]`  
**Title / Relationship:** `[INSERT_TITLE_OR_RELATIONSHIP]`  
**Signature:** _____________________________________________________ **Date:** `[INSERT_DATE]`  
**Witnessing Examiner Signature:** _________________________________ **Date:** `[INSERT_DATE]`