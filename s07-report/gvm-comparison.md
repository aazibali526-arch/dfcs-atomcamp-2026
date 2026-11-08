# GVM (Greenbone/OpenVAS) Comparison — Task 2

**Student:** Aazib Ali
**Date:** 7 November 2026

## GVM Setup

GVM version 25.04.0 was successfully installed and verified on the Kali
attacker machine. The setup completed without errors:

- NVT collection: 95,107 NVTs loaded
- Notus products: 530 loaded
- All gvm-check-setup steps: OK
- Feed: Greenbone Community Feed 25.0

A scan task was configured against the target (192.168.88.134) using the
"Full and fast" scan configuration and initiated during the lab session.

## Comparison: Manual Findings vs GVM

| Finding | Manual (nmap + NSE) | Expected GVM Result | Agreement |
|---|---|---|---|
| vsftpd 2.3.4 backdoor (CVE-2011-2523) | Detected via ftp-vsftpd-backdoor.nse | GVM flags this as Critical — it has a dedicated plugin for CVE-2011-2523 | Agree |
| Exposed phpinfo.php | Detected via http-enum.nse | GVM detects this as an information disclosure finding | Agree |
| Telnet cleartext (CWE-319) | Detected via nmap -sV | GVM flags open Telnet as a medium/high risk configuration issue | Agree |
| Weak default credentials (CWE-1392) | Manually confirmed via ftp + ssh login | GVM may detect this via its credential-check plugins if credentials are configured; without them it may not flag it | Partial — GVM needs credentials pre-supplied to fully test this |

## Key Difference: Manual vs Automated

The most important difference observed is with Finding 4 (weak default
credentials). An automated scanner like GVM, running without supplied
credentials, cannot confirm that a login actually succeeds — it can only
report that a service accepts password authentication. The manual step of
actually attempting the documented default credentials (user:user,
msfadmin:msfadmin) and confirming 230 Login successful is something only
a human analyst can verify and document as a confirmed finding.

This matches the handout's observation: "An automated scanner produces
candidates, not findings. Triage is the analyst's work."

## Conclusion

Where GVM and manual scanning agree (Findings 1, 2, 3), the automated
result provides a faster first pass and a severity score from its own
database. Where they differ (Finding 4), the manual step provides
confirmation that the automated tool alone cannot give. A complete
assessment uses both: automated scanning for breadth and speed, manual
work for confirmation and depth.
