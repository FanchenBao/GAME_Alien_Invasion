'''
Author: Fanchen Bao
Date: 02/02/2018

Description:
Bullet class
'''

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	''' a class to manage bullet'''

	def __init__(self, ai_settings, screen, ship, x_position):
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		self.x_position = x_position
		# create a bullet rect at (0, 0) position
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
		
		# bullet initial position depends on the projectile number
		self.rect.centerx = ship.rect.centerx + self.x_position
		
		# y coordinate does not change for each projectile
		self.rect.top = ship.rect.top
		# store bullet y-coordinate as float to fine tune the speed of bullet
		self.y = float(self.rect.y)

		self.color = ai_settings.bullet_color
		self.speed = ai_settings.bullet_speed

	def update(self):
		''' update the position of bullet'''
		# use self.y (a float) to record the most accurate current position
		self.y -= self.speed
		# update that position to the bullet rect y-coordinate
		self.rect.y = self.y

	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)