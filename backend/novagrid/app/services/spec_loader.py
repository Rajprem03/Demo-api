import hashlib
import json
from pathlib import Path
import httpx
import yaml

def load_spec_from_file(path: str) -> dict:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(path)
    text = p.read_text(encoding="utf-8")
    data = yaml.safe_load(text) if p.suffix.lower() in {".yaml", ".yml"} else json.loads(text)
    if not isinstance(data, dict):
        raise ValueError("OpenAPI specification must be an object")
    return data

def load_spec_from_url(url: str) -> dict:
    if not url.startswith("https://"):
        raise ValueError("Only HTTPS specification URLs are allowed")
    r = httpx.get(url, timeout=15, follow_redirects=False)
    r.raise_for_status()
    data = yaml.safe_load(r.text) if "yaml" in r.headers.get("content-type", "").lower() else r.json()
    if not isinstance(data, dict):
        raise ValueError("OpenAPI specification must be an object")
    return data

def load_spec(location: str) -> dict:
    return load_spec_from_url(location) if location.startswith("https://") else load_spec_from_file(location)

def calculate_hash(spec: dict) -> str:
    normalized = json.dumps(spec, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(normalized.encode()).hexdigest()
