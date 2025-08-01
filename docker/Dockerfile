# Multi-stage build for bamsnap
FROM python:3.11-slim as builder

# Install system dependencies needed for building Python packages
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    zlib1g-dev \
    libbz2-dev \
    liblzma-dev \
    libcurl4-openssl-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install --no-cache-dir poetry

# Set Poetry configuration
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VENV_IN_PROJECT=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

# Copy Poetry configuration files
WORKDIR /app
COPY pyproject.toml poetry.lock* README.md ./

# Copy source code (needed for local package installation)
COPY src/ ./src/

# Configure Poetry and install dependencies
RUN poetry config virtualenvs.in-project true && \
    poetry config virtualenvs.path /app/.venv && \
    poetry install --only=main && \
    ls -la /app/ && \
    ls -la /app/.venv/ && \
    rm -rf $POETRY_CACHE_DIR

# Production stage
FROM python:3.11-slim as runtime

# Install runtime system dependencies
RUN apt-get update && apt-get install -y \
    zlib1g \
    libbz2-1.0 \
    liblzma5 \
    libcurl4 \
    libssl3 \
    && rm -rf /var/lib/apt/lists/*

# Copy the virtual environment from builder stage
COPY --from=builder /app/.venv /app/.venv

# Make sure to use venv
ENV PATH="/app/.venv/bin:$PATH"

# Copy source code
WORKDIR /app
COPY src/ ./src/
COPY pyproject.toml README.md ./

# Install the package in the container
RUN pip install -e .

# Create a non-root user
RUN useradd --create-home --shell /bin/bash bamsnap
USER bamsnap
WORKDIR /home/bamsnap

# Set the entrypoint to use the CLI
# ENTRYPOINT ["bamsnap"]
# CMD ["--help"]
