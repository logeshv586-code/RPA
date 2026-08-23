# RPA-X Product Roadmap

The roadmap keeps RPA-X focused on one coherent product while increasing autonomy in controlled stages.

## Release philosophy

RPA-X should progress from **visibility → diagnosis → recommendation → bounded recovery → adaptive recovery**. We should not jump directly to unrestricted autonomous actions.

## Phase 0 — Foundation

**Status: in progress**

- [x] FastAPI runtime event endpoint
- [x] Failure classification foundation
- [x] Recovery decision foundation
- [x] Live Process Twin foundation
- [x] Evidence Ledger foundation
- [x] Vendor-neutral adapter interface
- [x] Process Genome sample
- [x] Initial tests and CI
- [x] Product architecture and workflow documentation
- [x] RPA-X product identity
- [ ] Persistent operational data store
- [ ] Configuration management
- [ ] Structured logging
- [ ] Docker development environment

## Phase 1 — Command Center MVP

**Goal:** make RPA-X useful in read-only production monitoring before autonomous changes.

- [ ] Unified run ingestion API
- [ ] Automation inventory
- [ ] Process Genome registry + validation
- [ ] Current-run Process Twin persistence
- [ ] Failure timeline
- [ ] Evidence viewer
- [ ] Reliability metrics: success rate, MTTD, MTTR, repeat failures
- [ ] Basic web Command Center
- [ ] Read-only adapter capability discovery

**Exit criteria:** an operations team can see automation health and diagnose a failed run from RPA-X without using autonomous recovery.

## Phase 2 — Automation Anywhere A360 integration

**Goal:** prove the platform against a real enterprise RPA runtime.

- [ ] Secure Control Room authentication adapter
- [ ] Bot execution ingestion
- [ ] Bot / device / runner health
- [ ] Queue and work-item visibility
- [ ] Error evidence ingestion
- [ ] Read-only production mode
- [ ] Retry / requeue capability behind policy
- [ ] Adapter capability tests

**Exit criteria:** RPA-X can monitor A360 production runs and safely execute one or more low-risk recovery actions in a controlled environment.

## Phase 3 — Policy-bounded Recovery Brain

- [ ] Recovery strategy registry
- [ ] Risk scoring model
- [ ] Policy-as-code engine
- [ ] Autonomy levels A0–A4
- [ ] Idempotency checks
- [ ] Human approval queue
- [ ] Recovery workers
- [ ] Outcome validation framework
- [ ] Rollback / stop conditions
- [ ] Complete Evidence Ledger trace

**Exit criteria:** every recovery has evidence, a policy decision, a validator and an auditable outcome.

## Phase 4 — AI Failure Intelligence

- [ ] Pluggable AI provider abstraction
- [ ] Evidence summarization
- [ ] Failure hypothesis generation
- [ ] Candidate recovery generation
- [ ] Confidence calibration
- [ ] Historical failure similarity
- [ ] Prompt/data redaction controls
- [ ] Deterministic fallbacks when AI is unavailable

**Exit criteria:** AI improves diagnosis or ranking while policy remains the final authorization layer.

## Phase 5 — Shadow Lab + UI self-healing

- [ ] DOM evidence model
- [ ] Selector fingerprinting
- [ ] Candidate element discovery
- [ ] Visual / semantic similarity scoring
- [ ] Shadow execution
- [ ] Expected-outcome validation
- [ ] Approved selector memory
- [ ] Developer promotion workflow for permanent selector updates

**Exit criteria:** a selector drift can be safely recovered at runtime without silently modifying source bot packages.

## Phase 6 — Multi-platform control plane

- [ ] UiPath adapter
- [ ] Power Automate adapter
- [ ] Selenium / Playwright adapter
- [ ] Generic REST / API adapter
- [ ] Serverless / Lambda adapter
- [ ] Database and queue connectors
- [ ] ITSM integration
- [ ] Webhook / event streaming integration

**Exit criteria:** the Command Center exposes one normalized automation estate across multiple execution technologies.

## Phase 7 — Enterprise productization

- [ ] SSO / OIDC / enterprise RBAC
- [ ] Tenant isolation
- [ ] Secrets-provider integration
- [ ] HA and horizontal scaling
- [ ] Audit exports
- [ ] Data retention policy
- [ ] Disaster recovery
- [ ] Deployment packages
- [ ] Helm / Kubernetes option
- [ ] Enterprise observability
- [ ] Security threat model

## Phase 8 — Proactive Automation Reliability

- [ ] Failure prediction
- [ ] Repeated-failure clustering
- [ ] SLA breach prediction
- [ ] Capacity and runner forecasting
- [ ] Preventive maintenance recommendations
- [ ] Change-impact detection
- [ ] Automation technical-debt score
- [ ] Recovery ROI / Automation FinOps

## North-star product metrics

| Metric | Direction |
|---|---|
| Automation success rate | ↑ |
| Mean time to recover | ↓ |
| Repeat incidents | ↓ |
| SLA breaches | ↓ |
| Autonomous recovery rate for approved low-risk failures | ↑ |
| Incorrect / unsafe recovery rate | → 0 |
| Time spent on manual production support | ↓ |
| Evidence completeness | → 100% |

## Definition of “top product”

RPA-X should be judged by production reliability, safety, explainability and measurable recovery outcomes—not by the number of AI features in the UI.
