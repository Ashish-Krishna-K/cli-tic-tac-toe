class PlayerManager:
    """A class to keep track of player name and marker"""

    def __init__(self, player_name: str, marker: str) -> None:
        self.name = player_name
        self.marker = marker
