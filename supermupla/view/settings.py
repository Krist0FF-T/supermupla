import pygame as pg
from .base import MenuView

class SettingsView(MenuView):
    def __init__(self, app):
        super().__init__(app)

    def draw(self):
        super().draw()

        count = 3
        for i in range(count):
            x = (i - (count-1)/2) * 50
            p = (
                self.app.screen.width / 2 + x,
                self.app.screen.height / 2
            )
            pg.draw.circle(self.app.screen, "white", p, 15)


