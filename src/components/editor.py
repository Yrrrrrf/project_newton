import math
from pygame.math import Vector2 as vector


import sys
import pygame
from dataclasses import dataclass
from components.util.unit_circle import UnitCircle

from config.globals import Config, Assets
from components.ui.origin_menu import OriginMenu
from components.util.trigonometry import draw_rectangular_components
from components.util.linear_algebra import  draw_arrow
from components.ui.text_input import TextInput


@dataclass
class Editor:
    """
    Editor class
    This class contains the logic for the GUI
    """
    pan_active: bool = False  # if the user is panning


    # App data (App State)
    display_surface: pygame.Surface = pygame.display.get_surface()
    # support_line_surface: pygame.Surface  # !this not
    # origin_menu: OriginMenu


    def __init__(self):
        """
        Initialize the app
        """
        self.display_surface: pygame.Surface = pygame.display.get_surface()

        # "Camera"
        self.pan_active: bool = False  # if the user is panning
        self.origin: vector = vector(self.display_surface.get_width() // 2, self.display_surface.get_height() // 2)
        corner_margin: int = 48
        # self.origin: vector = vector(corner_margin, self.display_surface.get_height() - corner_margin)


        # "Editor Grid"
        self.grid_size = 88  # size of the grid
        self.grid_size = 255  # size of the grid
        self.support_line_surface = pygame.Surface(self.display_surface.get_size())  # create a surface for the grid
        # self.support_line_surface = pygame.Surface(self.display_surface.get_size(), c  # create a surface for the grid
        self.support_line_surface.set_colorkey("green")  # set the colorkey of the surface (the colorkey is the color that is considered transparent)
        self.support_line_surface.set_alpha(32)  # set the transparency of the surface (0 is transparent and 255 is opaque)

        # menu
        self.origin_menu = OriginMenu()


    # ? Input --------------------------------------------------------------------------------------

    def event_loop(self):
        for event in pygame.event.get():  # get all events
            if event.type == pygame.QUIT:  # if the user closes the window
                pygame.quit()  # quit pygame
                sys.exit()  # exit the program
            self.pan_input(event)
            self.print_pixel_data(event)
            self.menu_click(event)
            self.user_input(event)  # handle user input

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
            self.origin.y += event.y * MOVE_SPEED  # move the origin in the y axis
            self.origin.x -= event.x * MOVE_SPEED  # move the origin in the x axis
        if self.pan_active:  # check if the user is panning
            self.origin = pygame.mouse.get_pos() - self.pan_offset


    def draw_grid(self):
        """
        Draw the grid on the screen

        The grid moves with the origin of the coordinate system, so it is always centered on the screen
        """
        # update the size of the surface
        columns: int = self.display_surface.get_width() // self.grid_size  # calculate the number of columns
        rows: int = self.display_surface.get_height() // self.grid_size  # calculate the number of rows
        self.support_line_surface.fill("green")  # fill the surface with transparent black

        # draw grid lines (vertical and horizontal)
        origin_offset: vector = vector(self.origin.x % self.grid_size, self.origin.y % self.grid_size)  # calculate the offset between the origin and the top left corner of the screen
        [pygame.draw.line(self.support_line_surface, (0, 0, 0), (self.grid_size * column + origin_offset.x, 0), (self.grid_size * column + origin_offset.x, self.display_surface.get_height())) for column in range(columns + 1)]
        [pygame.draw.line(self.support_line_surface, (0, 0, 0), (0, self.grid_size * row + origin_offset.y), (self.display_surface.get_width(), self.grid_size * row + origin_offset.y)) for row in range(rows + 1)]
        self.display_surface.blit(self.support_line_surface, (0, 0))  # draw the grid on the screen


    def draw_axes_lines(self, colored: bool = False):
        """
        Draw the axes of the coordinate system
        """
        if colored:
            pygame.draw.line(self.support_line_surface, (0, 0, 255), (self.origin.x, 0), (self.origin.x, self.display_surface.get_height()), 2)
            pygame.draw.line(self.support_line_surface, (255, 0, 0), (0, self.origin.y), (self.display_surface.get_width(), self.origin.y), 2)
        else:
            pygame.draw.line(self.support_line_surface, (0, 0, 0), (self.origin.x, 0), (self.origin.x, self.display_surface.get_height()), 2)
            pygame.draw.line(self.support_line_surface, (0, 0, 0), (0, self.origin.y), (self.display_surface.get_width(), self.origin.y), 2)
        self.display_surface.blit(self.support_line_surface, (0, 0))  # draw the grid on the screen


    def draw_ucs(self):
        """
        Draw the user coordinate system
        """
        arrow_length: int = self.grid_size  # length of the arrow
        draw_arrow(self.display_surface, (0, 0, 255), (int(self.origin.x), int(self.origin.y)), (int(self.origin.x), int(self.origin.y - arrow_length)))
        draw_arrow(self.display_surface, (255, 0, 0), (int(self.origin.x), int(self.origin.y)), (int(self.origin.x + arrow_length), int(self.origin.y)))


    def draw_numbers_on_grid(self):
        """
        Draw the numbers on the grid
        """
        # put a Natural number every grid_size pixels
        columns: int = self.display_surface.get_width() // self.grid_size  # calculate the number of columns
        rows: int = self.display_surface.get_height() // self.grid_size  # calculate the number of rows
        origin_offset: vector = vector(self.origin.x % self.grid_size, self.origin.y % self.grid_size)  # calculate the offset between the origin and the top left corner of the screen

        x_align = self.origin.x - 20
        y_align = self.origin.y + 4

        # draw the number 0 on the origin

        # draw Y axis coordinates
        for row in range(rows + 1, -1, -1):
            self.support_line_surface.blit(
                pygame.font.SysFont("Consolas", 16).render(
                    str(int((self.grid_size * row + origin_offset.y - self.origin.y) // self.grid_size * -1)),
                    True, (0, 0, 255)),  # render the number (true means that the text is anti-aliased)
                (x_align, self.grid_size * row + origin_offset.y + 4)
            )

        # draw X axis coordinates (red)
        for column in range(columns + 1):
            self.support_line_surface.blit(
                pygame.font.SysFont("Consolas", 16).render(
                    str(int((self.grid_size * column + origin_offset.x - self.origin.x) // self.grid_size)),
                    True, (255, 0, 0)),  # render the number (true means that the text is anti-aliased)
                (self.grid_size * column + origin_offset.x - 20, y_align)
            )

        self.support_line_surface.blit(pygame.font.SysFont("Consolas", 16).render("0",True, (0, 0, 0)), (x_align, y_align))
        self.display_surface.blit(self.support_line_surface, (0, 0))  # draw the grid on the screen


    def menu_click(self, event):
        """
        Handle menu clicks inside the `OriginMenu`
        """
        if event.type == pygame.MOUSEBUTTONDOWN and self.origin_menu.rect.collidepoint(pygame.mouse.get_pos()):
            self.origin_menu.click(pygame.mouse.get_pos(), event.button)  # check if the user clicked on a button


    def print_pixel_data(self, event):
        """
        Get the pixel data of the pixel that the user clicked on only when the user clicks the left mouse button
        """
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:  # check if the left mouse button is pressed
            colors = self.display_surface.get_at(pygame.mouse.get_pos())
            # print the color of the pixel that the user clicked on
            print(f"{pygame.mouse.get_pos()[0] - self.origin.x:4.0f}x, {pygame.mouse.get_pos()[1] - self.origin.y:4.0f}y = RGBA: (\033[91m{colors[0]:3}\033[0m, \033[92m{colors[1]:3}\033[0m, \033[94m{colors[2]:3}\033[0m, \033[97m{colors[3]:3}\033[0m)")


    def run(self, dt: float) -> None:
        """
        Initialize the Editor (GUI)

        ### Parameters:
            dt (float): time in seconds since the last tick
        """
        pygame.display.set_caption(f"{Config.NAME.value} {Config.VERSION.value} (Editor Mode)")  # set the window title 
        self.event_loop()  # handle events

        # self.display_surface.fill('white')  # fill the screen with white
        self.display_surface.fill((220, 220, 220))  # fill the screen with white
        self.draw_grid()  # draw grid
        self.draw_axes_lines(colored=False)  # draw axes
        # self.draw_axes_lines(colored=True)  # draw axes
        self.draw_numbers_on_grid()  # draw numbers on grid
        # self.draw_ucs()  # draw user coordinate system

        test_vector = vector(pygame.mouse.get_pos()) - self.origin
        test_vector.scale_to_length(self.grid_size)

        unit_circle: UnitCircle = UnitCircle(self.display_surface, self.origin, radius=self.grid_size, rect_components=(int(test_vector.x), int(test_vector.y)))  # type: ignore
        unit_circle.draw()  # draw the unit circle

        self.draw_fps(dt)  # draw fps on screen
        self.origin_menu.display()  # display origin menu


    def draw_fps(self, dt: float) -> None:
        """
        Draw the fps on the screen
        """
        fps = 1 / dt  # calculate the fps
        self.display_surface.blit(
            pygame.font.SysFont("Consolas", 16).render(
                f"{fps:3.0f} FPS", True, (63, 63, 63)),  # render the number (true means that the text is anti-aliased)
            (0, 0)  # position of the text
        )


    def user_input(self, event: pygame.event.Event):
        """
        Handle user input
        """
        if event.type == pygame.KEYDOWN:  # check if a key is pressed
            text_input = TextInput()
            text_input.user_input += event.unicode
            print(text_input.user_input)
            text_input.render_text(event)

            if event.key == pygame.K_ESCAPE:  # check if the key is the escape key
                pygame.quit()  # quit pygame
                sys.exit()  # exit the program

