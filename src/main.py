from ExampleAgent import RandomAgent
import time


if __name__ == "__main__":
	player1 = RandomAgent(1)
	player2 = RandomAgent(2)
	player1.env.reset()
	player2.env.reset()
	state1 = player1.get_state()
	state2 = player2.get_state()
	game_over = False


	while game_over == False:
		time.sleep(0.1)
		state1 = player1.do_action(player1.get_action(state1))
		state2 = player2.do_action(player2.get_action(state2))
		_, _, w = state2
		if (w is not None):
			game_over = True




# If you want to run a Machine learning algorithm you can use the reset function to reset the game and play many games
	# player1.env.reset()

	# state1 = player1.get_state()
	# state2 = player2.get_state()
	# game_over = False


	# while game_over == False:
	# 	time.sleep(0.1)
	# 	state1 = player1.do_action(player1.get_action(state1))
	# 	state2 = player2.do_action(player2.get_action(state2))
	# 	_, _, w = state2
	# 	if (w is not None):
	# 		game_over = True