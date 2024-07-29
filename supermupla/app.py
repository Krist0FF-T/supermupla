import pygame as pg
from time import sleep

from .view import View, PauseView
from .game import Game
from .config import Config


class App:
    def __init__(self, config: Config):
        pg.init()
        self.config = config
        self._create_window()
        self.running: bool
        self.clock = pg.time.Clock()
        self.views: list[View] = []
        self.game = Game(self)
        self.current_view = self.game

    def run(self):
        self.running = True
        while self.running:
            target_fps = self.config.fps
            if self.config.vsync:
                target_fps = 0

            dt_sec = self.clock.tick(target_fps) / 1000
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

    def _create_window(self):
        # flags = pg.OPENGL | pg.DOUBLEBUF
        flags = pg.RESIZABLE
        size = (0, 0)
        if self.config.fullscreen:
            flags |= pg.FULLSCREEN
        else:
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
            self.running = False
            return True

        elif ev.type == pg.KEYDOWN:
            if ev.key == pg.K_ESCAPE:
                if self.views:
                    self.pop_view()
                else:
                    self.push_view(PauseView(self))
                return True

            elif ev.key == pg.K_n:
                sleep(2)

        elif ev.type == pg.WINDOWRESIZED:
            print(ev.x, ev.y)

        return False
