# Intelligent ETL Metadata Platform

AI-driven ETL with a metadata layer, LLM Q&A agent, and Spark optimization suggestions.

## Project layout
- notebooks/ — Databricks notebooks (01_raw_ingestion, etc.)
- src/ — Python modules for ingestion, metadata, transforms, agents, API
- data/sample — sample CSVs
- docs/ — architecture and design docs
- tests/ — unit tests

## Quick start (Databricks)
1. Link GitHub repo in Databricks Repos.
2. Upload sample CSVs to data/sample or DBFS.
3. Open notebooks/01_raw_ingestion and run ingestion cells.
