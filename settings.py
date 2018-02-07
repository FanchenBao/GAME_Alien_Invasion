class Settings():
	''' to store all settings for alien_invasion'''
	def __init__(self):
		self.screen_height = 700
		self.screen_width = 1050
		self.background_color = (230, 230, 230)
		self.ship_speed = 50

		# bullet settings
		self.bullet_speed = 2
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullet_allowed = 4

		# alien speed
		self.alien_speed = 3