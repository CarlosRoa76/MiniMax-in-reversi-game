from players.player import Player
import re

class HumanPlayer(Player):
    
    TYPE_ = "human"
    
    def __init__(self, name):
        super().__init__(name)
             
    def play(self, board):
        
        print("Movimientos posibles:", board.posible_movements(self.tokens.color))
        print("Que movimiento desea hacer?")
        position = input("Ingrese la coordenada (x,y): ")
        
        if re.match(r'^\d{2}$', str(position)):
            x, y = divmod(int(position), 10)
        else:
            x, y = -1, -1
            
        while (x, y) not in board.posible_movements(self.tokens.color):
            print("Movimiento invalido. Intente de nuevo.")
            position = input("Ingrese la coordenada (x,y): ")
            
            if re.match(r'^\d{2}$', str(position)):
                x, y = divmod(int(position), 10)
            else:
                x, y = -1, -1
    
        return x, y
        
    


if __name__ == "__main__":
    player = HumanPlayer("Alice")
    print(player.name)  # Output: Alice
    print(player.TYPE_)  # Output: human