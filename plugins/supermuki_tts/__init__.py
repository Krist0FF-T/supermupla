from supermupla.plugin import Plugin, TileType
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

plugin_path = Path("plugins/supermuki_tts")

plugin = Plugin(
    name="Default",
    assets_dir=plugin_path,
    images=images,
    tile_types=tile_types
)
