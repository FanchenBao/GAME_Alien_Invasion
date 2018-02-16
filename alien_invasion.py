import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from button import Button
from score_board import ScoreBoard
import game_functions as gf
from game_stats import GameStats

def run_game():
	# initialize game and create a screen object.
	
	# initialize game
	pygame.init()

	# create game display with 1200 pixels wide and 800 pixels in height
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	# create an instance to store game stats
	stats = GameStats(ai_settings)

	ship = Ship(screen, ai_settings)
	bullets = Group()
	aliens = Group()

	# create a play button
	msg = 'Press "P" to Play'
	play_button = Button(screen, ai_settings, msg)

	score_board = ScoreBoard(screen, ai_settings, stats)
	
	# create an alient fleet
	gf.create_alien_fleet(screen, ai_settings, aliens, ship)

	# The main loop of the game
	while True:
		gf.check_events(ai_settings, screen, ship, bullets, play_button, stats, aliens, score_board)
		if stats.game_active:
			ship.update()
			gf.update_bullets(screen, ai_settings, aliens, ship, bullets, stats, score_board)
			gf.update_aliens(stats, aliens, bullets, ship, screen, ai_settings)
		gf.update_screen(ai_settings, screen, ship, bullets, aliens, play_button, stats, score_board)
		
run_game()
