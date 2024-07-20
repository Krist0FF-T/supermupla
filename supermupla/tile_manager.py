import pygame as pg

class TileManager:
    def __init__(self, game):
        self.game = game
        self.tiles = []

    def load_tiles(self):
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

        self.tiles = [
            [
                int(c == 'B')
                for c in row.split(" ")
            ]
            for row in tilemap
        ]

    def draw(self):
        screen = self.game.app.screen
        ts = self.game.camera.tile_size

        img = pg.Surface((2, 2))
        img.set_at((0, 0), "red")
        img.set_at((0, 1), "green")
        img.set_at((1, 0), "blue")
        img.set_at((1, 1), "yellow")
        img = pg.transform.scale(img, (ts, ts))

        colors = [
            "black",
            "blue",
        ]

        for i, row in enumerate(self.tiles):
            for j, tile in enumerate(row):
                if tile == 0:
                    continue

                # rect = pg.Rect(j * ts, i * ts, ts, ts)

                rect_world = pg.Rect(j, i, 1, 1)
                rect = self.game.camera.rect_to_screen(rect_world)

                pg.draw.rect(screen, "darkblue", rect)
                pg.draw.rect(screen, "white", rect, 2)

                # screen.blit(img, rect)

