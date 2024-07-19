import pygame as pg

from .pause import PauseView

from ..consts import DT
from .base import View

SPEED = 200

class GameView(View):
    def __init__(self, app):
        super().__init__(app)
        self.pos = pg.Vector2(10, 10)

    @property
    def tile_size(self):
        if self.app:
            return self.app.screen.height / 12

    def update(self):
        dx = SPEED * DT
        dy = 0

        keys = pg.key.get_pressed()
        if keys[pg.K_w]: dy -= SPEED * DT
        if keys[pg.K_s]: dy += SPEED * DT

        self.pos += (dx, dy)
        self.pos.x %= self.app.screen.width

    def draw(self):
        if self.app is None:
            return

        self.app.screen.fill("skyblue")

        pg.draw.circle(self.app.screen, "red", self.pos, 10)

    def handle_events(self, events: list[pg.Event]):
        for ev in events:
            if ev.type == pg.KEYDOWN:
                if ev.key == pg.K_ESCAPE:
                    self.app.push_view(PauseView(self.app))
        

