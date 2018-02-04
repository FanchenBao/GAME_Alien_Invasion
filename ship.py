import pygame

class Ship():
	def __init__(self, screen, ai_settings):
		'''initialize ship and determine its original position on screen'''
		self.screen = screen
		self.ai_settings = ai_settings

		#load the ship image and get its rect
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()

		# start new ship at the bottom center of screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		# store a decimal value for the ship's center
		self.center = float(self.rect.centerx)
		# movement flag
		self.moving_right = False
		self.moving_left = False

	def update(self):
		''' update new position of ship based on the movement flag, which itself is based on user key input'''
		''' ship will NOT disappear from the edge (different code compared to the book'''
		if self.moving_right:
			self.center += self.ai_settings.ship_speed
			self.current_right = self.center + self.rect.width/2
			if self.current_right > self.screen_rect.right:
				self.center = self.screen_rect.right - self.rect.width/2
		if self.moving_left:
			self.center -= self.ai_settings.ship_speed
			self.current_left = self.center - self.rect.width/2
			if self.current_left < self.screen_rect.left:
				self.center = self.screen_rect.left + self.rect.width/2

		# update the ship's current location, must pass self.center back to self.rect.centerx to change ship's location
		self.rect.centerx = self.center

	def blitme(self):
		''' draw the ship at its current location'''
		self.screen.blit(self.image, self.rect)