from supermupla.addon import Addon, TileType
from pathlib import Path

tile_types = [
    TileType(
        name="smiley",
        solid=False,
        appearance="smiley"
    )
]

images = {
    # "grass": "smiling_grass.png",
    "smiley": "smiley.png"
}

addon_path = Path("addons/haha")
images = {
    k: Path(v)
    for k, v in images.items()
}

addon = Addon(
    name="Default",
    assets_dir=addon_path,
    images=images,
    tile_types=tile_types
)
