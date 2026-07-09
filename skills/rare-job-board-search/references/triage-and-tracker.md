# Triage And Tracker

Use this file after leads are found.

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

- If a local tracker exists, check for the same company plus role before appending.
- Do not overwrite user notes.
- If the same role appears from a different search path, keep the strongest official link and update notes only if the new evidence is better.

## Tracker guidance

- Keep `why_fit` short and specific.
- Keep `next_step` action-oriented.
- Mark uncertain roles as uncertain instead of pretending they are clean fits.
- Preserve existing statuses such as `new`, `draft_started`, or `applied`.
- Keep board family and freshness notes consistent so duplicate checks stay useful.
