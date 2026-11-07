# Task B3: CVSS Vector Decoded — CVE-2011-2523 (vsftpd 2.3.4 Backdoor)

**Student:** Aazib Ali

**CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
**Base Score:** 9.8 (Critical)

Each metric below is decoded in plain English, without using NVD's own labels:

| Metric | Value | My decode (in my own words) |
|---|---|---|
| **AV** (Attack Vector) | N | The attacker does not need to be anywhere near the target. The attack can be launched from anywhere in the world, as long as there is a network connection to the target. |
| **AC** (Attack Complexity) | L | The attack is easy to carry out. No special timing, luck, or complicated setup is needed — it works reliably every time. |
| **PR** (Privileges Required) | N | The attacker does not need any existing account, login, or password. The attack can be carried out entirely from the outside, with zero prior access. |
| **UI** (User Interaction) | N | No person on the target machine needs to click, open, or approve anything. The whole attack can be fully automated, with no help from a victim. |
| **S** (Scope) | U | The impact stays within the one vulnerable service/machine; it does not directly take over separate, unrelated systems. |
| **C** (Confidentiality) | H | The attacker can read **all** of the target's data — nothing stays hidden. |
| **I** (Integrity) | H | The attacker can **change or write** anything on the target — files, settings, data, all of it. |
| **A** (Availability) | H | The attacker can also shut down or crash the target machine or service. |

**My summary:**
This score means that anyone, anywhere on the internet, with no account and
no help from any person on the target machine, can attack this vsftpd
server and gain complete control — the ability to read everything, change
everything, and take the system offline. That combination is why this
vulnerability is rated at the maximum severity, 9.8 (Critical).
