class User:
    username: str = ''
    password: str = ''
    is_waiting_for_game: bool = False

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
