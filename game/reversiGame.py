from game.reversiBoard import ReversiBoard
from players import humanPlayer, randomPlayer
import os
from game.color import Color
import time
from game.metrics import Metrics


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

        self.current_turn = (
            self.player1
            if self.current_turn.name == self.player2.name
            else self.player2
        )
        self.board.depth += 1

    def play(self, board: ReversiBoard):
        self.board = board
        # self.board = ReversiBoard()
        self.current_turn = self.player1
        os.system("cls")
        while not self.board.is_terminal():

            available_moves = self.board.posible_movements(
                self.current_turn.token_color
            )
            print(
                f"Turno de {self.current_turn.name} ({self.current_turn.token_color}) Profundidad: {self.board.depth}"
            )
            print(
                f"Puntajes:\n{Color.RED}Rojas{Color.RESET}: {self.board.points()['R']} - {Color.BLUE}Azules{Color.RESET}: {self.board.points()['B']}"
            )

            if self.current_turn.tokens.is_empty():
                print(f"{self.current_turn.name} no tiene fichas para jugar.")
                self.swap_turn()
                time.sleep(1)
                continue
            elif not available_moves:
                print(f"{self.current_turn.name} no tiene movimientos. Cede el turno.")
                self.swap_turn()
                time.sleep(1)
                continue

            print(self.board.show(self.current_turn))

            # if not isinstance(self.current_turn, humanPlayer.HumanPlayer):
            #     time.sleep(1)

            x, y = self.current_turn.play(self.board)
            self.board.insert_play(x, y, self.current_turn.tokens.pop())
            # os.system("cls")
            print(f"\n{self.current_turn.name} juega en ({x}, {y})")
            self.swap_turn()

        print(
            "Puntajes:\n",
            "Rojas:",
            self.board.points()["R"],
            "- Azules:",
            self.board.points()["B"],
        )
        print(self.board.show())
        winner = None
        points = 32
        if self.board.points()["B"] > self.board.points()["R"]:
            print("Ganador: Azul")
            winner = self.player1.name  if self.player1.token_color == "B" else self.player2.name
            points = self.board.points()["B"]
        elif self.board.points()["R"] > self.board.points()["B"]:
            print("Ganador: Rojo")
            winner = self.player1.name if self.player1.token_color == "R" else self.player2.name
            poins = self.board.points()["R"]
        else:
            print("Juego empate")
            
        for player, opponent in ((self.player1, self.player2),(self.player2, self.player1)):
            try:
                Metrics.generate_report(player, opponent.name, winner, self.board.points()[player.token_color], self.board.points()["R"]+self.board.points()["B"])
            except:
                pass

    def play_for_algorithms(self, board: ReversiBoard):
        self.board = board
        # self.board = ReversiBoard()
        self.current_turn = self.player1
        # os.system("cls")
        while not self.board.is_terminal():

            available_moves = self.board.posible_movements(
                self.current_turn.token_color
            )
            # print(
            #     f"Turno de {self.current_turn.name} ({self.current_turn.token_color}) Profundidad: {self.board.depth}"
            # )
            # print(
            #     f"Puntajes:\n{Color.RED}Rojas{Color.RESET}: {self.board.points()['R']} - {Color.BLUE}Azules{Color.RESET}: {self.board.points()['B']}"
            # )

            if self.current_turn.tokens.is_empty() or not available_moves:
                self.swap_turn()
                continue

            x, y = self.current_turn.play(self.board)
            self.board.insert_play(x, y, self.current_turn.tokens.pop())
            self.swap_turn()
        winner = None
        if self.board.points()["B"] > self.board.points()["R"]:
            return()
        elif self.board.points()["R"] > self.board.points()["B"]:
            print("Ganador: Rojo")
        else:
            print("Juego empate")
            
        for player, opponent in ((self.player1, self.player2),(self.player2, self.player1)):
            Metrics.generate_report(player, opponent.name, )
            
        

if __name__ == "__main__":
    board = ReversiBoard()
    game = ReversiGame()
    player1 = humanPlayer.HumanPlayer("Alice")
    player2 = randomPlayer.RandomPlayer("Bot")
    game.play(board)
    print(game)
