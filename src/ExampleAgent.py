from random import Random
from Environment import Environnement
import defines

class RandomAgent:
	def __init__(self, player_num):
		self.player_num = player_num
		self.env		= Environnement(player_num)
		print("I Am a random agent, please help me get smarter than this !")


	def get_action(self, state):
		"""
			This is where you put something smart to choose an action.
		"""
		return (Random().choice(defines.action_space))

	
	def do_action(self, action):
		"""
			Takes action and Returns a (state, players) tuple    
			players is an array of PlayerState objects representing the players
			state is an array of size (11, 11) containing the following strings
			Player1		: "1",
			Player2		: "2", 
			Bomb		: "B", 
			Explosion	: "E", 
			Wall		: "W", 
			Crate		: "C", 
			Bomb explosion Range Bonus 	: "r", 
			Extra Bomb Count Bonus		: "b", 
			Extra Speed Bonus			: "s"
		"""
		return self.env.do_action(action)

	
	
	def get_state(self):
		'''
			Send nothing action to get state.
		'''
		return self.env.do_action(defines.Nothing)

