# pyChess
python chess

this application is a project to build a chess game from scratch.
the game's state shall be transferred using a simple text file
after every move said text file is sent to the other player.
for now this process will be done via email.
each player needs to have a python file which will be the program that projects the game state using a gui.
the program displaying the file will remember the last game state of every game that it plays using some sort of a hash key.
The chessboard will be implemented using an array containing an array.
the latter array will either contain null or a chess piece value.
the game state file will remember: the location of every piece on the field, the color and name of each player.
