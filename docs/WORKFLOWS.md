# RPA-X Workflows

This document defines the target operating workflows for RPA-X as a single enterprise product.

## 1. Runtime observation workflow

```mermaid
sequenceDiagram
    participant Bot as Automation Runtime
    participant Adapter as RPA-X Adapter
    participant Gateway as Event Gateway
    participant Twin as Live Process Twin
    participant Ledger as Evidence Ledger

    Bot->>Adapter: Run / step / failure telemetry
    Adapter->>Gateway: Normalize runtime event
    Gateway->>Twin: Apply event to process state
    Twin->>Ledger: Record state transition evidence
    Twin-->>Gateway: Current state + expected next state
```

## 2. Failure-to-recovery workflow

```mermaid
flowchart TD
    A[Failure / anomaly event] --> B[Gather evidence]
    B --> C[Update Process Twin]
    C --> D[Classify failure]
    D --> E[Generate recovery candidates]
    E --> F[Score confidence + risk]
    F --> G{Policy decision}
    G -->|Observe only| H[Recommend + create evidence]
    G -->|Human approval| I[Approval queue]
    G -->|Allowed low risk| J[Shadow validation]
    I -->|Approved| J
    I -->|Rejected| H
    J --> K{Validation passed?}
    K -->|No| L[Stop / rollback / escalate]
    K -->|Yes| M[Execute recovery]
    M --> N[Validate business outcome]
    N --> O{Recovered?}
    O -->|Yes| P[Close recovery + learn]
    O -->|No| L
    P --> Q[Update Recovery Memory]
    L --> R[Incident / human support]
```

## 3. Selector self-healing workflow

```mermaid
flowchart LR
    A[Selector not found] --> B[Capture DOM + UI evidence]
    B --> C[Compare expected element signature]
    C --> D[Discover candidate elements]
    D --> E[Rank candidates]
    E --> F{Previously approved match?}
    F -->|Yes| G[Shadow click / validation]
    F -->|No| H{Confidence + policy}
    H -->|Low confidence| I[Developer review]
    H -->|Approval required| J[Human Control Gate]
    H -->|Safe allow-list| G
    J -->|Approved| G
    G --> K{Expected outcome reached?}
    K -->|Yes| L[Use fallback for this run]
    K -->|No| M[Abort recovery]
    L --> N[Store validated selector memory]
```

The target design does **not** silently rewrite source automation packages. Initial self-healing should be runtime-scoped. Permanent changes should be proposed through governed promotion workflows.

## 4. API failure workflow

```mermaid
flowchart TD
    A[API call failure] --> B{Failure type}
    B -->|Timeout / transient 5xx| C[Check idempotency]
    B -->|401 / 403| D[Credential / permission diagnosis]
    B -->|Schema change| E[Contract drift analysis]
    B -->|Business 4xx| F[Business exception]
    C -->|Idempotent| G[Retry with exponential backoff]
    C -->|Not proven idempotent| H[Approval / manual review]
    D --> I[Refresh session only if policy allows]
    E --> J[Recommend mapping / adapter update]
    F --> K[Do not technical-retry]
    G --> L[Validate response + downstream state]
    I --> L
```

## 5. Business exception workflow

```mermaid
flowchart LR
    A[Business exception] --> B[Classify reason]
    B --> C[Attach transaction evidence]
    C --> D{Configured business route}
    D -->|Skip| E[Mark business exception]
    D -->|Queue| F[Route to business work queue]
    D -->|Approval| G[Human Control Gate]
    D -->|Data correction allowed| H[Guided correction]
    E --> I[Continue remaining workload]
    F --> I
    G --> I
    H --> J[Revalidate transaction]
    J --> I
```

## 6. Human approval workflow

```mermaid
sequenceDiagram
    participant Engine as Recovery Brain
    participant Policy as Policy Engine
    participant Human as Approver
    participant Executor as Recovery Executor
    participant Ledger as Evidence Ledger

    Engine->>Policy: Proposed action + evidence + confidence
    Policy-->>Engine: approval_required
    Engine->>Human: Recovery proposal
    Human->>Ledger: Review decision + comment
    alt Approved
        Human->>Executor: Approve action
        Executor->>Ledger: Execution result
    else Rejected
        Human->>Ledger: Rejection reason
    end
```

## 7. Learning workflow

```mermaid
flowchart LR
    A[Completed recovery] --> B[Outcome validation]
    B --> C[Evidence enrichment]
    C --> D[Recovery Memory]
    D --> E[Pattern aggregation]
    E --> F[Repeated failure detection]
    F --> G[Preventive recommendation]
    G --> H[Developer / CoE backlog]
```

RPA-X should learn from **validated outcomes**, not merely from actions that executed without throwing an error.

## 8. End-to-end enterprise workflow

```mermaid
flowchart TB
    DESIGN[Design / Process Genome] --> DEPLOY[Automation deployed]
    DEPLOY --> OBSERVE[Unified observability]
    OBSERVE --> RUN[Run transactions]
    RUN -->|Success| KPI[Business + reliability metrics]
    RUN -->|Failure| DIAGNOSE[Failure Intelligence]
    DIAGNOSE --> RECOVER[Policy-bounded recovery]
    RECOVER --> VALIDATE[Outcome validation]
    VALIDATE -->|Recovered| KPI
    VALIDATE -->|Not recovered| INCIDENT[Incident / human support]
    KPI --> LEARN[Recovery Memory + optimization]
    INCIDENT --> LEARN
    LEARN --> DESIGN
```
