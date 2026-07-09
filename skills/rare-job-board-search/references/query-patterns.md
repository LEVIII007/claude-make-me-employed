# Query Patterns

Use this file when building manual searches or refining what `scripts/build_queries.py` prints.

## Quick recipe

- Start with domain-only `site:` syntax such as `site:jobs.ashbyhq.com`.
- Add one boolean group for titles.
- Add one boolean group for locations.
- Add one boolean group for experience terms.
- Add a skill or domain group only when the search is still too broad.
- Add exclusions only after you see noisy results.

## Core pattern

```text
site:<board-domain> (<title variants>) (<locations>) (<experience terms>) (<skills or domain terms>)
```

## Search passes

Use these in order when a search is too broad or too narrow:

1. Search titles plus locations.
2. Add experience language such as `new grad`, `graduate`, or `0-2 years`.
3. Add backend, platform, infra, or language keywords when the board is noisy.
4. Add exclusions such as `-senior -staff -principal` only after you have looked at the first result set.

## Title expansions

Use 3-6 titles at a time. Good default set for fresher software searches:

```text
("software engineer" OR "backend engineer" OR "software development engineer" OR "SDE I" OR "associate software engineer")
```

Add these when the user's profile supports them:

```text
("platform engineer" OR "infrastructure engineer" OR "founding engineer")
```

## Location expansions

For India-wide sweeps:

```text
("India" OR "Remote" OR "Bengaluru" OR "Bangalore" OR "Hyderabad" OR "Pune" OR "Gurgaon" OR "Noida" OR "Chennai")
```

For tighter local sweeps:

```text
("Bengaluru" OR "Bangalore")
```

## Experience expansions

For fresher-friendly searches:

```text
("new grad" OR "graduate" OR "entry level" OR "0-1 years" OR "0-2 years" OR internship)
```

For stretch searches:

```text
("1-2 years" OR "2 years" OR internships OR "academic projects")
```

## Skill expansions

Backend-focused:

```text
("backend" OR APIs OR Golang OR Go OR Python OR Java OR distributed OR "distributed systems" OR platform OR infra)
```

General SWE:

```text
("software engineer" OR backend OR platform OR systems)
```

Enterprise or public-company sweeps:

```text
("associate" OR "graduate" OR "early career" OR "new college graduate")
```

## Example board queries

Ashby:

```text
site:jobs.ashbyhq.com ("software engineer" OR "backend engineer" OR "SDE I") ("India" OR "Remote" OR "Bengaluru") ("new grad" OR "0-2 years" OR internship)
```

Lever:

```text
site:jobs.lever.co ("software engineer" OR "backend engineer" OR "associate software engineer") ("India" OR "Bangalore" OR "Hyderabad") ("0-1 years" OR "0-2 years" OR "new grad")
```

Greenhouse:

```text
site:boards.greenhouse.io ("software engineer" OR "backend engineer" OR "associate software engineer") ("India" OR "Remote" OR "Bengaluru") ("new grad" OR "graduate" OR "0-2 years")
```

Workday:

```text
site:wd5.myworkdayjobs.com ("software engineer" OR "associate software engineer" OR "new college graduate") ("India" OR "Bangalore")
```

SmartRecruiters:

```text
site:jobs.smartrecruiters.com ("software engineer" OR "associate software engineer" OR "new grad") ("Bengaluru" OR "India")
```

JazzHR:

```text
site:apply.jazz.co ("software engineer" OR "backend engineer") ("India" OR "Remote") ("new grad" OR "0-2 years")
```

Custom employer domain:

```text
site:careers.company.com ("software engineer" OR "backend engineer") ("India" OR "Remote") ("new grad" OR "0-2 years")
```

## Boolean guardrails

- Keep each query readable enough to debug.
- Widen one dimension at a time: titles first, then locations, then experience.
- Exclude obvious noise only when needed:

```text
-senior -staff -principal -manager
```

- Do not over-filter early. It is better to gather 15 leads and rank them than to over-tighten and find 3.
- Expect startup roles to show up on direct boards before they show up on LinkedIn, if they show up there at all.
