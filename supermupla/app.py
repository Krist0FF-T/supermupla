import pygame as pg
import time

from .view import View
from .game import Game
import OpenGL.GL as gl

class App:
    def __init__(self):
        pg.init()
        self.vsync = False
        self.fullscreen = False
        self._create_window()
        gl.glGetError()
        self.running: bool
        self.clock = pg.time.Clock()
        self.views: list[View] = []
        self.game = Game(self)
        self.fps = 60

    def run(self):
        self.running = True
        lag = 0
        c = 0
        while self.running:
            # self.dt = self.clock.tick(self.fps)
            if lag >= 1:
                lag -= 1
                print(c)
                c = 0

            t_start = time.time()

            events = pg.event.get()
            events = self._handle_global_events(events)
            self.current_view.handle_events(events)

            self.current_view.update()
            self.current_view.draw()

            pg.display.flip()

            t_end = time.time()
            lag += t_end - t_start
            c += 1

    @property
    def current_view(self) -> View:
        if self.views:
            return self.views[-1]
        return self.game

    def push_view(self, view: View):
        self.views.append(view)

    def pop_view(self) -> View:
        return self.views.pop()

    def _create_window(self):
        flags = pg.OPENGL | pg.DOUBLEBUF
        # flags = 0
        if self.fullscreen:
            flags |= pg.FULLSCREEN

        self.screen = pg.display.set_mode((1280, 720), flags, vsync=self.vsync)

        # info = pg.display.Info()
        # if self.vsync:
        #     if hasattr(info, "current_h"):
        #         self.fps = pg.display.gl_get_attribute(pg.GL_)
        # else:
        #     self.fps = 60


    def _handle_global_events(self, events) -> list[pg.Event]:
        unhandled = []

        for ev in events:
            handled = True

            if ev.type == pg.QUIT:
                self.running = False

            if ev.type == pg.KEYDOWN:
                if ev.key == pg.K_ESCAPE and self.views:
                    self.pop_view()
                    # self.running = False

                else:
                    handled = False

            if not handled:
                unhandled.append(ev)

        return unhandled


