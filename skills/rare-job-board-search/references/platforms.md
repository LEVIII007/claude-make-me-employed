# Platforms

Use this file when deciding which ATS families to search first.

## Core board domains

- `Ashby`: `jobs.ashbyhq.com`
  - Bias toward startups and modern growth-stage companies.
- `Lever`: `jobs.lever.co`
  - Common across startups and mid-size companies.
- `Greenhouse`: `boards.greenhouse.io`
  - Common for venture-backed startups and global tech companies.
- `Workable`: `careers.workable.com`, `apply.workable.com`
  - Useful for smaller startups and international remote teams.
- `JazzHR`: `apply.jazz.co`
  - Useful for smaller companies and less-advertised startup roles.
- `BambooHR`: `jobs.bamboohr.com`
  - Uneven, but worth checking for smaller companies.
- `SmartRecruiters`: `jobs.smartrecruiters.com`
  - Useful for both large companies and mid-size employers.
- `Jobvite`: `jobs.jobvite.com`
  - Good for mid-size companies and occasional early-career openings.
- `Workday`: `wd1.myworkdayjobs.com`, `wd3.myworkdayjobs.com`, `wd5.myworkdayjobs.com`, `wd12.myworkdayjobs.com`
  - Common for larger employers and enterprise companies.
  - Treat Workday as fragmented across many subdomains. Use extra custom domains when you know them.
- `iCIMS`: `careers.icims.com`
  - Useful for bigger or more traditional employers.

## Search order by company type

- For `startup-heavy` requests: Ashby, Lever, Greenhouse, Workable, JazzHR, BambooHR.
- For `late-stage or mixed` requests: Lever, Greenhouse, SmartRecruiters, Jobvite, Ashby.
- For `bigger brands` requests: Workday, iCIMS, SmartRecruiters, Jobvite.
- For `max volume` requests: Ashby, Lever, Greenhouse, Workday, SmartRecruiters, Jobvite, Workable, JazzHR, iCIMS, BambooHR.

## Custom-domain rule

- Expect some employers to hide ATS pages behind custom careers domains.
- Search `company name` plus the ATS family when board-domain queries look thin.
- Pass extra domains to `scripts/build_queries.py` with `--site` when you know the employer domain.

## Verification rule

- Treat search results as discovery only.
- Open the official listing before presenting it as a lead.
- If only mirrors or reposts are visible, mark the lead as unverified until the official page is found.
