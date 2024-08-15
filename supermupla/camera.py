from math import ceil
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
        return self.game.app.screen.height / self.height

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
        return pg.Vector2(
            self.game.app.screen.width / 2 + rx,
            self.game.app.screen.height / 2 + ry,
        )

    def rect_to_screen(self, rect: pg.Rect):
        tl = self.point_to_screen(pg.Vector2(rect.left, rect.top))
        # print(tl)
        br = self.point_to_screen(pg.Vector2(rect.right, rect.bottom))
        w = ceil(br.x - tl.x)
        h = ceil(br.y - tl.y)
        return pg.Rect(tl, (w, h))

    def point_to_world(self, p: pg.Vector2) -> pg.Vector2:
        rx = p.x - self.game.app.screen.width / 2
        ry = p.y - self.game.app.screen.height / 2
        return pg.Vector2(
            rx / self.tile_size + self.pos.x,
            ry / self.tile_size + self.pos.y
        )
