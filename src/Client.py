from ctypes import sizeof
import math
import socket
import json
import os
import logging
import os
# from enum import Enum

import keyboard  # using module keyboard?\


import colorama
from colorama import Fore
from matplotlib.pyplot import delaxes

HOST = "localhost"  # The server's hostname or IP address
PORT = 13000        # The port used by the server

# class ActionEnum(Enum):
dico = {0: Fore.BLUE + "P", 1:"P",2:"B",3:"E",4:"W",5: "C", 6 : "r",7:"b",8:"s"}

Nothing = 0
Up      = 1
Down   = 2
Left   = 3
Right  = 4     
Bomb   = 5

Untyped = 0
Player  = 1
Controller = 2

# Player1
# Player2,
# Bomb,
# Explosion,
# Wall,
# Crate,
# ExtraRange,
# ExtraBomb,
# ExtraSpeed
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



def itemtopos(item):
	return round(item["position"]["x"]), round(item["position"]["z"])


class  Client():
	def __init__(self):
		self.board		= []
		for i in range(10):
			self.board.append([([" "] * (10))])
		self.msg = ""
		self.player = 1

		# self.sock : socket
		# self.connect()
		

	def connect(self):
		print("CONNNNECTING\n\n\n\n")
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((HOST, PORT))
		self.connected = True
		
		
	def request_type(self, num = -1, typo = Player ,passw = "default"):
		'''
		num -1 for first available player. only works if player not instantiated;
		'''
		msg = {"requestedType" : typo, "pass" : passw, "playerNum" : num}
		self.send_msg(msg)


	def close(self):
		self.sock.close()


	def send_msg(self, msg):
		# if (self.sock.)
		data = json.dumps(msg)
		print("Sending: ", data)
		self.sock.sendall(bytes(data,encoding="utf-8"))
		print("Sent\n\n")
		# self.sock.send(bytes(data,encoding="utf-8"), 1024)
		# print(f"sending {data}")


	def recv_msg(self):
		received = self.sock.recv(5000)

		received = received.decode("utf-8")
		self.msg = received
		# print('Received', received)
		print('Received')
		# print("\n")
	


	
	def parseboard(self, msg):
		self.board		= []
		for i in range(10):
			self.board.append(([" "] * (10)))
		a = json.loads(msg)
		for e in a:
			x,y = itemtopos(e)
			self.board[y][x] = dico[e["type"]]
		for i in range(9):
			print(self.board[9 - i])

	def send_action(self, action):
		msg = {"action" : action, "playerNum" : self.player, "pass": "lolpas"}
		self.send_msg(msg)
		self.recv_msg()
		self.parseboard(self.msg)


	def loopyloop(self):
		while(True):
			if keyboard.is_pressed('w'):
				self.send_action(Up)
			elif keyboard.is_pressed('a'):
				self.send_action(Left)
			elif keyboard.is_pressed('s'):
				self.send_action(Down)
			elif keyboard.is_pressed('d'):
				self.send_action(Right)
			elif keyboard.is_pressed(' '):
				self.send_action(Bomb)






	

# test = '[{"type":5,"position":{"x":6.996999740600586,"y":0.5,"z":4.0}},{"type":5,"position":{"x":2.0,"y":0.5,"z":8.0}},{"type":5,"position":{"x":6.996999740600586,"y":0.5,"z":2.0}},{"type":5,"position":{"x":2.996999979019165,"y":0.5,"z":8.0}},{"type":5,"position":{"x":2.996999979019165,"y":0.5,"z":7.0}},{"type":5,"position":{"x":7.996999740600586,"y":0.5,"z":5.0}},{"type":5,"position":{"x":4.996999740600586,"y":0.5,"z":8.0}},{"type":5,"position":{"x":4.996999740600586,"y":0.5,"z":4.0}},{"type":5,"position":{"x":0.996999979019165,"y":0.5,"z":2.0}},{"type":5,"position":{"x":0.996999979019165,"y":0.5,"z":4.0}},{"type":5,"position":{"x":6.996999740600586,"y":0.5,"z":6.0}},{"type":5,"position":{"x":0.996999979019165,"y":0.5,"z":3.0}},{"type":5,"position":{"x":3.996999740600586,"y":0.5,"z":2.0}},{"type":5,"position":{"x":5.996999740600586,"y":0.5,"z":2.0}},{"type":5,"position":{"x":2.996999979019165,"y":0.5,"z":4.0}},{"type":5,"position":{"x":7.996999740600586,"y":0.5,"z":8.0}},{"type":4,"position":{"x":9.0,"y":0.5,"z":4.0}},{"type":0,"position":{"x":6.2354817390441898,"y":0.5,"z":3.9251511096954347},"playerNumber":1,"moveSpeed":6.0,"bombs":4,"bombRange":3,"dead":false,"bombPrefab":{"instanceID":4998}},{"type":1,"position":{"x":8.0,"y":0.5,"z":2.0},"playerNumber":2,"moveSpeed":4.0,"bombs":2,"bombRange":2,"dead":false,"bombPrefab":{"instanceID":4998}}]'
# a = json.loads(test)
c = Client()
c.connect()
# c.send_action(Down)
# c.send_action(Up)

# c.loopyloop()

# c.send_msg({"type" : "test", "im" : "gross"})
# board = c.play_move(181)


# # c = Client()
# # c.play_game()