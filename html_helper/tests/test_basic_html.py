"""Example showing how to create an HTML with a figure in it."""

import filecmp
from pathlib import Path

from html_helper.components.figure import HtmlFigure
from html_helper.generator.generate_html import create_html

test_dir = Path.cwd() / "tests"
data_dir = test_dir / "test_data"
reference_dir = data_dir / "reference"
output_dir = data_dir / "output"
figure_dir = data_dir / "figures"

for child in output_dir.iterdir():
    if Path.is_file(child):
        child.unlink()


def test_create_empty_html():
    """Test whether empty html is created correctly."""
    fpana_ref = reference_dir / "ref_create_empty_html.html"
    fpana_output = output_dir / "test_create_empty_html.html"
    create_html(fpana_output)

    assert filecmp.cmp(fpana_ref, fpana_output)


def test_create_empty_html_wrong():
    """Test whether test fails when comparing to wrong html."""
    fpana_ref = reference_dir / "ref_create_empty_html_wrong.html"
    fpana_output = output_dir / "test_create_empty_html_wrong.html"
    create_html(fpana_output)

    assert filecmp.cmp(fpana_ref, fpana_output) is False


def test_create_html_with_figure():
    """Test whether html with figure is properly created."""
    fpana_ref = reference_dir / "ref_create_html_with_figure.html"

    fig_path = "figures"
    fig_name = "HBC vlag.jpg"
    components = [
        HtmlFigure(fig_path, fig_name, "Test image.", "This is the logo of HBC")
    ]
    fpana_output = output_dir / "test_create_html_with_figure.html"
    create_html(fpana_output, components)

    assert filecmp.cmp(fpana_ref, fpana_output)
