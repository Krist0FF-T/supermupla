from typing import TYPE_CHECKING
from supermupla.plugin import Plugin, TileType
import importlib

if TYPE_CHECKING:
    from .app import App


class PluginManager:
    def __init__(self, app):
        self.app: App = app

        # specified in the config
        # e.g.
        self.globals: list[str] = []

        # addons that are dependencies of a level
        self.locals: list[str] = []

        self.loaded: dict[str, Plugin] = {}

    def sync_globals(self, names: list[str]):
        self.globals = names
        self._sync()

    def sync_locals(self, names: list[str]):
        self.locals = names
        self._sync()

    def reload(self):
        self.loaded.clear()
        self.app.asset_manager.images.clear()
        print(self.app.asset_manager.images)
        self._sync()

    def _sync(self):
        actives = set(self.globals + self.locals)
        loaded = set(self.loaded.keys())
        # loaded but not active
        to_unload = loaded - actives
        # active but not loaded
        to_load = actives - loaded

        print("syncing: -{}, +{}".format(to_unload, to_load))

        for name in to_unload:
            del self.loaded[name]

        for name in to_load:
            # print("loading plugin:", name)
            module = importlib.import_module(name)
            addon = module.plugin
            self.loaded[name] = addon

    def get_tiletype(self, name: str) -> TileType:
        for plugin in self.loaded.values():
            if name in plugin.palette:
                return plugin.palette[name]

        return TileType(name="error", solid=False, appearance=None)

    def every_tiletype(self) -> list[TileType]:
        tts = []

        for plugin in self.loaded.values():
            for tt in plugin.tile_types:
                if tt in tts:
                    continue

                tts.append(tt)

        return tts
