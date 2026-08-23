from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class ProcessTwin:
    process_id: str
    run_id: str
    current_step: str | None = None
    last_status: str = "created"
    history: list[dict] = field(default_factory=list)

    def apply(self, step_id: str, status: str, message: str = "") -> None:
        self.current_step = step_id
        self.last_status = status
        self.history.append(
            {
                "step_id": step_id,
                "status": status,
                "message": message,
                "timestamp": datetime.now(timezone.utc).isoformat(),
            }
        )

    def snapshot(self) -> dict:
        return {
            "process_id": self.process_id,
            "run_id": self.run_id,
            "current_step": self.current_step,
            "last_status": self.last_status,
            "history": self.history,
        }
