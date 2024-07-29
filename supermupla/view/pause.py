import pygame as pg

from .settings import SettingsView
from .base import MenuView


class PauseView(MenuView):
    def __init__(self, app):
        super().__init__(app)

    def draw(self):
        super().draw()
        rect1 = pg.Rect(0, 0, 30, 100)
        rect1.centery = self.app.screen.height // 2
        rect2 = rect1.copy()
        rect1.centerx = self.app.screen.width // 2 - 30
        rect2.centerx = self.app.screen.width // 2 + 30

        pg.draw.rect(self.app.screen, "white", rect1)
        pg.draw.rect(self.app.screen, "white", rect2)

    def handle_event(self, ev: pg.Event):
        if ev.type == pg.KEYDOWN:
            if ev.key == pg.K_s:
                self.app.push_view(SettingsView(self.app))
