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

        self.origin = vector()  # origin of the coordinate system
        self.pan_active = False  # if the user is panning


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
        # the first element of the tuple is the left mouse button, the second is the middle mouse button and the third is the right mouse button
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[1]:  # check if the middle mouse button is pressed
            self.pan_active = True  # set pan_active to True
            self.pan_offset = vector(pygame.mouse.get_pos()) - self.origin  # calculate the offset between the mouse position and the origin
        if not pygame.mouse.get_pressed()[1]:  # check if the middle mouse button is released
            self.pan_active = False  # set pan_active to False
        if event.type == pygame.MOUSEWHEEL:  # check if the mouse wheel is moved
            # print(event)
            # print(event.y, event.x)
            self.origin.y -= event.y * 50  # move the origin in the y axis
            self.origin.x += event.x * 50  # move the origin in the x axis


            
            # if pygame.key.get_pressed()[pygame.K_LCTRL]:  # check if the left control key is pressed
            #     self.origin.y -= event.y * 50  # move the origin in the y axis
            # else:  # if the left control key is not pressed
            #     self.origin.x -= event.y * 50  # move the origin in the x axis
        if self.pan_active:  # check if the user is panning
            self.origin = pygame.mouse.get_pos() - self.pan_offset


    def run(self, dt: float) -> None:
        """
        Initialize the Editor (GUI)

        ### Parameters:
            dt (float): time in seconds since the last tick
        """
        pygame.display.set_caption(f"{Config.NAME.value} {Config.VERSION.value} (Editor Mode)")  # set the window title 
        self.event_loop()  # handle events
        self.display_surface.fill('white')
        # print(self.origin)
        pygame.draw.circle(self.display_surface, (0, 255, 0), self.origin, 10)

