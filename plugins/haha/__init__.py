from supermupla.plugin import Plugin, TileType
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

plugin_path = Path("plugins/haha")
images = {
    k: Path(v)
    for k, v in images.items()
}

plugin = Plugin(
    name="Default",
    assets_dir=plugin_path,
    images=images,
    tile_types=tile_types
)
