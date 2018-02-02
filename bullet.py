import pygame
from pygame.sprite import sprite

class Bullet(Sprite):
	''' a class to manage bullet'''

	def __init__(self, ai_settings, screen, ship):
		super().__init__()
		self.screen = screen
		# create a bullet rect at (0, 0) position
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
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