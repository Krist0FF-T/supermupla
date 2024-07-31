from dataclasses import dataclass
from typing import Callable, Optional
import pygame as pg

from supermupla.addon import TileType

CHUNK_SIZE = 16


def chunk_key(x: int, y: int) -> str:
    return str(x) + ";" + str(y)


@dataclass
class Neighbors:
    left: TileType
    right: TileType
    top: TileType
    bottom: TileType


class TileManager():
    def __init__(self, game):
        self.game = game
        self.chunks = {}
        self.palette = [
            tt.name
            for tt in self.game.app.addon_manager.every_tiletype()
        ]
        self.reverse_palette = {
            name: idx
            for idx, name in enumerate(self.palette)
        }

    def load_chunks(self):
        tilemap = [
            "U . U U . U . U U . U . U U . U",
            ". U B B U B U B B U B B B B U .",
            "U B . . . . . . . . . . . . B U",
            "B B . S S . . . . . . S S . B B",
            ". B . S S . . U . . . S S . B .",
            "U B . S S . . B . . . S S . B U",
            ". B . . . . . . U . . . . . B .",
            "U B . . . . . U B . . . . . B U",
            "B B . U . . . . . . . . U . B B",
            ". B . . U . . . . . . U . . B .",
            "U B . . . U . . . . U . . . B U",
            ". B . . . . U U U U . . . . B .",
            "U B . . . . . . . . . . . . B U",
            "B B . . . . . . . . . . . . B B",
            ". B U U U U U U U U U U U U B .",
            "U . B B . B . B B . B . B B . U",
        ]

        chars = {
            '.': "air",
            'B': "dirt",
            'U': "dirt",
            'S': "smiley",
        }

        self.chunks[chunk_key(0, 0)] = [
            [
                self.reverse_palette[chars[c]]
                for c in row.split(" ")
            ]
            for row in tilemap
        ]

    def clear_chunk(self, key: str):
        self.chunks[key] = [
            [
                self.reverse_palette["air"]
                for _ in range(CHUNK_SIZE)
            ]
            for _ in range(CHUNK_SIZE)
        ]

    def get_at(self, x: int, y: int) -> str:
        # local_x = x % CHUNK_SIZE
        # local_y = y % CHUNK_SIZE
        # return self.chunks["0;0"][local_y][local_x]

        chunk_x = x // CHUNK_SIZE
        chunk_y = y // CHUNK_SIZE
        key = chunk_key(chunk_x, chunk_y)

        if key in self.chunks:
            local_x = x % CHUNK_SIZE
            local_y = y % CHUNK_SIZE
            idx = self.chunks[key][local_y][local_x]
            return self.palette[idx]

        return "air"

    def set_at(self, x: int, y: int, name: str):
        idx = self.reverse_palette[name]

        chunk_x = x // CHUNK_SIZE
        chunk_y = y // CHUNK_SIZE
        chunk_key = str(chunk_x) + ";" + str(chunk_y)
        # print(f"({x=}, {y=}), {name=}, {chunk_key=}")

        if chunk_key in self.chunks:
            local_x = x % CHUNK_SIZE
            local_y = y % CHUNK_SIZE
            self.chunks[chunk_key][local_y][local_x] = idx
        else:
            self.clear_chunk(chunk_key)

    def _get_neighbors(self, x: int, y: int):
        def g(dx: int, dy: int):
            name = self.get_at(x + dx, y + dy)
            return self.game.app.addon_manager.get_tiletype(name)

        return Neighbors(
            top=g(0, -1),
            bottom=g(0, 1),
            left=g(-1, 0),
            right=g(1, 0),
        )

    def get_appearance(
            self,
            x: int = 0,
            y: int = 0,
            name: Optional[str] = None
    ) -> Optional[pg.Surface]:
        name = name if name else self.get_at(x, y)
        t = self.game.app.addon_manager.get_tiletype(name)
        a = t.appearance

        if not a:
            return None

        if isinstance(a, Callable):
            neighbors = self._get_neighbors(x, y)
            a = a(neighbors)

        return self.game.app.asset_manager.get_image(a)

    def draw(self):
        screen = self.game.app.screen
        # ts = self.game.camera.tile_size

        # colors = [
        #     # "darkblue",
        #     # "darkgreen",
        #     "black",
        #     "white"
        # ]

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
                img = self.get_appearance(x, y)

                if not img:
                    continue

                rect_world = pg.Rect(x, y, 1, 1)
                rect = self.game.camera.rect_to_screen(rect_world)

                # idx = (x + y) % 2
                # color = colors[idx]
                # pg.draw.rect(screen, color, rect)

                scaled = pg.transform.scale(img, (rect.width, rect.height))
                screen.blit(scaled, rect)
