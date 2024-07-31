import pygame as pg

from .view import View, PauseView, EditorView
from .tile_manager import TileManager
from .camera import Camera

SPEED = 20


class Game(View):
    '''
    A special View that's stored outside of App.views, so it's unpoppable
    '''

    def __init__(self, app):
        super().__init__(app)
        self.tile_manager = TileManager(self)
        self.tile_manager.load_chunks()
        self.camera = Camera(self)
        self.camera.pos = pg.Vector2(8, 8)

    def update(self, dt_sec: float):
        keys = pg.key.get_pressed()

        d = pg.Vector2(
            (keys[pg.K_d] - keys[pg.K_a]),
            (keys[pg.K_s] - keys[pg.K_w]),
        ) * dt_sec * self.camera.height

        self.camera.height += (
            keys[pg.K_q] - keys[pg.K_e]
        ) * self.camera.height * dt_sec

        self.camera.move(d)

    def draw(self):
        self.app.screen.fill("skyblue")
        self.tile_manager.draw()

    def handle_event(self, ev: pg.Event):
        if ev.type == pg.KEYDOWN:
            if ev.key == pg.K_ESCAPE:
                self.app.push_view(PauseView(self.app))

            if ev.key == pg.K_t:
                self.app.push_view(EditorView(self.app))
