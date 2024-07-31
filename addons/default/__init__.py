from supermupla.addon import Addon, TileType
from pathlib import Path


def dirt_appearance(neighbors):
    # l = [
    #     neighbors.top,
    #     neighbors.bottom,
    #     neighbors.left,
    #     neighbors.right,
    # ]
    # if all([a.solid for a in l]):
    #     return "smiley"

    if neighbors.top.solid:
        return "dirt"

    return "dirt#grass-top"


tile_types = [
    TileType(
        name="air",
        solid=False,
        appearance=None
    ),
    TileType(
        name="dirt",
        solid=True,
        appearance=dirt_appearance
    ),
]

# relative to "$(assets_dir)/images"
images = {
    "dirt": "dirt.png",
    "dirt#grass-top": "grass.png",
}

addon_path = Path("addons/default")
images = {
    k: Path(v)
    for k, v in images.items()
}

addon = Addon(
    name="Default",
    tile_types=tile_types,
    assets_dir=addon_path,
    images=images
)
