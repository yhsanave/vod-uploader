from textual.containers import Horizontal, Vertical
from textual.widgets import Static, Label, Input, TextArea


class SetFormWidget(Static):
    """Form widget for entering the set info"""

    BINDINGS = [("^w", 'swap_players', 'Swap Players')]

    def compose(self):
        with Horizontal(id="players"):
            with Vertical(id="player1", classes="form-group"):
                yield Label("Player 1", classes="form-group-label")
                with Horizontal(classes="player-name"):
                    yield Input(placeholder="Sponsor", classes="sponsor")
                    yield Input(placeholder="Tag", classes="tag")
                yield Input(placeholder="Characters", classes="character")
            with Vertical(id="player2", classes="form-group"):
                yield Label("Player 2", classes="form-group-label")
                with Horizontal(classes="player-name"):
                    yield Input(placeholder="Sponsor", classes="sponsor")
                    yield Input(placeholder="Tag", classes="tag")
                yield Input(placeholder="Characters", classes="character")
        with Vertical(id="set", classes="form-group"):
            yield Label("Set", classes="form-group-label")
            yield Input(placeholder="Phase")
            yield Input(placeholder="Round")
            yield Input(placeholder="Tournament")
        with Vertical(id="preview", classes="form-group"):
            yield Label("Preview", classes="form-group-label")
            yield TextArea(id="title")
            yield TextArea(id="description")

    def action_swap_players(self):
        pass