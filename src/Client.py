from ctypes import sizeof
import math
import socket
import json
import os
import logging
import os
import subprocess
import time

# from enum import Enum

# import keyboard  # using module keyboard?\


import colorama
from colorama import Fore
from matplotlib.pyplot import delaxes
import defines

HOST 			= "localhost"  # The server's hostname or IP address
PORT 			= 13000        # The port used by the server
PATH_TO_BOMBER 	= "/home/yup/Desktop/build/bomber.x86_64"
SLEEP_TIME		= 5.0 			# If the progRam must start the bomberbuddy it will wait this many seconds for bomberbuddy to start before attempting to connect

dico = {0: "1", 1:"2",2:"B",3:"E",4:"W",5: "C", 6 : "r",7:"b",8:"s"}




def itemtopos(item):
	return round(item["position"]["x"]), round(item["position"]["z"])


class  Client():
	def __init__(self, player):
		self.board			= []
		self.h 				= 11
		self.w 				= 11
		self.msg 			= ""
		self.player 		= player
		self.player_states	= []
		self.connected		= False
		self.winner			= None

		for i in range(self.h):
			self.board.append([([" "] * (self.w))])
		

	def connect(self):
		print("CONNNNECTING\n\n\n\n")
		try:
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.sock.connect((HOST, PORT))
			self.connected = True
		except:
			subprocess.Popen([PATH_TO_BOMBER])
			time.sleep(SLEEP_TIME)
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.sock.connect((HOST, PORT))
			self.connected = True
		
		
	def request_type(self, num = -1, typo = defines.Player ,passw = "default"):
		'''
		num -1 for first available player. only works if player not instantiated;
		'''
		msg = {"requestedType" : typo, "pass" : passw, "playerNum" : num}
		self.send_msg(msg)
		self.recv_msg()
		self.parse_request()


	def close(self):
		self.sock.close()


	def send_msg(self, msg):
		# if (self.sock.)
		data = json.dumps(msg)
		# print("Sending: ", data)
		self.sock.sendall(bytes(data,encoding="utf-8"))
		# print("Sent\n\n")


	def recv_msg(self):
		self.msg = ""
		n = int(self.sock.recv(8))
		while (n > 0):
			received = self.sock.recv(4096)
			received = received.decode("utf-8")
			self.msg += received
			n = n - len(received)

	
	def parseboard(self, msg):
		print(self.msg)
		self.board			= []
		self.player_states	= []
		self.winner			= None

		for i in range(self.h):
			self.board.append(([" "] * (self.w)))
		a = json.loads(msg)
		for e in a:
			if (e["type"] == -1):
				self.winner = e["winner"]
				continue;
			x,y = itemtopos(e)
			self.board[y][x] = dico[e["type"]]
			try:
				if (e["is_player"] == True):
					self.player_states.append(e)
			except:
				continue


	def printboard(self):
		for i in range(self.h):
			print(self.board[self.h - 1 - i])


	def parse_request(self):
		rep = json.loads(self.msg)
		if (rep["requestedType"] == defines.Untyped):
			print("request denied")
			return
		
		self.player = rep["playerNum"]


	def send_action(self, action, print_state_to_terminal = True):
		msg = {"action" : action, "playerNum" : self.player, "pass": "lolpas"}
		self.send_msg(msg)
		self.recv_msg()
		self.parseboard(self.msg)


	def reset(self):
		self.winner = None
		self.send_action(defines.Reset)

	# def loopyloop(self):
	# 	while(True):
	# 		if keyboard.is_pressed('w'):
	# 			self.send_action(Up)
	# 		elif keyboard.is_pressed('a'):
	# 			self.send_action(Left)
	# 		elif keyboard.is_pressed('s'):
	# 			self.send_action(Down)
	# 		elif keyboard.is_pressed('d'):
	# 			self.send_action(Right)
	# 		elif keyboard.is_pressed(' '):
	# 			self.send_action(Bomb)
	# 		elif keyboard.is_pressed('r'):
	# 			self.send_action(Reset)

	
	def get_state(self):
		"""
			Returns a (state, players, winner) tuple
			players is an array of json objects representing the players
			winner is None if no one has won yet, otherwise it is 1 or 2
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
		return (self.board, self.player_states, self.winner)



# c = Client()
# c.connect()
# c.request_type(-1)