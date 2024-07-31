from pathlib import Path
from typing import TYPE_CHECKING
import pygame as pg

if TYPE_CHECKING:
    from .app import App


class AssetManager:
    def __init__(self, app):
        self.app: App = app
        self.images: dict[str, pg.Surface] = {}
        self.font = None

    def get_font(self):
        if self.font:
            return self.font

        self.font = pg.font.Font(self.app.config.font)
        return self.font

    def load_image(self, name: str, path: Path) -> pg.Surface:
        self.images[name] = pg.image.load(path)
        return self.images[name]

    def get_image(self, name: str) -> pg.Surface:
        if name in self.images:
            return self.images[name]

        for addon in self.app.addon_manager.addons:
            path = addon.get_image_path(name)
            if path and path.exists():
                return self.load_image(name, path)

        return self._generate_checkboard()

    def _generate_checkboard(
        self,
        width: int = 8,
        height: int = 8,
        colors: list = [
            "black",
            "white"
        ]
    ) -> pg.Surface:
        img = pg.Surface((width, height))

        for y in range(height):
            for x in range(width):
                idx = (x + y) % len(colors)
                img.set_at((x, y), colors[idx])

        return img
