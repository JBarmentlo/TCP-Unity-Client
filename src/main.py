from ExampleAgent import RandomAgent
import time


if __name__ == "__main__":
	player1 = RandomAgent(1)
	player2 = RandomAgent(2)
	state1 = player1.get_state()
	state2 = player2.get_state()


	while True:
		time.sleep(0.1)
		state1 = player1.do_action(player1.get_action(state1))
		state2 = player2.do_action(player2.get_action(state2))