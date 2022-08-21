class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if self.name == player.guild:
            return f"Player {player.name} is already in the guild."
        if player.guild != player.DEFAULT_GUILD:
            return f"Player {player.name} is in another guild."
        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name):
        if player_name not in self.players:
            return f"Player {player_name} is not in the guild."
        for player in self.players:
            if player.name == player_name:
                player.guild = player.DEFAULT_GUILD
                self.players.remove(player)

        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        result = f"Guild: {self.name}"
        for player in self.players:
            result += "\n" + f"{player.player_info()}"
        return result

