---

# 📄 **metadata_design.md (FULL CONTENT — COPY AS IS)**

```markdown
# Metadata Design — Intelligent ETL Metadata Platform

This document explains the structure, purpose, and mechanics of the **Metadata Layer**, which is the core intelligence behind the ETL pipeline, quality rules, lineage, and LLM agent behavior.

---

# 🎯 Purpose of the Metadata Layer

The metadata layer enables **dynamic and intelligent ETL** by separating *logic* from *code*.

Instead of hardcoding:
- Schemas  
- Data quality checks  
- Accepted values  
- Freshness SLAs  
- Table ownership  

…we store everything centrally in JSON.

This allows:
- Automated validation  
- AI-driven documentation  
- Self-service data discovery  
- LLM Q&A accuracy  
- Configurable pipelines  

---

# 📚 Metadata File Location

```

src/metadata/metadata_schema.json

```

This file stores definitions for each table.

Loaded using:

```

src/metadata/metadata_loader.py

```

Rules executed via:

```

src/metadata/rules_engine.py

````

---

# 🧩 Metadata JSON Structure

Each table follows this structure:

```json
{
  "table_name": {
    "schema": {
      "column1": "datatype",
      "column2": "datatype"
    },
    "quality_rules": {
      "not_null": [ "colA", "colB" ],
      "positive_values": [ "amount" ],
      "accepted_values": {
        "status": ["pending", "shipped", "delivered"]
      }
    },
    "freshness_hours": 24,
    "owner": "data-eng-team",
    "description": "Short summary of what this table represents"
  }
}
````

---

# 🧱 Components

## **1. schema (Required)**

Defines column names and types.

Example:

```json
"schema": {
  "order_id": "string",
  "customer_id": "string",
  "order_date": "timestamp",
  "amount": "double"
}
```

Used for:

* Casting columns
* Validation
* Auto schema documentation

---

## **2. quality_rules (Optional)**

Supports:

* **not_null** — important columns must not be null
* **positive_values** — numeric columns must be > 0
* **accepted_values** — enums

Example:

```json
"quality_rules": {
  "not_null": ["order_id", "customer_id"],
  "positive_values": ["amount"],
  "accepted_values": {
    "status": ["pending", "shipped", "delivered", "cancelled"]
  }
}
```

---

## **3. freshness_hours**

Defines how fresh data must be.

Example:

```json
"freshness_hours": 24
```

This is used in:

* SLA monitoring
* Alerts (future)
* LLM answers (“Which tables are stale?”)

---

## **4. owner**

Defines table ownership.

Example:

```json
"owner": "sales-eng-team"
```

Useful for:

* Lineage
* Approval workflows
* LLM queries (“Who owns orders?”)

---

## **5. description**

Human-readable purpose of the table.

Example:

```json
"description": "Contains all customer orders including amount and status."
```

Used heavily by:

* LLM Q&A agent
* Documentation generation

---

# 🛠 How the Metadata Layer Works in ETL

### Step 1 — Load metadata

`metadata_loader.py` loads JSON → Python dict

### Step 2 — Ingestion (Bronze)

Bronze data is read as-is.

### Step 3 — Schema Enforcement

During Silver transform, schema is applied:

* Cast types
* Drop invalid rows
* Standardize formats

### Step 4 — Apply Quality Rules

`rules_engine.py` checks:

* Null counts
* Negative values
* Enum mismatches

Results can be logged into MLflow (future).

### Step 5 — Gold Transform

Gold tables use validated Silver as source.

---

# 🤖 How Metadata Powers LLM Agents

## **Metadata Q&A Agent**

Uses:

* Schema → column-level questions
* Accepted values → ENUM explanations
* Owners → organizational structure
* Freshness → SLA questions
* Rules → data issues

Examples:

* “Show me quality rules for orders table”
* “What does `amount` represent?”
* “Which tables belong to data-eng-team?”

## **Optimization Agent**

Uses:

* Column types
* Schema complexity
* Partition suggestions

Examples:

* “Your timestamp-based table should be partitioned by date.”

---

# 🧪 Testing Metadata

File:

```
tests/test_metadata_engine.py
```

Validates:

* Schema file exists
* Can be loaded
* Contains required fields

---

# 🔮 Future Enhancements

* Metadata versioning (Delta)
* Automatic schema inference + update
* Data lineage visualization
* Integration with Unity Catalog
* Embedding index based on metadata descriptions

---

# ✔ Author

**Janardhana Rao Komanapalli (Janak)**
Senior Data Engineer — Azure | Databricks | Spark | AI/ML

```