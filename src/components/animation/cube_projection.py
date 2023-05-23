# Hypercube animation

# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# from matplotlib import cm

from pygame.math import Vector2 as vector
from dataclasses import dataclass


@dataclass
class Cube:
    vertices: list[int]

    def __init__(self, vertices: list[int]):
        # self.vertices = vertices

        # set the vertices of the cube
        self.vertices = [
            vector(0, 0, 0),
            vector(0, 0, 1),
            vector(0, 1, 0),
            vector(0, 1, 1),
            vector(1, 0, 0),
            vector(1, 0, 1),
            vector(1, 1, 0),
            vector(1, 1, 1)
        ]

        # set the edges of the cube
        self.edges = [
            (0, 1),
            (0, 2),
            (0, 4),
            (1, 3),
            (1, 5),
            (2, 3),
            (2, 6),
            (3, 7),
            (4, 5),
            (4, 6),
            (5, 7),
            (6, 7)
        ]


        