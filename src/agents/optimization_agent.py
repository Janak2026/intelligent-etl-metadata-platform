"""
optimization_agent.py
Skeleton for Spark optimization suggestions.
"""
def suggest_optimizations(query: str):
    # naive rule-based suggestions
    suggestions = []
    if "shuffle" in query.lower():
        suggestions.append("Consider repartitioning by join key or using broadcast join.")
    return suggestions
