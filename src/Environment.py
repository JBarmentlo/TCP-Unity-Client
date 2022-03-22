from Client 		import Client
from PlayerState 	import PlayerState

import defines

class Environnement:
	def __init__(self, player_num = -1):
		'''
		player_num is the number of the player we want to be (1 or 2) put -1 for any available number.
		'''
		self.client = Client(player_num)
		self.client.connect()
		self.client.request_type(player_num, defines.Player)
		self.client.send_action(defines.Nothing)
		self.player_num = self.client.player


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
		self.client.send_action(action)
		s, players, w = self.client.get_state()
		pp = []
		for p in players:
			pp.append(PlayerState(p, self.player_num))
		return (s, pp, w)


	def reset(self):
		self.client.reset()
		s, players, w = self.client.get_state()
		pp = []
		for p in players:
			pp.append(PlayerState(p, self.player_num))
		return (s, pp, w)
	