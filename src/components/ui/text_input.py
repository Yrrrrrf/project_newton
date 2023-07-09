# text input module

from dataclasses import dataclass

import pygame

from config.globals import Assets


# 1. Create a new text font
# 2. Render the text (get user input)
# 3. Create a new text surface

@dataclass
class TextInput:
    """	
    This class is responsible for creating a text input box.
    
    Attributes
    """
    def __init__(self): 
        self.display_surface: pygame.Surface = pygame.display.set_mode((800, 600))  # create a new display surface
        self.base_font: pygame.font.Font = pygame.font.SysFont("Consolas", 16)  # create a new font
        self.user_input: str = ""  # user input



        
    # def render_text(self, event: pygame.event.Event):
    def render_text(self, event):
        """
        Render the text (get user input)
        """
        text_surface: pygame.Surface = self.base_font.render(self.user_input, True, (255, 255, 255))  # create a new text surface
        text_rect: pygame.Rect = text_surface.get_rect()  # create a new rect
        text_rect.center = (self.display_surface.get_width() // 2, self.display_surface.get_height() // 2)  # center the rect

        self.display_surface.blit(text_surface, text_rect)  # draw the text

    
    # def display(self):
    #     """
    #     Make the text input visible
    #     """
    #     self.render_text()


    # def update(self, event: pygame.event.Event):
    #     """
    #     Update the text input
    #     """
    #     if event.type == pygame.KEYDOWN:
    #         if event.key == pygame.K_BACKSPACE:
    #             self.user_input = self.user_input[:-1]
    #         else:
    #             self.user_input += event.unicode

    