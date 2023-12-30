import os

from player_manager import PlayerManager

RESET = "\033[0m"
YELLOW = "\033[93m"
BLUE= "\033[94m"


def get_row_index(number: int) -> int:
    return (number // 3) - 1 if number % 3 == 0 else (number // 3)


def get_col_index(number) -> int:
    return (number - 1) % 3


class GameBoard:
    """A class to handle the gameboard"""

    def __init__(self) -> None:
        self.board: list[list[str]] = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

    def print_board(self) -> None:
        """Prints the board to the console"""
        os.system("clear")
        for (i, row) in enumerate(self.board):
            print("\n")
            for (j, cell) in enumerate(row):
                if cell == "X":
                    color: str = YELLOW
                elif cell == "O":
                    color: str = BLUE
                else:
                    color: str = RESET
                print(color + str(cell) + RESET, end="")
                if j != 2:
                    print(" | ", end="")
            if i != 2:
                print("\n")
                print("----------", end="")
        print("\n")

    def place_marker(self, pos: int, marker: str) -> None:
        """Places the given marker in the given position in the board"""
        self.board[get_row_index(pos)][get_col_index(pos)] = marker

    def transponse_board(self) -> list[list[str]]:
        """Transposes the board"""
        arr: list[list[str]] = [[] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                arr[j].append(self.board[i][j])
        return arr

    def check_winner(self, players_tuple) -> PlayerManager | None:
        """Checks if there's a winner"""
        rows: list[list[str]] = [row for row in self.board]
        cols: list[list[str]] = [row for row in self.transponse_board()]
        diagnols: list[list[str]] = [
            [self.board[0][0], self.board[1][1], self.board[2][2]],
            [self.board[0][2], self.board[1][1], self.board[2][0]],
        ]
        for row in rows + cols + diagnols:
            array_str = "".join(pos for pos in row)
            if array_str == "XXX":
                return players_tuple[0]
            if array_str == "OOO":
                return players_tuple[1]
        return None
