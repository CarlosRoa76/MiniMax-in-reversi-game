from abc import ABC, abstractmethod
from game.tokens import Token
from copy import deepcopy
import math

# --- IMPLEMENTACION DE LO QUE HIZO HECTOR EL MORENO MAGICO ---

POSITION_WEIGHTS = [
    [100, -20, 10, 5, 5, 10, -20, 100],
    [-20, -50, -2, -2, -2, -2, -50, -20],
    [10, -2, -1, -1, -1, -1, -2, 10],
    [5, -2, -1, -1, -1, -1, -2, 5],
    [5, -2, -1, -1, -1, -1, -2, 5],
    [10, -2, -1, -1, -1, -1, -2, 10],
    [-20, -50, -2, -2, -2, -2, -50, -20],
    [100, -20, 10, 5, 5, 10, -20, 100],
]


def opponent(color: str) -> str:
    """Devuelve el color opuesto."""
    return "W" if color == "B" else "B"


class Board(ABC):
    _state = None
    _depth = 0

    def __init__(self, state, depth=0, utility=0):
        self._state = state
        self._depth = depth

    @abstractmethod
    def childrens(self):
        pass


class ReversiBoard(Board):

    BOARD_SIZE = 8

    def __init__(self, state=None, depth=0, utility=0):
        super().__init__(state, depth, utility)
        self.players_tokens = {"B": 30, "W": 30}

        if not state:
            self.create_board()

    def create_board(self):
        self._state = [
            [None for _ in range(self.BOARD_SIZE)] for _ in range(self.BOARD_SIZE)
        ]
        self._state[3][3] = Token("B")
        self._state[3][4] = Token("W")
        self._state[4][3] = Token("W")
        self._state[4][4] = Token("B")

    def points(self):
        black_points = 0
        white_points = 0
        for row in self._state:
            for token in row:
                if token is None:
                    continue

                if token.color == "B":
                    black_points += 1
                elif token.color == "W":
                    white_points += 1

        return {"B": black_points, "W": white_points}

    def is_terminal(self):
        # The game ends when neither player can make a valid move
        if not self.posible_movements("B") and not self.posible_movements("W"):
            return True

        # Or when one player has no tokens and the other has no valid moves
        if (
            (self.players_tokens["B"] == 0 and not self.posible_movements("W"))
            or self.players_tokens["W"] == 0
            and not self.posible_movements("B")
        ):
            return True

        # Or when the board is full
        if all(
            self._state[y][x] is not None
            for y in range(self.BOARD_SIZE)
            for x in range(self.BOARD_SIZE)
        ):
            return True
        return False

    def childrens(self, player_color):

        options_available = self.posible_movements(player_color)
        children = []

        for x, y in options_available:
            new_state = deepcopy(self._state)
            child = ReversiBoard(new_state, self.depth + 1)
            child.insert_play(x, y, Token(player_color))
            children.append(child)

        return children

    @property
    def state(self):
        return self._state

    @property
    def depth(self):
        return self._depth

    @depth.setter
    def depth(self, new_depth: int):
        self._depth = new_depth

    def posible_movements(self, color):
        movements = []
        for y in range(self.BOARD_SIZE):
            for x in range(self.BOARD_SIZE):
                if self._state[y][x] is None:
                    # Check all 8 directions
                    directions = [
                        (-1, -1),
                        (-1, 0),
                        (-1, 1),
                        (0, -1),
                        (0, 1),
                        (1, -1),
                        (1, 0),
                        (1, 1),
                    ]
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

    def insert_play(self, x, y, token: Token):
        if (x, y) not in self.posible_movements(token.color):
            raise ValueError(f"Invalid move at ({x}, {y}) for color {token.color}.")
        self._state[y][x] = token
        self.players_tokens[token] -= 1

        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

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
                board_str += (
                    f"| {self._state[y][x] if self._state[y][x] != None else ' '} "
                )
            board_str += "|\n"
            board_str += f"  {'-'* (self.BOARD_SIZE* 4)}-\n"
        board_str += f"    " + "   ".join(str(i) for i in range(self.BOARD_SIZE)) + "\n"

        return board_str

    def __repr__(self):
        return f"ReversiBoard(state={self._state}, depth={self.depth})"

    # --- OTRA PARTE DEL CÓDIGO DEL HECTOR MAGICO ---

    def evaluate(self, color: str) -> float:
        """
        Función de evaluación principal (antes 'combined_heuristic').
        Calcula la puntuación del tablero para el color dado.
        """
        # Si el juego ha terminado, devuelve la puntuación final (victoria/derrota)

        if self.is_terminal():
            pts = self.points()
            myc = pts[color]
            opc = pts[opponent(color)]
            if myc > opc:
                return math.inf  # Victoria
            elif opc > myc:
                return -math.inf  # Derrota
            else:
                return 0.0  # Empate

        e = self._empty_count()
        W = self._phase_weights(e)

        h_corner = self._corner_occupancy(color)
        h_mob = self._mobility(color)
        h_stab = self._stable_discs(color)
        h_parity = self._coin_parity(color)
        h_pos = self._positional_weights(color)

        value = (
            W["corner"] * h_corner
            + W["mob"] * h_mob
            + W["stable"] * h_stab
            + W["parity"] * h_parity
            + W["pos"] * h_pos
        )
        return value

    def _empty_count(self) -> int:
        return sum(
            1
            for y in range(self.BOARD_SIZE)
            for x in range(self.BOARD_SIZE)
            if self.state[y][x] is None
        )

    def _coin_parity(self, color: str) -> float:
        pts = self.points()
        myc = pts[color]
        opc = pts[opponent(color)]
        total = myc + opc
        if total == 0:
            return 0.0
        return 100.0 * (myc - opc) / total

    def _mobility(self, color: str) -> float:
        my_moves = len(self.posible_movements(color))
        op_moves = len(self.posible_movements(opponent(color)))
        if my_moves + op_moves == 0:
            return 0.0
        return 100.0 * (my_moves - op_moves) / (my_moves + op_moves)

    def _corner_occupancy(self, color: str) -> float:
        corners = [(0, 0), (0, 7), (7, 0), (7, 7)]
        my_c = 0
        op_c = 0
        for x, y in corners:
            t = self.state[y][x]
            if t is None:
                continue
            if t.color == color:
                my_c += 1
            else:
                op_c += 1
        if my_c + op_c == 0:
            return 0.0
        return 100.0 * (my_c - op_c) / (my_c + op_c)

    def _line_stable_in_direction(self, x, y, dx, dy) -> bool:
        if self.state[y][x] is None:
            return False
        color = self.state[y][x].color
        cx, cy = x, y
        ok_to_edge = True
        while 0 <= cx < self.BOARD_SIZE and 0 <= cy < self.BOARD_SIZE:
            t = self.state[cy][cx]
            if t is None or t.color != color:
                ok_to_edge = False
                break
            cx += dx
            cy += dy
        return ok_to_edge

    def _is_stable(self, x, y) -> bool:
        if self.state[y][x] is None:
            return False
        dirs = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dx, dy in dirs:
            if not (
                self._line_stable_in_direction(x, y, dx, dy)
                or self._line_stable_in_direction(x, y, -dx, -dy)
            ):
                return False
        return True

    def _stable_discs(self, color: str) -> float:
        my_s = 0
        op_s = 0
        for y in range(self.BOARD_SIZE):
            for x in range(self.BOARD_SIZE):
                if self.state[y][x] is None:
                    continue
                if self._is_stable(x, y):
                    if self.state[y][x].color == color:
                        my_s += 1
                    else:
                        op_s += 1
        if my_s + op_s == 0:
            return 0.0
        return 100.0 * (my_s - op_s) / (my_s + op_s)

    def _positional_weights(self, color: str) -> float:
        score = 0
        for y in range(self.BOARD_SIZE):
            for x in range(self.BOARD_SIZE):
                t = self.state[y][x]
                if t is None:
                    continue
                w = POSITION_WEIGHTS[y][x]
                score += w if t.color == color else -w
        # El valor máximo absoluto es la suma de todos los pesos positivos
        max_abs = sum(abs(w) for row in POSITION_WEIGHTS for w in row)
        if max_abs == 0:
            return 0.0  # Evitar división por cero
        return 100.0 * score / max_abs

    def _phase_weights(self, empty_cells: int):
        if empty_cells >= 40:
            # Apertura
            return {
                "corner": 0.20,
                "mob": 0.35,
                "stable": 0.10,
                "parity": 0.05,
                "pos": 0.30,
            }
        elif empty_cells >= 15:
            # Medio juego
            return {
                "corner": 0.25,
                "mob": 0.30,
                "stable": 0.25,
                "parity": 0.05,
                "pos": 0.15,
            }
        else:
            # Final
            return {
                "corner": 0.15,
                "mob": 0.05,
                "stable": 0.40,
                "parity": 0.30,
                "pos": 0.10,
            }


if __name__ == "__main__":
    board = ReversiBoard()
    print(board)
    print("Movimientos posibles para 'B':", board.posible_movements("B"))
    print("Evaluación para 'B':", board.evaluate("B"))
    print("Evaluación para 'W':", board.evaluate("W"))
