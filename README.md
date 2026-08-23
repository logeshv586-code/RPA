# RPA-X — Autonomous Self-Healing RPA Control Plane

RPA-X is an open, vendor-neutral control plane for making enterprise automations more resilient, observable, and intelligent.

The core idea is simple: instead of treating an RPA bot as a fixed script, RPA-X gives every automation a **Process Genome** — a machine-readable description of its intent, steps, selectors, APIs, data contracts, expected outcomes, and approved recovery strategies. During execution, RPA-X builds a **Live Process Twin**, watches what is happening, detects drift or failure, and selects the safest recovery path.

> Goal: move RPA from **run → fail → ticket → manual fix** to **run → detect → reason → recover → learn**.

## Why this project

Traditional RPA platforms are strong at execution, but production support is still heavily reactive. Common failures include selector changes, slow applications, missing data, expired sessions, API changes, environment issues, and business-rule exceptions.

RPA-X is being built as a separate intelligence and reliability layer that can sit above tools such as Automation Anywhere A360, UiPath, Power Automate, Selenium, desktop automation, APIs, and serverless functions.

## Core concepts

### 1. Process Genome
A portable definition of what an automation is trying to achieve, not just how it clicks through a UI.

### 2. Live Process Twin
A runtime model of the current automation state, expected next state, dependencies, timing, and evidence.

### 3. Failure Intelligence
Classifies failures into business, technical, application, data, credential, API, infrastructure, and unknown categories.

### 4. Self-Healing Engine
Ranks recovery strategies such as retry, alternate selector, alternate API, session refresh, fallback path, requeue, or human approval.

### 5. Shadow Validation
Potential fixes can be simulated or validated before they are trusted for unattended execution.

### 6. Evidence Ledger
Every decision records what happened, why a recovery was selected, its confidence, result, and audit evidence.

## MVP architecture

```text
RPA / API / Browser / Desktop Events
                |
                v
        Runtime Event Gateway
                |
                v
       Live Process Twin Engine
                |
        +-------+--------+
        |                |
        v                v
 Failure Classifier   Policy Engine
        |                |
        +-------+--------+
                |
                v
        Healing Strategy Engine
                |
        +-------+--------+
        |                |
        v                v
  Auto Recovery     Human Approval
        |
        v
      Evidence Ledger
```

## First MVP

The first version will provide:

- FastAPI service for RPA runtime events
- Process/run data model
- Failure classification
- Recovery strategy ranking
- Policy-based safe auto-healing
- Evidence/audit records
- Unit tests
- Adapter interface for Automation Anywhere, UiPath, Power Automate, Selenium, and APIs

## Example use case

A bot expects a page element but the application UI changes.

1. RPA-X receives the failure event.
2. The Process Twin identifies the failed step and expected outcome.
3. Failure Intelligence classifies the problem as an application/UI drift issue.
4. The Healing Engine evaluates approved alternatives.
5. A safe fallback selector or API route is selected.
6. The recovery is executed or placed into approval depending on policy.
7. Evidence is stored so the system can learn which recovery works best over time.

## Vision

RPA-X should become a practical open-source **autonomous reliability layer for RPA**, focused on production support, self-healing, explainability, vendor neutrality, and enterprise governance.

## Status

🚧 Foundation stage — architecture and first runnable MVP are being built now.

## License

A license will be selected before the first public release.
