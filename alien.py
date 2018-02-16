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
		self.rect.y = self.rect.height * 2

		# store a decimal value for alien's location for fine tuning position
		self.x = float(self.rect.x)
		
	def check_edges(self):
		'''check whether an alien ship has hit the edge'''
		if self.rect.right >= self.screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True

	def update(self):
		''' update current alien position'''
		self.x += self.ai_settings.alien_speed * self.ai_settings.fleet_direction
		self.rect.x = self.x

		

	def blitme(self):
		''' draw the alien at its current location'''
		self.screen.blit(self.image, self.rect)