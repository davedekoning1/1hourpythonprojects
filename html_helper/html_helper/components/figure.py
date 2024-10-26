"""Class to help adding figures to an HTML page."""

from pathlib import Path


class FigureStyling:
    """Class containing information on basic figure styling."""

    def __init__(self):
        pass


class HtmlFigure:
    """Class to help adding figures to an HTML page."""

    def __init__(
        self,
        fpath: str,
        fname: str,
        caption: str = "",
        alt_text: str = "",
        fig_styling: FigureStyling = None,
    ):

        self.fpath = Path(fpath)
        self.fname = fname
        self.source = self.fpath / self.fname
        self.caption = caption
        self.alt_text = alt_text

        if fig_styling is None:
            self.fig_styling = FigureStyling()

    def _create_html_content(self):
        content = """
        <figure>
        <img src="{source}" alt="{alt_text}" style="width:100%">
        <figcaption>{caption}</figcaption>
        </figure>
        """

        return content.format(**self.__dict__)
