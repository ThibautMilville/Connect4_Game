# Connect4 Game

This is a simple implementation of the classic Connect4 game using Python and the Pygame library. Connect4 is a two-player connection game in which the players take turns dropping colored discs from the top into a vertically suspended grid. The objective of the game is to connect four of one's own discs of the same color consecutively in a row, column, or diagonal.

<img src="https://github.com/ThibautMilville/Connect4_Game/assets/87717065/bc7a9791-9b53-4343-8a9c-2cd768bef563" alt="Connect4" />

## How to Play

- Run the Game:
  - Make sure you have Python installed on your machine.
  - Install the Pygame library by running `pip install pygame`.
  - Run the game script: `python index.py`.

- Game Interface:
  - The game window displays a grid of 7 columns and 6 rows.
  - Player 1 (Red discs) starts the game.

- Gameplay:
  - Click on a column to drop a disc. The disc will occupy the lowest empty position in that column.
  - Players take turns, and the game alternates between Red and Yellow discs.

- Winning:
  - The game automatically detects a win when a player connects four of their discs horizontally, vertically, or diagonally.
  - Once a player wins, the game will print "Player [1 or 2] wins!" and exit.

## Game Controls

- Mouse Click:
  - Click on a column to drop a disc during your turn.

- Exit Game:
  - Click the close button on the game window to exit.

## Code Structure

- The game logic is implemented in `index.py`.
- The game board is represented as a 2D list (`board`), and Pygame is used for the graphical interface.

## Dependencies

- Python 3.x
- Pygame library

## Credits

- This Connect4 implementation was created using the Pygame library.
- Pygame: [https://www.pygame.org/](https://www.pygame.org/)

This game was fully developed using ChatGPT in just 5 minutes as an experiment, along with its README file.
