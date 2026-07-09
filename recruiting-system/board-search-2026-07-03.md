# ATS Board Search Pack - 2026-07-03

Prompted by an X post on the "most jobs aren't on LinkedIn, use `site:` search on ATS boards" technique. This is the same
technique already codified in `search-playbook.md` and used for the prior `board_search` sweeps
(2026-06-23, 2026-06-24, 2026-06-26, 2026-06-30), so today's pass mainly re-ran and widened that query set and,
critically, verified links before trusting them.

## Query set used today

```text
site:jobs.ashbyhq.com India ("software engineer" OR "backend engineer" OR "SDE I" OR "software development engineer")
site:jobs.lever.co India ("backend engineer" OR "software engineer I" OR "SDE I" OR "associate software engineer")
site:boards.greenhouse.io India ("software engineer" OR "backend engineer") ("new grad" OR "junior" OR "0-1 years" OR "1-2 years")
site:jobs.smartrecruiters.com India ("software engineer" OR "backend engineer" OR "junior software engineer" OR "associate software engineer")
site:myworkdayjobs.com India ("Associate Software Engineer" OR "Software Engineer I" OR "New Grad" OR "Graduate Software Engineer")
site:jobs.jobvite.com India ("software engineer" OR "backend engineer" OR "associate software engineer")
site:jobs.bamboohr.com India ("software engineer" OR "backend engineer" OR "SDE")
site:careers.workable.com India ("software engineer" OR "backend engineer" OR "SDE I" OR "junior software engineer")
site:careers.icims.com India ("software engineer" OR "backend engineer" OR "associate software engineer")
site:jobs.lever.co "Remote India" OR Bengaluru ("SDE 1" OR "SDE-1" OR "SDE I")
site:jobs.ashbyhq.com India ("fresher" OR "0-1 years" OR "new grad" OR "campus")
site:jobs.lever.co OR site:jobs.ashbyhq.com Zepto OR Groww OR CRED OR Slice OR Razorpay backend engineer OR "SDE 1"
```

BambooHR and Workable returned no usable India-specific hits through search (their public listings don't seem to be
well indexed under those site: patterns right now).

## Key finding: high dead-link rate today

Out of roughly 25 promising-looking titles pulled from search snippets, most did not survive a direct check:

- **Expired / 404 on the actual ATS page**: Grab (Software Engineer, Backend), Kwalee (Junior Software Engineer -
  Backend), Cartesia (Software Engineer, Platform), Aizen (Backend Software Engineer - India), Mercor (Software
  Engineer, India), Visa (SW Engineer, 1-2 years), Boeing (Associate Software Engineer, AI), Microsoft (Java
  Developer - Associate), Veeva (Associate Software Engineer - Seeking 2025 & 2026 Grads), Fam/FamPay (Data Engineer
  - SDE 1), Bloomreach (Backend, Junior) and Definitive Healthcare (Junior Software Engineer) original postings.
- **Misleading title/location**: Articul8's "Software Engineer (India)" role is actually Brazil/Remote and asks for
  7+ years; Xplor's "Backend Software Engineer" result was actually a Java role based in Atlanta, USA.
- **Title says junior, JD says senior**: Ema's "Software Engineer, Backend - India" wants 7+ years; FurtherAI's
  listing (despite a promising snippet) is a Senior Backend Engineer role wanting 5+ years.

Net: Google's index of these ATS boards includes a large share of closed or stale postings, and titles are not always
a reliable signal of true seniority. Worth re-running this sweep periodically, but always confirm a listing is live
before logging or applying.

## New verified lead added to job-tracker.csv

### Netomi - SDE I - Backend
- URL: https://jobs.lever.co/netomi/d61510b5-44ea-44c9-8441-097a48bf5e77
- Location: Remote, India
- Why it fits: explicitly wants 1-3 years, Java/J2EE, AWS; Y Combinator and Index Ventures-backed agentic AI CX
  platform (Delta, MetLife, MGM, United as customers)
- Notes: this exact posting has now surfaced three separate times (2026-06-24, in the 2026-06-30 pack, and today)
  but was never logged in the tracker until this pass. Confirmed live today.

## Other roles seen in search but not added (deprioritized or unverified)

- **Netomi - SDE I - Frontend / SDE I - Frontend (Analytics team)**: same 1-3 year band, but frontend-leaning rather
  than backend; keep as a backup only if backend roles dry up.
- **Oleria Security - Backend Software Engineer (India, onsite)**: asks for 3-6 years, above target band.
- **Sprinto (Bengaluru/Remote)**: only Senior Full-Stack (4+ years) and Technical Lead (8+ years) roles are open right
  now; nothing fresher-friendly today.
- **Bloomreach - Software Engineer II (Pulsar Team), India**: current live req at Bloomreach's India team, but "II"
  typically implies 2-4 years; worth a look only as a stretch shot.

## Process note for next sweep

Before adding a lead to `job-tracker.csv`, do at least one live check (direct fetch or browser open) rather than
trusting the search snippet alone — today's pass would have added ~10 dead links to the tracker without that step.
