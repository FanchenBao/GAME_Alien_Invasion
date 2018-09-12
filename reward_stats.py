'''
Author: Fanchen Bao
Date: 02/17/2018

Description:
RewardStats class, handle the statistics related to rewards from hitting alien.
Note that at different level of the game, the probability for different rewards are different.
'''

from random import randint

class RewardStats():
	''' a class to represent stats for the reward system'''
	''' reward I is to increase bullet number
		reward M is to increase projectile number
		reward S is to add shield
		reward U is to have unlimited number of bullets
		reward L is to add one life'''
	def __init__(self, level):
		self.level = level

		if self.level in [4, 5]:
			# number of rewards that will appear in the alien fleet
			self.number_of_reward = 1
			# probability of reward I and M appearing in a designated alien
			self.prob_i = 70
			self.prob_m = 30
			self.prob_u = 0
			self.prob_s = 0
			self.prob_l = 0

		if self.level in [6, 7]:
			# number of rewards that will appear in the alien fleet
			self.number_of_reward = 2
			# probability of reward I, M, and S appearing in a designated alien
			self.prob_i = 60
			self.prob_m = 25
			self.prob_u = 0
			self.prob_s = 15
			self.prob_l = 0

		if self.level in [8, 9]:
			# number of rewards that will appear in the alien fleet
			self.number_of_reward = 2
			# probability of reward I, M, S, and U appearing in a designated alien
			self.prob_i = 55
			self.prob_m = 25
			self.prob_u = 5
			self.prob_s = 15
			self.prob_l = 0

		if self.level >= 10:
			# number of rewards that will appear in the alien fleet
			self.number_of_reward = 3
			# probability of reward I, M, S, U, and L appearing in a designated alien
			self.prob_i = 50
			self.prob_m = 25
			self.prob_u = 5
			self.prob_s = 15
			self.prob_l = 5

	def assign_reward(self):
		list_i = list(range(1, self.prob_i + 1))
		list_m = list(range(self.prob_i + 1, self.prob_i + self.prob_m + 1))
		list_u = list(range(self.prob_i + self.prob_m + 1, self.prob_i + self.prob_m + self.prob_u + 1))
		list_s = list(range(self.prob_i + self.prob_m + self.prob_u + 1, 
			self.prob_i + self.prob_m + self.prob_u + self.prob_s + 1))
		list_l = list(range(self.prob_i + self.prob_m + self.prob_u + self.prob_s + 1, 
			self.prob_i + self.prob_m + self.prob_u + self.prob_s + self.prob_l + 1))
		test_number = randint(1, 100)
		if test_number in list_i:
			return("I")
		if test_number in list_m:
			return("M")
		if test_number in list_u:
			return("U")
		if test_number in list_s:
			return("S")
		if test_number in list_l:
			return("L")



