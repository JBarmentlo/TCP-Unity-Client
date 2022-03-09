from ExampleAgent import RandomAgent
from ExampleAgent import Agent
from Client import PATH_TO_BOMBER

import time
import subprocess
import sys


def play_game_against_random_agent(my_agent : Agent):
	enemy_num = 2 if (my_agent.player_num == 1 ) else 1
	enemy_agent = RandomAgent(enemy_num)
	enemy_agent.env.reset()
	my_agent.env.reset()
	state1 = enemy_agent.get_state()
	state2 = my_agent.get_state()
	game_over = False


	while game_over == False:
		time.sleep(0.1)
		state1 = enemy_agent.do_action(enemy_agent.get_action(state1))
		state2 = my_agent.do_action(my_agent.get_action(state2))
		_, _, w = state2
		if (w is not None):
			game_over = True

	print("the winner is Player " + w)


if __name__ == "__main__":
	if (len(sys.argv) != 4 or sys.argv[3] != "fast"):
		subprocess.Popen([PATH_TO_BOMBER])
		time.sleep(7)
	enemy_agent = RandomAgent(1)
	# enemy_agent.env.reset()
	subprocess.Popen(["python3", sys.argv[1], "1"])
	subprocess.Popen(["python3", sys.argv[2], "2"])




# If you want to run a Machine learning algorithm you can use the reset function to reset the game and play many games
	# agent_1.env.reset()

	# state1 = agent_1.get_state()
	# state2 = agent_2.get_state()
	# game_over = False


	# while game_over == False:
	# 	time.sleep(0.1)
	# 	state1 = agent_1.do_action(agent_1.get_action(state1))
	# 	state2 = agent_2.do_action(agent_2.get_action(state2))
	# 	_, _, w = state2
	# 	if (w is not None):
	# 		game_over = True