import pygame as pg

from .view import View
from .game import Game

class App:
    def __init__(self):
        self.vsync = True
        self.fullscreen = True
        self.screen = pg.display.set_mode((1280, 720))
        self.running: bool
        self.clock = pg.time.Clock()
        self.views: list[View] = []
        self.game = Game(self)
        self.fps = 60

    def run(self):
        self.running = True
        while self.running:
            self.clock.tick(self.fps)

            events = pg.event.get()
            events = self._handle_global_events(events)
            self.current_view.handle_events(events)

            self.current_view.update()
            self.current_view.draw()

            pg.display.update()

    @property
    def current_view(self) -> View:
        if self.views:
            return self.views[-1]
        return self.game

    def push_view(self, view: View):
        self.views.append(view)

    def pop_view(self) -> View:
        return self.views.pop()

    def _create_window(self, fullscreen=False):
        flags = pg.OPENGL | pg.DOUBLEBUF
        if fullscreen:
            flags |= pg.FULLSCREEN

        self.screen = pg.display.set_mode((1280, 720), flags, vsync=self.vsync)

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


