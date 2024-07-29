from supermupla.addon import Addon, TileType
from pathlib import Path

tile_types = {
    "air": TileType(
        solid=False,
        appearance=None
    ),
    "idk": TileType(
        solid=True,
        appearance="idk"
    )
}

images = {
    "idk": "idk.png"
}

images = {
    k: Path(v)
    for k, v in images
}

addon_path = Path("addons/default")
addon = Addon(
    name="Default",
    tile_types=tile_types,
    assets_dir=addon_path,
    images=images
)
