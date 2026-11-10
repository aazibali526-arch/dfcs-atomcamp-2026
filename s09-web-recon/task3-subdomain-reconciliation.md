
---

## Key Observation: Why the Combined Total Did Not Grow Much

After merging all three tools, the deduplicated total (15,258) was only
marginally larger than subfinder's result alone (14,235). This means
crtsh and assetfinder found very few subdomains that subfinder had
not already found.

This is explained by the tools' sources:
- **subfinder** queries many passive sources simultaneously —
  certificate logs, DNS datasets, search engines, and public APIs
  all at once. It is the broadest of the three.
- **assetfinder** draws from a narrower set of sources (primarily
  certificate transparency and web archives), so most of its results
  were already in subfinder's output.
- **crt.sh** queries certificate transparency logs only. Since
  subfinder also queries certificate transparency as one of its
  sources, the overlap was high.

---

## What Each Tool Found That Others Did Not

| Tool | Unique contribution |
|---|---|
| subfinder | The vast majority of unique results — 14,235 raw, covering the broadest source set |
| assetfinder | A small number of unique entries not in subfinder (web archive sources) |
| crt.sh | A small number of unique wildcard certificate entries (e.g. *.intel.com patterns) not surfaced by the other two |

---

## Sample Subdomains Found

Notable subdomains discovered across the tools:

- `www.intel.com` — main site
- `download.intel.com` — firmware and driver downloads
- `community.intel.com` — public forum
- `newsroom.intel.com` — press releases
- `ark.intel.com` — product specifications
- `cdrdv2-public.intel.com` — document hosting (also found in Dork 1)
- `supplier.intel.com` — supplier portal
- `builders.intel.com` — developer portal
- `software.intel.com` — software tools
- `premiersupport.intel.com` — partner support portal

---

## Why Three Tools and Not One

The handout's principle holds here: running three tools is not
redundancy for its own sake. Each draws from different sources, and
when results disagree or one finds something new, the disagreement
itself is informative. In this case, the high overlap between
subfinder and the other two tells us that intel.com's subdomains are
well-indexed across public sources — which is itself a finding: an
attacker needs only one good passive tool to map most of intel.com's
attack surface without sending a single packet.

---

## Note on Sublist3r

Sublist3r was attempted but crashed with a Python 3.14 compatibility
error (multiprocessing forkserver issue). crt.sh via curl was used
as a replacement third source, as it draws from a distinct mechanism
(certificate transparency API directly) compared to subfinder and
assetfinder.

