from typing import TYPE_CHECKING
import pygame as pg

if TYPE_CHECKING:
    from ..app import App


class View:
    def __init__(self, app):
        self.app: App = app

    def draw(self):
        pass

    def update(self, dt_sec: float):
        pass

    def handle_event(self, ev: pg.Event):
        pass


class MenuView(View):
    def __init__(self, app):
        super().__init__(app)

    def draw(self):
        self.app.game.draw()
        dark = pg.Surface(self.app.screen.size)
        dark.set_alpha(120)
        dark.fill("black")
        self.app.screen.blit(dark, (0, 0))
