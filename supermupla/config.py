from dataclasses import dataclass


@dataclass
class Config:
    '''
    configuration:
    - fps: target frames per second (0 for no limit)
    - vsync: should fps be limited by refresh rate
    - fullscreen: start in fullscreen mode
    - window_size: size if not fullscreen (screen resolution otherwise)
    '''

    fps: int
    vsync: bool
    fullscreen: bool
    window_size: tuple[int, int]
    addons: list[str]
