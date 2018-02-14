class GameStats():
	'''track game statistics for alien invasion'''
	def __init__(self, ai_settings):
		self.ai_settings = ai_settings
		self.game_active = False
		self.reset_stats()

	def reset_stats(self):
		'''initialize statistics that can change during game'''
		self.ship_left = self.ai_settings.ship_limit
