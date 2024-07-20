import pygame as pg

from .view import View, PauseView
from .tile_manager import TileManager
from .camera import Camera

SPEED = 10

class Game(View):
    '''
    A special View that's stored outside of App.views, so it's unpoppable
    '''

    def __init__(self, app):
        super().__init__(app)
        self.tile_manager = TileManager(self)
        self.tile_manager.load_tiles()
        self.camera = Camera(self)

    def update(self):
        dt = 1 / self.app.fps
        d = pg.Vector2(0.0, 0.0)

        keys = pg.key.get_pressed()
        if keys[pg.K_w]: d.y -= SPEED * dt
        if keys[pg.K_s]: d.y += SPEED * dt
        if keys[pg.K_a]: d.x -= SPEED * dt
        if keys[pg.K_d]: d.x += SPEED * dt

        if keys[pg.K_q]: self.camera.height += SPEED * dt
        if keys[pg.K_e]: self.camera.height -= SPEED * dt

        self.camera.move(d)

    def draw(self):
        screen = self.app.screen
        self.app.screen.fill("skyblue")
        self.tile_manager.draw()

    def handle_events(self, events: list[pg.Event]):
        for ev in events:
            if ev.type == pg.KEYDOWN:
                if ev.key == pg.K_ESCAPE:
                    self.app.push_view(PauseView(self.app))
        

