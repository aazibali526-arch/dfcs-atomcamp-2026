# Task B4: CWE Mapping — Three Metasploitable Vulnerabilities

**Student:** Aazib Ali

| # | Vulnerability | CWE | How remediation differs (in my own words) |
|---|---|---|---|
| 1 | vsftpd 2.3.4 backdoor (CVE-2011-2523) | **CWE-78** — OS Command Injection | This cannot be fixed by patching a single file, because the flaw was not in the source code itself but in the **distribution archive**. Remediation means re-downloading the software from a clean/official source and always verifying the vendor's signature. If this had been a true coding bug, patching the code alone would have been enough. |
| 2 | Exposed `/phpinfo.php` | **CWE-200** — Exposure of Sensitive Information | This is not a code bug at all, but a **deployment/configuration mistake** — a debugging file was left on a production server. Remediation means deleting the file or restricting access to it, and adding a deployment checklist so such files never reach production again. |
| 3 | Telnet cleartext protocol | **CWE-319** — Cleartext Transmission of Sensitive Information | This weakness lives in the **design of the protocol itself**, not in any one file or line of code. It cannot be "patched" — the entire service has to be disabled and replaced with an encrypted alternative (SSH). |

**My observation (in my own words):**
These three vulnerabilities show that the CWE category directly determines
the type of fix required:
- **CWE-78 (code-level flaw):** needs a patch or a verified clean reinstall.
- **CWE-200 (configuration flaw):** solved simply by removing or restricting a file/setting.
- **CWE-319 (design flaw):** requires replacing the whole protocol — no patch can fix it.

This is exactly why a report should never list only the CVE — the CWE tells
the developer or administrator whether they need a **code fix**, a
**configuration fix**, or an **architecture fix**.
