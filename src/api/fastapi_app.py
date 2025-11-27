"""
fastapi_app.py
FastAPI service for:
- Metadata Q&A Agent
- Spark Optimization Agent (simplified)
Author: Janak
"""

from fastapi import FastAPI
from pydantic import BaseModel
import json
import os
from typing import List

# ---------------------------------------
# Load Metadata (local file in repo)
# ---------------------------------------
METADATA_PATH = "src/metadata/metadata_schema.json"

with open(METADATA_PATH, "r") as f:
    METADATA = json.load(f)

# ---------------------------------------
# Metadata Q&A Helper Functions
# ---------------------------------------
def get_table_schema(table: str):
    info = METADATA.get(table)
    if not info:
        return {"error": f"Table not found: {table}"}
    return info.get("schema", {})

def get_quality_rules(table: str):
    info = METADATA.get(table)
    if not info:
        return {"error": f"Table not found: {table}"}
    return info.get("quality_rules", {})

def get_owner(table: str):
    info = METADATA.get(table)
    if not info:
        return f"Table not found: {table}"
    return info.get("owner", "Unknown")

def find_by_owner(owner: str) -> List[str]:
    owner = owner.lower()
    return [t for t,v in METADATA.items() if v.get("owner", "").lower() == owner]

def freshness_less_than(hours: int) -> List[str]:
    return [t for t,v in METADATA.items() if v.get("freshness_hours", 99999) < hours]

# ---------------------------------------
# Natural Language Q&A Router (Rule-based)
# ---------------------------------------
def metadata_agent_router(query: str):
    q = query.lower().strip()

    if q.startswith("show schema for"):
        table = q.split()[-1]
        return get_table_schema(table)

    if "quality rules for" in q:
        table = q.split()[-1]
        return get_quality_rules(table)

    if "who owns" in q:
        table = q.split()[-1]
        return {"owner": get_owner(table)}

    if "tables owned by" in q:
        owner = q.split("tables owned by")[1].strip()
        return {"tables": find_by_owner(owner)}

    if "freshness less than" in q:
        import re
        m = re.search(r"freshness less than (\d+)", q)
        if m:
            hours = int(m.group(1))
            return {"tables": freshness_less_than(hours)}

    # fallback keyword search
    matches = []
    for tname, info in METADATA.items():
        blob = " ".join([
            tname.lower(),
            info.get("description","").lower(),
            " ".join(info.get("schema", {}).keys()).lower()
        ])
        if any(k in blob for k in q.split()):
            matches.append(tname)
    if matches:
        return {"related_tables": matches}

    return {"message": "Query not understood. Try: 'show schema for orders'."}

# ---------------------------------------
# Optimization Agent (Simple Version)
# ---------------------------------------
def optimization_suggestions(operation: str):
    op = operation.lower()

    suggestions = []

    if "join" in op:
        suggestions.append("Consider broadcast join if one table is small.")
        suggestions.append("Repartition by join key to avoid shuffle.")

    if "shuffle" in op:
        suggestions.append("Shuffle detected — check skew or repartition by key.")

    if "aggregate" in op or "group" in op:
        suggestions.append("Aggregation — ensure proper partitioning or use map-side combine.")

    if not suggestions:
        suggestions.append("No clear optimization detected.")

    return suggestions

# ---------------------------------------
# FastAPI App
# ---------------------------------------

app = FastAPI(title="Intelligent ETL Metadata API", version="1.0")

class Query(BaseModel):
    q: str

class Operation(BaseModel):
    description: str

@app.get("/")
def home():
    return {"status": "running", "message": "Welcome to the Intelligent ETL Metadata API"}

@app.post("/qna")
def qna(query: Query):
    """Ask metadata-related natural language questions"""
    answer = metadata_agent_router(query.q)
    return {"query": query.q, "answer": answer}

@app.post("/optimize")
def optimize(op: Operation):
    """Get Spark optimization suggestions"""
    suggestions
