"""
qna_agent.py
Simple skeleton for metadata-driven Q&A using embeddings + retriever (fill model details later).
"""
def answer_query(query: str, metadata_store: dict):
    # placeholder: use metadata to answer simple queries
    if "owners" in query.lower() or "owner" in query.lower():
        return [t for t,v in metadata_store.items() if v.get("owner")]
    return "Agent needs embeddings + retriever implemented."
