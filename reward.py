'''
Author: Fanchen Bao
Date: 02/17/2018

Description:
Reward class, handle the import and drawing of reward images
'''

import pygame
from pygame.sprite import Sprite

class Reward(Sprite):
	def __init__(self, screen, ai_settings, reward_flag):
		super().__init__()
		''' initialize the reward class'''
		self.screen = screen
		self.ai_settings = ai_settings
		self.screen_rect = self.screen.get_rect()

		self.reward_flag = reward_flag
		
		#load the bullet number increase image and get its rect
		if self.reward_flag == "I":
			self.image = pygame.image.load('images/I.bmp')

		if self.reward_flag == "M":
			#load the projectile number increase image and get its rect
			self.image = pygame.image.load('images/M.bmp')

		if self.reward_flag == "U":
			#load the unlimited bullets image and get its rect
			self.image = pygame.image.load('images/U.bmp')

		if self.reward_flag == "L":
			#load the life boost image and get its rect
			self.image = pygame.image.load('images/L.bmp')

		if self.reward_flag == "S":
			#load the shield image and get its rect
			self.image = pygame.image.load('images/S.bmp')

		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 0
		# store a decimal value for reward's location for fine tuning position
		self.y = float(self.rect.y)

	def update(self):
		''' update the position of reward'''
		self.y += self.ai_settings.reward_speed
		self.rect.y = self.y

	def blitme(self):
		''' draw the reward at its current location'''
		self.screen.blit(self.image, self.rect)















