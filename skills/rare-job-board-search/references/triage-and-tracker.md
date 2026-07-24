# Triage And Tracker

Use this file after leads are found.

## File split

- `seen-jobs.csv`
  - Treat as the canonical discovery ledger.
  - Update it for every verified role, even if the role is weak, stale for now, or not worth applying to yet.
- `job-tracker.csv`
  - Treat as the application pipeline.
  - Keep only roles worth acting on, revisiting, or preserving because they are already in progress.

## Minimum capture fields

- Company
- Company tier
- Role title
- Official link
- Source or board family
- Location
- Remote policy
- Employment type
- Experience clue
- Compensation clue
- Tech stack clue
- Posting freshness
- Why the role fits
- Recommended next step

## Seen-jobs minimum fields

- First seen date
- Last seen date
- Latest source
- Company
- Role title
- Official link
- Seen count
- Pipeline status
- Last check result

## Ranking buckets

- `strong fit`
  - The title, seniority, and location clearly fit.
  - The role matches the user's core lane.
  - Internship or project experience is enough, or the role is explicitly new-grad or associate.
  - The company tier or team maturity matches the user's stated priorities.
- `decent fit`
  - The role is relevant, but one area is weaker: title breadth, location, tech stack, or seniority ambiguity.
- `stretch`
  - The role is interesting enough to keep, but the seniority bar or ownership expectations are visibly above target.

## Fast scoring heuristic

- Start at `5/10`.
- Add `2` for direct title match.
- Add `2` for clear experience match or explicit new-grad language.
- Add `1` for strong stack or domain alignment.
- Add `1` for preferred company tier or obvious fresher-friendly team structure.
- Subtract `1-2` for seniority drift, relocation mismatch, compensation below floor, or unclear fit.

## Duplicate handling

- Check `seen-jobs.csv` first before adding a newly discovered role anywhere else.
- Use `company + role + link` as the default duplicate key.
- If the link changes but the company and role are clearly the same, update the existing `seen-jobs.csv` row instead of adding a fresh duplicate.
- If a role is rediscovered, update `last_seen_date`, `latest_source`, and `seen_count` in `seen-jobs.csv`.
- If a local tracker exists, check for the same company plus role before appending.
- Do not overwrite user notes.
- If the same role appears from a different search path, keep the strongest official link and update notes only if the new evidence is better.

## Tracker guidance

- Keep weaker-but-verified roles in `seen-jobs.csv` even when they do not make the application pipeline.
- Keep `why_fit` short and specific.
- Keep `next_step` action-oriented.
- Mark uncertain roles as uncertain instead of pretending they are clean fits.
- Preserve existing statuses such as `new`, `draft_started`, or `applied`.
- Keep board family and freshness notes consistent so duplicate checks stay useful.
