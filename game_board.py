import os


def get_row_index(number):
    if number % 3 == 0:
        return (number // 3) - 1
    else:
        return number // 3


def get_col_index(number):
    return (number - 1) % 3


class GameBoard:
    """A class to handle the gameboard"""

    def __init__(self):
        self.board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def print_board(self):
        """Prints the provided board to the console"""
        os.system("clear")
        for i, row in enumerate(self.board):
            print("\n")
            for j, cell in enumerate(row):
                if cell == "X":
                    color = "\033[93m"
                elif cell == "O":
                    color = "\033[94m"
                else:
                    color = "\033[0m"
                print(color + str(cell) + "\033[0m", end="")
                if j != 2:
                    print(" | ", end="")
            if i != 2:
                print("\n")
                print("----------", end="")
        print("\n")

    def place_marker(self, pos, marker):
        """Places the given marker in the given position in the given board"""
        self.board[get_row_index(pos)][get_col_index(pos)] = marker

    def transponse_board(self):
        """Transposes the board"""
        arr = [[] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                arr[j].append(self.board[i][j])
        return arr

    def check_winner(self):
        """Checks if there's a winner"""
        rows = [row for row in self.board]
        cols = [row for row in self.transponse_board()]
        diagnols = [
            [self.board[0][0], self.board[1][1], self.board[2][2]],
            [self.board[0][2], self.board[1][1], self.board[2][0]],
        ]
        for row in rows + cols + diagnols:
            array_str = "".join(str(pos) for pos in row)
            if array_str == "XXX":
                return "X"
            if array_str == "OOO":
                return "O"
        return "-"
