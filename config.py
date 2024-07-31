from pathlib import Path
from supermupla import Config


c = Config(
    # window config
    fps=0,  # limited by vsync, or unlimited
    vsync=True,
    fullscreen=False,
    window_size=(1280, 720),
    # other
    font=Path("assets/fffforwa.ttf"),
    addons=[
        "addons.supermuki_tts",
        "addons.haha",
        "addons.default"
    ],

)
