# Recruiting System

This folder is the working memory for Shashank's job search.

## Current goal

- Primary target: Software Engineer roles
- Experience band: 0-1 years
- Positioning: fresher with meaningful internship and project experience
- Internship rule: consider internships only if compensation is at least INR 80,000 per month

## How we will operate

1. Discover jobs from LinkedIn, X, company pages, and referrals.
2. Save every verified role in `seen-jobs.csv` so discovery memory does not reset.
3. Move only promising roles into `job-tracker.csv` instead of applying blindly.
4. Score jobs based on fit, freshness, and compensation.
5. Apply using the default profile and resume, with human review before final submission.
6. Save every new answer or correction from chat so future applications get easier.

## Human-in-the-loop rules

- Do not submit an application without a final go-ahead when the page creates an external action.
- If a form asks something new and the user answers it in chat, save that answer in the answer bank.
- Re-check time-sensitive facts before submission.
- Do not reuse uncertain answers as facts.

## Files in this folder

- `candidate-profile.md`: primary source of truth for personal, education, and preference details used in applications
- `job-search-preferences.md`: targeting rules and search priorities
- `job-answer-bank.md`: reusable answers and newly learned answers
- `high-signal-application-responses.md`: preserved long-form answers for thoughtful application prompts where wording quality matters
- `seen-jobs.csv`: canonical memory of every verified role discovered, including roles we decide not to pursue right now
- `job-tracker.csv`: application pipeline for roles we want to act on, revisit, or have already touched
- `search-playbook.md`: repeatable search patterns for LinkedIn and X
- `application-playbook.md`: repeatable browser workflow for filling applications safely and efficiently

## Automation roadmap

### Phase 1: assisted

- Search manually with Shashank's guidance
- Track leads and applications
- Reuse saved profile data

### Phase 2: semi-structured

- Score jobs automatically from saved rules
- Draft tailored short answers
- Flag missing information before applications

### Phase 3: semi-automated

- Use the browser to sweep target searches
- Extract every verified role into `seen-jobs.csv`
- Move only the strongest roles into `job-tracker.csv`
- Deduplicate jobs across LinkedIn, X, and company pages using `seen-jobs.csv` first

### Phase 4: guided automation

- Run repeatable search routines
- Pre-fill routine applications
- Pause only for unknown answers, sensitive data, or final submit

## Operational learnings

- Verify resume upload on one low-stakes form before starting a batch of applications. Do not assume browser file access is working until a real upload succeeds.
- Prefer the user's already signed-in default Chrome tabs and sessions instead of opening fresh login flows when possible.
- On Workday and similar portals, treat each dropdown as stateful and re-check the page after every selection. Repeated `Select One` controls are easy to mis-target.
- Expect forms to rerender or auto-advance. Do not trust stale locators or assumptions from the previous page state.
- Always inspect the final review page before submission. Autofill or default values can be wrong even when the form looks mostly complete.
- Prefer applications that do not require creating a new account when batching. Queue account-gated forms for after the user signs in.
- Only use third-party resume import flows like Indeed, Dropbox, or OneDrive when the user is already signed in there and it is genuinely faster than manual upload.
- If blocked mid-application, keep the live tab open in a handoff state so the next pass resumes from the same point.
- On LinkedIn post searches, treat posts with multiple outbound links as potentially noisy. A second or third link is often a channel, promo, referral, or unrelated ad rather than the true apply destination.
- For LinkedIn roundup posts, do not collapse multiple outbound links into one assumed apply URL. Either save all plausible apply links or verify the real one before writing the lead down.
- On ATS `site:` search sweeps (Ashby, Lever, Greenhouse, SmartRecruiters, Workday, Jobvite, iCIMS), expect a high rate of dead or expired links from Google's index — confirmed roughly 20 of 25 promising titles were expired, 404, or location/seniority-mismatched in the 2026-07-03 pass. Always fetch or open a listing directly before logging it in `seen-jobs.csv` or `job-tracker.csv`; do not trust the search snippet or title alone.
