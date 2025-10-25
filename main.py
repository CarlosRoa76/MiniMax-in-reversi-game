from game.reversiBoard import ReversiBoard
from game.reversiGame import ReversiGame
from game.tokens import StackToken
from players.humanPlayer import HumanPlayer
from players.randomPlayer import RandomPlayer
from players.minimax import MinimaxPlayer
from players.greedy import GreedyPlayer
from players.badPlayer import BadPlayer

if __name__ == "__main__":
    print("\033[30mHola\033[0m")
    board = ReversiBoard()
    game = ReversiGame()

    # player1 = HumanPlayer("Deybby")
    # player1 = RandomPlayer("Random")
    # player1 = GreedyPlayer("Greedy")
    # player1 = BadPlayer(max_time=1)
    player1 = MinimaxPlayer("Minimax2", max_time=1)
    player2 = MinimaxPlayer("Minimax", max_time=1)
    
    
    

    player1.tokens = StackToken("B")
    player2.tokens = StackToken("R")

    game.players(player1, player2)
    game.play(board)
