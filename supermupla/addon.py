from dataclasses import dataclass
from pathlib import Path


@dataclass
class TileType:
    solid: bool
    appearance: None | str = None


class Addon:
    def __init__(
        self,
        name: str = "Unnamed addon",
        tile_types: dict[str, TileType] = {},
        assets_dir: Path = Path(),
        images: dict[str, Path] = {}
    ):
        self.name = name
        self.tile_types = tile_types
        self.images = images
        self.assets_dir = assets_dir
