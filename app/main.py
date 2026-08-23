from fastapi import FastAPI

from app.engine import classify_failure, choose_recovery
from app.models import HealingDecision, RuntimeEvent
from app.product import (
    PRODUCT_MISSION,
    PRODUCT_NAME,
    PRODUCT_TAGLINE,
    PRODUCT_VERSION,
    product_manifest,
)

app = FastAPI(
    title=PRODUCT_NAME,
    version=PRODUCT_VERSION,
    description=(
        f"{PRODUCT_TAGLINE}. {PRODUCT_MISSION} "
        "RPA-X is an early-stage vendor-neutral reliability and governance control plane "
        "for enterprise automation."
    ),
    docs_url="/docs",
    redoc_url="/redoc",
)


@app.get("/")
def product() -> dict[str, object]:
    """Return the unified RPA-X product manifest and capability status."""
    return product_manifest()


@app.get("/health")
def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "rpa-x",
        "version": PRODUCT_VERSION,
    }


@app.get("/capabilities")
def capabilities() -> dict[str, object]:
    """Expose the current product capability registry for operators and integrations."""
    manifest = product_manifest()
    return {
        "product": manifest["name"],
        "version": manifest["version"],
        "capabilities": manifest["capabilities"],
    }


@app.post("/events", response_model=HealingDecision)
def ingest_event(event: RuntimeEvent) -> HealingDecision:
    failure_type = classify_failure(event)
    return choose_recovery(event, failure_type)
