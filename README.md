# Tic Tac Toe
This application is a simple game of Tic Tac Toe built with Python. The user has the option of playing versus another human player or versus "the computer".

## Getting started
1. Make sure you have Python installed on your computer.

2. Download this repository.

3. Open a terminal or command prompt window and navigate to the directory where the file is located.

4. Run the script using the command `python main.py`.

5. Follow the on-screen instructions to play the game.

## Features
### Number of players
Before the game begins, the player is prompted to inform the number of human players. In case 2 players are present, each player will have their own turn to make their moves. If only 1 player is present, the player will play against the computer.

![number-players.png](https://i.ibb.co/z6WdDr7/number-players.png)

### Choosing a move
In every human-player's turn, the player is reminded of which symbol ("X" or "O") they're playing as. The user chooses the space on the board where they're making a move by informing the row and column desired.

![choosing-move.png](https://i.ibb.co/w7GpRSC/choosing-move.png)

### Occupied space
In case the player chooses a space that's already been chosen by the other player (human or computer), the player is informed accordingly and prompted to choose another space.

![already-occupied.png](https://i.ibb.co/1GxbNPk/already-occupied.png)

### Computer's turn
When playing versus the computer, the player is notified when it's the computer's turn and the game displays what move did the computer make.

![ai-turn.png](https://i.ibb.co/dMYRkb8/ai-turn.png)

### Checking for victory
After every turn, the code checks whether any of the winning combinations is present on the board. If a victory is detected, it is announced who won and the player is prompted to inform whether they would like to play another game.

![victory.png](https://i.ibb.co/5s1Kjbc/victory.png)

### Checking for a tie
It is also possible that the players fill up the board spaces without ever winning. In that case, the bode checks for that possibility and announces when a tie has happened, prompting the players to inform whether they would like to play another game.

![tie.png](https://i.ibb.co/7RQ4rKH/tie.png)

## Requirements
This app requires the following:

+ Python 3
