
# cv-generator

Generate a professional resume from structured JSON data using Jinja2 templates and CSS, with PDF export via WeasyPrint. Formatting and content are fully separated for easy customization and privacy.

## Features
- Store resume content in a simple JSON file
- Use Jinja2 templates and CSS for flexible formatting
- Export to HTML and PDF (via WeasyPrint)
- Hide sensitive data using environment variables and a `.env` file
- Easily customizable and automation-friendly

## Project Structure

```
cv-generator/
├── data/
│   └── resume.json         # Resume content (with env var placeholders for secrets)
├── templates/
│   └── resume.html.j2      # Jinja2 template
├── static/
│   └── style.css           # CSS for styling
├── output/
│   ├── resume.html         # Generated HTML
│   └── resume.pdf          # Generated PDF
├── .env                    # Secrets (not committed)
├── main.py                 # Main script
├── Makefile                # Common commands
├── pyproject.toml          # Project metadata
├── uv.lock                 # Dependency lock file
└── README.md
```

## Setup

1. Install [uv](https://github.com/astral-sh/uv) (if not already):
	 ```sh
    # On macOS and Linux.
    curl -LsSf https://astral.sh/uv/install.sh | sh
	 ```
2. Install dependencies:
	 ```sh
	 make install
	 ```
3. Copy `.env.example` to `.env` and fill in your secrets (phone, city, etc):
	 ```sh
	 cp .env.example .env
	 # Edit .env with your values
	 ```

## Usage

- Generate HTML and PDF resume:
	```sh
	make run
	```
- Format code:
	```sh
	make format
	```
- Clean generated files:
	```sh
	make clean
	```

## Customization

- Edit `data/resume.json` for your content (use `${VAR}` for secrets)
- Edit `templates/resume.html.j2` for layout/sections
- Edit `static/style.css` for styling

## Security & Privacy

Sensitive fields (like phone, city) are replaced with environment variable placeholders in `resume.json` and loaded from `.env` at runtime. Do not commit your `.env` file to public repositories.

## License

MIT
