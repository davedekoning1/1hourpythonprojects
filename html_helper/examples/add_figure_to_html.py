"""Example showing how to create an HTML with a figure in it."""

from pathlib import Path

from html_helper.generator.generate_html import create_html

if __name__ == "__main__":
    fpana_output = Path.cwd() / "examples" / "output" / "test.html"
    create_html(fpana_output)
