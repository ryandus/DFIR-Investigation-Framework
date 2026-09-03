# LIVE SYSTEM TRIAGE & VOLATILE ARTIFACT COLLECTION CHEAT SHEET
**Document Control ID:** DFIR-REF-003
**Target Standard:** RFC 3227 (Guidelines for Evidence Collection and Archiving)
**Classification:** TECHNICAL REFERENCE // FIELD GUIDE

---

## 1. RFC 3227 ORDER OF VOLATILITY EXECUTION MODEL

When acquiring evidence from a live system, collect data in order of decreasing volatility to prevent overwriting critical transient state artifacts:

1. **Registers & CPU Cache / Physical RAM** (Highest volatility - lost on power off)
2. **Routing Tables, ARP Cache, Process Tables, Kernel Memory**
3. **Active Network Sockets & Ephemeral Connections**
4. **Temporary File Systems, Swap Space / Pagefile**
5. **Persistent Storage & Disk Logs**
6. **Remote Logging & Archival Backups** (Lowest volatility)

> **CORE FORENSIC RULE:**
> Run all triage binaries directly from an external, forensically prepared triage drive (`E:\`). Do NOT install software on the suspect host. Pipe all CLI outputs directly to the triage drive to prevent disk contamination.

---

## 2. VOLATILE MEMORY (RAM) EXTRACTION COMMANDS

* **WinPmem (Windows Raw RAM Dump):**
  `winpmem.exe -o E:\Triage_Output\[CASE_ID]_[HOSTNAME]_RAM.raw`

* **DumpIt (Automated Memory Capture):**
  `DumpIt.exe /OUTPUT E:\Triage_Output\[CASE_ID]_[HOSTNAME]_RAM.dmp`

* **LiME (Linux Kernel Module Memory Capture):**
  `insmod lime.ko "path=/mnt/triage_usb/[CASE_ID]_[HOSTNAME]_RAM.lime format=raw"`

---

## 3. LIVE WINDOWS TRIAGE CLI MATRIX

Run these commands from an elevated command prompt residing on your external triage volume (`E:\`):

| Target Artifact | Native Command Syntax | Forensic Objective / Output |
| :--- | :--- | :--- |
| **System Time & Date** | `net time \\127.0.0.1` / `Get-Date -Format o` | Records exact clock skew against NIST/GPS reference time. |
| **Active Network Sockets** | `netstat -ano -b > E:\Triage\network_sockets.txt` | Identifies active listening ports, remote C2 connections, and associated Process IDs (PID). |
| **Routing Table & ARP** | `route print & arp -a > E:\Triage\routing_arp.txt` | Captures gateway redirects, MITM caches, and local subnet neighbors. |
| **Process Tree & Arguments** | `wmic process get ProcessId,ParentProcessId,CommandLine,ExecutablePath /format:csv > E:\Triage\processes.csv` | Full command-line launch strings (detects encoded PowerShell, injected processes, and LOLBAS). |
| **Active Services** | `Get-CimInstance Win32_Service | Select-Object Name,State,StartMode,PathName | Export-Csv E:\Triage\services.csv` | Identifies malicious persistence mechanisms masquerading as legitimate services. |
| **Scheduled Tasks** | `schtasks /query /fo CSV /v > E:\Triage\scheduled_tasks.csv` | Captures persistent scheduled tasks, triggers, and hidden script paths. |
| **Logged-in Sessions** | `query user & qwinsta > E:\Triage\user_sessions.txt` | Identifies active console, RDP, and disconnected background sessions. |
| **Network Shares** | `net share & net use > E:\Triage\smb_shares.txt` | Discovers mounted network drives and internal staging shares. |
| **Loaded Drivers** | `driverquery /v /fo CSV > E:\Triage\drivers.csv` | Identifies unsigned, obsolete, or malicious kernel drivers (BYOVD exploits). |
| **Firewall Status** | `netsh advfirewall show allprofiles > E:\Triage\firewall_rules.txt` | Verifies whether local perimeter firewall policies were disabled or modified. |

---

## 4. POWER-STATE DECISION MATRIX

* **If System is Powered OFF:**
  * Keep powered OFF.
  * Remove AC power cable and battery (if applicable).
  * Transport inside an RF-shielded Faraday container.
  * Acquire via write-blocked dead-box disk imaging.
* **If System is Powered ON and Disk is Encrypted (BitLocker / FileVault / LUKS):**
  * **DO NOT PULL THE PLUG.**
  * Capture RAM first (preserves in-memory volume decryption keys).
  * Extract volume recovery keys/escrow passwords.
  * Perform live logical or physical capture while volume is mounted and unlocked.
* **If System is Powered ON and Active Malware is Wiping/Encrypting Disk:**
  * Immediately sever network connections (pull Ethernet / toggle physical Wi-Fi switch).
  * Immediately pull power cable from the rear of the machine to halt destructive write cycles.

---

## 5. TRIAGE LOG & MD5/SHA-256 INTEGRITY MANIFEST

Immediately after completing live triage commands, calculate cryptographic hashes for all collected output files:

```powershell
Get-ChildItem -Path "E:\Triage_Output" -Recurse -File | Get-FileHash -Algorithm SHA256 | Export-Csv "E:\Triage_Output\Manifest_SHA256.csv" -NoTypeInformation
```

**Field Examiner Signature:** _____________________________________________  
**Printed Name:** [INSERT_EXAMINER_NAME], [CREDENTIALS]  
**Date & Time Completed (UTC):** [INSERT_TIMESTAMP_UTC]
