# Mancala-Python-Boardgame
This is a re-creation of the Mancala boardgame but in Python! Please see the rules pdf file if you need a refresher on how to play Mancala. 

# Usage
Clone the repository to your computer. Open the file in your IDE and try playing a game of Mancala! See below for an example of how to play the game in Python. 


Type the following into your cloned file to create a Mancala game object and to begin an instance of the game. Create your two players as shown below and take turns moving. The first number indicates player number and the second indicates which pit that player is taking from. For example: game.play(1,1) is saying player 1 will take a seed from their first pit.

game = Mancala() <br />
player1 = game.create_player("Lily") <br />
player2 = game.create_player("Lucy") <br />
print(game.play_game(1, 3)) <br />
game.play_game(1, 1) <br />
game.play_game(2, 3) <br />
game.play_game(2, 4) <br />
game.play_game(1, 2) <br />
game.play_game(2, 2) <br />
game.play_game(1, 1) <br />
game.print_board() <br />
print(game.return_winner()) <br />

Another example:

game = Mancala() <br />
player1 = game.create_player("Lily") <br />
player2 = game.create_player("Lucy") <br />
game.play_game(1, 1) <br />
game.play_game(1, 2) <br />
game.play_game(1, 3) <br />
game.play_game(1, 4) <br />
game.play_game(1, 5) <br />
game.play_game(1, 6) <br />
game.print_board() <br />
print(game.return_winner()) <br />
