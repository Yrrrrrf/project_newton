# this module contains the code to show (in pygame) the solution of the n-travelers problem

#? Imports ------------------------------------------------------------------------------------

# Python imports
import sys
from threading import Thread
import pygame
import random
import time
from dataclasses import dataclass  # dataclass decorator

# Own imports
from config.globals import *
from components.editor import Editor
from components.level import Level

#? Logic --------------------------------------------------------------------------------------


#  create app class
@dataclass
class App:
    """
    App class
    This class contains the logic for the GUI
    """
    # App data (App State)
    # display_surface: pygame.Surface = pygame.display.set_mode((Config.WIDTH.value, Config.HEIGHT.value), pygame.RESIZABLE)
    theme = Theme.DEBUG
    running: bool = True
    # clock: pygame.time.Clock = pygame.time.Clock()

    def __init__(self):
        """
        Initialize the app
        """
        pygame.init()  # initialize pygame
        display_surface: pygame.Surface = pygame.display.set_mode((Config.WIDTH.value, Config.HEIGHT.value), pygame.RESIZABLE)
        pygame.display.set_caption(f"{Config.NAME.value} {Config.VERSION.value}")  # set the window title
        pygame.display.set_icon(pygame.image.load((f"{Assets.IMAGES.value}physics.png")))  # set the window icon
        print(f"\033[94mApp Running\033[0m")
        self.clock: pygame.time.Clock = pygame.time.Clock()

        # SET ALWAYS ON TOP
        # if sys.platform == "win32":
        #     import win32gui, win32con
        #     hwnd = win32gui.GetForegroundWindow()
        #     win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
        #                             win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
            


    def run(self) -> None:
        """
        Pop up the window and run the app while the user doesn't close the window
        """
        # [pygame.draw.circle(self.display_surface, (0, 255, 0), point, 5) for point in [(random.randint(0, Config.WIDTH.value), random.randint(0, Config.HEIGHT.value)) for _ in range(5)]]

        self.editor = Editor()  # create editor instance/

        while self.running:  # while the app is running
        # while True
            dt: float = self.clock.tick() / 1000.0  # get the time in seconds since the last tick
            self.clock.tick(144)  # set the fps to 144
            self.editor.run(dt)  # run editor
            # show fps on screen
            
            pygame.display.update()  # update display_surface
        # ? End of test code -------------------------------------------------------------------------
