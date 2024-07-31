from supermupla.addon import Addon, TileType
import importlib


class AddonManager:
    def __init__(self):
        self.addons = []

    def load_addons(self, addons: list[str]):
        for name in addons:
            print(name)
            module = importlib.import_module(name)
            addon = module.addon
            self.addons.append(addon)

    def get_tiletype(self, name: str) -> TileType:
        for addon in self.addons:
            if name in addon.palette:
                return addon.palette[name]

        return TileType(name="error", solid=False, appearance=None)

    def every_tiletype(self) -> list[TileType]:
        tts = []

        for addon in self.addons:
            for tt in addon.tile_types:
                if tt in tts:
                    continue

                tts.append(tt)

        return tts
