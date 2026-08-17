def generate_fix(change: dict, dependency) -> dict:
    file_path = dependency.file_path
    t = change.get("type")
    if t == "response_property_renamed":
        return {"description":f"Replace '{change['old_property']}' with '{change['new_property']}' in {file_path}.","patch":f"# Candidate patch for {file_path}\n# Replace references to {change['old_property']} with {change['new_property']}.\n# Run tests before applying.","status":"PROPOSED"}
    if t == "parameter_removed":
        return {"description":f"Stop sending '{change['parameter']}' from {file_path}.","patch":f"# Remove '{change['parameter']}' from the request payload.","status":"PROPOSED"}
    if t == "parameter_type_changed":
        return {"description":f"Update '{change['parameter']}' serialization in {file_path}.","patch":f"# Convert '{change['parameter']}' to {change['new_type']} before sending.","status":"PROPOSED"}
    return {"description":"No safe automatic fix generated.","patch":None,"status":"REQUIRES_HUMAN"}
