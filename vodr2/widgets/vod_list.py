from textual.containers import Vertical
from textual.widgets import Static, DirectoryTree


class VODListWidget(Static):
    """List of VODs"""
    CSS = """
        VODListWidget {
            dock: left;
            width: 20;
            height: 100%;
        }
        """

    def compose(self):
        with Vertical():
            yield DirectoryTree('./')
