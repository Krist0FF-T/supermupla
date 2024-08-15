#!/usr/bin/env python

from pathlib import Path
from supermupla import Config, App

config = Config(
    # window config
    fps=0,  # limited by vsync, or unlimited
    vsync=True,
    fullscreen=False,
    window_size=(1280, 720),
    # other
    font=Path("assets/fffforwa.ttf"),
    addons=[
        "plugins.supermuki_tts",
        "plugins.haha",
        "plugins.default"
    ],
)

if __name__ == "__main__":
    app = App(config)
    app.run()
