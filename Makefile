.PHONY: run test lint format

run:
	uvicorn app.main:app --reload

test:
	pytest -v

lint:
	ruff check app tests

format:
	ruff check --fix app tests
