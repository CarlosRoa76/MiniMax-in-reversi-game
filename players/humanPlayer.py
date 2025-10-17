from players.player import Player
import re

class HumanPlayer(Player):
    
    TYPE_ = "human"
    
    def __init__(self, name):
        super().__init__(name)
             
    def play(self, board):
        
        print("Movimientos posibles:", board.posible_movements(self.tokens.color))
        print("Que movimiento desea hacer?")
        position = int(input("Ingrese la coordenada (x,y): "))
        x, y = divmod(position, 10)
        while (x, y) not in board.posible_movements(self.tokens.color):
            print("Movimiento invalido. Intente de nuevo.")
            position = input("Ingrese la coordenada (x,y): ")
            x, y = int(position[0]), int(position[1])
        return x, y
        
    


if __name__ == "__main__":
    player = HumanPlayer("Alice")
    print(player.name)  # Output: Alice
    print(player.TYPE_)  # Output: human