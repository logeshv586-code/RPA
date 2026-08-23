# RPA-X Architecture

## Architecture objective

RPA-X is a vendor-neutral control plane that receives telemetry from automation runtimes, reconstructs process state, evaluates failures, proposes or executes recovery, and records every decision for governance and learning.

## Logical architecture

```mermaid
flowchart TB
    subgraph Sources[Automation & Enterprise Sources]
      AA[Automation Anywhere A360]
      UI[UiPath]
      PA[Power Automate]
      SEL[Selenium / Browser]
      API[APIs / Lambda / Services]
      VM[VDI / VM / Desktop]
      Q[Queues / Databases / Files]
    end

    subgraph Fabric[Integration Fabric]
      AD[Platform Adapters]
      GW[Runtime Event Gateway]
      NORM[Event Normalizer]
    end

    subgraph Intelligence[RPA-X Intelligence Plane]
      GEN[Process Genome Registry]
      TWIN[Live Process Twin]
      FI[Failure Intelligence]
      RB[Recovery Brain]
      MEM[Recovery Memory]
      LLM[Optional AI / LLM Reasoning]
    end

    subgraph Safety[Safety & Governance Plane]
      POL[Policy Engine]
      RISK[Risk Scoring]
      HITL[Human Control Gate]
      SEC[RBAC / Secrets / Tenant Controls]
    end

    subgraph Execution[Recovery Execution Plane]
      RETRY[Retry / Backoff]
      REQUEUE[Requeue / Resume]
      SESSION[Session / Credential Refresh]
      ALT[Alternate Selector / API Path]
      EXEC[Platform Recovery Executor]
    end

    subgraph Assurance[Assurance & Operations]
      SHADOW[Shadow Lab / Replay]
      VAL[Outcome Validator]
      LEDGER[Evidence Ledger]
      OBS[Observability / Metrics]
      INC[Incident / ITSM Integration]
    end

    Sources --> AD --> GW --> NORM
    NORM --> TWIN
    GEN --> TWIN
    TWIN --> FI --> RB
    MEM --> RB
    LLM -. optional enrichment .-> FI
    LLM -. candidate reasoning .-> RB
    RB --> RISK --> POL
    POL -->|allow| Execution
    POL -->|approval required| HITL --> Execution
    Execution --> SHADOW --> VAL
    VAL --> LEDGER
    LEDGER --> MEM
    VAL --> OBS
    OBS --> INC
    LEDGER --> TWIN
```

## Separation of concerns

### Data plane
Carries events, bot execution telemetry, transaction state, queue status, screenshots/DOM references, API responses and runtime evidence.

### Intelligence plane
Determines what happened and what recovery candidates are available. It may use deterministic rules, historical patterns, ML models or LLMs.

### Policy plane
Determines what is allowed. This is deliberately independent from AI confidence.

### Execution plane
Performs only approved recovery actions through platform-specific adapters.

### Assurance plane
Validates outcomes, captures evidence, supports replay, and measures reliability.

## Core domain objects

### Process Genome
Versioned intent definition for an automation:

- Process identity and owner
- Business outcome
- Steps and expected outcomes
- Applications and APIs
- Selectors and alternate selectors
- Inputs / outputs / data contracts
- Idempotency characteristics
- SLAs and timing thresholds
- Known exceptions
- Approved recovery playbooks
- Risk classification
- Required approvals

### Runtime Event
Normalized observation emitted by a runtime or adapter.

### Process Twin
Current state representation built from Genome + events + evidence.

### Healing Decision
A proposed recovery containing failure type, action, confidence, expected impact, risk, policy result and approval requirement.

### Evidence Record
Append-only event describing input evidence, decision logic, policy evaluation, executor action and outcome.

## Multi-platform adapter contract

Every adapter should expose a common capability vocabulary rather than leaking vendor-specific APIs into the intelligence layer.

```mermaid
classDiagram
    class AutomationAdapter {
      +health()
      +list_runs()
      +get_run(run_id)
      +get_failure_evidence(run_id)
      +retry(run_id)
      +requeue(item_id)
      +pause(process_id)
      +resume(process_id)
      +capabilities()
    }

    AutomationAdapter <|-- A360Adapter
    AutomationAdapter <|-- UiPathAdapter
    AutomationAdapter <|-- PowerAutomateAdapter
    AutomationAdapter <|-- SeleniumAdapter
    AutomationAdapter <|-- APIAdapter
```

Adapters must advertise supported operations so the Recovery Brain cannot request a capability that a runtime does not safely expose.

## Recovery contract

Every recovery action should answer:

1. **What failed?**
2. **What evidence proves it?**
3. **What action is proposed?**
4. **Is the action idempotent?**
5. **What is the blast radius?**
6. **What policy permits it?**
7. **How will success be validated?**
8. **How will it be rolled back or stopped?**

## Deployment model

```mermaid
flowchart LR
    subgraph CustomerNetwork[Customer / Enterprise Network]
      RT[RPA Runtimes]
      AG[Optional Edge Agent]
      DB[(Operational Store)]
      SEC[Secrets Provider]
    end

    subgraph RPAX[RPA-X Platform]
      API[API Gateway]
      CORE[Control Plane Services]
      WORK[Recovery Workers]
      LED[(Evidence Ledger)]
      OBS[Observability]
    end

    RT --> AG --> API
    API --> CORE
    CORE --> DB
    CORE --> WORK
    WORK --> RT
    CORE --> SEC
    CORE --> LED
    CORE --> OBS
```

RPA-X should support both a central service model and enterprise-hosted deployment. Credentials should remain in approved secret stores and never be embedded in Process Genomes.

## Architectural guardrails

- Default to read-only integration first.
- Prefer idempotent recovery actions.
- Separate diagnosis from authorization.
- Keep AI providers replaceable.
- Never make secrets part of prompts or audit logs.
- Make every autonomous action traceable to policy.
- Require outcome validation after any recovery.
- Preserve platform-specific evidence while normalizing metadata.
- Design for replay and deterministic testing.
- Treat unknown failures as a valid class, not a reason to guess.
