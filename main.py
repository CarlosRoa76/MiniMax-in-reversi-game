from game.reversiBoard import ReversiBoard
from game.reversiGame import ReversiGame
from game.tokens import StackToken
from players.humanPlayer import HumanPlayer
from players.randomPlayer import RandomPlayer


if __name__ == "__main__":
    board = ReversiBoard()
    game = ReversiGame()
    
    player1 = HumanPlayer("Deybby")
    player2 = RandomPlayer("Bot")
    
    player1.tokens = StackToken('B')
    player2.tokens = StackToken('W')
    
    game.players(player1, player2)
    game.play(board)