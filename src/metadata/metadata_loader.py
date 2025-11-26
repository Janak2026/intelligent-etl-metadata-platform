"""
metadata_loader.py
Loads metadata_schema.json and returns metadata objects.
"""
import json
from pathlib import Path
from typing import Dict, Any

def load_metadata(path: str) -> Dict[str, Any]:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Metadata file not found: {path}")
    with open(p, "r") as f:
        return json.load(f)

if __name__ == "__main__":
    md = load_metadata("src/metadata/metadata_schema.json")
    print(md.keys())
