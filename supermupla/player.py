from typing import TYPE_CHECKING
import pygame as pg

if TYPE_CHECKING:
    from .game import Game

class Player:
    def __init__(self, game, color):
        self.color = pg.Color(color)
        self.game: Game = game

    def draw(self):
        screen = self.game.app.screen

        x = screen.width // 2
        y = screen.height // 2
        rect = pg.Rect(0, 0, x, y)
        rect.center = x, y
        pg.draw.rect(screen, self.color, rect)

