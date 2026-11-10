# Task 4: Scanner Comparison — ZAP vs Burp Suite

**Student:** Aazib Ali
**Target:** http://192.168.88.134 (Metasploitable 2, port 80)
**Date:** November 2026

---

## Tools Used

| Tool | Version | Method |
|---|---|---|
| OWASP ZAP | 2.17.0 | Automated Scan (traditional spider + AJAX spider + active scan) |
| Burp Suite Community | N/A | Could not install — Kali repo returned 404 for burpsuite package. Comparison based on documented tool behaviour and handout |

---

## ZAP Results (Actual Scan)

**Total alerts: 24**

| Severity | Count |
|---|---|
| High | 0 |
| Medium | 6 |
| Low | 10 |
| Informational | 8 |

**Full alert list:**

| Alert | Severity | Count |
|---|---|---|
| Application Error Disclosure | Medium | 28 instances |
| Content Security Policy (CSP) Header Not Set | Medium | — |
| Directory Browsing | Medium | 2 |
| Vulnerable JS Library | Medium | — |
| Missing Anti-clickjacking Header | Medium | — |
| Absence of Anti-CSRF Tokens | Medium | — |
| Cookie No HttpOnly Flag | Low | 4 |
| Cookie without SameSite Attribute | Low | — |
| Private IP Disclosure | Low | 6 |
| Server Leaks Information via "X-Powered-By" | Low | — |
| Server Leaks Version Information via "Server" | Low | — |
| Strict-Transport-Security Header Not Set | Low | — |
| Timestamp Disclosure - Unix | Low | — |
| X-Content-Type-Options Header Missing | Low | — |
| Authentication Request Identified | Informational | 5 |
| Information Disclosure - Sensitive Information | Informational | — |
| In Page Banner Information Leak | Informational | — |

**Notable findings:**
- **Application Error Disclosure (28 instances):** The application is
  leaking internal error messages, revealing server-side technology
  and logic to any visitor. This is a research lead for further
  exploitation.
- **Directory Browsing (2):** Two directories are browsable without
  authentication — anyone can list their contents.
- **Private IP Disclosure (6):** Internal IP addresses are leaking
  in HTTP responses, confirming the network layout to an attacker.
- **Vulnerable JS Library:** An outdated JavaScript library is in
  use — a common entry point for client-side attacks.

---

## Burp Suite — Expected Behaviour (Based on Documentation)

Burp Suite Community Edition was not successfully installed during
this session (Kali repository 404 error for burpsuite package).
The following comparison is based on documented tool behaviour from
the course handout and PortSwigger's published documentation.

**What Burp would likely find that ZAP missed:**
- **Manual proxy-based findings:** Burp excels when the tester
  browses the application manually through its proxy, populating
  the site map with every request. This surfaces authenticated
  endpoints, hidden parameters and logic flows that an automated
  spider cannot see. ZAP's automated spider follows links; Burp's
  manual browse records every request the tester makes.
- **Repeater-based parameter testing:** Burp's Repeater tab allows
  precise, one-change-at-a-time testing of parameters. ZAP can
  replicate this but its workflow is less streamlined for manual work.
- **Intruder (rate-limited in CE):** Burp CE's Intruder performs
  brute-force and fuzzing but at a deliberately throttled rate. ZAP's
  Fuzzer has no such limit in its free version — ZAP wins here.

**What ZAP found that Burp CE would likely also find:**
- All header-based findings (CSP, HSTS, X-Content-Type-Options,
  clickjacking) — both tools check HTTP response headers by default.
- Cookie flags (HttpOnly, SameSite) — standard passive checks in
  both tools.
- Server version disclosure — both tools parse response headers.

**What ZAP found that Burp CE might miss:**
- **AJAX spider coverage:** ZAP's built-in AJAX spider (used in this
  scan with Firefox) crawls JavaScript-rendered content. Burp CE's
  crawler is weaker on single-page applications without manual
  browsing through the proxy first.
- **Directory Browsing:** ZAP's active scanner probed directories
  directly. Burp CE's scanner in the community edition is restricted
  and may not run the same active checks at full depth.

---

## Summary: Key Differences

| Capability | ZAP (CE) | Burp Suite (CE) |
|---|---|---|
| Automated scan | Full, unrestricted | Restricted in CE |
| AJAX spider | Built-in | Weaker without manual proxy use |
| Fuzzer | Full speed, no throttle | Throttled in CE |
| Manual proxy workflow | Available | Superior UX |
| Repeater (manual testing) | Available | Superior UX |
| Price | Free (Apache 2.0) | Free CE / Paid Pro |
| Best for | Full automated scanning, students | Manual testing, professional engagements |

---

## Conclusion

ZAP is the stronger choice for automated scanning in a free/lab
environment — it runs a complete scan with no licence restrictions.
Burp CE's real strength is in manual testing: its proxy, Repeater
and site map workflow give a tester precise control over individual
requests that ZAP's interface does not match. A professional
engagement uses both: ZAP to clear the routine automated findings
quickly, and Burp to investigate the interesting ones manually.

This matches the handout's observation: "Automation clears the
routine findings. Authorization and business logic need a human."

