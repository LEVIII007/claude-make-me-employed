# High-Signal Application Responses

Use this file for reflective application questions where stronger long-form answers help.
These responses came from a strong application draft on 2026-06-25 and should be preserved closely.
Do not casually rewrite or compress them unless a form limit forces it.

## Best link to understand your work

Use when a form asks for the best link or best way to understand Shashank's work.

`LinkedIn: https://www.linkedin.com/in/shas007,  GitHub: https://github.com/LEVIII007, Portfolio: https://shashanktyagi.vercel.app , LeetCode: https://leetcode.com/u/shashank_2375,  X: https://x.com/tyagi_Shashankk,  Verly AI ( my own startup ): https://verlyai.xyz, blog: https://medium.com/@tyagishashank118`

## What kind of problems do you enjoy working on?

Use when the prompt asks about problem taste, motivation, or what kind of work is energizing.

`I enjoy working on problems that have some meaningful value behind them. For me, solving a hard engineering problem is much more motivating when I know what gets easier because of it, whether it's saving users hours of manual work, making a system more reliable, or enabling something that wasn't possible before. I don't enjoy complexity for its own sake. I enjoy it when solving that complexity creates a real impact.`

## Anything you've built, broken, or researched that you're proud of?

Use these when the form wants a technical story, a systems story, or a project the user is proud of.

### Mindtickle bulk actions system

`At Mindtickle, I worked as part of a 2 person team building a Bulk Actions system that lets enterprise admins update settings across hundreds of modules and hundreds of thousands of learners with a single operation. Before this, many of these tasks were completely manual.

The problem was that enablement admins had to perform repetitive operations at a massive scale. For example, resetting learner progress for 50,000 users, publishing over 100 modules, or updating due dates across an entire learning program. Each of these involved multiple manual steps, making the process slow and error-prone. From a product perspective, the ask sounded simple. Make it a single click. From an engineering perspective, though, it was much more challenging. We had to support workflows involving up to 1 mil learners, ensure dependent operations executed in the correct order, provide real-time progress to admins, and handle partial failures gracefully without rolling back an entire workflow. For example, a reset operation had to finish before learners could be marked as complete.

Before we started building, we evaluated three different approaches. We first looked at our existing Baton-based queue system because it was already used internally. It was quick to adopt, but it had production stability issues, no dead letter queue support, and no way to model workflow dependencies. We then considered a Kafka-based worker architecture, which was much simpler operationally. However, Kafka has no concept of workflow state or execution ordering, and a single workflow involving hundreds of thousands of learners could easily flood a topic and delay every other workflow. We realized we would end up building our own orchestration layer on top of Kafka. Instead, we chose AWS Step Functions with Lambda and S3 because it gave us native workflow orchestration, built-in retries, isolated execution for every workflow, and visual execution graphs that made debugging much easier.

I was involved throughout the project, from the initial design discussions and HLD reviews to implementation, production support, and bug fixes. One of my biggest contributions was building the learner resolution pipeline. Instead of sending explicit learner IDs, admins define filters such as "all learners in the APAC group who haven't completed Module X." I built the backend service that resolves those filters into actual learner IDs by making parallel Dashboard API calls for each module using Go goroutines, paginating through results of up to 5,000 learners per request, and finally deduplicating users across modules.

I also built the processor Lambdas that execute each batch of operations. Each Lambda receives work from Step Functions, processes operations concurrently using a Go semaphore capped at ten in-flight requests, routes each operation to the appropriate downstream gRPC service, and persists the execution results to S3.

Another part of my work was integrating more than ten existing microservices into the orchestration flow. Most of the low-level database APIs already existed. My responsibility was to wire them into the new workflow correctly, handle their different error contracts, and ensure the entire execution remained idempotent so retries were always safe.

Finally, I built the GraphQL service that powered the frontend throughout the bulk actions flow. It exposed workflow status, operation-level progress, and execution results so admins could monitor long-running jobs in real time.

The system now supports workflows involving up to 1 mil learners and more than 100 modules in single workflow, completing operations in around three to five minutes instead of several hours of manual work. What I enjoyed most about the project was that we recognized early that this wasn't a CRUD problem. It was an orchestration problem. That architectural decision influenced almost every technical choice we made and made the system much easier to reason about and operate.`

### Trench Exchange trading system

`At Trench Exchange, I was the only backend developer at an early-stage Solana DEX startup. Before our private beta launch, we needed core trading automations — copy trading, limit orders, and take-profit/stop-loss. These were on the critical path, and I built the entire system myself.
I started with the API layer where users configure their strategies, designed the database schemas for storing orders, and built a matching engine in Go that processes around 2,000 events per second. The transaction service executes trades on Solana in under a second.
One part I'm genuinely proud of is that I had zero Solana experience when I started. I learned the ecosystem from scratch, understood how different DEX protocols worked, implemented the transaction logic myself, and then packaged it into a reusable library so the rest of our backend could integrate with multiple protocols over time without duplicating that logic.
The hardest part was copy trading at scale. Supporting a single follower copying a wallet is straightforward. Supporting hundreds of users following the same wallet, each with different position sizes, slippage limits, and risk settings, is not. The execution pipeline gets complex fast. To keep latency low, I built a multi-layer in-memory cache that filtered out orders which didn't need to trigger, so only relevant automations reached the matching engine. I also had to handle hundreds of simultaneous triggers, support order cancellations while execution was already in progress, prevent race conditions between concurrent workers, and keep the cache and database in sync. I made a deliberate architecture decision to keep automation types pluggable so adding a new order type later wouldn't require refactoring the core pipeline.
APIs were in NestJS and TypeScript, matching engine in Go, RedPanda for cache synchronization across services. We shipped on time, and copy trading became the most-used feature on the platform, consistently hitting sub-second execution latency.
It was my first time building a trading system and my first time working seriously with Go at this scale. There are things I'd design differently now, but we shipped something that worked reliably in production.`

## Anything else we should know

Use when the prompt asks for extra context, strengths, or anything notable outside the main resume bullets.

`One thing I'd like to mention is that I learn very quickly. If I don't know something today, I'm pretty confident I can pick it up before it becomes a blocker. That's how I learned Solana from scratch at Trench Exchange, and it's also why I enjoy working on unfamiliar problems.

I also spend a lot of time experimenting with AI tools like Claude to improve how I build software. At my current workplace, teammates often ask me to share my workflows, prompts, and techniques because they've found them useful.

Outside of engineering, I've developed a real interest in product and UX. While building Verly AI, I talked to more than 50 users, watched where they got stuck, collected feedback, and kept improving the product based on those conversations. That experience taught me that writing good code is only part of the job. Understanding how people actually use what you build is just as important.`
