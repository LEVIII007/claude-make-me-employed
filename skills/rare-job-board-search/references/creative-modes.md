# Creative Modes

Use this file when the first ATS-board sweep is thin, repetitive, or stale.

## 1. Hidden-junior title mode

Use less obvious early-career titles after the standard `software engineer` and `backend engineer` passes:

- `software engineer i`
- `software engineer 1`
- `SDE 1`
- `SDE-1`
- `junior software engineer`
- `graduate software engineer`
- `graduate engineer`
- `entry level software engineer`

Keep these in smaller packs so the query stays readable.

## 2. Company-seeded discovery mode

Start from a company list instead of a board domain when:

- the user already has preferred company tiers
- direct board sweeps keep surfacing stale results
- you want fresher roles from a short list of target companies

For each company, run at least two searches:

- company plus careers language
- company plus ATS vendor language

Example pattern:

```text
"Company Name" (careers OR jobs OR hiring) ("software engineer" OR "backend engineer" OR "SDE I") ("India" OR "Remote")
```

Example vendor-discovery pattern:

```text
"Company Name" (Ashby OR Lever OR Greenhouse OR Workday OR Teamtailor OR Recruitee) ("software engineer" OR "backend engineer") ("India" OR "Remote")
```

## 3. Custom-domain recovery mode

Some employers use branded careers domains instead of obvious ATS-board domains.

- Search `company name` plus `careers`, `jobs`, and the likely role title.
- If a branded careers domain appears, rerun with `site:jobs.company.com` or `site:careers.company.com`.
- Feed discovered domains back into `scripts/build_queries.py` with `--site`.

## 4. Stale-snippet recovery mode

When Google returns an expired ATS page that still looks promising:

- rerun the search with the company name and role title, but without the original board restriction
- search the company careers site directly
- check whether the role was reposted under a nearby title, location, or requisition

This often recovers a live replacement listing even when the original indexed URL is dead.

## 5. Social-to-official mode

Use founder, recruiter, or engineering-lead posts only as discovery hints.

- Search X or LinkedIn for `hiring`, `backend`, `software engineer`, `India`, `remote`, or company names.
- Do not log or recommend the job until the official page is found.
- If the post names the company but not the link, switch immediately into company-seeded discovery mode.

## 6. Adjacent-role mode

When pure backend roles are scarce, widen into nearby lanes only if the JD stays junior-friendly:

- platform engineer
- infrastructure engineer
- production engineer
- developer productivity engineer
- integrations engineer
- reliability engineer

Keep these as secondary passes, not the default first search.
