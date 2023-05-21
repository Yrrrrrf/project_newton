# import pygame, sys 
# from pygame.math import Vector2 as vector
# from pygame.mouse import get_pressed as mouse_buttons
# from pygame.mouse import get_pos as mouse_pos
# from settings import *

# class Editor:
# 	def __init__(self):
# 		# main setup 
# 		self.display_surface = pygame.display.get_surface()

# 		# navigation
# 		self.origin = vector()
# 		self.pan_active = False
# 		self.pan_offset = vector()

# 		# support lines 
# 		self.support_line_surf = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
# 		self.support_line_surf.set_colorkey('green')
# 		self.support_line_surf.set_alpha(30)


# 	# input
# 	def event_loop(self):
# 		for event in pygame.event.get():
# 			if event.type == pygame.QUIT:
# 				pygame.quit()
# 				sys.exit()
# 			self.pan_input(event)

# 	def pan_input(self, event):

# 		# middle mouse button pressed / released 
# 		if event.type == pygame.MOUSEBUTTONDOWN and mouse_buttons()[1]:
# 			self.pan_active = True
# 			self.pan_offset = vector(mouse_pos()) - self.origin

# 		if not mouse_buttons()[1]:
# 			self.pan_active = False

# 		# mouse wheel 
# 		if event.type == pygame.MOUSEWHEEL:
# 			if pygame.key.get_pressed()[pygame.K_LCTRL]:
# 				self.origin.y -= event.y * 50
# 			else:
# 				self.origin.x -= event.y * 50


# 		# panning update
# 		if self.pan_active:
# 			self.origin = vector(mouse_pos()) - self.pan_offset

# 	# drawing 
# 	def draw_tile_lines(self):
# 		cols = WINDOW_WIDTH // TILE_SIZE
# 		rows = WINDOW_HEIGHT// TILE_SIZE

# 		origin_offset = vector(
# 			x = self.origin.x - int(self.origin.x / TILE_SIZE) * TILE_SIZE,
# 			y = self.origin.y - int(self.origin.y / TILE_SIZE) * TILE_SIZE)

# 		self.support_line_surf.fill('green')

# 		for col in range(cols + 1):
# 			x = origin_offset.x + col * TILE_SIZE
# 			pygame.draw.line(self.support_line_surf,LINE_COLOR, (x,0), (x,WINDOW_HEIGHT))

# 		for row in range(rows + 1):
# 			y = origin_offset.y + row * TILE_SIZE
# 			pygame.draw.line(self.support_line_surf,LINE_COLOR, (0,y), (WINDOW_WIDTH,y))

# 		self.display_surface.blit(self.support_line_surf,(0,0))

# 	def run(self, dt):
# 		self.event_loop()

# 		# drawing
# 		self.display_surface.fill('white')
# 		self.draw_tile_lines()
# 		pygame.draw.circle(self.display_surface, 'red', self.origin, 10)


# from pygame.math import Vector2 as vector


# import sys
# import pygame
# from dataclasses import dataclass

# from config.globals import Config


# @dataclass
# class Editor:
#     """
#     Editor class
#     This class contains the logic for the GUI
#     """
#     # App data (App State)
#     display_surface: pygame.Surface = pygame.display.get_surface()


#     def __init__(self):
#         """
#         Initialize the app
#         """
#         self.display_surface: pygame.Surface = pygame.display.get_surface()

#         self.origin = vector()  # origin of the coordinate system
#         self.pan_active = False  # if the user is panning


#     # ? Input --------------------------------------------------------------------------------------
#     def event_loop(self):
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             self.pan_input(event)
			
#     def pan_input(self, event):
# 		# middle mouse button pressed / released 
#         if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[1]:
#             self.pan_active = True
#             self.pan_offset = vector(pygame.mouse.get_pos()) - self.origin
#         if not pygame.mouse.get_pressed()[1]:
#             self.pan_active = False
#         if event.type == pygame.MOUSEWHEEL:
#             if pygame.key.get_pressed()[pygame.K_LCTRL]:
#                 self.origin.y -= event.y * 50
#             else:
#                self.origin.x -= event.y * 50
# 		# panning update
#         if self.pan_active:
#             self.origin = vector(pygame.mouse.get_pos()) - self.pan_offset




#     # def event_loop(self):
#     #     for event in pygame.event.get():  # get all events
#     #         if event.type == pygame.QUIT:  # if the user closes the window
#     #             pygame.quit()  # quit pygame
#     #             sys.exit()  # exit the program
#     #         self.pan_input(event)


#     # def pan_input(self, event):
#     #     # check if the middle mouse button is pressed
#     #     # pygame.mouse.get_pressed() returns a tuple with the state of the mouse buttons
#     #     # the first element of the tuple is the left mouse button, the second is the middle mouse button and the third is the right mouse button
#     #     if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[1]:
#     #         self.pan_active = True
#     #         # print(self.pan_active)
#     #     if not pygame.mouse.get_pressed()[1]:
#     #         self.pan_active = False
#     #         # print(self.pan_active)
#     #     if self.pan_active:
#     #         self.origin = pygame.mouse.get_pos()
#     #         print(self.origin)


#     def run(self, dt: float) -> None:
#         """
#         Initialize the Editor (GUI)

#         ### Parameters:
#             dt (float): time in seconds since the last tick
#         """
#         pygame.display.set_caption(f"{Config.NAME.value} {Config.VERSION.value} (Editor Mode)")  # set the window title
#         self.event_loop()  # handle events
#         self.display_surface.fill('white')
#         # print(self.origin)
#         pygame.draw.circle(self.display_surface, (0, 255, 0), self.origin, 10)

import pygame, sys 
from pygame.math import Vector2 as vector
from pygame.mouse import get_pressed as mouse_buttons
from pygame.mouse import get_pos as mouse_pos
# from settings import *

class Editor:
	def __init__(self):
		# main setup 
		self.display_surface = pygame.display.get_surface()

		# navigation
		self.origin = vector()
		self.pan_active = False
		self.pan_offset = vector()

		# support lines 
		# self.support_line_surf = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
		# self.support_line_surf.set_colorkey('green')
		# self.support_line_surf.set_alpha(30)


	# input
	def event_loop(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			self.pan_input(event)

	def pan_input(self, event):

		# middle mouse button pressed / released 
		if event.type == pygame.MOUSEBUTTONDOWN and mouse_buttons()[1]:
			self.pan_active = True
			self.pan_offset = vector(mouse_pos()) - self.origin

		if not mouse_buttons()[1]:
			self.pan_active = False

		# mouse wheel 
		if event.type == pygame.MOUSEWHEEL:
			if pygame.key.get_pressed()[pygame.K_LCTRL]:
				self.origin.y -= event.y * 50
			else:
				self.origin.x -= event.y * 50


		# panning update
		if self.pan_active:
			self.origin = vector(mouse_pos()) - self.pan_offset

	# # drawing 
	# def draw_tile_lines(self):
	# 	cols = WINDOW_WIDTH // TILE_SIZE
	# 	rows = WINDOW_HEIGHT// TILE_SIZE

	# 	origin_offset = vector(
	# 		x = self.origin.x - int(self.origin.x / TILE_SIZE) * TILE_SIZE,
	# 		y = self.origin.y - int(self.origin.y / TILE_SIZE) * TILE_SIZE)

	# 	self.support_line_surf.fill('green')

	# 	for col in range(cols + 1):
	# 		x = origin_offset.x + col * TILE_SIZE
	# 		pygame.draw.line(self.support_line_surf,LINE_COLOR, (x,0), (x,WINDOW_HEIGHT))

	# 	for row in range(rows + 1):
	# 		y = origin_offset.y + row * TILE_SIZE
	# 		pygame.draw.line(self.support_line_surf,LINE_COLOR, (0,y), (WINDOW_WIDTH,y))

	# 	self.display_surface.blit(self.support_line_surf,(0,0))

	def run(self, dt):
		self.event_loop()

		# drawing
		self.display_surface.fill('white')
		# self.draw_tile_lines()
		pygame.draw.circle(self.display_surface, 'red', self.origin, 10)