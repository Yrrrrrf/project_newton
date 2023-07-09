'''
This module contains some of the most used trigonometric functions in the app

These functions draw components on the screen surface
'''

from dataclasses import dataclass
import math
import pygame
from components.util.linear_algebra import  draw_arrow
from components.util.trigonometry import get_angle, get_distance


@dataclass
class UnitCircle:
    display_surface: pygame.Surface
    rect_components: tuple[int, int]  # describe the direction of the vector
    radius: int = 1
    origin: tuple[int, int] = (0, 0)
    color: tuple[int, int, int] = (0, 0, 0)
    thickness: int = 1

    def __init__(self, display_surface: pygame.Surface, origin: tuple[int, int] = (0, 0), rect_components: tuple[int, int] = (0, 0), radius: int = 1, color: tuple[int, int, int] = (0, 0, 0), thickness: int = 1):
        self.display_surface = display_surface
        self.rect_components = rect_components
        self.origin = origin
        self.radius = radius
        self.color = color
        self.thickness = thickness + 1


    def draw(self):
        pygame.draw.circle(self.display_surface, self.color, self.origin, self.radius, self.thickness)
        self.draw_phantom_line()
        self.draw_tetha() 

        self.draw_sin(color="green")
        self.draw_cos(color="red")
        # self.draw_tan(color="cyan")
        # self.draw_sec(color="magenta")
        # self.draw_csc(color="blue")
        # self.draw_cot(color="yellow")


    def draw_phantom_line(self):
        """
        Draw a phantom line in the same direction as the vector, but starting at the origin
        """
        angle: float = get_angle(self.origin, (self.origin[0] + self.rect_components[0], self.origin[1] + self.rect_components[1]))
        distance: float = 10 * get_distance(self.origin, (self.origin[0] + self.rect_components[0], self.origin[1] + self.rect_components[1]))
        pygame.draw.line(self.display_surface, (127, 127, 127), self.origin, (self.origin[0] + distance * math.cos(angle), self.origin[1] + distance * math.sin(angle)), 1)


    def draw_tetha(self, arc_size: int = 32, text_true: bool = False):
        """
        Draw the tetha component of a given Vector on the screen surface
        """
        pygame.draw.arc(self.display_surface, (127, 127, 127), (self.origin[0] - arc_size, self.origin[1] - arc_size, arc_size * 2, arc_size * 2), 0, 2*math.pi - get_angle(self.origin, (self.origin[0] + self.rect_components[0], self.origin[1] + self.rect_components[1])), 2)
        pos = (24, -24)  # position of the text relative to the origin
        beta_text: pygame.Surface = pygame.font.SysFont("Cambria Math", 16).render(f"{math.degrees(2*math.pi - get_angle(self.origin, (self.origin[0] + self.rect_components[0], self.origin[1] + self.rect_components[1]))):.2f}°", True, (64, 64, 64))  # create the text surface
        self.display_surface.blit(beta_text, (self.origin[0]+ pos[0], self.origin[1] + pos[1]- 16), beta_text.get_rect())  # draw the text surface on the screen

        if text_true:
            theta_text: pygame.Surface = pygame.font.SysFont("Consolas", 16).render(f"θ = {math.degrees(2*math.pi - get_angle(self.origin, (self.origin[0] + self.rect_components[0], self.origin[1] + self.rect_components[1]))):.2f}°", True, (0, 0, 0))  # create the text surface
            self.display_surface.blit(theta_text, (48, 40), theta_text.get_rect())  # draw the text surface on the screen


    def draw_sin(self, color = (0, 0, 0)):
        """
        Draw the sin component of a given Vector on the screen surface
        """
        pygame.draw.line(self.display_surface, color, (self.origin[0] + self.rect_components[0], self.origin[1]), (self.origin[0] + self.rect_components[0], self.origin[1] + self.rect_components[1]), 2)


    def draw_cos(self, color = (0, 0, 0)):
        """
        Draw the cos component of a given Vector on the screen surface
        """
        pygame.draw.line(self.display_surface, color, (self.origin[0], self.origin[1] + self.rect_components[1]), (self.origin[0] + self.rect_components[0], self.origin[1] + self.rect_components[1]), 2)


    def draw_tan(self, color = (0, 0, 0)):
        """
        Draw the tan component of a given Vector on the screen surface
        """
        if self.rect_components[1] != 0 and self.rect_components[0] != 0:  # if cos is not 0
            tan = self.rect_components[0] / self.rect_components[1]
            distance: float = get_distance(self.origin, (self.origin[0] + self.rect_components[0], self.origin[1] + self.rect_components[1]))
            sec: float = distance / self.rect_components[0]
            pygame.draw.line(self.display_surface, color, (self.origin[0] + self.rect_components[0], self.origin[1] + self.rect_components[1]), (self.origin[0] + distance * sec, self.origin[1]), 2)  # draw the y component

            if self.rect_components[0] > 0:  # draw this line only if the vector is on the right side` of the origin
                pygame.draw.line(self.display_surface, color, (self.origin[0] + distance, self.origin[1]), (self.origin[0] + distance, self.origin[1] + distance * (1 / tan)), 2)  # draw the y component
            else:  # otherwise draw it on the left side
                pygame.draw.line(self.display_surface, color, (self.origin[0] - distance, self.origin[1]), (self.origin[0] - distance, self.origin[1] - distance * (1 / tan)), 2)  # draw the y component

            tan_text: pygame.Surface = pygame.font.SysFont("Consolas", 16).render(f"tan = {tan:8.4f}", True, color)  # create the text surface
            self.display_surface.blit(tan_text, (48, 112), tan_text.get_rect())  # draw the text surface on the screen


    def draw_sec(self, color = (0, 0, 0)):
        """
        Draw the sec component of a given Vector on the screen surface
        """
        if self.rect_components[1] != 0 and self.rect_components[0] != 0:  # if cos is not 0
            distance: float = get_distance(self.origin, (self.origin[0] + self.rect_components[0], self.origin[1] + self.rect_components[1]))
            sec: float = distance / self.rect_components[0]
            tan: float = self.rect_components[0] / self.rect_components[1]

            if self.rect_components[0] > 0:  # draw this line only if the vector is on the right side of the origin
                pygame.draw.line(self.display_surface, color, self.origin, (self.origin[0] + distance, self.origin[1] + distance * (1/ tan)), 2)  # draw the y component
            else:  # otherwise draw it on the left side
                pygame.draw.line(self.display_surface, color, self.origin, (self.origin[0] - distance, self.origin[1] - distance * (1/ tan)), 2)  # draw the y component

            pygame.draw.line(self.display_surface, color, self.origin, (self.origin[0] + distance * sec, self.origin[1]), 2)  # draw the y component

            sec_text: pygame.Surface = pygame.font.SysFont("Consolrect_components[1SELF.]as", 16).render(f"sec = {sec:8.4f}", True, color)  # create the text surface
            self.display_surface.blit(sec_text, (48, 128), sec_text.get_rect())  # draw the text surface on the screen

 
    def draw_cot(self, color = (0, 0, 0)):
        """
        Draw the cot component of a given Vector on the screen surface
        """
        if self.rect_components[0]!= 0 and self.rect_components[1] != 0:
            distance: float = get_distance(self.origin, (self.origin[0] + self.rect_components[0], self.origin[1] + self.rect_components[1]))
            cot: float = self.rect_components[0] / - self.rect_components[1]  # -1 / tan
            csc: float = distance / - self.rect_components[1]  # 1 / sin

            pygame.draw.line(self.display_surface, color, (self.origin[0] + self.rect_components[0], self.origin[1] + self.rect_components[1]), (self.origin[0], self.origin[1] - distance * csc), 2)  # draw the x component

            cot_text: pygame.Surface = pygame.font.SysFont("Consolas", 16).render(f"cot = {cot:8.4f}", True, color)  # create the text surface
            self.display_surface.blit(cot_text, (48, 144), cot_text.get_rect())  # draw the text surface on the screen


    def draw_csc(self, color = (0, 0, 0)):
        """
        Draw the csc component of a given Vector on the screen surface
        """
        if self.rect_components[1] != 0:
            distance: float = get_distance(self.origin, (self.origin[0] + self.rect_components[0], self.origin[1] + self.rect_components[1]))
            csc: float = distance / - self.rect_components[1]  # 1 / sin

            pygame.draw.line(self.display_surface, color, self.origin, (self.origin[0], self.origin[1] - distance * csc), 2)

            csc_text: pygame.Surface = pygame.font.SysFont("Consolas", 16).render(f"csc = {csc:8.4f}", True, color)  # create the text surface
            self.display_surface.blit(csc_text, (48, 160), csc_text.get_rect())  # draw the text surface on the screen
