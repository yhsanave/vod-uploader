from textual.app import App
from textual.containers import Vertical
from textual.widgets import Header, Footer, ContentSwitcher, Label
# from services.vod_provider import VODProvider
from widgets.set_form import SetFormWidget
from widgets.vod_list import VODListWidget


class VODrApp(App):
    # vodProvider: VODProvider

    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        # self.vodProvider = vodProvider

    BINDINGS = [
        ("^w", 'swap_players', 'Swap Players'),
        ("^s", 'next_vod', 'Next Vod'),
        ("^e", 'export', 'Export'),
    ]

    CSS_PATH = "vodr.tcss"

    def compose(self):
        with Vertical(id="sidebar"):
            yield VODListWidget()
        with ContentSwitcher(initial="test", id="setForm"):
            yield Label("Select a VOD", id="noneSelected")
            yield SetFormWidget(id="test")
        yield Header()
        yield Footer()

    def action_swap_players(self):
        pass

    def action_next_vod(self):
        pass

    def action_export(self):
        pass


if __name__ == "__main__":
    VODrApp().run()
