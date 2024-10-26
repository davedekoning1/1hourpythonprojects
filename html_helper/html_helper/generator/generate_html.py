"""Module to generate the HTML."""

from pathlib import Path
from typing import List

from html_helper.components.figure import HtmlFigure

html_template = """
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

{html_content}

</body>
</html>
"""


def create_html(
    fpana_output: Path, components: List[HtmlFigure] = [], template: str = ""
):
    """
    Create HTML page.

    Returns an empty HTML page when no input is given.

    :param fpana_output: Output filename and path
    :type: str
    :param components: Provide components to be present in the HTML page, defaults to []
    :type components: list[HtmlFigure], optional
    :param template: Provide a new template, defaults to ""
    :type template: str, optional
    """
    if template == "":
        template = html_template

    html_content = []

    for component in components:
        html_content.append(component._create_html_content())

    final_html = template.format(html_content="\n".join(html_content))

    with open(fpana_output, "w", encoding="utf-8") as fh:
        fh.write(final_html)
