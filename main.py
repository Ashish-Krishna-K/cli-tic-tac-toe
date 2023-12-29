from game_board import GameBoard

def get_user_input(played_tiles):
    valid = False
    x = "0"
    while valid is not True:
        x = input("Type the tile number to place your marker: ")
        if x in played_tiles:
            print("That place is already marked, try a different tile!")
        elif not (49 <= ord(x) <= 57):
            print("That's not a valid input please try again!")
        else:
            valid = True
    return x  


played_set = set()
winner = "-"
game_loop = 0
game_board = GameBoard()
while winner == "-" and game_loop < 9:
    game_board.print_board()
    marker_to_place = "X" if game_loop % 2 == 0 else "O"
    user_input = get_user_input(played_set)
    played_set.add(user_input)
    game_board.place_marker(int(user_input), marker_to_place)

    winner = game_board.check_winner()
    game_loop += 1

game_board.print_board()
print(f"Winner is {winner}")

