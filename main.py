import json
import os
import re
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
from dotenv import load_dotenv


def load_resume_data(path):
    """Load resume data from a JSON file and substitute env vars."""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return substitute_env_vars(data)


def substitute_env_vars(obj):
    """Recursively substitute ${VAR} in strings with environment variables."""
    if isinstance(obj, dict):
        return {k: substitute_env_vars(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [substitute_env_vars(i) for i in obj]
    elif isinstance(obj, str):
        # Replace ${VAR} with value from environment
        return re.sub(r"\$\{(\w+)\}", lambda m: os.getenv(m.group(1), m.group(0)), obj)
    else:
        return obj


def render_resume_html(data, template_dir, template_name="resume.html.j2"):
    """Render resume HTML from data using a Jinja2 template."""
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(template_name)
    return template.render(**data)


def write_file(path, content):
    """Write content to a file."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def convert_html_to_pdf(html_path, pdf_path):
    """Convert an HTML file to PDF using WeasyPrint."""
    HTML(html_path).write_pdf(pdf_path)


def main():
    """
    Main entry point for the resume generator.
    Loads resume data, renders HTML, writes output, and generates PDF.
    """

    # Load environment variables from .env if present
    load_dotenv()

    data_path = os.path.join("data", "resume.json")
    template_path = os.path.join("templates")
    output_dir = os.path.join("output")
    output_html = os.path.join(output_dir, "resume.html")
    output_pdf = os.path.join(output_dir, "resume.pdf")

    os.makedirs(output_dir, exist_ok=True)

    resume_data = load_resume_data(data_path)
    rendered_html = render_resume_html(resume_data, template_path)
    write_file(output_html, rendered_html)
    print(f"Resume HTML generated at {output_html}")

    convert_html_to_pdf(output_html, output_pdf)
    print(f"Resume PDF generated at {output_pdf}")


if __name__ == "__main__":
    main()
