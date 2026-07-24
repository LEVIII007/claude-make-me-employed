# 2 best problems i have worked on in past few months :

SHORT INTRO ABOUT ME : 

Hi, I'm Shashank. I recently graduated with a B.Tech in Computer Science from IIIT Nagpur, and over the last couple of years I've been focused on building backend systems that operate at production scale.

I'm currently a Software Engineering Intern at Mindtickle, where I've primarily worked on  backend systems in Go and AWS. Most of my work has been around taking product ideas and building the backend infrastructure that makes them production-ready.

One of the larger projects I worked on was **Bulk Settings Updates**, where any company admin can update settings across hundreds of learning modules and millions of learners in a single operation potentially saving hours of effort. Since these workflows can involve millions of updates with ordering dependencies, we built an orchestration system using AWS Step Functions, Lambda, Go services to process them reliably while providing real-time progress tracking and auditability.

Another project I enjoyed was redesigning the **Voice and Language Management** for our AI scnerio based Roleplay product. AI Roleplay allows learners to practice realistic sales or customer support conversations with AI personas across different customer types and sales stages. The challenge was that voice and language configuration was hardcoded across multiple services, making every voice update a multi-day engineering effort. I led the migration to a centralized database-backed platform with gRPC APIs, automated lifecycle management, and Kubernetes scheduled jobs that proactively handle voice deprecations, notify customers before changes, and ensure roleplays continue seamlessly using safe fallback voices.

Before Mindtickle, I worked at **Trench Exchange**, a Solana-based trading startup, where I built latency-critical backend systems for an automated trading platform. I developed the execution pipeline for copy trading, limit orders, take-profit, and stop-loss strategies, where low latency and reliability were fundamental requirements. That experience taught me a lot about writing performance-sensitive Go services, optimizing databases, and designing systems where milliseconds directly impact business outcomes.

Alongside that, I built an AI pipelines that analyzed large volumes of market data from sources like Twitter and Discord. We used multiple LLMs and routing strategies to select the right model for different tasks, improving both response quality and inference cost.

Outside my internships, I'm the Co-founder and CTO of **Verly AI**, where we're building an AI-native customer support platform across web, WhatsApp, and voice. I lead the technical direction of the product, from our graph-based RAG architecture and MCP integrations to custom AI evaluation pipelines that automatically measure response quality and help us continuously improve system performance without relying entirely on manual review.

Across all of these experiences, the common theme has been building systems that are reliable, scalable, and easy to evolve. I enjoy working on backend infrastructure, distributed systems, and increasingly on AI systems where good engineering matters just as much as good models. I'm happy to dive deeper into any of these projects.

**At Mindtickle,** 

# Bulk Actions :

I recently worked on a two-engineer project called **Bulk Actions** at Mindtickle.

To understand the project, it helps to first understand the problem.

Mindtickle is used by large enterprises to train and certify their sales teams. A company can have hundreds of learning modules and hundreds of thousands of learners. As an admin, you often need to perform the same operation across a huge part of the platform. Maybe you want to publish 150 modules, extend due dates for everyone, or reset the learning progress of 500,000 learners after updating the course content.

Before Bulk Actions, all of this had to be done manually. Even something as simple as changing one setting across hundreds of modules could take hours. The product asked us single thing: **make all of this a single action.**

From the admin's perspective, the experience is straightforward.

They start by choosing what they want to update. They can select any number of modules or learners. Selection works much like Gmail. They can search, apply filters, select everything matching a filter, and then exclude a few specific items.

Once the targets are selected, they see every configurable setting in one place. Settings common across all module types appear together, while module-specific settings are grouped into their own tabs because Mindtickle supports more than twenty different module types.

After choosing the new values, the admin gets a confirmation screen showing exactly what will change before anything is executed. They can compare the old values with the new values for every affected setting. Once they confirm, the workflow starts in the background. Progress appears live in the notification drawer, and when everything finishes they receive a detailed audit report showing every successful update, every failed update, and the reason behind each failure.

Making that experience reliable turned out to be much harder than building the UI.

A single workflow could involve over a million learner updates across hundreds of modules. Some operations depended on others. For example, learner progress had to be reset before completion status could be updated. We also wanted admins to see live progress while the workflow was running, and we couldn't fail an entire workflow just because two modules out of two hundred encountered an error.

Very early in the design, we realised we weren't building another CRUD service. We were building a workflow orchestration system.

Before writing any code, we evaluated three different architectures.

Our existing internal queue was the fastest to adopt, but it had production stability issues, no dead-letter queue, and no concept of workflow dependencies.

Kafka looked attractive because the worker model was simple. The problem was that Kafka understands queues, not workflows. It doesn't know that one set of operations must finish before another begins. It also doesn't isolate workflows. A single million-learner job could flood the topic and delay every smaller workflow behind it. We realised we'd end up building our own orchestration engine on top of Kafka.

Instead, we chose AWS Step Functions with Lambda and S3. Step Functions already solved orchestration, retries, workflow state, dependency management, and observability. That let us spend our time solving product problems instead of infrastructure problems.

I worked across most parts of the system, from design discussions through implementation and production support.

One of the biggest pieces I owned was the learner resolution pipeline.

One interesting challenge was that the frontend never actually knew which learners were selected.

Imagine an admin clicks "Select All" on a filter that matches 800,000 learners. Obviously we can't send 800,000 IDs to the browser just so it can remember what's selected.

Instead, the frontend only stores the admin's intent.

If they select everything, we store the filter along with a small exclusion list for the learners they manually deselect. If they manually pick individual learners, we store only those inclusions.

My backend service takes that compact representation and resolves it into actual learner IDs. It fans out Dashboard API requests in parallel using Go goroutines, paginates through thousands of learners at a time, deduplicates users across modules, and finally produces execution batches for the workflow engine.

I also built the processor Lambdas that execute those batches. Each Lambda receives work from Step Functions, processes multiple operations concurrently using Go semaphores, routes every operation to the correct downstream gRPC service, and persists execution state back to S3.

Another part I enjoyed was integrating more than ten existing microservices into the workflow. Most of those services already existed. The challenge wasn't writing new business logic. It was making sure they all behaved correctly inside one orchestration engine, handled retries safely, and remained idempotent.

Finally, I built the GraphQL APIs that powered the frontend throughout the entire execution lifecycle, exposing workflow status, operation-level progress, audit information, and live updates while the workflow was running.

The result was a system that could process workflows involving more than a million learner updates and hundreds of modules in a few minutes instead of several hours of manual work.

### One ambiguity

One ambiguity we had to resolve was what it actually means when an admin says, "I selected these learners."

Sometimes that meant a handful of manually selected users. Sometimes it meant everyone matching a filter except three excluded people. Those are very different things.

Instead of sending large lists of learner IDs back and forth, we decided the frontend would send the user's intent and the backend would resolve that into concrete learner IDs only when execution started. That kept the UI responsive while still allowing us to process extremely large workflows.

### One tradeoff

The biggest architectural tradeoff was choosing Step Functions over Kafka.

Kafka would have been cheaper and operationally simpler, but it doesn't understand workflow dependencies. We would have had to build ordering, retries, workflow state, and progress tracking ourselves.

Step Functions costs more and comes with account-level concurrency limits, but it gave us workflow orchestration, retries, execution history, and much better operational visibility. For this problem, that tradeoff was absolutely worth it.

### One mistake

One mistake I made was assuming every downstream operation behaved synchronously.

That assumption broke when we integrated learner progress reset. The downstream service didn't complete immediately. Instead, it launched its own long-running workflow that could take several minutes.

My processor Lambda ended up waiting for another asynchronous workflow to finish. It worked most of the time, but I had accidentally created a bounded Lambda waiting on an unbounded operation. We reduced batch sizes and added polling with exponential backoff, which made production stable, but afterwards I realised we had only reduced the probability of failure. We hadn't removed the design flaw.

If I were designing it today, I'd do it differently. I'd let the downstream workflow notify Step Functions when it finishes using callback tokens instead of keeping the Lambda alive waiting for completion. That completely removes timeout risk while still preserving workflow ordering.

That experience changed how I think about distributed systems. A mitigation isn't the same thing as a solution.

### One review comment that changed my mind

During one design review, someone asked a simple question:

*"What happens if Step Functions retries this Lambda?"*

Until then, I had been thinking about retries as an orchestration concern.

That question made me realise every downstream service also has to tolerate duplicate requests. We ended up making every operation idempotent using deterministic operation identifiers so retries became safe by design.

That review fundamentally changed how I think about distributed workflows. Retries are never somebody else's responsibility.

### Shipped

The project is internal to Mindtickle, so I can't share the product itself publicly. I'd instead link to a public project or technical article that reflects the kind of engineering work I enjoy building.

# AI Roleplay Voice & Language Platform

## The Product

One project I'm particularly proud of was redesigning the Voice and Language Management system behind **AI Roleplay** at Mindtickle.

AI Roleplay is an AI-powered sales coaching platform where learners practice realistic business conversations instead of simply consuming training content.

A learner might practice making their first cold call, handling objections from a skeptical customer, negotiating pricing, or closing a renewal. Customers can build different personas, industries, and scenarios, and they can configure exactly how those conversations should be evaluated. One customer might care about objection handling, another about empathy, another about product positioning or whether the learner successfully reached the intended business outcome.

The learner speaks with an AI persona using voice, the AI responds naturally, and once the conversation finishes, our evaluation system scores the learner across the configured parameters.

Because the entire experience is conversational, voice quality is a critical part of the product.

---

## The Problem

As AI Roleplay expanded to more languages and voice providers. 

Every supported language, accent, voice ID, and deprecated voice list was hardcoded across more than seven different services. Each service maintained its own copy of the configuration.

If Product wanted to introduce a new language, onboard a new voice from ElevenLabs, or update a provider's voice ID, engineers had to modify multiple repositories, raise several pull requests, coordinate deployments, and verify that every service stayed in sync.

Something that should have been a simple configuration change routinely became **two to three days of engineering work**.

There was an even bigger operational problem.

Voice providers periodically deprecate voices. Whenever that happened, our services silently fell back to a default voice. The platform technically continued working, but nobody inside Mindtickle knew that a customer's AI persona had changed voices. We usually found out only after the customer reported that their roleplay suddenly sounded different.

That was the biggest insight from the project.

The problem wasn't that voices were hardcoded.

The problem was that voices had no lifecycle management.

---

## Our Goal

We wanted to completely separate configuration from code.

Instead of every service maintaining its own voice catalog, we wanted a single platform responsible for managing languages, voices, provider metadata, deprecations, and future extensions.

Every other service should simply ask one question:

*"What are the supported voices for this language?"*

instead of maintaining its own hardcoded copy.

---

## The Solution

I designed a centralized Voice Management platform backed by a database.

The platform stores supported languages, voices, speech-to-text configuration, and voice feedback.

On top of the database, I built a gRPC service that became the single source of truth for voice information.

Every service that previously depended on hardcoded constants was migrated to fetch voice and language information through this service instead.

Once that migration was complete, adding a new language or voice no longer required touching multiple repositories or deploying several services. It became a configuration change instead of a software release.

!image.png

```jsx
{
"id": "ELEVENLABS_VOICE_182",
"provider_voice_id": "abcd",
"provider_type": "11labs",
"name": "Eryn",
"gender": "female",
"accent": "American",
"description": "",
"verified": true,
"is_active": true,
"language_id": "english",
"language_name": "english",
"created_time": 1717000000000,
"updated_time": 1717000000000
}
```

---

## Automating Voice Lifecycle

Moving everything into a database solved only half the problem.

Voice providers continuously introduce new voices and retire existing ones. If engineers still had to manually update the database every time that happened, we had only moved the maintenance burden somewhere else.

To solve that, I built Kubernetes scheduled jobs that automate the voice lifecycle.

The scheduler periodically scans the voice catalog looking for voices that are approaching their deprecation window.

When a voice enters its notice period, the scheduler marks it as deprecated and identifies every tenant and AI persona currently using that voice.

Those customers automatically receive an email informing them that the voice will be removed in seven days and asking them to select a replacement.

One interesting design discussion was whether we should automatically replace deprecated voices.

We intentionally decided not to.

A voice is part of a customer's AI persona and brand experience. Automatically switching to another voice could completely change how conversations feel.

Instead, until the customer selects a replacement, we temporarily assign a language-compatible fallback voice so that roleplays continue working without interruption while giving customers enough time to migrate.

---

## My Contribution

This project took roughly two months and touched more than seven services.

I worked across the entire implementation.

I designed the database schema, built the gRPC APIs, migrated existing services away from hardcoded configurations, implemented the voice lifecycle management, and built the Kubernetes scheduled jobs that automate deprecation handling.

I was also involved in the initial design discussions where we identified that this wasn't simply a refactoring exercise. We were building a platform that other services could depend on.

---

## Result

The impact was much larger than simply removing hardcoded constants.

Adding a new language or voice became a configuration update instead of a deployment.

Multiple services now consume a single source of truth instead of maintaining duplicate configuration.

Customers receive proactive notifications before their voices are deprecated instead of discovering the issue themselves.

And the platform now has a foundation for future capabilities like automated provider synchronization, voice quality monitoring, and richer feedback-driven voice management.

---

## What I Learned

The biggest lesson from this project was that we weren't solving a storage problem.

We were solving a lifecycle management problem.

Once we started treating voices as a managed platform instead of static configuration inside source code, everything became much easier to reason about.

Good platform engineering isn't just about moving data into a database.

It's about centralizing ownership, lifecycle, and operational responsibility so the rest of the system becomes simpler.

**2nd : ( Trench Exchange Internship ) :**

At Trench Exchange, I was the only backend developer at an early-stage Solana DEX startup. Before our private beta launch, we needed core trading automations — copy trading, limit orders, and take-profit/stop-loss. These were on the critical path, and I built the entire system myself.
I started with the API layer where users configure their strategies, designed the database schemas for storing orders, and built a matching engine in Go that processes around 2,000 events per second. The transaction service executes trades on Solana in under a second.
One part I'm genuinely proud of is that I had zero Solana experience when I started. I learned the ecosystem from scratch, understood how different DEX protocols worked, implemented the transaction logic myself, and then packaged it into a reusable library so the rest of our backend could integrate with multiple protocols over time without duplicating that logic.
The hardest part was copy trading at scale. Supporting a single follower copying a wallet is straightforward. Supporting hundreds of users following the same wallet, each with different position sizes, slippage limits, and risk settings, is not. The execution pipeline gets complex fast. To keep latency low, I built a multi-layer in-memory cache that filtered out orders which didn't need to trigger, so only relevant automations reached the matching engine. I also had to handle hundreds of simultaneous triggers, support order cancellations while execution was already in progress, prevent race conditions between concurrent workers, and keep the cache and database in sync. I made a deliberate architecture decision to keep automation types pluggable so adding a new order type later wouldn't require refactoring the core pipeline.
APIs were in NestJS and TypeScript, matching engine in Go, RedPanda for cache synchronization across services. We shipped on time, and copy trading became the most-used feature on the platform, consistently hitting sub-second execution latency.
It was my first time building a trading system and my first time working seriously with Go at this scale. There are things I'd design differently now, but we shipped something that worked reliably in production.