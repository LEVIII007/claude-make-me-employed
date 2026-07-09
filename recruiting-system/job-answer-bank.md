# Job Answer Bank

This file stores reusable answers for application forms. Add new answers here whenever Shashank replies in chat.

## Canonical rules

- Primary role target: Software Engineer
- Experience band to target: 0-1 years
- Internship rule: only if compensation is at least INR 80,000 per month

## Reusable positioning

- Recent CS graduate from IIIT Nagpur
- Fresher with strong internship and project experience
- Strongest areas: backend engineering, distributed systems, infra, realtime systems, and AI-native products
- For reflective long-form questions, prefer the preserved answers in `high-signal-application-responses.md` over ad-lib rewrites.

## Experience snippets

### Mindtickle

- Software Engineering Intern
- Built a bulk learner/module settings update feature with real-time progress tracking
- Worked with AWS Step Functions, Lambda, Go pipelines, and multiple gRPC services
- Led an anti-cheating proctoring integration into assessments
- Worked on production on-call and smaller improvements

### Trench Exchange

- Backend and infra work on a high-performance Solana trading platform
- Built trading automation features
- Built a high-throughput matching engine
- Worked on AI data-processing and model routing

### Verly AI

- Co-founded Verly AI
- AI-native customer support platform across web chat, WhatsApp, and voice
- Includes human escalation, lead generation, and custom integrations

## Learned answers

- Question: Should we skip roles that mention IIT/NIT-tier style expectations?
- Answer: No. Still consider and pursue them when the fit is otherwise strong; IIIT Nagpur should be treated as comparable for search and triage purposes. If an application asks an explicit institute eligibility question, answer truthfully.
- Scope: safe default
- Date learned: 2026-06-22

- Question: What email should be used by default on applications?
- Answer: Use `tyagishashank118@gmail.com` unless Shashank explicitly says otherwise.
- Scope: safe default
- Date learned: 2026-06-22

- Question: What notice period should be used by default on applications?
- Answer: Use `Immediate / 0-15 days`.
- Scope: personal profile default
- Date learned: 2026-06-22

- Question: What expected compensation should be used by default on applications?
- Answer: Use `18-20 LPA+` unless the form forces a different format.
- Scope: personal profile default
- Date learned: 2026-06-22

- Question: What current compensation should be used by default on applications?
- Answer: Use `0 (intern)`.
- Scope: personal profile default
- Date learned: 2026-06-22

- Question: What GPA should be used by default on application forms?
- Answer: Use `7.0 / 10`.
- Scope: personal profile default
- Date learned: 2026-06-22

- Question: What gender should be used by default on application forms?
- Answer: Use `Male` unless Shashank explicitly says otherwise.
- Scope: personal profile default
- Date learned: 2026-06-22

- Question: What address should be used when a form splits location into address fields for India?
- Answer: Country `India`, Address Line 1 `Bellandur`, City `Bengaluru`, State `Karnataka`, Postal Code `560103`.
- Scope: personal profile default
- Date learned: 2026-06-22

- Question: If a form asks for notice period in days instead of a text phrase, what should be used?
- Answer: Use `0`.
- Scope: personal profile default
- Date learned: 2026-06-23

- Question: If a form asks for expected salary as free text rather than a strict number, what should be used?
- Answer: Use `18-20 LPA`.
- Scope: personal profile default
- Date learned: 2026-06-23

- Question: How should work authorization be answered for India and international roles?
- Answer: Shashank is authorized to work in `India`. For onsite roles outside India, visa sponsorship is required. Remote work from India for non-India employers may still be possible, but do not mark global onsite work authorization as `Yes` unless the question is specifically about India or the applied country is India.
- Scope: high importance, do not overgeneralize
- Date learned: 2026-06-22

- Question: How should relative-check questions be answered?
- Answer: `No` for both close-relative and extended-relative employment questions.
- Scope: Qualcomm-specific
- Date learned: 2026-06-22

- Question: What additional note should be used by default when a software engineering application includes an open text field?
- Answer: Use a short summary centered on internships and real production work: IIIT Nagpur CS background, Mindtickle backend work with Go/AWS/gRPC/WebSockets, TrenchExchange backend and low-latency systems with Go/Kafka/Redis/PostgreSQL/ClickHouse, Heizen GenAI tooling with FastAPI/NestJS/TypeScript, and strong backend plus full-stack product execution. End by tailoring one sentence to the target role/company.
- Scope: reusable default, tailor the final sentence
- Date learned: 2026-06-23

- Question: How should work experience descriptions be written on application forms by default?
- Answer: Do not use 2-3 line summaries when stronger detail is available. Use 4-5 crisp point-style sentences per role, centered on ownership, systems, scale, tools, and measurable impact. Prefer the richer internship details already stored in the profile files for Mindtickle, Trench Exchange, and Heizen.
- Scope: high importance, default for all application forms
- Date learned: 2026-06-24

- Question: What should be used for strong reflective prompts such as `What kind of problems do you enjoy?`, `What are you proud of?`, or `Anything else we should know?`
- Answer: Use the preserved long-form responses in `high-signal-application-responses.md` as the primary source. Stay close to the wording. Do not casually shorten, genericize, or remix them unless the form limit forces it.
- Scope: high importance, default for thoughtful free-text application questions
- Date learned: 2026-06-25

## Workflow learnings

- Qualcomm's Eightfold application can look complete while still hiding required address fields under `Application questions` after `Country` is selected.
- Before treating an application draft as complete, rescan all sections and look for inline section errors such as `1 error found`.
- SuccessFactors can parse the resume into employment and education after upload, but the imported rows still need a manual cleanup pass before submission.
- On SuccessFactors, saving the draft successfully is a strong checkpoint before the final `Apply` click.
- When a form asks for role descriptions, default to the richer 4-5 point version of each internship instead of compressing it into a short generic paragraph.
