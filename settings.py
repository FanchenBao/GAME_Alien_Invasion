class Settings():
	''' to store all settings for alien_invasion'''
	def __init__(self):
		self.screen_height = 700
		self.screen_width = 1050
		self.background_color = (230, 230, 230)
		
		# ship settings
		self.ship_speed = 5
		self.ship_limit = 3

		# bullet settings
		self.bullet_speed = 4
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullet_allowed = 4

		# alien settings
		self.alien_speed = 50
		self.alien_drop_speed = 10
		# alien fleet moving direction. 1 = move right, -1 = move left
		self.fleet_direction = 1