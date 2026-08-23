<p align="center">
  <img src="assets/rpa-x-logo.svg" alt="RPA-X — Autonomous Automation Control Plane" width="900" />
</p>

<h3 align="center">The Autonomous Reliability & Intelligence Layer for Enterprise Automation</h3>

<p align="center"><strong>Observe · Understand · Decide · Heal · Govern · Learn</strong></p>

---

# RPA-X

**RPA-X** is being built as a single, vendor-neutral enterprise product for operating automations across RPA platforms, APIs, browsers, desktops, queues and serverless workloads.

It is not another bot designer. RPA-X sits **above automation runtimes** and gives the automation estate one intelligence, reliability, recovery and governance control plane.

> **North-star:** move enterprise automation from **run → fail → ticket → investigate → fix → restart** to **run → observe → understand → recover → validate → learn** — without sacrificing human control, security or auditability.

## Why RPA-X exists

Production automation support is still highly reactive. A selector moves, an API slows down, a session expires, a queue item is corrupted, a VM becomes unhealthy, or an application changes. The bot fails, an incident is created, and a human reconstructs what happened.

RPA-X is designed to turn that fragmented support model into a unified reliability loop.

```mermaid
flowchart LR
    A[Automation executes] --> B[RPA-X observes]
    B --> C[Live Process Twin]
    C --> D[Failure Intelligence]
    D --> E[Recovery Brain]
    E --> F{Policy + Risk}
    F -->|Low-risk allowed| G[Auto-heal]
    F -->|Approval required| H[Human Control Gate]
    H --> G
    G --> I[Outcome Validation]
    I --> J[Evidence Ledger]
    J --> K[Recovery Memory]
    K --> B
```

## One product, one control plane

RPA-X is intentionally designed as **one coherent platform**, not separate tools stitched together.

| Product capability | What it does |
|---|---|
| **Command Center** | One operational view of bots, processes, transactions, failures, SLAs and recovery status |
| **Process Genome Studio** | Defines automation intent, expected outcomes, dependencies, known exceptions and safe recovery strategies |
| **Live Process Twin** | Maintains a real-time model of where an automation is versus where it should be |
| **Failure Intelligence** | Diagnoses business, application, API, data, credential, infrastructure and unknown failures |
| **Recovery Brain** | Ranks recovery strategies using evidence, history, confidence and platform capabilities |
| **Shadow Lab** | Tests candidate recoveries before they are trusted in production |
| **Human Control Gate** | Routes medium/high-risk actions for approval instead of blindly executing them |
| **Evidence Ledger** | Records what happened, why a decision was made, what policy allowed it and whether it worked |
| **Recovery Memory** | Learns from validated recoveries and recognizes repeated failure patterns |
| **Integration Fabric** | Normalizes Automation Anywhere, UiPath, Power Automate, Selenium, APIs, queues and infrastructure |
| **Policy & Governance** | Controls autonomy levels, risk, RBAC, secrets, environment restrictions and auditability |
| **Automation FinOps** | Target capability for support cost, reliability, utilization and business value metrics |

See the full **[Product Blueprint](docs/PRODUCT_BLUEPRINT.md)**.

## The core innovation model

### 🧬 Process Genome

A versioned, machine-readable description of the automation's **intent**, not only its implementation.

A Genome can describe business outcome and owner, process steps, expected outcomes, applications, APIs, selectors, data contracts, SLAs, known exceptions, recovery playbooks, risk classification and approvals.

### 🛰️ Live Process Twin

A runtime representation assembled from the Process Genome + current events + execution evidence. It answers where the run is now, what should happen next, which dependency changed, what evidence is available and whether recovery is still safe.

### 🧠 Failure Intelligence

Failure diagnosis is normalized across platforms rather than being tied to one bot vendor.

Target classes include:

`business` · `application` · `selector/UI drift` · `api` · `data` · `credential` · `infrastructure` · `queue` · `timeout` · `unknown`

### ⚡ Recovery Brain

The Recovery Brain does not simply retry everything. It evaluates evidence, previous outcomes, available adapter capabilities, idempotency, confidence, risk and policy.

Potential strategies include bounded retry, resume from checkpoint, requeue, session refresh, approved selector fallback, alternate API route, business-exception routing, circuit breaker, human approval and evidence-rich escalation.

### 🛡️ Policy-bounded autonomy

AI confidence is **not** permission.

```mermaid
flowchart TD
    A[Recovery candidate] --> B[Confidence score]
    A --> C[Risk score]
    B --> D[Policy Engine]
    C --> D
    D -->|Denied| E[No execution]
    D -->|Approval| F[Human Control Gate]
    D -->|Allow-listed low risk| G[Recovery Executor]
    F -->|Approved| G
    F -->|Rejected| E
    G --> H[Outcome Validator]
    H -->|Success| I[Evidence + Learning]
    H -->|Failure| J[Stop / rollback / escalate]
```

Read **[Security & Governance](docs/SECURITY_GOVERNANCE.md)** for the safety model.

## Target enterprise architecture

```mermaid
flowchart TB
    subgraph Runtime[Automation Runtime Layer]
      AA[Automation Anywhere A360]
      UIP[UiPath]
      PA[Power Automate]
      WEB[Browser / Selenium]
      APIS[APIs / Lambda]
      INFRA[VM / VDI / Queues / DB]
    end

    subgraph Integration[RPA-X Integration Fabric]
      ADAPTERS[Platform Adapters]
      EVENTS[Runtime Event Gateway]
      NORMAL[Event Normalizer]
    end

    subgraph Core[RPA-X Intelligence Core]
      GENOME[Process Genome]
      TWIN[Live Process Twin]
      FAIL[Failure Intelligence]
      BRAIN[Recovery Brain]
      MEMORY[Recovery Memory]
    end

    subgraph Guardrails[Governance & Safety]
      RISK[Risk Engine]
      POLICY[Policy Engine]
      HITL[Human Control Gate]
      SECURITY[RBAC / Secrets]
    end

    subgraph Assurance[Execution & Assurance]
      EXEC[Recovery Executor]
      SHADOW[Shadow Lab]
      VALIDATE[Outcome Validator]
      LEDGER[Evidence Ledger]
      OBS[Observability]
    end

    Runtime --> ADAPTERS --> EVENTS --> NORMAL --> TWIN
    GENOME --> TWIN
    TWIN --> FAIL --> BRAIN
    MEMORY --> BRAIN
    BRAIN --> RISK --> POLICY
    POLICY -->|allowed| EXEC
    POLICY -->|approval| HITL --> EXEC
    EXEC --> SHADOW --> VALIDATE
    VALIDATE --> LEDGER --> MEMORY
    VALIDATE --> OBS
```

Detailed architecture: **[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)**

## End-to-end self-healing workflow

```mermaid
flowchart TD
    A[Bot / API / desktop event] --> B[Normalize event]
    B --> C[Update Process Twin]
    C --> D{Anomaly or failure?}
    D -->|No| E[Continue monitoring]
    D -->|Yes| F[Gather evidence]
    F --> G[Classify failure]
    G --> H[Generate recovery candidates]
    H --> I[Score confidence + risk]
    I --> J{Policy decision}
    J -->|Observe only| K[Recommend / escalate]
    J -->|Needs approval| L[Human Control Gate]
    J -->|Allowed| M[Shadow validation]
    L -->|Approved| M
    L -->|Rejected| K
    M --> N{Candidate safe?}
    N -->|No| K
    N -->|Yes| O[Execute recovery]
    O --> P[Validate technical + business outcome]
    P --> Q{Recovered?}
    Q -->|Yes| R[Record + learn]
    Q -->|No| S[Stop / rollback / incident]
```

More workflow drawings: **[docs/WORKFLOWS.md](docs/WORKFLOWS.md)**

## Product autonomy levels

| Level | Mode | Meaning |
|---|---|---|
| **A0** | Observe | Diagnose only; no recovery writes |
| **A1** | Recommend | Suggest recovery to operators |
| **A2** | Assist | Human approval required before execution |
| **A3** | Bounded Auto-Heal | Allow-listed low-risk recoveries may execute automatically |
| **A4** | Adaptive | Previously validated recovery patterns may be reused inside policy |
| **A5** | Autonomous | Future research target; still governed by hard policy boundaries |

## Command Center foundation preview

RPA-X now includes a lightweight integrated **Command Center preview** served by the same FastAPI product. It reads the live `/health` and `/capabilities` APIs and presents the product identity, control loop, autonomy model and current capability registry.

This is intentionally a **foundation preview**, not yet a production monitoring dashboard. Real bot health, run history, SLA metrics and recovery evidence will be connected as the persistence and platform adapters are built.

## What exists in the repository today

Current foundation includes:

- ✅ FastAPI service
- ✅ Unified product manifest and capability registry
- ✅ Integrated Command Center preview
- ✅ Runtime event model
- ✅ Failure classification foundation
- ✅ Recovery strategy foundation
- ✅ Live Process Twin foundation
- ✅ Evidence Ledger foundation
- ✅ Vendor-neutral adapter interface
- ✅ Sample Process Genome
- ✅ Unit tests
- ✅ GitHub Actions CI definition
- ✅ Product architecture and workflow documentation
- ✅ RPA-X executive application icon and wordmark

The following are **planned**, not yet production-complete:

- 🚧 Persistent operational database
- 🚧 Automation Anywhere A360 Control Room adapter
- 🚧 Production Command Center telemetry and dashboards
- 🚧 Policy-as-code engine
- 🚧 Human approval service
- 🚧 Shadow execution environment
- 🚧 AI/LLM provider abstraction
- 🚧 Selector discovery and visual/DOM recovery
- 🚧 Multi-platform production adapters
- 🚧 Enterprise SSO/RBAC/secrets integration
- 🚧 Automation FinOps and predictive reliability

This distinction is intentional: RPA-X should never market roadmap concepts as production features.

## First target: Automation Anywhere A360

The first enterprise runtime integration is planned around Automation Anywhere A360.

```mermaid
flowchart LR
    CR[A360 Control Room] --> AD[A360 Adapter]
    AD --> RUNS[Bot Runs]
    AD --> DEV[Device / Runner Health]
    AD --> QUEUE[Work Items / Queues]
    AD --> ERR[Failure Evidence]
    RUNS --> RPAX[RPA-X Process Twin]
    DEV --> RPAX
    QUEUE --> RPAX
    ERR --> RPAX
    RPAX --> POLICY[Policy Engine]
    POLICY -->|future controlled write| REC[Retry / Requeue / Resume]
    REC --> CR
```

The integration should start **read-only**, prove observability and diagnosis, then enable restricted recovery operations through explicit policy.

## Example use case: UI selector drift

A bot expects a button, but the target application changes its DOM.

1. The runtime reports `selector not found`.
2. RPA-X captures the failed step and available DOM/UI evidence.
3. The Process Twin compares the expected outcome with the current state.
4. Failure Intelligence classifies UI drift.
5. The Recovery Brain finds candidate elements.
6. Previously approved recovery memory is checked first.
7. Candidate action is evaluated against risk and policy.
8. Safe candidates are tested in the Shadow Lab.
9. The business outcome is validated.
10. Evidence is recorded and the validated fallback may be remembered.

**Important:** the target design does not silently rewrite production bot source packages. Runtime recovery and permanent source changes are separate governed workflows.

## Repository structure

```text
RPA/
├── assets/
│   ├── rpa-x-app-icon.svg
│   └── rpa-x-logo.svg
├── app/
│   ├── engine.py
│   ├── ledger.py
│   ├── main.py
│   ├── models.py
│   ├── product.py
│   └── twin.py
├── adapters/
│   └── base.py
├── genomes/
│   └── sample_invoice_process.yaml
├── docs/
│   ├── ARCHITECTURE.md
│   ├── PRODUCT_BLUEPRINT.md
│   ├── ROADMAP.md
│   ├── SECURITY_GOVERNANCE.md
│   └── WORKFLOWS.md
├── web/
│   ├── app.css
│   ├── app.js
│   ├── index.html
│   └── rpa-x-app-icon.svg
├── tests/
├── .github/workflows/
├── pyproject.toml
└── README.md
```

## Run the current product foundation

```bash
git clone https://github.com/logeshv586-code/RPA.git
cd RPA
python -m venv .venv
pip install -e .
uvicorn app.main:app --reload
```

Open the product surfaces:

```text
Command Center preview: http://127.0.0.1:8000/ui/
FastAPI documentation:  http://127.0.0.1:8000/docs
Product manifest:       http://127.0.0.1:8000/
Capability registry:    http://127.0.0.1:8000/capabilities
Health:                 http://127.0.0.1:8000/health
```

## Example runtime event

```json
{
  "process_id": "invoice-processing",
  "run_id": "run-2026-001",
  "step_id": "submit-invoice",
  "status": "failed",
  "message": "API timeout while calling vendor endpoint"
}
```

Send it to `POST /events`. The current engine can classify the event and select a basic recovery decision. Future versions will enrich that decision with process state, evidence, policy, history and outcome validation.

## Design principles

1. **One product experience** — monitoring, diagnosis, recovery, governance and learning belong in one control plane.
2. **Vendor neutral** — platform adapters translate runtimes into a common capability model.
3. **Read first** — new enterprise integrations start in observation mode.
4. **Intent before clicks** — reason from business outcome and expected state, not only selector errors.
5. **Policy before autonomy** — AI can recommend; policy authorizes.
6. **Evidence before confidence** — every recovery should be explainable.
7. **Validate the outcome** — technical success is not automatically business success.
8. **Unknown is acceptable** — RPA-X must never invent certainty to keep a process moving.
9. **Recovery must stop** — bounded retries and circuit breakers prevent runaway automation.
10. **Learn only from validated results** — failed or ambiguous repairs should not become trusted memory.

## Roadmap

The detailed roadmap is maintained in **[docs/ROADMAP.md](docs/ROADMAP.md)**.

```mermaid
flowchart LR
    P0[Foundation] --> P1[Command Center]
    P1 --> P2[A360 Integration]
    P2 --> P3[Policy Recovery]
    P3 --> P4[AI Intelligence]
    P4 --> P5[Shadow + Self-Healing]
    P5 --> P6[Multi-Platform]
    P6 --> P7[Enterprise Scale]
    P7 --> P8[Predictive Reliability]
```

## Long-term vision

RPA-X should become an **Automation Reliability Operating System** for enterprises: one place to understand the health, intent, risk and recovery state of every important automation, regardless of which technology executes it.

The product is successful when automation teams spend less time restarting bots and reconstructing incidents—and more time improving business processes—while security and governance teams gain **more** control, not less.

## Project status

**Stage:** early foundation / architecture build.

The repository is public and evolving quickly. Production use is **not yet recommended**.

## License

A project license has not yet been selected. A license should be chosen before the first public release intended for external adoption or contribution.
