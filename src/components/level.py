import pygame
from dataclasses import dataclass

from config.globals import Config


@dataclass
class Level:
    """
    Level class contains all the data and logic for the level
    """
    # App data (App State)
    display_surface: pygame.Surface

    def __init__(self, display_surface: pygame.Surface):
        """
        Initialize the level
        """
        self.display_surface = display_surface


    def run(self, dt: float) -> None:
        self.display_surface.fill('white')
