from typing import TYPE_CHECKING
import pygame as pg

if TYPE_CHECKING:
    from .app import App

class Player:
    def __init__(self, color):
        self.color = pg.Color(color)
        self.app: None | App = None

    def set_app(self, app):
        self.app = app

    def draw(self):
        if self.app is None:
            return

        x = self.app.screen.width // 2
        y = self.app.screen.height // 2
        rect = pg.Rect(0, 0, x, y)
        rect.center = x, y
        pg.draw.rect(self.app.screen, self.color, rect)

