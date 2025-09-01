.PHONY: help install test test-cov test-html clean docker-build docker-test docker-clean setup

# Default target
help:
	@echo "Available commands:"
	@echo "  setup          - Set up development environment"
	@echo "  install        - Install dependencies"
	@echo "  test           - Run all tests"
	@echo "  test-cov       - Run tests with coverage"
	@echo "  test-html      - Run tests with HTML coverage report"
	@echo "  test-watch     - Run tests in watch mode"
	@echo "  lint           - Run code linting"
	@echo "  clean          - Clean up generated files"
	@echo "  docker-build   - Build Docker image"
	@echo "  docker-test    - Run tests in Docker"
	@echo "  docker-clean   - Clean Docker images and containers"

# Development setup
setup:
	python -m venv envSearchAlgo
	@echo "Virtual environment created. Activate with:"
	@echo "  Windows: envSearchAlgo\\Scripts\\activate"
	@echo "  macOS/Linux: source envSearchAlgo/bin/activate"

# Install dependencies
install:
	pip install --upgrade pip
	pip install -r requirements.txt
	touch Search_Algo/__init__.py

# Testing commands
test:
	pytest -v

test-cov:
	pytest -v --cov=Search_Algo --cov-report=term-missing

test-html:
	pytest -v --cov=Search_Algo --cov-report=html --cov-report=term-missing
	@echo "HTML coverage report generated in htmlcov/index.html"

test-watch:
	pytest-watch -- -v --cov=Search_Algo

test-specific:
	pytest test_searching.py -v

test-graph:
	pytest test_searching2.py -v

# Code quality
lint:
	flake8 Search_Algo/ --max-line-length=127
	flake8 test_*.py --max-line-length=127

format:
	black Search_Algo/ test_*.py

# Cleanup
clean:
	rm -rf __pycache__/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf coverage.xml
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete

# Docker commands
docker-build:
	docker build -t searching-algo-pytest .

docker-test:
	docker run --rm searching-algo-pytest

docker-interactive:
	docker run -it --rm -v $(PWD):/app searching-algo-pytest /bin/bash

docker-clean:
	docker rmi searching-algo-pytest || true
	docker system prune -f

# Compose commands
compose-test:
	docker-compose up pytest-runner

compose-watch:
	docker-compose up pytest-watch

compose-interactive:
	docker-compose run pytest-interactive

# Performance benchmarking
benchmark:
	pytest --benchmark-only --benchmark-json=benchmark.json

# Generate requirements
freeze:
	pip freeze > requirements.txt

# Security scanning
security:
	safety check -r requirements.txt
	bandit -r Search_Algo/