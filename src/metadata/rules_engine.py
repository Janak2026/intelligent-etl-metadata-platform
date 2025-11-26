"""
rules_engine.py
Simple rules engine skeleton: validate schema, not-null checks, positive checks.
"""
from pyspark.sql import DataFrame
from typing import List, Dict, Any

def validate_not_null(df: DataFrame, cols: List[str]) -> Dict[str, int]:
    results = {}
    for c in cols:
        null_count = df.filter(df[c].isNull()).count()
        results[c] = null_count
    return results

def validate_positive(df: DataFrame, cols: List[str]) -> Dict[str, int]:
    results = {}
    for c in cols:
        neg_count = df.filter(df[c] < 0).count()
        results[c] = neg_count
    return results

def apply_quality_rules(df: DataFrame, rules: Dict[str, Any]) -> Dict[str, Any]:
    out = {}
    if "not_null" in rules:
        out["not_null"] = validate_not_null(df, rules["not_null"])
    if "positive_values" in rules:
        out["positive_values"] = validate_positive(df, rules["positive_values"])
    return out
