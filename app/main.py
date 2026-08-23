from fastapi import FastAPI
from app.models import RuntimeEvent, HealingDecision
from app.engine import classify_failure, choose_recovery

app = FastAPI(title="RPA-X", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "rpa-x"}


@app.post("/events", response_model=HealingDecision)
def ingest_event(event: RuntimeEvent) -> HealingDecision:
    failure_type = classify_failure(event)
    return choose_recovery(event, failure_type)
