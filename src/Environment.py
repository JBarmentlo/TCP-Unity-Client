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
		self.client.send_action(action)
		s, players = self.client.get_state()
		pp = []
		for p in players:
			pp.append(PlayerState(p, self.player_num))
		return (s, pp)


	def reset(self):
		return self.do_action(defines.Reset)
	