'''
Author: Fanchen Bao
Date: 02/18/2018

Description:
Missle class, handle missles fired by aliens.
'''

import pygame
from pygame.sprite import Sprite

class Missile(Sprite):
	''' a class to manage alien missile'''

	def __init__(self, ai_settings, screen, alien):
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		self.screen_rect = self.screen.get_rect()
		
		# create a bullet rect at (0, 0) position
		self.rect = pygame.Rect(0, 0, ai_settings.missile_width, ai_settings.missile_height)
		
		# bullet initial position depends on the projectile number
		self.rect.centerx = alien.rect.centerx
		self.rect.top = alien.rect.bottom
		
		# store missile y-coordinate as float to fine tune the speed of bullet
		self.y = float(self.rect.y)

		self.color = ai_settings.missile_color
		self.speed = ai_settings.missile_speed

	def update(self):
		''' update the position of bullet'''
		# use self.y (a float) to record the most accurate current position
		self.y += self.speed
		# update that position to the bullet rect y-coordinate
		self.rect.y = self.y

	def draw_missile(self):
		pygame.draw.rect(self.screen, self.color, self.rect)