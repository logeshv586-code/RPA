from __future__ import annotations

from dataclasses import asdict, dataclass


PRODUCT_NAME = "RPA-X"
PRODUCT_VERSION = "0.1.0"
PRODUCT_TAGLINE = "Autonomous Automation Control Plane"
PRODUCT_MISSION = (
    "Observe, understand, recover, govern, and learn across enterprise automation runtimes."
)


@dataclass(frozen=True)
class Capability:
    key: str
    name: str
    description: str
    status: str


CAPABILITIES: tuple[Capability, ...] = (
    Capability(
        key="process_genome",
        name="Process Genome",
        description="Versioned automation intent, dependencies, outcomes, and recovery policy.",
        status="foundation",
    ),
    Capability(
        key="live_process_twin",
        name="Live Process Twin",
        description="Runtime state model of an automation run and its expected next state.",
        status="foundation",
    ),
    Capability(
        key="failure_intelligence",
        name="Failure Intelligence",
        description="Vendor-neutral failure classification and evidence-driven diagnosis.",
        status="foundation",
    ),
    Capability(
        key="recovery_brain",
        name="Recovery Brain",
        description="Ranks safe recovery actions using evidence, risk, policy, and history.",
        status="foundation",
    ),
    Capability(
        key="evidence_ledger",
        name="Evidence Ledger",
        description="Audit trail for events, decisions, approvals, execution, and validation.",
        status="foundation",
    ),
    Capability(
        key="command_center",
        name="Command Center",
        description="Unified operational experience for automation health, SLAs, and recovery.",
        status="planned",
    ),
    Capability(
        key="shadow_lab",
        name="Shadow Lab",
        description="Controlled validation of candidate recoveries before trusted execution.",
        status="planned",
    ),
    Capability(
        key="human_control_gate",
        name="Human Control Gate",
        description="Approval workflow for medium and high-risk recovery actions.",
        status="planned",
    ),
    Capability(
        key="integration_fabric",
        name="Integration Fabric",
        description="Common adapter layer for RPA platforms, APIs, browsers, queues, and infrastructure.",
        status="foundation",
    ),
    Capability(
        key="automation_finops",
        name="Automation FinOps",
        description="Reliability, utilization, support-cost, and business-value measurement.",
        status="planned",
    ),
)


def product_manifest() -> dict[str, object]:
    return {
        "name": PRODUCT_NAME,
        "version": PRODUCT_VERSION,
        "tagline": PRODUCT_TAGLINE,
        "mission": PRODUCT_MISSION,
        "capabilities": [asdict(capability) for capability in CAPABILITIES],
    }
