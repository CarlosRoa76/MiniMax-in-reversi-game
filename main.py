from game.reversiBoard import ReversiBoard
from game.reversiGame import ReversiGame
from game.tokens import StackToken
from players.humanPlayer import HumanPlayer
from players.randomPlayer import RandomPlayer
from players.minimax import MinimaxPlayer

if __name__ == "__main__":
    print("\033[30mHola\033[0m")
    board = ReversiBoard()
    game = ReversiGame()

    player1 = HumanPlayer("Deybby")
    # player2 = RandomPlayer("Bot")
    player2 = MinimaxPlayer("Bot-Minimax", max_time=1)

    player1.tokens = StackToken("B")
    player2.tokens = StackToken("R")

    game.players(player1, player2)
    game.play(board)
