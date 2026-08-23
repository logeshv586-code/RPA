from typing import Any, Literal
from pydantic import BaseModel, Field

FailureType = Literal[
    "business",
    "technical",
    "application",
    "data",
    "credential",
    "api",
    "infrastructure",
    "unknown",
]


class RuntimeEvent(BaseModel):
    process_id: str
    run_id: str
    step_id: str
    status: Literal["started", "success", "failed"]
    message: str = ""
    metadata: dict[str, Any] = Field(default_factory=dict)


class HealingDecision(BaseModel):
    process_id: str
    run_id: str
    step_id: str
    failure_type: FailureType
    action: str
    confidence: float
    requires_approval: bool
    reason: str
