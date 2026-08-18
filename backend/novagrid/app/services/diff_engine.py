HTTP_METHODS = {"get", "post", "put", "patch", "delete", "head", "options"}

def _operations(spec):
    result = {}
    for path, item in spec.get("paths", {}).items():
        if not isinstance(item, dict):
            continue
        for method, operation in item.items():
            if method.lower() in HTTP_METHODS and isinstance(operation, dict):
                result[(path, method.lower())] = operation
    return result

def _props(schema):
    return (schema or {}).get("properties", {})

def _required(schema):
    return set((schema or {}).get("required", []))

def _response_schemas(operation):
    result = []
    for status, response in operation.get("responses", {}).items():
        for media in (response or {}).get("content", {}).values():
            schema = (media or {}).get("schema")
            if isinstance(schema, dict):
                result.append((status, schema))
    return result

def _compare_operation(path, method, old, new):
    changes = []
    old_params = {(p.get("name"), p.get("in")): p for p in old.get("parameters", []) if isinstance(p, dict)}
    new_params = {(p.get("name"), p.get("in")): p for p in new.get("parameters", []) if isinstance(p, dict)}

    for key in old_params.keys() - new_params.keys():
        name, loc = key
        changes.append({"type":"parameter_removed","method":method.upper(),"path":path,"parameter":name,"location":loc,"classification":"BREAKING","message":f"Parameter '{name}' was removed"})
    for key in new_params.keys() - old_params.keys():
        name, loc = key
        required = new_params[key].get("required", False)
        changes.append({"type":"parameter_added_required" if required else "parameter_added_optional","method":method.upper(),"path":path,"parameter":name,"location":loc,"classification":"BREAKING" if required else "SAFE","message":f"{'Required' if required else 'Optional'} parameter '{name}' was added"})
    for key in old_params.keys() & new_params.keys():
        name, _ = key
        a, b = old_params[key], new_params[key]
        if not a.get("required", False) and b.get("required", False):
            changes.append({"type":"parameter_required","method":method.upper(),"path":path,"parameter":name,"classification":"BREAKING","message":f"Parameter '{name}' is now required"})
        ta, tb = a.get("schema", {}).get("type"), b.get("schema", {}).get("type")
        if ta and tb and ta != tb:
            changes.append({"type":"parameter_type_changed","method":method.upper(),"path":path,"parameter":name,"old_type":ta,"new_type":tb,"classification":"BREAKING","message":f"Parameter '{name}' changed from {ta} to {tb}"})

    old_body, new_body = old.get("requestBody", {}), new.get("requestBody", {})
    if not old_body.get("required", False) and new_body.get("required", False):
        changes.append({"type":"request_body_required","method":method.upper(),"path":path,"classification":"BREAKING","message":"Request body is now required"})

    old_status, new_status = set(old.get("responses", {})), set(new.get("responses", {}))
    for status in old_status - new_status:
        changes.append({"type":"response_removed","method":method.upper(),"path":path,"status":status,"classification":"BREAKING","message":f"Response status {status} was removed"})

    old_s = dict(_response_schemas(old)); new_s = dict(_response_schemas(new))
    for status in old_s.keys() & new_s.keys():
        op, np = _props(old_s[status]), _props(new_s[status])
        for name in op.keys() - np.keys():
            changes.append({"type":"response_property_removed","method":method.upper(),"path":path,"status":status,"property":name,"classification":"BREAKING","message":f"Response property '{name}' was removed"})
        for name in _required(new_s[status]) - _required(old_s[status]):
            if name in op:
                changes.append({"type":"response_property_required","method":method.upper(),"path":path,"status":status,"property":name,"classification":"WARNING","message":f"Response property '{name}' is now required"})
        removed, added = op.keys() - np.keys(), np.keys() - op.keys()
        for old_name in removed:
            for new_name in added:
                if op[old_name].get("type") == np[new_name].get("type") and op[old_name].get("type"):
                    changes.append({"type":"response_property_renamed","method":method.upper(),"path":path,"status":status,"old_property":old_name,"new_property":new_name,"classification":"BREAKING","message":f"Response property '{old_name}' appears to have been renamed to '{new_name}'"})
    return changes

def compare_specs(old_spec, new_spec):
    old_ops, new_ops = _operations(old_spec), _operations(new_spec)
    changes = []
    for path, method in sorted(old_ops.keys() - new_ops.keys()):
        changes.append({"type":"endpoint_removed","method":method.upper(),"path":path,"classification":"BREAKING","message":f"{method.upper()} {path} was removed"})
    for path, method in sorted(new_ops.keys() - old_ops.keys()):
        changes.append({"type":"endpoint_added","method":method.upper(),"path":path,"classification":"SAFE","message":f"{method.upper()} {path} was added"})
    for key in sorted(old_ops.keys() & new_ops.keys()):
        path, method = key
        changes.extend(_compare_operation(path, method, old_ops[key], new_ops[key]))
    return changes
