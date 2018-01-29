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
		# movement flag
		self.moving_right = False
		self.moving_left = False

	def update(self):
		''' update new position of ship based on the movement flag, which itself is based on user key input'''
		if self.moving_right:
			self.rect.centerx += 1
		if self.moving_left:
			self.rect.centerx -= 1

	def blitme(self):
		''' draw the ship at its current location'''
		self.screen.blit(self.image, self.rect)