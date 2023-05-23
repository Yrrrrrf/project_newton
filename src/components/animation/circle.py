# import math
# from pygame.math import Vector2 as vector


# import sys
# import pygame
# from dataclasses import dataclass

# from config.globals import Config, Assets
# from components.ui.origin_menu import OriginMenu



# @dataclass
# class Editor:
#     """
#     Editor class
#     This class contains the logic for the GUI
#     """
#     display_surface: pygame.Surface = pygame.display.get_surface()


#     def __init__(self):
#         """
#         Initialize the app
#         """
#         self.display_surface: pygame.Surface = pygame.display.get_surface()

#         # "Camera"
#         self.pan_active: bool = False  # if the user is panning
#         # self.origin: vector = vector(self.display_surface.get_width() // 2, self.display_surface.get_height() // 2)
#         corner_margin: int = 48
#         self.origin: vector = vector(corner_margin, self.display_surface.get_height() - corner_margin)


#         # "Editor Grid"
#         self.grid_size = 88  # size of the grid
#         self.support_line_surface = pygame.Surface(self.display_surface.get_size())  # create a surface for the grid
#         # self.support_line_surface = pygame.Surface(self.display_surface.get_size(), c  # create a surface for the grid
#         self.support_line_surface.set_colorkey("green")  # set the colorkey of the surface (the colorkey is the color that is considered transparent)
#         self.support_line_surface.set_alpha(32)  # set the transparency of the surface (0 is transparent and 255 is opaque)

#         # menu
#         self.origin_menu = OriginMenu()
