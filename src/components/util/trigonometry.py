'''
This module contains some of the most used trigonometric functions in the app

These functions draw components on the screen surface
'''

import math
import sys
import pygame
from dataclasses import dataclass

from config.globals import Config, Assets
from components.ui.origin_menu import OriginMenu


def draw_rectangular_components(display_surface: pygame.Surface, origin: tuple[int, int], vector: tuple[int, int]) -> None:
    """
    Draw the rectangular components of a given Vector on the screen surface
    """
    # draw an arc that represents the angle of the vector
    arc_size: int = 16
    pygame.draw.arc(display_surface, (0, 0, 0), (origin[0] - arc_size, origin[1] - arc_size, arc_size * 2, arc_size * 2), 0, 2*math.pi - get_angle(origin, (origin[0] + vector[0], origin[1] + vector[1])), 1)

    draw_phantom_line(display_surface, origin, vector)  # draw the phantom line
    draw_arrow(display_surface, (0, 0, 0), origin, (origin[0] + vector[0], origin[1] + vector[1]))  # draw the vector

    draw_alpha(display_surface, origin, vector)  # draw the polar components

    # draw_sin(display_surface, origin, vector)  # draw the sin component
    # draw_cos(display_surface, origin, vector)  # draw the cos component
    # draw_sin_cos_identity(display_surface, origin, vector)  # draw the pythagorean identity

    # draw_tan(display_surface, origin, vector)  # draw the tan component
    # draw_sec(display_surface, origin, vector)  # draw the tan component
    # draw_tan_sec_identity(display_surface, origin, vector)  # draw the pythagorean identity

    draw_cot(display_surface, origin, vector)  # draw the tan component
    draw_csc(display_surface, origin, vector)  # draw the tan component
    draw_cot_csc_identity(display_surface, origin, vector)  # draw the pythagorean identity


def draw_phantom_line(display_surface: pygame.Surface, origin: tuple[int, int], vector: tuple[int, int]) -> None:
    """
    Draw a phantom line in the same direction as the vector, but starting at the origin
    """
    # get the angle of the vector
    angle: float = get_angle(origin, (origin[0] + vector[0], origin[1] + vector[1]))
    # get the distance from the origin to the end of the vector
    distance: float = get_distance(origin, (origin[0] + vector[0], origin[1] + vector[1]))
    # get the point at the end of the vector
    end: tuple[int, int] = get_point(origin, angle, distance*10)
    # draw the phantom line
    pygame.draw.line(display_surface, (127, 127, 127), origin, end, 1)


def draw_alpha(display_surface: pygame.Surface, origin: tuple[int, int], vector: tuple[int, int]) -> None:
    alpha_text: pygame.Surface = pygame.font.SysFont("Consolas", 16).render(f"alpha = {math.degrees(2*math.pi - get_angle(origin, (origin[0] + vector[0], origin[1] + vector[1]))):.2f}°", True, (0, 0, 0))  # create the text surface
    display_surface.blit(alpha_text, (48, 40), alpha_text.get_rect())  # draw the text surface on the screen


def draw_sin(display_surface: pygame.Surface, origin: tuple[int, int], vector: tuple[int, int]) -> None:
    """
    Draw the sin component of a given Vector on the screen surface
    """
    if vector[0] == 0:
        pygame.draw.line(display_surface, (0, 0, 255), (origin[0] + vector[0], origin[1]), (origin[0] + vector[0], origin[1] + vector[1]), 1)
    else:
        # draw the sin component
        pygame.draw.line(display_surface, (0, 0, 255), (origin[0] + vector[0], origin[1]), (origin[0] + vector[0], origin[1] + vector[1]), 1)  # draw the y component
        # draw the sin value (same as draw_alpha)
        sin_value: float = -get_sin_component(origin, (origin[0] + vector[0], origin[1] + vector[1]))[0] / get_distance(origin, (origin[0] + vector[0], origin[1] + vector[1]))
        sin_text: pygame.Surface = pygame.font.SysFont("Consolas", 16).render(f"sin = {sin_value:8.4f}", True, (0, 0, 0))  # create the text surface
        display_surface.blit(sin_text, (48, 64), sin_text.get_rect())  # draw the text surface on the screen


def draw_cos(display_surface: pygame.Surface, origin: tuple[int, int], vector: tuple[int, int]) -> None:
    """
    Draw the cos component of a given Vector on the screen surface
    """
    if vector[1] == 0:
        pygame.draw.line(display_surface, (255, 0, 0), (origin[0], origin[1] + vector[1]), (origin[0] + vector[0], origin[1] + vector[1]), 1)
    else:
        # draw the cos component
        pygame.draw.line(display_surface, (255, 0, 0), (origin[0], origin[1] + vector[1]), (origin[0] + vector[0], origin[1] + vector[1]), 1)  # draw the y component
        # draw the cos value
        cos_value: float = get_sin_component(origin, (origin[0] + vector[0], origin[1] + vector[1]))[1] / get_distance(origin, (origin[0] + vector[0], origin[1] + vector[1]))
        cos_text: pygame.Surface = pygame.font.SysFont("Consolas", 16).render(f"cos = {cos_value:8.4f}", True, (0, 0, 0))  # create the text surface
        display_surface.blit(cos_text, (48, 80), cos_text.get_rect())  # draw the text surface on the screen


def draw_sin_cos_identity(display_surface: pygame.Surface, origin: tuple[int, int], vector: tuple[int, int]) -> None:
    sin: float = -get_sin_component(origin, (origin[0] + vector[0], origin[1] + vector[1]))[0] / get_distance(origin, (origin[0] + vector[0], origin[1] + vector[1]))
    cos: float = get_sin_component(origin, (origin[0] + vector[0], origin[1] + vector[1]))[1] / get_distance(origin, (origin[0] + vector[0], origin[1] + vector[1]))
    # text: pygame.Surface = pygame.font.SysFont("Consolas", 16).render(f"{sin:.4f}² + {cos:.4f}² = {sin**2 + cos**2:.4f}", True, (0, 0, 0))  # create the text surface
    text: pygame.Surface = pygame.font.SysFont("Consolas", 16).render(f"{sin**2:.4f} + {cos**2:.4f} = {sin**2 + cos**2:.4f}", True, (0, 0, 0))  # create the text surface
    display_surface.blit(text, (48, 96), text.get_rect())  # draw the text surface on the screen


def draw_tan(display_surface: pygame.Surface, origin: tuple[int, int], vector: tuple[int, int]) -> None:
    """
    Draw the tan component of a given Vector on the screen surface
    """
    rect_components: tuple[int, int] = get_sin_component(origin, (origin[0] + vector[0], origin[1] + vector[1]))
    if rect_components[1] != 0:  # if cos is not 0
        tan = -rect_components[0] / rect_components[1]

        distance: float = get_distance(origin, (origin[0] + vector[0], origin[1] + vector[1]))

        # if vector[0] > 0:  # draw this line only if the vector is on the right side of the origin
        #     pygame.draw.line(display_surface, (255, 0, 255), (origin[0] + distance, origin[1]), (origin[0] + distance, origin[1] - distance*tan), 1)  # draw the y component
        # else:  # otherwise draw it on the left side
        #     pygame.draw.line(display_surface, (255, 0, 255), (origin[0] - distance, origin[1]), (origin[0] - distance, origin[1] + distance*tan), 1)  # draw the y component

        pygame.draw.line(display_surface, (255, 0, 255), (origin[0] + vector[0], origin[1] + vector[1]), (origin[0] + distance * distance / get_sin_component(origin, (origin[0] + vector[0], origin[1] + vector[1]))[1], origin[1]), 1)  # draw the y component

        tan_text: pygame.Surface = pygame.font.SysFont("Consolas", 16).render(f"tan = {tan:8.4f}", True, (0, 0, 0))  # create the text surface
        display_surface.blit(tan_text, (48, 112), tan_text.get_rect())  # draw the text surface on the screen


def draw_sec(display_surface: pygame.Surface, origin: tuple[int, int], vector: tuple[int, int]) -> None:
    """
    Draw the sec component of a given Vector on the screen surface
    """
    rect_components: tuple[int, int] = get_sin_component(origin, (origin[0] + vector[0], origin[1] + vector[1]))
    if rect_components[1] != 0:  # if cos is not 0
        distance: float = get_distance(origin, (origin[0] + vector[0], origin[1] + vector[1]))
        sec: float = distance / rect_components[1]
        tan: float = -rect_components[0] / rect_components[1]

        if vector[0] > 0:  # draw this line only if the vector is on the right side of the origin
            pygame.draw.line(display_surface, (255, 255, 0), origin, (origin[0] + distance, origin[1] - distance*tan), 1)  # draw the y component
        else:  # otherwise draw it on the left side
            pygame.draw.line(display_surface, (255, 255, 0), origin, (origin[0] - distance, origin[1] + distance*tan), 1)  # draw the y component

        pygame.draw.line(display_surface, (255, 255, 0), origin, (origin[0] + distance * sec, origin[1]), 1)  # draw the y component

        sec_text: pygame.Surface = pygame.font.SysFont("Consolas", 16).render(f"sec = {sec:8.4f}", True, (0, 0, 0))  # create the text surface
        display_surface.blit(sec_text, (48, 128), sec_text.get_rect())  # draw the text surface on the screen


def draw_tan_sec_identity(display_surface: pygame.Surface, origin: tuple[int, int], vector: tuple[int, int]) -> None:
    rect_components: tuple[int, int] = get_sin_component(origin, (origin[0] + vector[0], origin[1] + vector[1]))
    if rect_components[1] != 0:  # if cos is not 0    
        tan: float = -get_sin_component(origin, (origin[0] + vector[0], origin[1] + vector[1]))[0] / get_sin_component(origin, (origin[0] + vector[0], origin[1] + vector[1]))[1]
        sec: float = get_distance(origin, (origin[0] + vector[0], origin[1] + vector[1])) / get_sin_component(origin, (origin[0] + vector[0], origin[1] + vector[1]))[1]
        # text: pygame.Surface = pygame.font.SysFont("Consolas", 16).render(f"{tan:.4f}² + {sec:.4f}² = {tan**2 + sec**2:.4f}", True, (0, 0, 0))  # create the text surface
        text: pygame.Surface = pygame.font.SysFont("Consolas", 16).render(f"{tan**2:.4f} + {1} = {sec**2:.4f}", True, (0, 0, 0))  # create the text surface
        display_surface.blit(text, (48, 144), text.get_rect())  # draw the text surface on the screen


def draw_cot(display_surface: pygame.Surface, origin: tuple[int, int], vector: tuple[int, int]) -> None:
    """
    Draw the cot component of a given Vector on the screen surface
    """
    rect_components: tuple[int, int] = get_sin_component(origin, (origin[0] + vector[0], origin[1] + vector[1]))
    if rect_components[0] != 0:  # if the vector is not horizontal
        distance: float = get_distance(origin, (origin[0] + vector[0], origin[1] + vector[1]))
        csc: float = distance / rect_components[0]
        pygame.draw.line(display_surface, (255, 255, 0), (origin[0] + vector[0], origin[1] + vector[1]), (origin[0], origin[1] + distance * csc), 1)  # draw the x component

        cot_text: pygame.Surface = pygame.font.SysFont("Consolas", 16).render(f"cot = {-rect_components[1] / rect_components[0]:8.4f}", True, (0, 0, 0))  # create the text surface
        display_surface.blit(cot_text, (48, 160), cot_text.get_rect())  # draw the text surface on the screen


def draw_csc(display_surface: pygame.Surface, origin: tuple[int, int], vector: tuple[int, int]) -> None:
    """
    Draw the csc component of a given Vector on the screen surface
    """
    rect_components: tuple[int, int] = get_sin_component(origin, (origin[0] + vector[0], origin[1] + vector[1]))
    if rect_components[0] != 0:  # if sin is not 0
        distance: float = get_distance(origin, (origin[0] + vector[0], origin[1] + vector[1]))
        csc: float = distance / -rect_components[0]

        pygame.draw.line(display_surface, (0, 255, 255), origin, (origin[0], origin[1] - distance * csc), 1)  # draw the x component

        csc_text: pygame.Surface = pygame.font.SysFont("Consolas", 16).render(f"csc = {csc:8.4f}", True, (0, 0, 0))  # create the text surface
        display_surface.blit(csc_text, (48, 176), csc_text.get_rect())  # draw the text surface on the screen


def draw_cot_csc_identity(display_surface: pygame.Surface, origin: tuple[int, int], vector: tuple[int, int]) -> None:
    rect_components: tuple[int, int] = get_sin_component(origin, (origin[0] + vector[0], origin[1] + vector[1]))
    if rect_components[0] != 0 and rect_components[1] != 0:  # if sin and cos are not 0
        cot: float = - rect_components[1] / rect_components[0]
        csc: float =  get_distance(origin, (origin[0] + vector[0], origin[1] + vector[1])) / rect_components[0]
        text: pygame.Surface = pygame.font.SysFont("Consolas", 16).render(f"{cot**2:.4f} + {1} = {csc**2:.4f}", True, (0, 0, 0))  # create the text surface
        display_surface.blit(text, (48, 192), text.get_rect())  # draw the text surface on the screen


def draw_dotted_line(display_surface: pygame.Surface, color: tuple[int, int, int], start: tuple[int, int], end: tuple[int, int], dot_size: int = 8) -> None:
    """
    Draw a dotted line on the screen from the start point to the end point

    ### Parameters:
    - `display_surface`: The surface on which the line will be drawn
    - `color`: The color of the line
    - `start`: The start point of the line
    - `end`: The end point of the line
    """
    pygame.draw.line(display_surface, color, start, end, 1)  # draw the segment
    points: list[tuple[int, int]] = []
    if end[0] > 0:  # if the line is not vertical
        slope: float = end[1] / end[0]
        # print(slope)
        # y_intercept: float = start[1] - slope * start[0]  # calculate the y intercept of the line (b)
    else:  # if the line is vertical
        # get the other slope
        slope: float = end[0] / end[1]

    for x in range(int(start[0]), int(start[0] + end[0]), 20):  # get 20 points on the line (for 10 lines)
        # y: int = int(slope * x + y_intercept)
        y: int = int(slope * x + start[1] - slope * start[0])
        points.append((x, y))  # add the point to the list
        # points.append((x + 8 * math.cos(math.atan(slope)), y + 8 * math.sin(math.atan(slope))))  # add the end of the line to the list

    # draw the lines between the points
    for i in range(1, len(points), 2):
        pygame.draw.line(display_surface, color, points[i-1], points[i], 1)  # draw the segment


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



# ? TRIGONOMETRY FUNCTIONS --------------------------------------------------------------------------------------------


def get_angle(origin: tuple[int, int], point: tuple[int, int]) -> float:
    """
    Return the angle between the origin and the point

    ### Parameters:
    - `origin`: The origin point
    - `point`: The point to calculate the angle from

    ### Returns:
    - `angle`: Angle on radians
    """
    # calculate the angle of the vector
    angle: float = math.atan2(point[1] - origin[1], point[0] - origin[0])
    if angle < 0: angle += 2 * math.pi
    return angle


def get_distance(origin: tuple[int, int], point: tuple[int, int]) -> float:
    """
    Return the distance between the origin and the point
    """
    return math.sqrt((point[0] - origin[0]) ** 2 + (point[1] - origin[1]) ** 2)


def get_vector(origin: tuple[int, int], point: tuple[int, int]) -> tuple[int, int]:
    """
    Return the vector between the origin and the point
    """
    return (point[0] - origin[0], point[1] - origin[1])


def get_point(origin: tuple[int, int], angle: float, distance: float) -> tuple[int, int]:
    """
    Return the point at the given angle and distance from the origin
    """
    return (int(origin[0] + distance * math.cos(angle)), int(origin[1] + distance * math.sin(angle)))


def get_sin_component(origin: tuple[int, int], point: tuple[int, int]) -> tuple[int, int]:
    """
    Return the sin component of the vector between the origin and the point

    ### Parameters:
    - `origin`: The origin point
    - `point`: The point to calculate the sin component from

    ### Returns:
    - `sin_component`: Component on rectangular coordinates
    """
    angle: float = get_angle(origin, point)
    distance: float = get_distance(origin, point)
    return (int(distance * math.sin(angle)), int(distance * math.cos(angle)))


def rect_to_polar(vector: tuple[int, int]) -> tuple[float, float]:
    """
    Convert a vector from rectangular to polar coordinates
    """
    polar: tuple[float, float] = (get_angle((0, 0), vector), get_distance((0, 0), vector))
    return polar


def polar_to_rect(polar: tuple[float, float]) -> tuple[int, int]:
    """
    Convert a vector from polar to rectangular coordinates
    """
    vector: tuple[int, int] = (int(polar[1] * math.cos(polar[0])), int(polar[1] * math.sin(polar[0])))
    return vector

