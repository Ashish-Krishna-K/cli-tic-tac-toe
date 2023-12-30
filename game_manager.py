from random import randint
from player_manager import PlayerManager

class GameManager:
    player1: PlayerManager | None = None
    player2: PlayerManager | None = None


    def __init__(self) -> None:
        self.player1 = PlayerManager(player_name="Player 1", marker="X")
        self.played_tiles: set[str] = set[str]()
        self.winner: PlayerManager | None = None

    def get_opponent_pref(self) -> None:
        user_choice:str = ""
        while user_choice not in ["p", "c"]:
            user_choice = input("Do you want to play against another player or computer? (p/c) ").lower()
        if user_choice == "p":
            player_name = "Player 2"
        else:
            player_name = "Computer"
        self.player2 = PlayerManager(player_name, "O")
    
    def get_user_input(self) -> str:
        valid: bool = False
        pos: str = "0"
        while valid is not True:
            pos = input("Type the tile number to place your marker: ")
            if pos in self.played_tiles:
                print("That place is already marked, try a different tile!")
            elif not (49 <= ord(pos) <= 57):
                print("That's not a valid input please try again!")
            else:
                valid = True
        return pos
    
    def computer_plays(self) -> int:
        random_play:int = randint(1, 9)
        while str(random_play) in self.played_tiles:
            random_play = randint(1, 9)
        return random_play

    def get_players(self) -> tuple[PlayerManager, PlayerManager] | None:
        if self.player1 is None or self.player2 is None:
            return None
        return (self.player1, self.player2)
    
    def set_winner(self, new_winner) -> None:
        self.winner = new_winner

    def print_winner(self) -> None:
        if self.winner is None:
            print("It's a draw")
        else:
            print(f"Winner is {self.winner.name} ({self.winner.marker})")

