import pygame as pg
from . import consts

CAMERA_LERP = 0

class Camera:
    def __init__(self):
        self.pos = pg.Vector2(0, 0)
        self.mode = CAMERA_LERP

    def update(self, target: pg.Vector2):
        self.pos.lerp(target, 0.95 * consts.DT)


