"""
This library provides a Python implementation of the game Isolation.
Isolation is a deterministic, two-player game of perfect information in
which the players alternate turns moving between cells on a square grid
(like a checkerboard).  Whenever either player occupies a cell, that
location is blocked for the rest of the game. The first player with no
legal moves loses, and the opponent is declared the winner.
"""
from isolation import Board

player1 = RandomPlayer()
player2 = GreedyPlayer()
game = Board(player1, player2)

# place player 1 on the board at row 2, column 3, then place player 2 on
# the board at row 0, column 5; display the resulting board state.  Note
# that the .apply_move() method changes the calling object in-place.

game.apply_move((2, 3))
game.apply_move((0, 5))
print(game.to_string())
