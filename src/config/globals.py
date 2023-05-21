# Global Settings for the application

# ? Imports -------------------------------------------------------------------------------------

from enum import Enum
from dataclasses import dataclass

import pygame


# ? Globals -------------------------------------------------------------------------------------


class Config(Enum):
    """
    Project Config
    """
    # App info
    NAME = "Project ..."
    VERSION = "v0.1.0"
    
    # App settings
    WIDTH = 1080
    HEIGHT = 720
    # FPS = 60  # frames per second
    TILE_SIZE = 32  # tile size in pixels
    ANIMATION_SPEED = 8  # seconds


class Assets(Enum):
    """
    Assets paths
    """
    # Images
    IMAGES = "assets/images/"
    # Fonts
    TITLE_FONT = "assets/fonts/"
    # Sounds
    # Music
    # Videos
    # Animations
    # Other
    # ...


@dataclass
class Theme(Enum):
    LIGHT = ("Light Theme", (255, 255, 255), (191, 191, 191), (255, 0, 0), "assets/fonts/Roboto-Regular.ttf")
    DARK = ("Dark Theme", (0, 0, 0), (63, 63, 63), (255, 0, 0), "assets/fonts/Roboto-Regular.ttf")
    DARK_PLUS = ("Dark+ Theme", (0, 0, 0), (31, 31, 31), (255, 0, 0), "assets/fonts/Roboto-Regular.ttf")
    DEBUG = ("Debug Theme", (255, 0, 0), (0, 0, 0), (255, 0, 0), "Consolas")


    # title: str
    main_color: tuple
    secondary_color: tuple
    highlight_color: tuple
    font: str
    

    def __init__(self, title, main_color, secondary_color, highlight_color, font):
        # use the name of the enum as the title but in title case
        self.title = self.name.title()

        self.main_color = main_color
        self.secondary_color = secondary_color
        self.highlight_color = highlight_color
        self.font = font