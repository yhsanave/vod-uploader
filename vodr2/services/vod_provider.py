from pathlib import Path
from model.vod import VOD
import utils
import os


class VODProvider:
    vods: dict[str, list[VOD]]

    def __init__(self) -> None:
        self.vods = {}

    def get_vods(self) -> dict[str, list[VOD]]:
        return self.vods

    def search_vods(self, search: str = '') -> dict[str, list[VOD]]:
        return dict(map(lambda g: (g[0], list(filter(lambda v: v.search(search) > 75, g[1]))), self.vods.items())) if search else self.get_vods()

    def load_vods(self) -> list[VOD]:
        raise NotImplementedError()


class LocalVODProvider(VODProvider):
    root: Path

    def __init__(self, root: str = './videos') -> None:
        super().__init__()
        self.root = Path(root)

    def load_vods(self, path: str = './videos') -> None:
        self.vods[path] = [VOD(f)
                           for f in utils.filter_videos(os.listdir(path))]


class YouTubeVODProvider(VODProvider):
    pass
