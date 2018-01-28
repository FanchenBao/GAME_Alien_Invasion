import pygame

class Ship():
	def __init__(self, screen):
		'''initialize ship and determine its original position on screen'''
		self.screen = screen

		#load the shit image and get its rect
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()

		# start new ship at the bottom center of screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

	def blitme(self):
		''' draw the ship at its current location'''
		self.screen.blit(self.image, self.rect)