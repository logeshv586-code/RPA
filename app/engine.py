from app.models import FailureType, HealingDecision, RuntimeEvent

KEYWORDS: list[tuple[FailureType, tuple[str, ...]]] = [
    ("credential", ("password", "credential", "unauthorized", "401", "login")),
    ("api", ("api", "endpoint", "http 5", "timeout", "429")),
    ("data", ("missing field", "invalid data", "null", "schema", "validation")),
    ("application", ("selector", "element", "window", "page", "ui")),
    ("infrastructure", ("server", "vm", "network", "disk", "memory")),
    ("business", ("business rule", "not eligible", "duplicate", "limit exceeded")),
]


def classify_failure(event: RuntimeEvent) -> FailureType:
    if event.status != "failed":
        return "unknown"
    haystack = f"{event.message} {event.metadata}".lower()
    for failure_type, words in KEYWORDS:
        if any(word in haystack for word in words):
            return failure_type
    return "technical"


def choose_recovery(event: RuntimeEvent, failure_type: FailureType) -> HealingDecision:
    strategies = {
        "credential": ("refresh_session", 0.82, True),
        "api": ("retry_with_backoff", 0.88, False),
        "data": ("route_to_data_validation", 0.93, True),
        "application": ("try_approved_fallback_selector", 0.80, True),
        "infrastructure": ("retry_on_healthy_worker", 0.86, False),
        "business": ("mark_business_exception", 0.98, False),
        "technical": ("controlled_retry", 0.68, True),
        "unknown": ("observe_only", 0.40, True),
    }
    action, confidence, requires_approval = strategies[failure_type]
    return HealingDecision(
        process_id=event.process_id,
        run_id=event.run_id,
        step_id=event.step_id,
        failure_type=failure_type,
        action=action,
        confidence=confidence,
        requires_approval=requires_approval,
        reason=f"Policy selected {action} for {failure_type} failure.",
    )
