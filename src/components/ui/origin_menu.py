from dataclasses import dataclass
import pygame

from config.globals import Assets


# @dataclass
class OriginMenu:
    # buttons: pygame.sprite.Group = pygame.sprite.Group()
    margin: int = 12
    button_size: int = 128


    def __init__(self):
        self.display_surface: pygame.Surface = pygame.display.get_surface()
        self.buttons: pygame.sprite.Group = pygame.sprite.Group()
        self.create_buttons()

        
    def create_buttons(self):
        """
        Create the buttons of the origin menu
        """
        self.update_rect()  # update the size of the surface
        # create the buttons of the origin menu
        button_paths: list[str] = ["axis.png", "rotation.png", "search.png", "size.png"]
        button_functions: list[callable] = [
            print("Clicked"),
            print("Clicked"),
            print("Clicked"),
            print("Clicked")
        ]
        # create the buttons
        [Button(button_rect, button_function, button_path, self.buttons) for button_rect, button_function, button_path in zip(self.buttons_rect, button_functions, button_paths)]

        # create 1 button
        # Button(self.rect, print("Clicked"), "axis.png", self.buttons)


    def update_rect(self):
        # create the buttons
        self.rect: pygame.Rect = pygame.Rect(
            self.display_surface.get_width() - self.button_size - self.margin,
            self.display_surface.get_height() - self.button_size - self.margin,
            self.button_size, self.button_size  # width, height
        )
        
        mini_button_size = (self.button_size - self.margin * 3) / 2  # size of the mini buttons
        self.buttons_rect: list[pygame.Rect] = [  # create the buttons rectangles
            pygame.Rect(self.rect.x + self.margin, self.rect.y + self.margin, mini_button_size, mini_button_size),
            pygame.Rect(self.rect.x + self.margin * 2 + mini_button_size, self.rect.y + self.margin, mini_button_size, mini_button_size),
            pygame.Rect(self.rect.x + self.margin, self.rect.y + self.margin * 2 + mini_button_size, mini_button_size, mini_button_size),
            pygame.Rect(self.rect.x + self.margin * 2 + mini_button_size, self.rect.y + self.margin * 2 + mini_button_size, mini_button_size, mini_button_size)
        ]  # create 4 buttons inside the rect with a margin of 8 pixels


    def display(self):
        """
        Make all the buttons visible
        """
        pygame.draw.rect(self.display_surface, (32, 32, 32), self.rect)  # draw the rect of the button
        self.update_rect()  # update the size of the surface
        self.buttons.update()  # update the buttons
        self.buttons.draw(self.display_surface)  # draw the buttons


    def click(self, mouse_pos: tuple[int, int], mouse_button: int):
        """
        Check if the user clicked on a button
        """
        for button in self.buttons:
            if button.rect.collidepoint(mouse_pos):
                match mouse_button:
                    case 1: print("Left Click")
                    case 2: print("Middle Click")
                    case 3: print("Right Click")
                    case _: print("Unknown Click")
                # return button.get_id()


# @dataclass
class Button(pygame.sprite.Sprite):
    """
    Button class
    This class represents a button in the GUI
    """
    def __init__(self, rect: pygame.Rect, function: callable, img_path: str, group: pygame.sprite.Group):
        super().__init__(group)
        self.image: pygame.Surface = pygame.Surface(rect.size)  # create a surface for the button
        self.rect = rect
        self.function = function
        self.img_path = img_path
        self.update()

    
    # def update(self):
        self.image.fill((128, 128, 128))
        button_margin = 4
        surf = pygame.transform.scale(
            pygame.image.load(f"{Assets.IMAGES.value}static\\{self.img_path}"),  # load the image
            (self.rect.width - button_margin * 2, self.rect.height - button_margin * 2)  # scale the image -> (width, height)
        )
        rect = surf.get_rect(center=self.image.get_rect().center)  # = surf.get_rect(center=(self.image.get_width() // 2, self.image.get_height() // 2))
        self.image.blit(surf, rect)  # draw the image on the button surface
