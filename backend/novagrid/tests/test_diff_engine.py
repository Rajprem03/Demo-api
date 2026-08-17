from app.services.diff_engine import compare_specs

def spec(prop="id"):
    return {"openapi":"3.0.0","paths":{"/users/{id}":{"get":{"parameters":[{"name":"id","in":"path","required":True,"schema":{"type":"integer"}}],"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{prop:{"type":"integer"}}}}}}}}}}}

def test_removed_endpoint():
    assert compare_specs(spec(),{"openapi":"3.0.0","paths":{}})[0]["classification"]=="BREAKING"

def test_added_endpoint():
    assert compare_specs({"openapi":"3.0.0","paths":{}},spec())[0]["classification"]=="SAFE"

def test_rename():
    changes=compare_specs(spec("customer_id"),spec("user_id"))
    rename=next(x for x in changes if x["type"]=="response_property_renamed")
    assert rename["old_property"]=="customer_id" and rename["new_property"]=="user_id"
