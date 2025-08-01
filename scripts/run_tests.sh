#!/bin/bash
# Test runner script for bamsnap

set -e  # Exit on any error

echo "🧪 Running bamsnap tests..."

# Check if we're in a poetry environment
if command -v poetry &> /dev/null; then
    echo "📦 Using Poetry for dependency management"
    RUN_CMD="poetry run"
else
    echo "🐍 Using direct Python"
    RUN_CMD=""
fi

# Install test dependencies if using poetry
if command -v poetry &> /dev/null; then
    echo "📥 Installing test dependencies..."
    poetry install --with dev
fi

echo ""
echo "🏃‍♂️ Running all tests..."
$RUN_CMD pytest

echo ""
echo "📊 Running tests with coverage..."
$RUN_CMD pytest --cov=src --cov-report=html --cov-report=term

echo ""
echo "🔍 Running only unit tests..."
$RUN_CMD pytest tests/unit/ -v

echo ""
echo "🔗 Running only integration tests..."
$RUN_CMD pytest tests/integration/ -v

echo ""
echo "⚡ Running fast tests only (excluding slow tests)..."
$RUN_CMD pytest -m "not slow" -v

echo ""
echo "🏷️  Running tests with specific markers..."
echo "Unit tests:"
$RUN_CMD pytest -m "unit" -v

echo "CLI tests:"
$RUN_CMD pytest -m "cli" -v

echo ""
echo "✅ Test run complete!"
echo "📁 Coverage report available in htmlcov/index.html"
