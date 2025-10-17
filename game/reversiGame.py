from game.reversiBoard import ReversiBoard
from players import humanPlayer, randomPlayer

class ReversiGame:
    
    def __init__(self):
        self.player1 = None
        self.player2 = None
        self.board = None
        self.current_turn = None    
    
    
    def players(self, player1=None, player2=None):
        self.player1 = player1 if player1 else self.player1
        self.player2 = player2 if player2 else self.player2
        
    
    def app(self):
        pass
    
    def swap_turn(self):
        
        self.current_turn = self.player1 if self.current_turn.name == self.player2.name else self.player2
        self.board.depth += 1
        
    def play(self, board:ReversiBoard):
        self.board = board
        # self.board = ReversiBoard()
        self.current_turn = self.player1
        
        while not self.board.is_terminal():
            print(f"Turno de {self.current_turn.name} ({self.current_turn.token_color}) Profoundidad: {self.board.depth}")
            print(self.board)
            x, y = self.current_turn.play(self.board)
            self.board.insert_play(x, y, self.current_turn.tokens.pop())
            print(f"\n{self.current_turn.name} juega en ({x}, {y})")
            self.swap_turn()
            
        print("Game over!")
        print(self.board)
        
    
if __name__ == "__main__":
    board = ReversiBoard()
    game = ReversiGame()
    player1 = humanPlayer.HumanPlayer("Alice")
    player2 = randomPlayer.RandomPlayer("Bot")
    game.play(board)
    print(game)