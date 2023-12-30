from time import sleep

from game_board import GameBoard
from game_manager import GameManager
from player_manager import PlayerManager

manager: GameManager = GameManager()
game_board: GameBoard = GameBoard()


players: tuple[PlayerManager, PlayerManager] | None = manager.get_players()

while players is None:
    manager.get_opponent_pref()
    players = manager.get_players()

game_loop: int = 0
while manager.winner is None and game_loop < 9:
    game_board.print_board()
    print(
        f"{players[0].name}'s marker is '{players[0].marker}'; {players[1].name}'s marker is '{players[1].marker}'"
    )

    current_player: PlayerManager = players[game_loop % 2]

    print(f"{current_player.name} ({current_player.marker})'s turn...")

    current_play: str = ""
    if current_player.name == "Computer":
        sleep(1)
        current_play = str(manager.computer_plays())
    else:
        current_play = manager.get_user_input()

    manager.add_played_tile(current_play)

    game_board.place_marker(pos=int(current_play), marker=current_player.marker)

    round_winner: PlayerManager | None = game_board.check_winner(players_tuple=players)
    manager.set_winner(new_winner=round_winner)
    game_loop += 1

game_board.print_board()
manager.print_winner()
