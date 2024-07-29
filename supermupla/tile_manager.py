import pygame as pg
from .addon import TileType

CHUNK_SIZE = 16


class TileManager():
    def __init__(self, game):
        self.game = game
        self.chunks = {}
        self.palette = ["air", "idk"]

    def load_chunks(self):
        tilemap = [
            "B . B B . B . B B . B . B B . B",
            ". B B B B B B B B B B B B B B .",
            "B B . . . . . . . . . . . . B B",
            "B B . B . . . . . . . . B . B B",
            ". B . B . . . B . . . . B . B .",
            "B B . B . . . B . . . . B . B B",
            ". B . . . . . . B . . . . . B .",
            "B B . . . . . B B . . . . . B B",
            "B B . B . . . . . . . . B . B B",
            ". B . . B . . . . . . B . . B .",
            "B B . . . B . . . . B . . . B B",
            ". B . . . . B B B B . . . . B .",
            "B B . . . . . . . . . . . . B B",
            "B B . . . . . . . . . . . . B B",
            ". B B B B B B B B B B B B B B .",
            "B . B B . B . B B . B . B B . B",
        ]

        tiles = [
            [
                int(c == 'B')
                for c in row.split(" ")
            ]
            for row in tilemap
        ]

        self.chunks["0;0"] = tiles

    def get_at(self, x: int, y: int):
        # local_x = x % CHUNK_SIZE
        # local_y = y % CHUNK_SIZE
        # return self.chunks["0;0"][local_y][local_x]

        chunk_x = x // CHUNK_SIZE
        chunk_y = y // CHUNK_SIZE
        chunk_key = str(chunk_x) + ";" + str(chunk_y)

        if chunk_key in self.chunks:
            local_x = x % CHUNK_SIZE
            local_y = y % CHUNK_SIZE
            return self.chunks[chunk_key][local_y][local_x]

        return 0

    def draw(self):
        screen = self.game.app.screen
        # ts = self.game.camera.tile_size

        colors = [
            "darkblue",
            "darkgreen",
        ]

        # def gen_img(color):
        #     img = pg.Surface((ts, ts))
        #     img.fill(color)
        #     return img

        # imgs = [
        #     gen_img(color)
        #     for color in colors
        # ]

        screen_topleft = pg.Vector2(0, 0)
        screen_bottomright = pg.Vector2(self.game.app.screen.size)
        x1, y1 = self.game.camera.point_to_world(screen_topleft)
        x2, y2 = self.game.camera.point_to_world(screen_bottomright)

        for y in range(int(y1-1), int(y2+1)):
            for x in range(int(x1-1), int(x2+1)):
                tile = self.get_at(x, y)

                if tile == 0:
                    continue

                rect_world = pg.Rect(x, y, 1, 1)
                rect = self.game.camera.rect_to_screen(rect_world)

                color = colors[tile - 1]
                pg.draw.rect(screen, color, rect)
                # pg.draw.rect(screen, "white", rect, 2)

                # img = imgs[tile - 1]
                # screen.blit(img, rect)
