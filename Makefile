install:
	uv run pre-commit install

format:
	uv run pre-commit run --all-files

run:
	uv run main.py
