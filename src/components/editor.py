from pygame.math import Vector2 as vector


import sys
import pygame
from dataclasses import dataclass

from config.globals import Config


@dataclass
class Editor:
    """
    Editor class
    This class contains the logic for the GUI
    """
    # App data (App State)
    display_surface: pygame.Surface = pygame.display.get_surface()


    def __init__(self):
        """
        Initialize the app
        """
        self.display_surface: pygame.Surface = pygame.display.get_surface()

        # "Camera"
        self.origin = vector()  # origin of the coordinate system
        self.pan_active = False  # if the user is panning

        # "Editor Grid"
        self.grid_size = 64  # size of the grid
        self.grid_color = (191, 191, 191)  # color of the grid


    # ? Input --------------------------------------------------------------------------------------

    def event_loop(self):
        for event in pygame.event.get():  # get all events
            if event.type == pygame.QUIT:  # if the user closes the window
                pygame.quit()  # quit pygame
                sys.exit()  # exit the program
            self.pan_input(event)


    def pan_input(self, event):
        """
        Handle pan input
        Pan means to move the origin of the coordinate system
        """
        MOVE_SPEED = 32  # speed at which the origin moves

        # the first element of the tuple is the left mouse button, the second is the middle mouse button and the third is the right mouse button
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[1]:  # check if the middle mouse button is pressed
            self.pan_active = True  # set pan_active to True
            self.pan_offset = vector(pygame.mouse.get_pos()) - self.origin  # calculate the offset between the mouse position and the origin
        if not pygame.mouse.get_pressed()[1]:  # check if the middle mouse button is released
            self.pan_active = False  # set pan_active to False
        if event.type == pygame.MOUSEWHEEL:  # check if the mouse wheel is moved
            self.origin.y -= event.y * MOVE_SPEED  # move the origin in the y axis
            self.origin.x += event.x * MOVE_SPEED  # move the origin in the x axis
        if self.pan_active:  # check if the user is panning
            self.origin = pygame.mouse.get_pos() - self.pan_offset


    def draw_grid(self):
        """
        Draw the grid on the screen

        The grid moves with the origin of the coordinate system, so it is always centered on the screen
        """
        columns: int = self.display_surface.get_width() // self.grid_size  # calculate the number of columns
        rows: int = self.display_surface.get_height() // self.grid_size  # calculate the number of rows

        # draw grid lines (vertical and horizontal)
        origin_offset: vector = vector(self.origin.x % self.grid_size, self.origin.y % self.grid_size)  # calculate the offset between the origin and the top left corner of the screen
        [pygame.draw.line(self.display_surface, self.grid_color, (self.grid_size * column + origin_offset.x, 0), (self.grid_size * column + origin_offset.x, self.display_surface.get_height())) for column in range(columns + 1)]
        [pygame.draw.line(self.display_surface, self.grid_color, (0, self.grid_size * row + origin_offset.y), (self.display_surface.get_width(), self.grid_size * row + origin_offset.y)) for row in range(rows + 1)]

        # draw origin lines (black lines)
        pygame.draw.line(self.display_surface, (0, 0, 0), (self.origin.x, 0), (self.origin.x, self.display_surface.get_height()))
        pygame.draw.line(self.display_surface, (0, 0, 0), (0, self.origin.y), (self.display_surface.get_width(), self.origin.y))



    def run(self, dt: float) -> None:
        """
        Initialize the Editor (GUI)

        ### Parameters:
            dt (float): time in seconds since the last tick
        """
        pygame.display.set_caption(f"{Config.NAME.value} {Config.VERSION.value} (Editor Mode)")  # set the window title 
        self.event_loop()  # handle events
        self.display_surface.fill('white')  # fill the screen with white
        self.draw_grid()  # draw grid
        pygame.draw.circle(self.display_surface, (0, 0, 0), self.origin, 8, 1)  # draw origin point

