
import supermupla.config as c
import pygame as pg

players = [
    ["Kristóf", (0, 0, 255)],
    ["Anna", (255, 0, 0)],
    ["Encsi", (0, 255, 0)],
]


players = [
    Player(
        name="Kristóf",
        keys=wasd,
        color=(0, 0, 255),
    ),

    Player(
        name="Encsi",
        keys=arrows,
        color=(0, 255, 0)
    ),

    Player(
        name="Anna",
        keys=ijkl,
        color=(255, 0, 0)
    ),
]

