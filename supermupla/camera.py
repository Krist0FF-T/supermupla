import pygame as pg

CAMERA_INSTANT = 0
CAMERA_LERP = 1

class Camera:
    def __init__(self, game, mode=CAMERA_INSTANT):
        self.game = game
        self.mode = mode

        self.pos = pg.Vector2(0, 0)

        # number of tile visible horizontally
        self.height = 20.0

    @property
    def tile_size(self):
        return int(self.game.app.screen.height / self.height)

    def update(self, target: pg.Vector2):
        if self.mode == CAMERA_LERP:
            self.pos.lerp(target, 0.95 / self.game.app.fps)

        else:
            self.pos = target

    def move(self, displacement):
        self.update(self.pos + displacement)

    def point_to_screen(self, p: pg.Vector2):
        rx = (p.x - self.pos.x) * self.tile_size
        ry = (p.y - self.pos.y) * self.tile_size
        return (
            self.game.app.screen.width  // 2 + round(rx),
            self.game.app.screen.height // 2 + round(ry),
        )

    def rect_to_screen(self, rect: pg.Rect):
        tl = self.point_to_screen(pg.Vector2(rect.x, rect.y))
        return pg.Rect(tl, (self.tile_size,) * 2)

    def point_to_world(self, p: pg.Vector2):
        rx = p.x - self.game.app.screen.width  / 2
        ry = p.y - self.game.app.screen.height / 2
        return (
            rx / self.tile_size + self.pos.x,
            ry / self.tile_size + self.pos.y
        )


