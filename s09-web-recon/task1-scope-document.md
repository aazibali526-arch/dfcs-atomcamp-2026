# Scope and Rules of Engagement
## Hypothetical Web Application Penetration Test — *.intel.com

**Prepared by:** Aazib Ali
**Date:** November 2026
**Engagement type:** Grey-box

---

## 1. In Scope

| Asset | Notes |
|---|---|
| *.intel.com | All subdomains except those explicitly excluded |
| Associated IP ranges | As disclosed by client at engagement start |
| Web applications and APIs | Accessible via in-scope domains |

---

## 2. Explicitly Out of Scope

| Asset | Reason |
|---|---|
| career.intel.com | Third-party recruitment platform; not owned by client |
| *.intel.com subdomains pointing to third-party services | Outside client's control |
| Internal networks and non-web infrastructure | Not in scope for this engagement |
| Any system not reachable via in-scope domains | Out of scope by default |

**Default rule:** Anything not explicitly listed as in scope is out of scope.
When in doubt, stop and contact the emergency contact before proceeding.

---

## 3. Prohibited Techniques

- Denial-of-service (DoS/DDoS) of any kind
- Social engineering of staff or customers
- Physical access attempts
- Destructive payloads (deleting, encrypting or corrupting data)
- Exfiltrating more than one record to prove access
- Testing from IP addresses not listed in section 6

---

## 4. Access Granted

| Item | Detail |
|---|---|
| Engagement type | Grey-box |
| Test accounts | Two accounts provided by client (one per role) |
| VPN access | Client VPN credentials supplied for authenticated testing |
| Jump server | None required for this engagement |

---

## 5. Testing Window

| Item | Detail |
|---|---|
| Start date | As agreed in contract |
| End date | As agreed in contract |
| Permitted hours | 20:00 – 06:00 local time (off-hours only) |
| Reason | Production systems; off-hours reduces risk of disruption |

---

## 6. Source Addresses

All testing will originate from the following IP addresses only.
The client must whitelist these before testing begins:

- Tester IP 1: (to be confirmed before engagement start)
- Tester IP 2: (to be confirmed before engagement start)

Any testing from an unlisted IP is unauthorised and must stop immediately.

---

## 7. Break-Glass Clause

The wildcard scope *.intel.com may surface subdomains not anticipated at
scoping time. Before testing any newly discovered subdomain, the tester
must:

1. Stop all activity against that host.
2. Contact the named emergency contact (see section 8) for explicit
   written authorisation.
3. Record the authorisation (name, time, method) before proceeding.

A subdomain discovered during the engagement is not automatically in
scope. Authorisation is required each time.

---

## 8. Emergency Contact and Stop Procedure

| Item | Detail |
|---|---|
| Named contact | (Client security lead — name to be supplied) |
| Direct number | (Mobile number — must be reachable 24/7 during window) |
| Email | (Secure email address) |
| Stop procedure | Cease all testing immediately; preserve logs; notify contact within 15 minutes |

**Stop conditions:**
- Any system becomes unstable or unresponsive
- A critical finding is confirmed (immediate notification required)
- Tester is unsure whether an action is authorised

---

## 9. Data Handling

| Item | Detail |
|---|---|
| Data collected | Minimum necessary to prove access (one record maximum) |
| Storage | Encrypted storage on tester's machine only |
| Retention | Destroyed within 7 days of final report delivery |
| Confirmation | Written confirmation of destruction provided to client |

---

## 10. Reporting Obligations

| Event | Action |
|---|---|
| Critical finding | Immediate verbal notification, followed by written summary within 2 hours |
| High finding | Notification within 24 hours |
| Final report | Delivered within agreed deadline post-engagement |
