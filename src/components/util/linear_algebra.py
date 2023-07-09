# This file contains some of the most common linear algebra operations
from dataclasses import dataclass
import pygame
import numpy as np
import math


@dataclass
class Vector:
    value: np.ndarray


    def __init__(self, value: np.ndarray):
        self.value = value


    def draw_arrow(self, surface: pygame.Surface, color: tuple[int, int, int], arrow_size: int = 16):
        """
        Draw an arrow on the screen from the start point to the end point
        """
        start = self.value[0], self.value[1]

        end = (start[0] + self.value[0], start[1] + self.value[1])
        pygame.draw.line(surface, color, start, end, 2)


# ? useful functions ------------------------------------------------------------------------------------

def draw_arrow(surface: pygame.Surface, color: tuple[int, int, int], start: tuple[int, int], end: tuple[int, int], arrow_size: int = 16):
    """
    Draw an arrow on the screen from the start point to the end point
    """
    pygame.draw.line(surface, color, start, end, 2)  # draw the line

    angle = math.atan2(end[1] - start[1], end[0] - start[0])
    arrow_angle: float = math.pi / 12  # angle of the arrow head (15 degrees)
    left_side = (end[0] - arrow_size * math.cos(angle + arrow_angle), end[1] - arrow_size * math.sin(angle + arrow_angle))
    right_side = (end[0] - arrow_size * math.cos(angle - arrow_angle), end[1] - arrow_size * math.sin(angle - arrow_angle))
    # now draw the arrow head on top of the line
    pygame.draw.polygon(surface, color, [end, left_side, right_side])
