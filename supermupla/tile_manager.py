from dataclasses import dataclass
import time
from typing import Callable, Optional
import pygame as pg
from math import ceil, floor

from supermupla.plugin import TileType

CHUNK_SIZE = 16


def chunk_key(x: int, y: int) -> str:
    return str(x) + ";" + str(y)


def tile_to_chunk_key(x: int, y: int) -> str:
    return chunk_key(
        floor(x / CHUNK_SIZE),
        floor(y / CHUNK_SIZE)
    )


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
            for tt in self.game.app.plugin_manager.every_tiletype()
        ]

        self.reverse_palette = {
            name: idx
            for idx, name in enumerate(self.palette)
        }

        self.scaled_cache: dict[str, pg.Surface] = {}
        self.cache_tile_size = 0
        self.fpss = []

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

    def clear_chunk(self, key: str, name="air"):
        self.chunks[key] = [
            [
                self.reverse_palette[name]
                for _ in range(CHUNK_SIZE)
            ]
            for _ in range(CHUNK_SIZE)
        ]

    def delete_chunk(self, key: str):
        if key in self.chunks:
            # print(self.chunks[key])
            self.chunks.pop(key)

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
            return self.game.app.plugin_manager.get_tiletype(name)

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
    ) -> Optional[str]:
        if not name:
            name = self.get_at(x, y)

        t = self.game.app.plugin_manager.get_tiletype(name)
        a = t.appearance

        if not a:
            return None

        if isinstance(a, Callable):
            neighbors = self._get_neighbors(x, y)
            a = a(neighbors)

        return a

    def get_scaled(self, img_key: str) -> pg.Surface:
        if img_key in self.scaled_cache:
            return self.scaled_cache[img_key]

        img = self.game.app.asset_manager.get_image(img_key)
        s = (self.cache_tile_size, ) * 2
        scaled = pg.transform.scale(img, s)
        self.scaled_cache[img_key] = scaled
        return scaled

    def _draw_chunk(self, chx: int, chy: int) -> list[tuple]:
        k = chunk_key(chx, chy)

        if k not in self.chunks:
            return []

        blits = []

        for i in range(CHUNK_SIZE):
            for j in range(CHUNK_SIZE):
                tx = chx * CHUNK_SIZE + j
                ty = chy * CHUNK_SIZE + i

                img_key = self.get_appearance(tx, ty)

                if not img_key:
                    continue

                if img_key in self.scaled_cache:
                    scaled = self.scaled_cache[img_key]

                else:
                    img = self.game.app.asset_manager.get_image(img_key)
                    s = (self.cache_tile_size, ) * 2
                    scaled = pg.transform.scale(img, s)
                    self.scaled_cache[img_key] = scaled
                    # print("cached", img_key, time.time(), s)

                p = pg.Vector2(tx, ty)
                p = self.game.camera.point_to_screen(p)

                # self.game.app.screen.blit(scaled, p)
                blits.append((scaled, p))

        # self.game.app.screen.blits(blits)
        return blits

    def draw(self):
        scr = self.game.app.screen
        cam = self.game.camera
        ts = ceil(self.game.camera.tile_size)

        if ts != self.cache_tile_size:
            self.scaled_cache.clear()
            self.cache_tile_size = ts

        tl_tile = cam.point_to_world(pg.Vector2(0, 0))
        br_tile = cam.point_to_world(pg.Vector2(scr.size))

        tl_chunk = (
            floor(tl_tile.x / CHUNK_SIZE),
            floor(tl_tile.y / CHUNK_SIZE)
        )

        br_chunk = (
            ceil(br_tile.x / CHUNK_SIZE),
            ceil(br_tile.y / CHUNK_SIZE)
        )

        start = time.time()

        c = 0
        dc = 0
        blits: list[tuple] = []
        for chunk_y in range(tl_chunk[1], br_chunk[1]):
            for chunk_x in range(tl_chunk[0], br_chunk[0]):
                c += 1

                k = chunk_key(chunk_x, chunk_y)
                if k in self.chunks:
                    blits += self._draw_chunk(chunk_x, chunk_y)
                    dc += 1

        self.game.app.screen.blits(blits)

        end = time.time()
        fps = int(1 / (end - start))
        self.fpss.append(fps)
        if len(self.fpss) > 10:
            # self.fpss.pop(0)
            avg_fps = int(sum(self.fpss) / len(self.fpss))
            print(f"{dc}/{c}", "chunks", len(blits), "tiles", avg_fps, "fps")
            self.fpss.clear()
