# DFCS Bootcamp 2026 — Assignments

**Student:** Aazib Ali
**Course:** Digital Forensics & Cyber Security Bootcamp, Atomcamp
**Trainer:** Waseem Abbas Khan — Senior Cybersecurity Specialist, CEI Master Trainer

This repository contains my assignment submissions for the DFCS Bootcamp,
organized by session.

---

## Repository Structure

dfcs-atomcamp-2026/
├── readme.md
├── .gitignore
├── s01-foundations/ Day 1 — Foundations, Linux & Networks, Cryptography
└── s06-scanning/ Day 2 — Network, Port & Vulnerability Scanning


---

## s01-foundations (Day 1)

Covers Linux/network foundations and cryptography (encoding, hashing,
encryption: Caesar, Base64, AES, RSA, hybrid encryption).

| File | Description |
|---|---|
| `task-a-malware-types.md` | Task A (compulsory): overview table of 12 malware types with real-world examples, plus an SME summary paragraph |
| `task-b3-caesar-decoder.md` | Task B3: Caesar cipher brute-force decoder, built and run in the Kali lab |
| `task-b4-openssl-salted.md` | Task B4: OpenSSL salted encryption/decryption walkthrough using `openssl` and `xxd` |
| `caesar_brute.py` | Python script used for the Caesar brute-force exercise (Task B3) |
| `security-monitor.sh` | Extra script written during the session (not part of the graded assignment) |
| `screenshots/` | Evidence screenshots for Tasks B3 and B4 |

---

## s06-scanning (Day 2)

Covers network discovery, port scanning, the Nmap Scripting Engine (NSE),
and converting a service version into a documented, scored vulnerability
finding (CVE / CVSS / CWE), performed against Metasploitable 2 in an
isolated NAT lab.

| File | Description |
|---|---|
| `task-a-three-findings.md` | Task A (compulsory): three complete vulnerability findings — vsftpd 2.3.4 backdoor (CVE-2011-2523), exposed `/phpinfo.php`, and cleartext Telnet |
| `task-b3-cvss-decode.md` | Task B3: full plain-English decode of the CVSS vector for CVE-2011-2523 |
| `task-b4-cwe-mapping.md` | Task B4: CWE classification for three Metasploitable vulnerabilities and how remediation differs by weakness class |
| `scan-*.txt` | Raw nmap scan outputs used as evidence for the findings |
| `screenshots/` | Evidence screenshots for all findings and scans |

### Lab setup
- **Attacker:** Kali Linux
- **Target:** Metasploitable 2 (intentionally vulnerable Linux VM)
- **Network:** NAT only — the target was never exposed to an untrusted or
  bridged network
- All commands were executed only against the lab target described above.

---

## Notes

- All write-ups are in my own words, with commands, outputs, and screenshots
  included as evidence for each claim.
- `.gitignore` excludes secret/sensitive files (`*.pem`, `*.enc`, `*.key`)
  that were generated during the cryptography labs but must never be
  committed.
