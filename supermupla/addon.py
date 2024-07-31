from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Optional


@dataclass
class TileType:
    name: str
    solid: bool
    appearance: None | str | Callable = None


class Addon:
    def __init__(
        self,
        name: str = "Unnamed addon",
        tile_types: list[TileType] = [],
        assets_dir: Path = Path(),
        images: dict[str, Path] = {}
    ):
        self.name = name
        self.tile_types = tile_types
        self.images = images
        self.assets_dir = assets_dir

        self.palette = {
            tt.name: tt
            for tt in tile_types
        }

    def get_image_path(self, name) -> Optional[Path]:
        if name not in self.images:
            return None

        return self.assets_dir / "images" / self.images[name]
