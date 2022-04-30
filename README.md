# Algorithms with bombs

This is a client to control a player in a BomberBuddy game. The purpose is to have a competition where AI agents and algorithms try to blow each other up! However this project is in beta and probably has some bugs so please raise an issue or send me a message on the 42 slack (jbarment).  

<br/>

## How it works

<br/>

### Download the game

mac:  
https://drive.google.com/file/d/1F5GoeN_-0d1NlI7jnxCjBKJHthOO0Bk1/view?usp=sharing

Linux:  
https://drive.google.com/file/d/19j9jLHTMItYzpvW5AvbufL0z1VLRaVST/view?usp=sharing

You may have to `chmod +x bomber.x86_64`.  
If you want to move the game, move the whole extracted folder, not just the executable, it wont work otherwise.

Finally you need to modify in Client.py the variable `PATH_TO_BOMBER`.

<br/>

### FIGHT !

You can now ***start the game*** and run fight.py with python3.  
Fight.py will make the two agents fight each other.  
```bash
cd src
python3 fight.py "./ExampleAgent.py" "./ExampleAgent.py" 
```

The code to ExampleAgent.py contains what you need to know to start building an agent.  

<br/>

## How you can help ?

You can help by reporting bugs or suggesting features / improvements.  
Don't be shy to say something looks wierd or stupid or to ask for stuff (i.e I wanna be able to play against my AI)  
If you want to help dev on the project contact us at contact@42ai.fr.  

<br/>

## Thanks

Thank you for participating in the beta of this project and helping 42AI organize cool competitions in the school