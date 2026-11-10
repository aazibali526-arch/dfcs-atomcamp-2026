# Task 2: Google Dork Report — intel.com

**Student:** Aazib Ali
**Domain:** intel.com (passive reconnaissance only — no systems were accessed)
**Date:** November 2026

---

## Dork 1: Exposed PDF Documents

**Dork:** `site:intel.com filetype:pdf "confidential"`

**Result:** Multiple PDF files found publicly indexed containing the word
"confidential" in their content, including Intel Quality Manual and
Platform Security Report hosted on cdrdv2-public.intel.com and
download.intel.com.

**Example URL found:**
`https://cdrdv2-public.intel.com/621722/Intel%20Quality%20Manual.pdf`

**What this means:** Internal documents marked "confidential" are
publicly indexed by Google. An attacker learns document naming
conventions, internal processes and terminology without touching
any system.

**Fix:** Review all publicly hosted PDFs. Remove or restrict access
to documents marked confidential. Implement a robots.txt rule and
access controls on the document hosting subdomain.

---

## Dork 2: Open Directory Listings

**Dork:** `site:intel.com intitle:"index of"`

**Result:** Google returned intel.com archive and design pages with
directory-style listings (e.g. `/design/archives/index.htm`), suggesting
some older sections of the site expose directory-style navigation.
Third-party mirrors of Intel data books also appeared with open
directory listings.

**What this means:** Open directory listings expose the full file
structure of a web server. Attackers can enumerate files, backups
and configuration files that were never meant to be public.

**Fix:** Disable directory listing in the web server configuration
(`Options -Indexes` in Apache). Audit legacy subdomains and archive
sections.

---

## Dork 3: Admin/Portal Interfaces

**Dork:** `site:intel.com inurl:admin -inurl:login`

**Result:** Several supplier and partner portal pages were found,
including `supplier.intel.com`, `premiersupport.intel.com`,
`rdc.intel.com` and `orders.intel.com`. A sign-in FAQ page also
revealed that `signin.intel.com` is no longer active, which could
indicate a forgotten or unmaintained subdomain.

**What this means:** Exposed portal and admin URLs give an attacker
a map of authenticated entry points to target. Discontinued portals
(like `signin.intel.com`) may still resolve and present an attack
surface.

**Fix:** Decommission and remove DNS entries for unused portals.
Ensure all portal login pages enforce MFA. Restrict access to known
IP ranges where possible.

---

## Dork 4: PHP Info / Debug Pages

**Dork:** `site:intel.com intext:"phpinfo()" OR intext:"phpMyAdmin"`

**Result:** No direct phpinfo() or phpMyAdmin pages were found on
intel.com itself — this is a positive finding. Intel's main
infrastructure does not appear to expose PHP debug pages publicly.

**What this means:** No immediate finding. This confirms that Intel's
primary web properties do not expose PHP configuration pages, which
is good security hygiene.

**Fix:** N/A for this dork. Continue monitoring periodically as new
subdomains are added.

---

## Dork 5: Sensitive File Extensions

**Dork:** `site:intel.com ext:env OR ext:log OR ext:bak`

**Result:** No .env, .log or .bak files were returned directly for
intel.com. However, search results confirmed that Intel hosts log
file documentation and that configuration file extensions are
referenced internally (e.g. Intel XTU log files discussion on
community.intel.com).

**What this means:** No direct file exposure found. However, the
community subdomain (community.intel.com) surfaces internal
technical discussions that reveal configuration file paths and
software versions — useful reconnaissance information for an
attacker even without direct file access.

**Fix:** Review community forum posts for inadvertent disclosure of
internal paths, software versions and configuration details.

---

## Dork 6: Subdomain Discovery (Hidden Subdomains)

**Dork:** `site:intel.com -www`

**Result:** Multiple non-www subdomains were found indexed, including:
- `community.intel.com`
- `newsroom.intel.com`
- `download.intel.com`
- `cdrdv2-public.intel.com`
- `builders.intel.com`
- `ark.intel.com`
- `supplier.intel.com`
- `premiersupport.intel.com`

**What this means:** Each subdomain is a separate attack surface with
its own technology stack, authentication logic and potential
vulnerabilities. `cdrdv2-public.intel.com` in particular hosts
documents that include confidential-marked content (see Dork 1).

**Fix:** Maintain an up-to-date asset inventory of all subdomains.
Apply the same security standards to every subdomain as to the main
site. Regularly audit subdomains for forgotten or unmaintained
services.

---

## Summary Table

| # | Dork | Finding | Severity |
|---|---|---|---|
| 1 | filetype:pdf "confidential" | Confidential PDFs publicly indexed | Medium |
| 2 | intitle:"index of" | Archive/legacy directory listings exposed | Medium |
| 3 | inurl:admin -inurl:login | Supplier/partner portals publicly mapped | Low |
| 4 | intext:"phpinfo()" | No finding — positive result | None |
| 5 | ext:env OR ext:log | No direct files; community forum discloses paths | Low |
| 6 | site:intel.com -www | Multiple subdomains discovered passively | Informational |

**Note:** All six dorks were run as passive Google searches only.
No request was sent to any intel.com server. No system was accessed,
tested or modified. This is entirely passive reconnaissance using
publicly indexed information.
