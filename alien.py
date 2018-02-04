import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	def __init__(self, screen, ai_settings):
		super().__init__()
		'''initialize alien and determine its original position on screen'''
		self.screen = screen
		self.ai_settings = ai_settings

		#load the alien image and get its rect
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()

		# start new alien NEAR the top left of screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		# store a decimal value for the ship's center
		self.x = float(self.rect.x)
	
		# get alien speed
		# self.speed = ai_settings.alien_speed

	# def update(self):
	# 	self.x += self.speed
	# 	self.rect.x = self.x

		

	def blitme(self):
		''' draw the alien at its current location'''
		self.screen.blit(self.image, self.rect)