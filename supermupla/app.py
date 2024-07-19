import pygame as pg

from .view import View, GameView

class App:
    def __init__(self):
        self.screen = pg.display.set_mode((1280, 720))
        self.running: bool
        self.clock = pg.time.Clock()
        self.views: list[View] = []
        self.game = GameView(self)

    @property
    def current_view(self) -> View:
        if self.views:
            return self.views[-1]
        return self.game

    def run(self):
        # self.push_view(View())
        self.running = True
        while self.running:
            self.clock.tick(60)
            self._handle_events()

            self.current_view.update()
            self.current_view.draw()
            pg.display.update()

    def push_view(self, view: View):
        self.views.append(view)

    def pop_view(self) -> View:
        return self.views.pop()

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

    def _handle_events(self):
        events = pg.event.get()
        events = self._handle_global_events(events)
        self.current_view.handle_events(events)

