from ctypes import sizeof
import socket
import json
import os
import logging
import os
# from enum import Enum

import keyboard  # using module keyboard?\




HOST = "localhost"  # The server's hostname or IP address
PORT = 13000        # The port used by the server

# class ActionEnum(Enum):
Nothing	= 0
Up 		= 1
Down 	= 2
Left 	= 3
Right 	= 4	
Bomb 	= 5	
	

class  Client():
	def __init__(self):
		self.sim_port	= None
		self.board		= ["e"] * (19 * 19)
		self.winner		= "no"
		self.illegal	= False
		self.w_captures	= 0
		self.b_captures	= 0
		self.connected	= False

		# self.sock : socket
		# self.connect()
		

	def connect(self):
		print("CONNNNECTING\n\n\n\n")
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((HOST, PORT))
		self.connected = True
		

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
		print('Received', received)
		print("\n")
	

	def send_action(self, action):
		msg = {"action" : action}
		self.send_msg(msg)
		self.recv_msg()
	

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
				

	

c = Client()
c.connect()
# c.send_action(Down)
c.loopyloop()

# c.send_msg({"type" : "test", "im" : "gross"})
# board = c.play_move(181)


# # c = Client()
# # c.play_game()