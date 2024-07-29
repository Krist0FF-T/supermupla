from supermupla import Config

c = Config(
    fps=0,  # limited by vsync, or unlimited
    vsync=True,
    fullscreen=False,
    window_size=(1280, 720),
    addons=[
        "default"
    ]
)
