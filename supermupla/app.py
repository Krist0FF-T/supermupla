import pygame as pg
from time import sleep
import sys

from supermupla.asset_manager import AssetManager
from supermupla.view.editor import EditorView

from .addon_manager import AddonManager

from .view import View
from .game import Game
from .config import Config


class App:
    def __init__(self, config: Config):
        pg.init()
        self.config = config
        self._create_window()

        self.addon_manager = AddonManager()
        self.addon_manager.load_addons(self.config.addons)

        self.views: list[View] = []
        self.game = Game(self)
        self.current_view = self.game

        self.asset_manager = AssetManager(self)

    def run(self):
        clock = pg.time.Clock()
        running = True
        self.push_view(EditorView(self))
        while running:
            target_fps = self.config.fps
            if self.config.vsync:
                target_fps = 0

            dt_sec = clock.tick(target_fps) / 1000
            dt_sec = min(dt_sec, 0.1)
            # print(round(self.clock.get_fps()))

            if self.views:
                self.current_view = self.views[-1]
            else:
                self.current_view = self.game

            events = pg.event.get()
            for ev in events:
                if not self._global_event(ev):
                    self.current_view.handle_event(ev)

            self.current_view.update(dt_sec)
            self.current_view.draw()

            pg.display.flip()

    def push_view(self, view: View):
        self.views.append(view)

    def pop_view(self) -> View:
        return self.views.pop()

    def close(self):
        pg.quit()
        sys.exit()

    def _create_window(self):
        # flags = pg.OPENGL | pg.DOUBLEBUF
        flags = pg.RESIZABLE
        size = (0, 0)
        if self.config.fullscreen:
            flags |= pg.FULLSCREEN
        else:
            pass
        size = self.config.window_size

        self.screen = pg.display.set_mode(
            size, flags, vsync=self.config.vsync
        )

        # info = pg.display.Info()
        # if self.vsync:
        #     if hasattr(info, "current_h"):
        #         self.fps = pg.display.gl_get_attribute(pg.GL_)
        # else:
        #     self.fps = 60

    def _global_event(self, ev: pg.Event) -> bool:
        if ev.type == pg.QUIT:
            self.close()
            return True

        elif ev.type == pg.KEYDOWN:
            if ev.key == pg.K_ESCAPE:
                # self.close()
                if self.views:
                    self.pop_view()
                    return True

            elif ev.key == pg.K_n:
                sleep(2)

        elif ev.type == pg.WINDOWRESIZED:
            print(ev.x, ev.y)

        return False
