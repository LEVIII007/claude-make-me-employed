---
name: rare-job-board-search
description: Find jobs by searching direct ATS boards with Google `site:` and boolean queries instead of relying on LinkedIn alone. Use when Codex needs to discover current openings on Ashby, Lever, Greenhouse, Workday, SmartRecruiters, Jobvite, BambooHR, JazzHR, Workable, or iCIMS; expand beyond plain board sweeps with company-seeded searches, custom career domains, hidden-junior title variants, and social-to-official discovery; adapt searches to the user's role, location, and skill preferences; verify official listings; rank fresher-friendly backend, platform, infrastructure, or general software roles; avoid duplicates; and update local `seen-jobs.csv` and `job-tracker.csv` files with fit notes.
---

# Rare Job Board Search

Use Google `site:` sweeps across ATS boards to surface roles that never hit LinkedIn or stay much less crowded there. Start from direct boards, verify the official listing, and return a ranked batch instead of raw search noise.

## Lock The Search Target First

- Read the user's target role, level, location, compensation floor, remote preference, and work authorization constraints first.
- If the workspace contains these files, read them before searching:
  - `recruiting-system/job-search-preferences.md`
  - `recruiting-system/candidate-profile.md`
  - `recruiting-system/search-playbook.md`
  - `recruiting-system/seen-jobs.csv`
  - `recruiting-system/job-tracker.csv`
- Read `references/default-profile.md` when the workspace is missing the local preference files.
- Use the preferences and profile to widen titles, locations, and skill terms without widening into obvious poor fits.
- Widen titles before seniority, and widen locations before accepting clearly weak-fit titles.
- Use `seen-jobs.csv` as the canonical discovery-memory file for duplicate checks.
- Use `job-tracker.csv` as the application pipeline and source of prior notes on roles already worth acting on.

## Google-First Workflow

1. Generate queries.
- Start with `site:<board-domain>` plus boolean groups for title, location, experience, and skills.
- Use `scripts/build_queries.py` when you want a fast first batch of board-specific Google queries.
- Read `references/query-patterns.md` when you need manual boolean patterns, board-specific variations, or company-tier search passes.
- Use domain-only `site:` syntax such as `site:jobs.ashbyhq.com`, not full `http://...` URLs.

2. Run creative expansion passes when the first sweep plateaus.
- Read `references/creative-modes.md`.
- Do not keep rerunning the same obvious `backend engineer` queries across every board.
- Use hidden-junior title packs when core titles are crowded or dry.
- Use company-seeded discovery queries when you already know the company tier or target list you want.
- Use custom-domain searches when an employer likely has a branded careers page instead of a plain ATS domain.
- Use social-to-official loops when founders, recruiters, or engineering leads hint at hiring before the role is easy to find by board domain alone.
- Use `scripts/build_queries.py --company ... --title-pack ...` when you want these extra passes generated quickly.

3. Search current openings.
- Job listings change often, so use live web search and open the official listing before presenting it as a lead.
- Prefer official application pages over mirrors, reposts, and aggregator summaries.
- Search boards in this order unless the user asks for something different:
  - Startup-heavy: Ashby, Lever, Greenhouse, Workable, JazzHR, BambooHR
  - Mixed: SmartRecruiters, Jobvite, Lever, Greenhouse
  - Larger employers: Workday, iCIMS, SmartRecruiters, Jobvite
- Rotate through multiple board families when the user wants volume. Do not stop after the first board that returns a few matches.
- Read `references/platforms.md` when you need board domains, board-family guidance, or custom-domain help.

4. Verify and triage.
- Confirm title, location, remote policy, experience bar, and whether the role appears open.
- Capture compensation and tech-stack clues when visible.
- Reject clearly senior roles unless the user asked for stretch targets.
- Mark results as `strong fit`, `decent fit`, or `stretch`.
- Prefer backend-heavy, general software engineering, platform, and infrastructure roles.
- Treat some `1-2 years` roles as stretch when internships or projects can plausibly substitute.
- Keep founding-engineer roles only when the scope still looks realistic for a fresher.
- Enforce the user's internship compensation floor when that information is visible.
- Read `references/triage-and-tracker.md` for capture fields and a lightweight scoring rubric.

5. Return a usable batch.
- For volume requests, aim for 10-20 ranked leads rather than stopping at 3-5.
- For each lead, include company, company tier, role, official link, source board, location or remote policy, experience clue, freshness clue, and why it fits.
- If `recruiting-system/seen-jobs.csv` exists, update or append every verified role there, even if it is not strong enough for the application pipeline.
- If `recruiting-system/job-tracker.csv` exists, append only pipeline-worthy non-duplicate rows there and keep notes short and actionable.

## Search Heuristics

- Treat LinkedIn as optional validation or outreach support, not the main discovery surface.
- Expect direct ATS boards to be less saturated than LinkedIn for many early-career roles.
- Assume startup roles may live only on direct boards, founder posts, or company career pages.
- Prefer direct application pages.
- Prefer recent postings when freshness is visible.
- Count internships and academic projects when the JD explicitly allows them.
- When the user is a fresher, widen titles before widening seniority:
  - `Software Engineer`
  - `Backend Engineer`
  - `Software Development Engineer`
  - `SDE I`
  - `Associate Software Engineer`
  - `Platform Engineer`
  - `Infrastructure Engineer`
  - `Founding Engineer` only when the JD still looks realistic
- Expand one dimension at a time: titles first, then locations, then skills, then experience bands.
- When a role is interesting but more senior, flag it as `stretch` instead of silently dropping it.

## Resources

- `references/default-profile.md`
  - Use as a fallback search target when local preference files are missing.
- `scripts/build_queries.py`
  - Build board-specific Google queries from titles, locations, skills, presets, or custom sites.
- `references/platforms.md`
  - Board families, domains, search order, and custom-domain guidance.
- `references/query-patterns.md`
  - Manual boolean patterns, board-specific examples, and search expansions.
- `references/creative-modes.md`
  - Hidden-junior searches, company-seeded discovery, custom-domain recovery, and social-to-official loops.
- `references/triage-and-tracker.md`
  - Capture fields, ranking rules, and `seen-jobs.csv` / `job-tracker.csv` update guidance.

## Failure Modes To Avoid

- Searching only LinkedIn or only one ATS family.
- Using full URLs inside `site:` queries instead of the cleaner domain form.
- Rerunning only the same obvious titles after the first query family goes stale.
- Ignoring company-seeded or custom-domain passes when direct ATS domains go quiet.
- Returning mirror pages instead of official listings.
- Over-tightening the first search pass until good roles disappear.
- Treating every broad `Software Engineer` result as a real fit.
- Ignoring compensation, work authorization, or location constraints.
- Ignoring company tier or posting freshness when those clues are available.
