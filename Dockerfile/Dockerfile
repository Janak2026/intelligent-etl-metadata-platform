# ----------------------------------------------------
# Base Image (Official Python slim)
# ----------------------------------------------------
FROM python:3.10-slim

# ----------------------------------------------------
# Set working directory
# ----------------------------------------------------
WORKDIR /app

# ----------------------------------------------------
# Install system dependencies (optional: for pandas, uvicorn)
# ----------------------------------------------------
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# ----------------------------------------------------
# Copy project files
# ----------------------------------------------------
COPY ./requirements.txt /app/requirements.txt
COPY ./src /app/src

# ----------------------------------------------------
# Install Python dependencies
# ----------------------------------------------------
RUN pip install --no-cache-dir -r /app/requirements.txt

# ----------------------------------------------------
# Expose FastAPI default port
# ----------------------------------------------------
EXPOSE 8000

# ----------------------------------------------------
# Start the FastAPI server
# ----------------------------------------------------
CMD ["uvicorn", "src.api.fastapi_app:app", "--host", "0.0.0.0", "--port", "8000"]
