from random import Random
from Environment import Environnement
import defines

class Agent:
	def __init__(self, player_num):
		self.player_num = player_num
		self.env		= Environnement(player_num)


	def get_action(self, state):
		pass

	
	def do_action(self, action):
		pass

	
	def get_state(self):
		pass


class RandomAgent(Agent): 
	def __init__(self, player_num):
		self.player_num = player_num
		self.env		= Environnement(player_num)
		print("I Am a random agent, please help me get smarter than this !")


	def get_action(self, state):
		"""
			This is where you put something smart to choose an action.

			Returns
			-------
			action   : int
				The action you think we should do based on the state. (for example defines.Bomb)
		"""
		return (Random().choice(defines.action_space))

	
	def do_action(self, action):
		"""
		Takes action and Returns a (state, players, winner) tuple.

		Parameters
		----------
		action : int
			An action value defined in defines.py

		Returns
		-------
		state   : array
			An array of strings of size (11, 11) representing the board, player positions are rounded to the grid, for exact positions refer to the players array

		players : array
			array of PlayerState objects representing the players

		winner   : int
			1, 2 or None if game is not over.

		Notes
		-----
			UNDERSTANDING THE STATE ARRAY
			Here are the strings and what they represent:
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
		Returns
		-------
		state   : array
			An array of strings of size (11, 11) representing the board, player positions are rounded to the grid, for exact positions refer to the players array

		players : array
			array of PlayerState objects representing the players

		winner   : int
			1, 2 or None if game is not over.

		Notes
		-----
			UNDERSTANDING THE STATE ARRAY
			Here are the strings and what they represent:
			Player1		: "1",
			Player2		: "2", 
			Bomb		: "B", 
			Explosion	: "E", 
			Wall		: "W", 
			Crate		: "C", 
			Bomb explosion Range Bonus 	: "r", 
			Extra Bomb Count Bonus		: "b", 
			Extra Speed Bonus			: "s"
		'''
		return self.env.do_action(defines.Nothing)


import sys
import time
if __name__ == "__main__":
	agent = RandomAgent(int(sys.argv[1]))
	# agent.env.reset()
	state1 = agent.get_state()
	game_over = False


	while game_over == False:
		time.sleep(0.1)
		state = agent.do_action(agent.get_action(state1))
		_, _, w = state
		if (w is not None):
			game_over = True