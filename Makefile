install:
	uv run pre-commit install

format:
	uv run pre-commit run --all-files

clean:
	rm -rf output/*

run:
	uv run main.py
