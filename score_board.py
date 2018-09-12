'''
Author: Fanchen Bao
Date: 02/15/2018

Description:
ScoreBoard class, prepares and updates game score, game level, and ships remained.
'''

import pygame.font
from pygame.sprite import Group
from ship import Ship

class ScoreBoard():
	''' a class to record and draw scores on the screen'''
	
	def __init__(self, screen, ai_settings, stats):
		''' initialize scoreboard'''
		self.screen = screen
		self.ai_settings = ai_settings
		self.stats = stats

		self.screen_rect = screen.get_rect()

		# setting font for score
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 28)

		# draw score information on the screen
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ships()

	def prep_score(self):
		''' convert score information into image'''
		# round the score to the nearest 10 (if the second argument is 1, that means to ronud to nearest 0.1)
		rounded_score = round(self.stats.score, -1)
		# syntax to insert comma to long number
		score_str = "Score: " + "{:,}".format(rounded_score)
		self.score_image = self.font.render(score_str, True, self.text_color, 
			self.ai_settings.background_color)
		self.score_image_rect = self.score_image.get_rect()
		self.score_image_rect.right = self.screen_rect.right - 20
		self.score_image_rect.top = 20

	def prep_high_score(self):
		''' convert high score into image'''
		rounded_high_score = round(self.stats.high_score, -1)
		# syntax to insert comma to long number
		high_score_str = "High Score: " + "{:,}".format(rounded_high_score)
		self.high_score_image = self.font.render(high_score_str, True, self.text_color, 
			self.ai_settings.background_color)
		self.high_score_image_rect = self.score_image.get_rect()
		self.high_score_image_rect.centerx = self.screen_rect.centerx
		self.high_score_image_rect.top = self.score_image_rect.top

	def prep_level(self):
		''' convert level information into image'''
		level_str = "Level " + str(self.stats.level)
		self.level_image = self.font.render(level_str, True, self.text_color, 
			self.ai_settings.background_color)
		self.level_image_rect = self.level_image.get_rect()
		self.level_image_rect.right = self.screen_rect.right - 20
		self.level_image_rect.top = self.score_image_rect.bottom + 10

	def prep_ships(self):
		self.ships = Group()
		if self.stats.ship_left > 0:
			for ship_number in range(self.stats.ship_left):
				ship = Ship(self.screen, self.ai_settings)
				ship.rect.x = 10 + ship_number * ship.rect.width
				ship.rect.y = 10
				self.ships.add(ship)
		else:
			self.ships.empty()

	def show_score(self):
		''' draw score information on the screen'''
		self.screen.blit(self.score_image, self.score_image_rect)
		self.screen.blit(self.high_score_image, self.high_score_image_rect)
		self.screen.blit(self.level_image, self.level_image_rect)
		self.ships.draw(self.screen)