from dataclasses import asdict, dataclass
from datetime import datetime, timezone


@dataclass
class EvidenceRecord:
    process_id: str
    run_id: str
    step_id: str
    event: str
    decision: str
    confidence: float
    result: str
    reason: str
    created_at: str

    @classmethod
    def create(
        cls,
        process_id: str,
        run_id: str,
        step_id: str,
        event: str,
        decision: str,
        confidence: float,
        result: str,
        reason: str,
    ) -> "EvidenceRecord":
        return cls(
            process_id=process_id,
            run_id=run_id,
            step_id=step_id,
            event=event,
            decision=decision,
            confidence=confidence,
            result=result,
            reason=reason,
            created_at=datetime.now(timezone.utc).isoformat(),
        )

    def to_dict(self) -> dict:
        return asdict(self)
