# Algorithms with bombs

This is a client to control a player in a BomberBuddy game. The purpose is to have a competition where AI agents and algorithms try to blow each other up! However this project is in beta and probably has some bugs so please raise an issue or send me a message on the 42 slack (jbarment).    

## How it works

Download the game and put the path to the game in Client.py

```python
PATH_TO_BOMBER = "/home/me/bomber.x86_64"
```

run fight.py with python3.  

```bash
cd src
python3 fight.py "./ExampleAgent.py" "./ExampleAgent.py" 
```

The code to ExampleAgent.py contains what you need to know to start building an agent.  
use fight.py to make two agents fight.


## Thanks

Thank you for participating in the beta of this project and helping 42AI organize cool competitions in the school

