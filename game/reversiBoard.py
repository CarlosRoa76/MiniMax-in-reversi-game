from abc import ABC, abstractmethod
from game.tokens import Token
from copy import deepcopy


class Board(ABC):
    _state = None
    depth = 0
    cost = 0
    def __init__(self, state, depth=0, utility=0):
        self._state = state
        self.depth = depth
        self.utility = utility
    
    @abstractmethod
    def childrens(self):
        pass
    
    
class ReversiBoard(Board):
    
    BOARD_SIZE = 8
    
    def __init__(self, state=None, depth=0, utility=0):
        super().__init__(state, depth, utility)
        self.create_board()
        
    def create_board(self):
        self._state = [[None for _ in range(self.BOARD_SIZE)] for _ in range(self.BOARD_SIZE)]
        self._state[3][3] = Token('B')
        self._state[3][4] = Token('W')
        self._state[4][3] = Token('W')
        self._state[4][4] = Token('B')
    
    def points(self):
        black_points = 0
        white_points = 0
        for row in self._state:
            for token in row:
                if token is None:
                    continue
                
                if token.color == 'B':
                    black_points += 1
                elif token.color == 'W':
                    white_points += 1
                    
        return {'B': black_points, 'W': white_points}
        
    def is_terminal(self):
        # The game ends when neither player can make a valid move
        if not self.posible_movements('B') and not self.posible_movements('W'):
            return True
        
        # Or when the board is full
        if all(self._state[y][x] is not None for y in range(self.BOARD_SIZE) for x in range(self.BOARD_SIZE)):
            return True
        return False
    
    def childrens(self):
        pass
    
    def evaluate(self):
        pass
    
    def state(self):
        return self._state
    
    def posible_movements(self, color):
        movements = []
        for y in range(self.BOARD_SIZE):
            for x in range(self.BOARD_SIZE):
                if self._state[y][x] is None:
                    # Check all 8 directions
                    directions = [(-1, -1), (-1, 0), (-1, 1),
                                  (0, -1),           (0, 1),
                                  (1, -1), (1, 0),   (1, 1)]
                    for dy, dx in directions:
                        ny, nx = y + dy, x + dx
                        found_opponent = False
                        while 0 <= ny < self.BOARD_SIZE and 0 <= nx < self.BOARD_SIZE:
                            if self._state[ny][nx] is None:
                                break
                            elif self._state[ny][nx].color != color:
                                found_opponent = True
                            elif self._state[ny][nx].color == color:
                                if found_opponent:
                                    movements.append((x, y))
                                break
                            ny += dy
                            nx += dx
        return list(set(movements))
    
    def insert_play(self, x, y, token:Token):
        if (x, y) not in self.posible_movements(token.color):
            raise ValueError(f"Invalid move at ({x}, {y}) for color {token.color}.")
        self._state[y][x] = token
        
        
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),           (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]
        
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            opponents_found = []

            while 0 <= ny < self.BOARD_SIZE and 0 <= nx < self.BOARD_SIZE:
                if self._state[ny][nx] is None:
                    break
                elif self._state[ny][nx].color == token.color:
                    if opponents_found:
                        for ox, oy in opponents_found:
                            self._state[oy][ox].flip()
                    break

                else:
                    opponents_found.append((nx, ny))
                    ny += dy
                    nx += dx
            
            
                
    def __str__(self):
        
        board_str = f"  {'-'* (self.BOARD_SIZE* 4)}-\n"
        for y in range(self.BOARD_SIZE):
            board_str += f"{y} "
            for x in range(self.BOARD_SIZE):
                board_str += f"| {self._state[y][x] if self._state[y][x] != None else ' '} "
            board_str += "|\n"
            board_str += f"  {'-'* (self.BOARD_SIZE* 4)}-\n"
        board_str += f"    " + "   ".join(str(i) for i in range(self.BOARD_SIZE)) + "\n" 
            
        return board_str
    
    def __repr__(self):
        return f"ReversiBoard(state={self._state if any(x!=None for y in self._state for x in y) else None}, depth={self.depth}, utility={self.utility})"
    
    
    
    
if __name__ == "__main__":
    board = ReversiBoard()
    print(board)
    print(board.posible_movements("B"))