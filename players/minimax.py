import math
from copy import deepcopy
from typing import List, Tuple, Optional
import time

from players.player import Player
from game.reversiBoard import ReversiBoard, opponent  # <-- Importamos ReversiBoard Y la función opponent
from game.tokens import Token


class MinimaxPlayer(Player):
    
    TYPE_ = "minimax"
    
    def __init__(self, name, depth=math.inf, max_time=math.inf, 
                enabled_heuristics: Optional[List[str]] = None,
                custom_weights: Optional[dict] = None):
        
        super().__init__(name)
        self.max_depth = depth  
        self.enabled_heuristics = set(enabled_heuristics) if enabled_heuristics else None
        self.custom_weights = custom_weights
        self.max_time = max_time
        
        
    def play(self, board: ReversiBoard) -> Tuple[int, int]:
        """
        Punto de entrada principal. Encuentra el mejor movimiento
        llamando al algoritmo Minimax (con poda alfa-beta).
        """
        print(f"{self.name}")
        possible_moves = board.posible_movements(self.tokens.color)
        self.time_start = time.time()
        
        
        if not possible_moves:
            return None
        
        best_move = possible_moves[0]
        best_score = -math.inf
        alpha = -math.inf
        beta = math.inf
        

        
        for move in possible_moves:
            x, y = move
            
            child_board = deepcopy(board)
            child_board.insert_play(x, y, Token(self.tokens.color))
            
            #minimax
            score = self._minimax(child_board, self.max_depth - 1, alpha, beta, False)
            
            if score > best_score:
                best_score = score
                best_move = move
            
            alpha = max(alpha, best_score)
        
        print(f"{self.name} elige {best_move} (Puntuación: {best_score:.4f})")
        return best_move

    def _minimax(self, board: ReversiBoard, depth: int, alpha: float, beta: float, is_maximizing_player: bool) -> float:
        """
        Función recursiva de Minimax con poda Alfa-Beta.
        """
        
        if depth == 0 or board.is_terminal() or time.time() - self.time_start >= self.max_time:
            return board.evaluate(self.tokens.color, enabled_heuristics=self.enabled_heuristics,
                                custom_weights=self.custom_weights)
        
        if is_maximizing_player:
            max_eval = -math.inf
            my_color = self.tokens.color
            
            children_boards = board.childrens(my_color)
            
            if not children_boards:
                return self._minimax(board, depth - 1, alpha, beta, False)

            for child in children_boards:
                eval = self._minimax(child, depth - 1, alpha, beta, False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break  # Poda Beta
            return max_eval
        
        else:
            #oponente
            min_eval = math.inf
            opponent_color = opponent(self.tokens.color)
            
            children_boards = board.childrens(opponent_color)

            if not children_boards:
                #no movimientos
                return self._minimax(board, depth - 1, alpha, beta, True)

            for child in children_boards:
                eval = self._minimax(child, depth - 1, alpha, beta, True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break 
            return min_eval
        



"""
DEYBBY EL ORDEN IMPORTA, SOLO SI HAY UNA MEJORA CAMBIA ESTE ORDEN
"""