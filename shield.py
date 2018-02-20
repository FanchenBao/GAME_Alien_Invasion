import pygame
from pygame.sprite import Sprite

class Shield(Sprite):
	def __init__(self, screen, ai_settings, ship):
		super().__init__()
		'''initialize shield and determine its original position on screen'''
		self.screen = screen
		self.ai_settings = ai_settings
		self.ship = ship
		#load the shield image and get its rect
		self.image = pygame.image.load('images/shield.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()


		# present shield ahead of the ship
		self.rect.centerx = self.ship.rect.centerx
		self.rect.y = self.ship.rect.y + 5

		# store a decimal value for alien's location for fine tuning position
		self.x = float(self.rect.x)

	def update(self):
		self.x = self.ship.rect.x
		self.rect.x = self.x

	def blitme(self):
		''' draw the alien at its current location'''
		self.screen.blit(self.image, self.rect)