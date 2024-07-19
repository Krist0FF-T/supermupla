import pygame as pg
from .base import MenuView

class SettingsView(MenuView):
    def __init__(self, app):
        super().__init__(app)

    def draw(self):
        super().draw()

        p = (
            self.app.screen.width / 2,
            self.app.screen.height / 10
        )
        pg.draw.circle(self.app.screen, "red", p, 10)


