# Interview Notes - Natural Spoken Version

## Why the current version is hard to speak

Your original document is strong, but it reads like written content, not spoken conversation.

The main problems are:

- The sentences are too long, so they are hard to remember and hard to say naturally.
- A lot of the ownership is buried inside explanation, so in the interview it is easy to miss what *you* actually built.
- It sounds polished on paper, but not like how someone normally talks under pressure.

For interviews, do **not** try to memorize paragraphs.

Just remember this structure:

1. What was the problem?
2. Why was it hard?
3. What exactly did I do?
4. What was the result?
5. What did I learn?

---

## Short Intro

Hi, I’m Shashank. I recently graduated in Computer Science from IIIT Nagpur, and over the last couple of years I’ve mainly worked on backend systems.

Right now I’m a software engineering intern at Mindtickle, where I work mostly with Go, AWS, and distributed backend systems. A lot of my work has been around taking product ideas that sound simple on the surface, and then building the backend systems needed to make them reliable at scale.

Two of the projects I’ve worked on there are Bulk Actions and the Voice and Language platform for AI Roleplay. In Bulk Actions, I worked on a workflow system that lets admins update settings across huge numbers of learners and modules in one operation. In the voice platform project, I helped move hardcoded voice and language configs into a centralized system so multiple services could use a single source of truth.

Before Mindtickle, I worked at Trench Exchange, which was a Solana trading startup. There I built latency-sensitive backend systems for features like copy trading, limit orders, and take-profit and stop-loss.

The common theme across my work has been backend engineering, scalability, reliability, and designing systems that are practical in production.

---

## Intro - shorter version

Hi, I’m Shashank. I recently graduated from IIIT Nagpur, and I’ve been mainly focused on backend engineering.

At Mindtickle, I work on Go and AWS based backend systems. The two projects I usually talk about are Bulk Actions and the Voice and Language platform for AI Roleplay. Before that, at Trench Exchange, I built trading automation systems like copy trading and limit orders. Across these roles, I’ve mostly worked on scalable backend systems, reliability, and production-focused engineering.

---

## Project 1 - Bulk Actions

### Natural version

One of the main projects I worked on at Mindtickle was Bulk Actions. The idea sounds simple: let an admin update settings across a very large number of learners or learning modules in one go.

But in practice, it was a hard backend problem. A single action could involve hundreds of modules and even millions of learner-level updates. Some steps also depended on others. For example, one operation had to finish before another could start. So this was not just a CRUD feature. It was really a workflow orchestration problem.

I worked on a lot of the core backend pieces of that system.

One thing I owned was the learner resolution pipeline. In the UI, the admin might click something like "select all learners matching this filter" and then exclude a few people. The frontend does not actually send every learner ID, because that could be huge. So I built the backend flow that takes that compact selection intent, resolves it into actual learner IDs, deduplicates them, and turns them into execution batches.

I also built processor Lambdas that handled those batches. They took work from the orchestration layer, processed multiple operations concurrently, called the right downstream gRPC services, and stored execution state so we could track progress reliably.

Another part I worked on was integrating a lot of existing microservices into the workflow. The challenge there was not just wiring them together. We had to make sure retries were safe, operations were idempotent, and failures in a few items did not break the whole workflow.

I also built GraphQL APIs for the frontend so admins could see workflow status, live progress, and audit details while the job was running.

From an architecture point of view, we evaluated a few options and chose Step Functions because we needed proper workflow orchestration, dependency handling, retries, and visibility. That saved us from building that machinery ourselves.

The final system could handle very large workflows involving millions of learner updates and complete them in minutes instead of admins doing all of that manually over hours.

### Very short version

At Mindtickle, I worked on Bulk Actions, which let admins update settings across huge numbers of learners and modules in one workflow. The hard part was that these jobs could involve millions of updates with dependencies between steps.

I built key backend pieces including the learner resolution pipeline, processor Lambdas, service integrations, and GraphQL APIs for progress tracking. We used Step Functions for orchestration, and the result was that very large admin operations became reliable and scalable instead of manual and time-consuming.

### What to emphasize if they ask "what exactly did you do?"

- I built the learner resolution pipeline.
- I built processor Lambdas for batch execution.
- I integrated downstream gRPC services into the workflow.
- I worked on idempotency and retry safety.
- I built GraphQL APIs for live progress and audit details.

### Good human way to say ownership

Instead of saying:
"I worked across most parts of the system."

Say:
"I was involved in a lot of the core backend work. The biggest pieces I personally built were the learner resolution pipeline, the processor Lambdas, and the APIs for workflow tracking."

---

## Project 2 - AI Roleplay Voice and Language Platform

### Natural version

Another project I’m proud of at Mindtickle was the Voice and Language platform for AI Roleplay.

AI Roleplay is basically a product where learners practice realistic conversations with AI personas, so voice quality and language support are a big part of the experience.

The problem was that voice and language configuration was hardcoded across multiple services. So if the product team wanted to add a new language, change a voice, or update a provider voice ID, engineers had to touch multiple repos, raise multiple PRs, and coordinate deployments. It was slow and painful.

There was also an operational issue. Voice providers sometimes deprecate voices, and when that happened, services would silently fall back to something else. So customers could suddenly hear a different voice in their roleplays, and we would often only find out after they complained.

That’s why we realized this was not just a refactoring problem. It was really a lifecycle management problem.

I worked across the full implementation of the new system. I designed the database schema, built the gRPC APIs, migrated services away from hardcoded configs, and implemented the lifecycle management side as well.

I also built Kubernetes scheduled jobs that periodically checked for upcoming voice deprecations. When a voice was about to be removed, the system would mark it, figure out which tenants were affected, and trigger proactive communication so customers had time to choose a replacement.

One design choice we made was that we did not automatically replace a deprecated voice permanently. We felt voice is part of a customer’s persona and brand experience, so blindly switching it could create a bad experience. Instead, we kept the system working with a safe language-compatible fallback, while still notifying the customer and asking them to choose the replacement themselves.

The end result was that adding a new language or voice became a configuration change instead of a multi-repo engineering effort. Multiple services moved to a single source of truth, and we also made the system much more operationally safe.

### Very short version

I worked on redesigning the Voice and Language platform for AI Roleplay at Mindtickle. Earlier, voice and language configs were hardcoded across many services, which made even small updates slow and error-prone.

I helped build a centralized database-backed platform with gRPC APIs, migrated services to use it, and built scheduled jobs for voice deprecation handling. That turned multi-service code changes into simple configuration updates and also improved how we handled provider voice deprecations.

### What to emphasize if they ask "what exactly did you do?"

- I designed the database schema.
- I built the gRPC APIs.
- I migrated multiple services away from hardcoded configs.
- I built lifecycle management for voice deprecations.
- I built Kubernetes scheduled jobs for automation.

---

## Project 3 - Trench Exchange

### Natural version

Before Mindtickle, I worked at Trench Exchange, which was an early-stage Solana trading startup. I was the only backend developer there, and I built some of the core trading automation systems before the private beta launch.

The main features I worked on were copy trading, limit orders, and take-profit and stop-loss. These were important product features, and I built the system end to end.

I started from the API layer where users configured their strategies, designed the database schemas for storing orders, and then built the matching engine in Go that processed trading events at high throughput.

I also built the transaction execution service for Solana. One thing I’m particularly proud of is that I had no Solana background when I joined. I learned the ecosystem from scratch, understood how the DEX protocols worked, implemented the transaction layer myself, and then turned that into a reusable library so the rest of the backend could support multiple protocols more cleanly.

The hardest part was copy trading at scale. Supporting one user copying a wallet is easy. Supporting hundreds of users following the same wallet, each with different position sizes, slippage settings, and risk rules, is much harder.

To keep latency low, I built a multi-layer in-memory cache so we could quickly filter out orders that did not need to trigger. That meant only relevant automations reached the matching engine. I also had to deal with concurrent triggers, order cancellations during execution, race conditions, and cache consistency with the database.

I made the architecture modular so new automation types could be added later without rewriting the core pipeline.

We shipped on time, and copy trading became the most-used feature on the platform with sub-second execution latency.

### Very short version

At Trench Exchange, I was the only backend developer and built core trading automations like copy trading, limit orders, and take-profit and stop-loss.

I built the APIs, data models, matching engine in Go, and the Solana transaction execution layer. The hardest part was making copy trading work at scale with low latency and concurrency safety. We shipped it on time, and it became the most-used feature on the platform.

### What to emphasize if they ask "what exactly did you do?"

- I built the APIs for strategy configuration.
- I designed the order storage schema.
- I built the matching engine in Go.
- I built the Solana transaction execution layer.
- I built caching and concurrency handling for low-latency copy trading.

---

## A better way to answer in interviews

Do not try to say the full polished version from memory.

Use this format:

### 30-second answer

- What was the project?
- Why was it hard?
- What did I personally build?
- What was the result?

### 2-minute answer

- Short product context
- Core technical challenge
- My specific contribution
- Architecture decision or tradeoff
- Impact and learning

---

## Simple formula you can memorize

"The problem was ___. It was challenging because ___. My main contribution was ___, ___, and ___. We chose ___ because ___. The result was ___."

Example:

"The problem was letting admins update settings across massive numbers of learners and modules in one go. It was challenging because the workflows involved millions of updates and dependencies between steps. My main contribution was building the learner resolution pipeline, processor Lambdas, and progress APIs. We chose Step Functions because we needed orchestration and retries out of the box. The result was that these operations became reliable and scalable instead of manual."

---

## Final advice

In interviews, the goal is not to sound polished. The goal is to sound clear, real, and confident.

A good answer should sound like:

"Here’s what the problem was. Here’s why it was hard. Here’s what I personally built."

That is much stronger than sounding overly formal.
