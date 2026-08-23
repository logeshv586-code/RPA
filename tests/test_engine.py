from app.engine import classify_failure, choose_recovery
from app.models import RuntimeEvent


def event(message: str) -> RuntimeEvent:
    return RuntimeEvent(
        process_id="demo",
        run_id="run-1",
        step_id="step-1",
        status="failed",
        message=message,
    )


def test_selector_failure_is_application():
    failure = classify_failure(event("UI selector not found"))
    assert failure == "application"


def test_api_timeout_gets_safe_retry():
    runtime_event = event("API timeout while calling vendor endpoint")
    failure = classify_failure(runtime_event)
    decision = choose_recovery(runtime_event, failure)
    assert decision.failure_type == "api"
    assert decision.action == "retry_with_backoff"
    assert decision.requires_approval is False


def test_business_exception_is_not_retried():
    runtime_event = event("Business rule: duplicate invoice")
    failure = classify_failure(runtime_event)
    decision = choose_recovery(runtime_event, failure)
    assert decision.failure_type == "business"
    assert decision.action == "mark_business_exception"
