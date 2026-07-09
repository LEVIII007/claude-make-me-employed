---
name: india-friendly-sea-job-search
description: Find fresher-friendly software engineering jobs in Singapore, Malaysia, and nearby Southeast Asia or APAC markets that can hire candidates working from India. Use when Codex needs to search, filter, or shortlist backend, platform, infrastructure, or general SWE roles for a 0-1 year candidate, especially remote, India-tagged, contractor, or employer-of-record openings while avoiding clearly senior roles and compensation bands that imply experienced hires.
---

# India Friendly Sea Job Search

Use this skill to turn broad "find me jobs in Singapore or Malaysia that can hire from India" requests into a tight shortlist of realistic roles instead of a pile of aspirational links.

## Quick Start

1. Read local preference files first when they exist:
   - `recruiting-system/job-search-preferences.md`
   - `recruiting-system/candidate-profile.md`
   - `recruiting-system/search-playbook.md`
2. Fall back to [default-profile.md](references/default-profile.md) when those files are missing.
3. Search live sources because job freshness, remote policy, and compensation change quickly.
4. Shortlist only roles that are realistically compatible with a fresher or internship-heavy candidate.
5. Return structured leads, not just links.

## Search Workflow

### 1. Lock the target before searching

Use these defaults unless the user overrides them:

- Prioritize `Software Engineer`, `Backend Engineer`, `Platform Engineer`, `Infrastructure Engineer`, and broad `SWE` titles.
- Treat `0-1 years` as the sweet spot.
- Treat some `1-2 years` roles as stretch only when the wording stays junior-friendly.
- Prefer Singapore and Malaysia first.
- Expand next to Indonesia, Vietnam, Thailand, Philippines, and other SEA/APAC hubs only when the company can hire from India.

### 2. Prefer India-compatible hiring patterns

Prioritize roles with one or more of these signals:

- `Remote - India`
- `Remote in APAC`
- `India`, `Singapore`, and `Malaysia` all listed in the allowed locations
- contractor, EOR, or employer-of-record wording
- global remote companies with clear async or distributed hiring
- explicit acceptance of candidates located in India

Treat these as weaker fits unless the job explicitly mentions sponsorship:

- onsite Singapore or Malaysia roles with no work authorization guidance
- hybrid roles anchored to local office attendance
- roles that say `must be based in Singapore` or `must have work rights`

### 3. Filter for junior realism

Prefer roles where at least two of these are true:

- title includes `software engineer`, `backend engineer`, `associate`, `graduate`, `new grad`, or `entry level`
- experience asks for `0-1` or `1-2` years
- JD mentions mentorship, learning, or working with senior engineers
- internships or projects can plausibly substitute for years of full-time experience
- scope is feature or service ownership, not org-level architecture

Down-rank or skip roles with signals like:

- `senior`, `staff`, `principal`, `lead`, `architect`
- founding engineer expectations that clearly require an independent 2-3 year engineer
- owning greenfield systems alone from day one
- mandatory prior production ownership at scale without room for ramp-up

### 4. Use compensation as a realism check

Do not assume every high-paying remote role is reachable for a fresher.

- Treat explicit compensation around `USD 100k+` base or equivalent as a strong signal that the role is probably not fresher-targeted.
- Keep such roles only when the JD very clearly says `new grad`, `graduate`, `entry-level`, or the company is known to pay unusually high junior comp.
- Treat compensation below the user's stated floor as lower priority, not automatic rejection, unless the user says otherwise.
- For internships, enforce the INR 80k monthly floor when compensation is visible.

### 5. Search in the right places

Start with current job sources that regularly surface SEA hiring:

- LinkedIn
- Wellfound
- JobStreet Singapore
- JobStreet Malaysia
- MyCareersFuture Singapore
- MyFutureJobs Malaysia
- company career pages for target firms

Read [search-sources-and-queries.md](references/search-sources-and-queries.md) for query patterns and market-specific search terms.

### 6. Return a shortlist with fit reasons

For every promising job, capture:

- company
- country or company base
- role title
- source
- posting freshness
- remote policy
- India-hiring evidence
- experience asked
- compensation clue
- why the role fits or fails the target

## Output Standard

When returning results, separate them into:

- `Strong matches`: fresh, India-compatible, fresher-reasonable
- `Stretch matches`: one notable risk, but still worth a look
- `Discard`: attractive on paper but clearly too senior or location-locked

Keep explanations blunt and practical. Do not inflate fit when the role is obviously senior.

## Reference Files

- Read [default-profile.md](references/default-profile.md) when local preference files are absent.
- Read [search-sources-and-queries.md](references/search-sources-and-queries.md) when generating search strings, target boards, or expansion countries.
