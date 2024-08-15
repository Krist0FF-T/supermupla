import pygame as pg
from math import floor  # -2 for -1.2

from supermupla.view import View
from supermupla.tile_manager import CHUNK_SIZE, tile_to_chunk_key

SPEED = 20


class EditorView(View):
    def __init__(self, app):
        super().__init__(app)
        self.focused = (0, 0)
        self.tile = "aimbot"
        self.chunk_mode = False

        # config
        self.grid_enabled = False
        self.chunk_borders_enabled = True

    def update(self, dt_sec: float):
        keys = pg.key.get_pressed()
        cam = self.app.game.camera

        cam.height += (
            keys[pg.K_q] - keys[pg.K_e]
        ) * cam.height * dt_sec

        d = pg.Vector2(
            (keys[pg.K_d] - keys[pg.K_a]),
            (keys[pg.K_s] - keys[pg.K_w]),
        ) * dt_sec * cam.height
        cam.move(d)

        mouse_pos = pg.mouse.get_pos()
        # mouse_pos = (
        #     self.app.screen.width // 2,
        #     self.app.screen.height // 2,
        # )
        in_world = cam.point_to_world(pg.Vector2(mouse_pos))
        self.focused = (
            floor(in_world.x),
            floor(in_world.y),
        )

        x, y = self.focused
        tm = self.app.game.tile_manager

        if not self.chunk_mode:
            mouse_buttons = pg.mouse.get_pressed()
            # mouse_buttons = [
            #     keys[pg.K_j],
            #     keys[pg.K_u],
            #     keys[pg.K_k],
            # ]
            if mouse_buttons[0]:
                tm.set_at(x, y, "air")
            if mouse_buttons[2] and tm.get_at(x, y) == "air":
                tm.set_at(x, y, self.tile)
        else:
            mouse_buttons = pg.mouse.get_just_pressed()
            # _keys = pg.key.get_just_pressed()
            # mouse_buttons = [
            #     _keys[pg.K_j],
            #     _keys[pg.K_u],
            #     _keys[pg.K_k],
            # ]
            key = tile_to_chunk_key(*self.focused)
            if mouse_buttons[0]:
                tm.delete_chunk(key)
            if mouse_buttons[2] and key not in tm.chunks:
                tm.chunks[key] = tm.chunks["0;0"].copy()
                # tm.clear_chunk(key, self.tile)

        if keys[pg.K_x]:
            self.tile = tm.get_at(x, y)

    def draw(self):
        self.app.screen.fill("skyblue")
        self.app.game.tile_manager.draw()

        self._draw_focused()

        # pg.draw.circle(
        #     self.app.screen, "red",
        #     (
        #         self.app.screen.width // 2,
        #         self.app.screen.height // 2,
        #     ),
        #     5
        # )

        if self.grid_enabled:
            self._draw_grid()

        if self.chunk_borders_enabled:
            self._draw_chunk_borders()

    def handle_event(self, ev: pg.Event):
        if ev.type == pg.KEYDOWN:
            if ev.key == pg.K_g:
                self.grid_enabled = not self.grid_enabled
            elif ev.key == pg.K_c:
                # self.app.game.tile_manager.clear_chunk(
                #     tile_to_chunk_key(*self.focused), self.tile
                # )
                self.chunk_mode = not self.chunk_mode

        elif ev.type == pg.MOUSEWHEEL:
            tm = self.app.game.tile_manager
            current_idx = tm.reverse_palette[self.tile]
            idx = (current_idx + ev.y) % len(tm.palette)
            self.tile = tm.palette[idx]

    def _draw_focused(self):
        x, y = self.focused
        img_key = self.app.game.tile_manager.get_appearance(x, y, self.tile)

        if not img_key:
            return

        img = self.app.asset_manager.get_image(img_key)

        rect_world = pg.Rect(x, y, 1.0, 1.0)
        rect = self.app.game.camera.rect_to_screen(rect_world)
        pos = self.app.game.camera.point_to_screen(pg.Vector2(x, y))

        # idx = (x + y) % 2
        # color = colors[idx]
        # pg.draw.rect(screen, color, rect)

        scaled = pg.transform.scale(img, (rect.width, rect.height))
        scaled.set_alpha(128)
        self.app.screen.blit(scaled, pos)

    def _draw_grid(self):
        scr = self.app.screen
        cam = self.app.game.camera

        tl = cam.point_to_world(pg.Vector2(0, 0))
        br = cam.point_to_world(pg.Vector2(scr.width, scr.height))

        for wx in range(int(tl.x), int(br.x) + 1):
            sx = cam.point_to_screen(pg.Vector2(wx, 0)).x
            pg.draw.line(scr, "black", (sx, 0), (sx, scr.height))

        for wy in range(int(tl.y), int(br.y) + 1):
            sy = cam.point_to_screen(pg.Vector2(0, wy)).y
            pg.draw.line(scr, "black", (0, sy), (scr.width, sy))

    def _draw_chunk_borders(self):
        scr = self.app.screen
        cam = self.app.game.camera
        tm = self.app.game.tile_manager

        tl = cam.point_to_world(pg.Vector2(0, 0))
        br = cam.point_to_world(pg.Vector2(scr.width, scr.height))
        tl_chunk = tl / CHUNK_SIZE
        br_chunk = br / CHUNK_SIZE

        for y in range(int(tl_chunk.y)-1, int(br_chunk.y)+1):
            for x in range(int(tl_chunk.x)-1, int(br_chunk.x)+1):
                key = str(x) + ";" + str(y)
                if key in tm.chunks:
                    rect = cam.rect_to_screen(pg.Rect(
                        x * CHUNK_SIZE,
                        y * CHUNK_SIZE,
                        CHUNK_SIZE,
                        CHUNK_SIZE
                    ))

                    line_width = max(int(cam.tile_size * 0.1), 1)
                    pg.draw.rect(scr, "darkblue", rect, line_width)
