from supermupla.addon import Addon, TileType
from pathlib import Path

ports = [
    "aimbot", "box", "checkpoint", "enemy", "falling",
    "flag", "laser", "shooter", "spike", "trampoline"
]

tile_types = [
    TileType(
        name=port,
        solid=False,
        appearance=port
    )
    for port in ports
]

images = {
    port: Path(port + ".png")
    for port in ports
}

addon_path = Path("addons/supermuki_tts")

addon = Addon(
    name="Default",
    assets_dir=addon_path,
    images=images,
    tile_types=tile_types
)
