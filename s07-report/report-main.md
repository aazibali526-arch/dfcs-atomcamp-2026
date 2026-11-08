# Vulnerability Assessment & Penetration Test Report

**Prepared by:** Aazib Ali
**Course:** Digital Forensics & Cyber Security Bootcamp, Atomcamp
**Trainer:** Waseem Abbas Khan
**Date of Assessment:** 7 November 2026
**Classification:** Student Lab Exercise — Not for Distribution

---

**Target environment:**
| Role | OS | IP Address | Network |
|---|---|---|---|
| Attacker | Kali Linux | 192.168.88.133 | NAT |
| Target | Metasploitable 2 (Ubuntu-based Linux) | 192.168.88.134 | NAT |

**Engagement type:** Grey-box
**Simulation type:** Reconnaissance, exploitation and post-exploitation

---

## 1. Executive Summary

This assessment was conducted against a single Linux host (Metasploitable 2)
in an isolated NAT laboratory environment. The engagement covered network
discovery, port scanning, automated vulnerability scanning, manual CVE
research, and controlled exploitation using the Metasploit Framework.

**Findings summary:**

| Severity | Count |
|---|---|
| Critical | 1 |
| High | 1 |
| Medium | 1 |
| Low | 1 |
| **Total** | **4** |

**Highest severity:** Critical (CVSS 9.8)

**Primary impact:** An unauthenticated attacker with network access to
port 21 can gain complete root-level control of the target host — full
read and write access to all data, including database services running
on the same machine — without any credentials and without any action
from a legitimate user.

**Engagement type:** Grey-box — the target IP address was known in
advance; no source-code or credentials were provided at the start.

**Simulation type:** External attacker with network access only.

---

## 2. Engagement Scope and Details

**Scope type:** Grey-box
**Target IP:** 192.168.88.134 (Metasploitable 2)
**Testing window:** 7 November 2026
**Network:** Isolated NAT — target not reachable from any external network

**Methodology (in order performed):**
1. Network discovery (nmap -sn, netdiscover)
2. Port scanning (nmap default, full-range, targeted)
3. Version and OS detection (nmap -sV, -O)
4. NSE script enumeration (ftp, http, smb scripts)
5. Manual CVE research (NVD, Debian tracker, CWE)
6. Automated vulnerability scanning (Greenbone/OpenVAS GVM)
7. Exploitation (Metasploit Framework)
8. Post-exploitation confirmation (Meterpreter, shell access)

**Exclusions:**
- No denial-of-service techniques were used
- No data was exfiltrated from the target
- No persistence mechanisms were installed
- All changes to the target were limited to read-only confirmation of access

**Access granted:** Target IP address only (grey-box)

---

## 3. Findings and Proofs of Concept

*(See individual finding files:*
- *Finding 1: vsftpd 2.3.4 Backdoor — CVE-2011-2523 — Critical)*
- *Finding 2: Exposed phpinfo.php — CWE-200 — Medium)*
- *Finding 3: Telnet Cleartext Protocol — CWE-319 — High)*
- *Finding 4: Weak Default Credentials — CWE-1392 — High)*

---

## 4. Remediation Summary (Prioritised)

| Priority | Finding | Action |
|---|---|---|
| 1 — Immediate | vsftpd 2.3.4 backdoor | Upgrade vsftpd; verify package signatures |
| 2 — Immediate | Weak default credentials | Change all default passwords before network exposure |
| 3 — High | Telnet cleartext | Disable Telnet; replace with SSH |
| 4 — Medium | Exposed phpinfo.php | Remove debugging files from production server |

---

## 5. References

- https://nvd.nist.gov/vuln/detail/CVE-2011-2523
- https://security-tracker.debian.org/tracker/CVE-2011-2523
- https://cwe.mitre.org/data/definitions/78.html
- https://cwe.mitre.org/data/definitions/200.html
- https://cwe.mitre.org/data/definitions/319.html
- https://cwe.mitre.org/data/definitions/1392.html
- https://www.exploit-db.com/exploits/49757

---

## Appendix: Raw Evidence

Raw nmap scan outputs are included in the s07-report folder:
- scan-default.txt
- scan-versions.txt
- scan-backdoor-check.txt
- scan-http-enum.txt
- scan-telnet.txt

Screenshots are in the screenshots/ folder.
