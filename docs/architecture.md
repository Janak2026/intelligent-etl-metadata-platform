```markdown
# Architecture — Intelligent ETL Metadata Platform

This document describes the full end-to-end architecture of the **Intelligent ETL Metadata Platform**, including system components, data flow, metadata governance, and LLM agent integration.

---

# 📘 Overview

The platform is designed to be:

- **Metadata-driven**
- **Delta Lake optimized**
- **Databricks-native**
- **AI-augmented** via LLM agents
- **Scalable** across multiple datasets
- **API-accessible** via FastAPI

It supports the full pipeline lifecycle:

**Ingestion → Validation → Silver (clean) → Gold (aggregated) → LLM Agents → API Layer**

---

# 🏗 High-Level Architecture Diagram

```

```
            ┌──────────────────────────┐
            │ External Data Sources    │
            │ (CSV, APIs, DB dumps)    │
            └─────────────┬────────────┘
                          │
                          ▼
          ┌──────────────────────────────────┐
          │        Bronze Layer (Raw)        │
          │ Delta tables generated via        │
          │ PySpark ingestion                 │
          └───────────────┬──────────────────┘
                          │
                          ▼
          ┌──────────────────────────────────┐
          │        Metadata Layer             │
          │ - Table schema definitions        │
          │ - Quality rules (null, enums)     │
          │ - Freshness SLAs                  │
          │ - Owners & lineage                │
          └───────────────┬──────────────────┘
                          │
                          ▼
          ┌──────────────────────────────────┐
          │         Silver Layer              │
          │ Clean, standardized data using    │
          │ metadata-driven transformations   │
          └───────────────┬──────────────────┘
                          │
                          ▼
          ┌──────────────────────────────────┐
          │          Gold Layer               │
          │ Curated business aggregates       │
          │ for analytics & dashboards        │
          └───────────────┬──────────────────┘
                          │
                          ▼
            ┌────────────────────────────────┐
            │      LLM Agents (AI)           │
            │  ▸ Metadata Q&A Agent          │
            │  ▸ Spark Optimization Agent    │
            └────────────┬───────────────────┘
                          │
                          ▼
            ┌────────────────────────────────┐
            │          FastAPI Layer          │
            │  REST endpoints for QnA & AI    │
            │  Deployable on Azure / AWS      │
            └────────────────────────────────┘
```

```

---

# 🧱 Core Components

## 1. **Bronze Layer (Raw)**
- Stores raw ingested files as Delta tables.
- Schema-on-read.
- No transformations except basic type normalization.

**Tech:**  
PySpark, Delta Lake, Databricks Notebooks

---

## 2. **Metadata Layer**
Central to this platform.  
Stored as JSON + loaded via Python.

Contains:

- Column types  
- Accepted values (ENUM)  
- Null constraints  
- Primary key candidates  
- Freshness SLA  
- Table owner  
- Descriptions  

**Files:**
```

src/metadata/metadata_schema.json
src/metadata/metadata_loader.py
src/metadata/rules_engine.py

```

Used by:

- ETL validation  
- LLM Q&A Agent  
- Future lineage tools  

---

## 3. **Silver Layer (Clean Layer)**
Based on metadata:

- Enforces schema  
- Removes duplicates  
- Casts columns  
- Standardizes date formats  
- Applies quality rules (null checks, positive checks)

---

## 4. **Gold Layer (Business Aggregations)**
Examples:

- Revenue per day  
- Top products  
- Customer cohorts  
- Order funnel metrics  

Gold layer tables become the source for:

- BI dashboards  
- LLM explanations  
- API outputs  

---

## 5. **LLM Agents**
Two main agents:

### **(A) Metadata Q&A Agent**
Uses the metadata JSON + embeddings (future).

Example queries:
- “What columns are required in `orders`?”
- “What tables have freshness SLA < 24 hours?”
- "Show the accepted status values."

### **(B) Spark Optimization Agent**
Rule-based + LLM hybrid.

Suggests improvements like:
- Use broadcast join  
- Reduce shuffle  
- Increase partitions  
- Optimize file sizes  
- Use Delta Z-order  

---

## 6. **API Layer — FastAPI**
Exposes endpoints:

- `/qna` → metadata agent  
- `/optimize` → optimization agent  

Deployable on:
- Azure Container Apps  
- AWS Lambda  
- Docker containers  

---

# 🔄 Data Flow Summary

### STEP 1 → Ingestion  
PySpark reads raw CSV → Bronze Delta tables

### STEP 2 → Metadata Validation  
rules_engine applies:
- not-null  
- positive-values  
- enum checks  

### STEP 3 → Silver Transform  
Standardized output  
Clean records  

### STEP 4 → Gold Aggregations  
Metrics for business use  

### STEP 5 → Agents  
Use metadata + logs + Spark plan to answer or optimize.

### STEP 6 → FastAPI  
External integration layer.

---

# 🔧 Technology Stack

- **Apache Spark (PySpark)**  
- **Delta Lake**  
- **Databricks Notebooks + Repos**  
- **Python**  
- **FastAPI**  
- **LLM (OpenAI/Azure)**  
- **Unit Testing — PyTest**  
- **MLflow (future extension)**  

---

# 🗺 Future Enhancements

- Add embeddings for smarter Q&A  
- Add a Streamlit UI  
- Add MLflow tracking  
- Add monitoring for SLAs  
- Add audit logs to metadata reports  

---

# ✔ Author
**Janardhana Rao Komanapalli (Janak)**  
Senior Data Engineer — Spark | Azure | Databricks | AI Integrations  

```