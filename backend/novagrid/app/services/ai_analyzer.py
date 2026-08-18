from typing import Any


def analyze_change(change: dict[str, Any]) -> dict[str, Any]:
    """
    Analyze an API specification change and return a normalized impact result.

    This is intentionally deterministic for now. An AI/LLM implementation can
    later replace or extend this function without changing the rest of NovaGrid.
    """

    change_type = change.get("type", "unknown")
    message = change.get("message", "API behavior changed.")
    method = change.get("method", "").upper()
    path = change.get("path", "")

    # Endpoint removed: existing consumers can immediately fail.
    if change_type == "endpoint_removed":
        return {
            "impact_level": "CRITICAL",
            "explanation": f"{method} {path} no longer exists.",
            "recommendation": (
                "Migrate all consumers to a supported endpoint and "
                "verify all request paths before deployment."
            ),
            "human_review": True,
        }

    # Request contract changes that can break callers.
    if change_type == "parameter_removed":
        parameter = change.get("parameter", "unknown")
        return {
            "impact_level": "HIGH",
            "explanation": message,
            "recommendation": (
                f"Remove '{parameter}' from affected requests and "
                "update callers before deployment."
            ),
            "human_review": True,
        }

    if change_type == "parameter_required":
        parameter = change.get("parameter", "unknown")
        return {
            "impact_level": "HIGH",
            "explanation": message,
            "recommendation": (
                f"Ensure every caller supplies the required parameter "
                f"'{parameter}' and update request validation."
            ),
            "human_review": True,
        }

    if change_type == "parameter_added_required":
        parameter = change.get("parameter", "unknown")
        return {
            "impact_level": "HIGH",
            "explanation": message,
            "recommendation": (
                f"Update affected callers to provide the new required "
                f"parameter '{parameter}'."
            ),
            "human_review": True,
        }

    if change_type == "parameter_type_changed":
        parameter = change.get("parameter", "unknown")
        old_type = change.get("old_type", "unknown")
        new_type = change.get("new_type", "unknown")

        return {
            "impact_level": "HIGH",
            "explanation": (
                f"Parameter '{parameter}' changed from "
                f"{old_type} to {new_type}."
            ),
            "recommendation": (
                f"Update serialization and validation for '{parameter}' "
                f"from {old_type} to {new_type}, then run affected tests."
            ),
            "human_review": True,
        }

    # Response contract changes.
    if change_type == "response_property_removed":
        property_name = change.get("property", "unknown")

        return {
            "impact_level": "HIGH",
            "explanation": message,
            "recommendation": (
                f"Find consumers reading '{property_name}', update their "
                "response handling, and run compatibility tests."
            ),
            "human_review": True,
        }

    if change_type == "response_property_renamed":
        old_property = change.get("old_property", "unknown")
        new_property = change.get("new_property", "unknown")

        return {
            "impact_level": "HIGH",
            "explanation": (
                f"Response property '{old_property}' appears to have "
                f"been renamed to '{new_property}'."
            ),
            "recommendation": (
                f"Update consumers from '{old_property}' to "
                f"'{new_property}' and validate response parsing."
            ),
            "human_review": True,
        }

    if change_type == "response_property_required":
        property_name = change.get("property", "unknown")

        return {
            "impact_level": "MEDIUM",
            "explanation": message,
            "recommendation": (
                f"Check consumers of '{property_name}' and ensure their "
                "validation and serialization logic handles the property."
            ),
            "human_review": False,
        }

    # Non-breaking additions.
    if change_type == "endpoint_added":
        return {
            "impact_level": "LOW",
            "explanation": message,
            "recommendation": (
                "No migration is required for existing consumers. "
                "Adopt the endpoint only where needed."
            ),
            "human_review": False,
        }

    if change_type == "parameter_added_optional":
        parameter = change.get("parameter", "unknown")

        return {
            "impact_level": "LOW",
            "explanation": message,
            "recommendation": (
                f"No migration is required. The optional parameter "
                f"'{parameter}' can be adopted when appropriate."
            ),
            "human_review": False,
        }

    # Safe fallback for future diff-engine change types.
    return {
        "impact_level": "MEDIUM",
        "explanation": message,
        "recommendation": (
            "Inspect affected consumers and validate compatibility "
            "before deployment."
        ),
        "human_review": True,
    }