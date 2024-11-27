"""Football."""
import random

class Player:
    """Player class."""

    def __init__(self, name: str, player_number: int):
        """
        Initialize player class.

        :param name: The name of the player.
        :param player_number: The number of the player.
        """
        self.name = name
        self.player_number = player_number
        self.goals = 0
        self.red_cards = 0

    def __repr__(self) -> str:
        """
        Represent player.

        Format the string of the player as:
        '[name] ([player_number])'

        :return: The string representation of the player.
        """
        return f"{self.name} ({self.player_number})"

    def get_player_name(self) -> str:
        """
        Get player name.

        :return: The player name.
        """
        return self.name

    def get_player_number(self) -> int:
        """
        Get player number.

        :return: The player number.
        """
        return self.player_number

    def get_goals_scored(self) -> int:
        """
        Get amount of goals scored by player.

        :return: The goals scored.
        """
        return self.goals

    def get_red_cards(self) -> int:
        """
        Get amount of red cards given to player.

        :return: Amount of red cards.
        """
        return self.red_cards



class Team:
    """Team class."""

    def __init__(self, name: str):
        """
        Initialize team.

        Each team should have a name and can have up to 11 players.

        :param name: The name of the team.
        """
        self.name = name
        self.players = []

    def __repr__(self) -> str:
        """
        Represent team.

        Format the string of the team as:
        '[name]'

        :return: The string representation of the team.
        """
        return f"{self.name}"

    def is_full(self) -> bool:
        """
        Check if team is full.

        :return: The method should return True if the team is full, else False.
        """
        return len(self.players) >= 11

    def add_player(self, player: Player) -> bool:
        """
        Add a player to the team.

        A player can only be added if the team has less than 11 players.
        The same player cannot be added twice.
        The method should return True if the player was added, else False.

        :param player: The player to add.
        :return: True if the player was added, else False.
        """
        if player not in self.players:
            self.players += [player]
            return True
        else:
            return False

    def remove_player(self, player: Player) -> bool:
        """
        Remove a player from the team.

        The method should return True if the player was removed, else False.

        :param player: The player to remove.
        :return: True if the player was removed, else False.
        """
        if player in self.players:
            self.players.remove(player)
            return True
        else:
            return False

    def get_team_name(self) -> str:
        """
        Get team name.

        :return: The team name.
        """
        return self.name

    def get_player_by_number(self, player_number: int) -> Player | None:
        """
        Get player with matching player number.

        :param player_number: The player number to check for.
        :return: Player object if found, None if not found.
        """
        for player in self.players:
            if player.player_number == player_number:
                return player

    def get_players(self) -> list[Player]:
        """
        Return a list with all the players in the team.

        :return: Team players as a list.
        """
        return self.players

    def get_players_sorted(self) -> list[Player]:
        """
        Return a sorted list with all the players in the team.

        The sorting order goes like this:
        1. Most goals scored
        2. Least red cards gotten
        If both parameters are equal, then order randomly.

        :return: Team players as a sorted list.
        """
        random.shuffle(self.players)
        return sorted(self.players, key=lambda x: (-x.goals, x.red_cards))


class Match:
    """Match class."""

    def __init__(self, team1: Team, team2: Team):
        """
        Initialize match.

        A match consists of two teams and a score for each team.

        :param team1: The first team.
        :param team2: The second team.
        """
        self.team1 = team1
        self.team2 = team2
        self.team1_score = 0
        self.team2_score = 0

    def player_scored(self, team: Team, player: Player) -> bool:
        """
        Increment score and keep records of the goalscorer.

        The method should return True if the score was set, else False.

        :param team: The team of the player who scored.
        :param player: The player who scored.
        :return: True if the score was set, else False.
        """
        if team == self.team1 or team == self.team2:

            if team == self.team1:

                if player in self.team1.get_players() and not self.has_red_card(player):
                    self.team1_score += 1

                else:
                    return False

            elif team == self.team2:

                if player in self.team2.get_players() and not self.has_red_card(player):
                    self.team2_score += 1

                else:
                    return False            

            player.goals += 1
            return True

        return False

    def give_red_card(self, player: Player) -> bool:
        """
        Give a red card to a player.

        The player should be prevented from scoring for the rest of the game.
        The method should return True if the red card was given, else False.

        :param player: The player to give the red card to.
        :return: True if the red card was given, else False.
        """
        if player in self.team1.get_players() or player in self.team2.get_players():
            player.red_cards += 1
            return True
        else:
            return False

    def get_score(self, team: Team) -> int:
        """
        Return the score of the given team.

        :param team: The team whose score to return.
        :return: The score of the given team.
        """
        if team == self.team1:
            return self.team1_score
        
        if team == self.team2:
            return self.team2_score

    def get_winner(self) -> Team | None:
        """
        Get the winner of the match.

        Return the team with the higher score.
        If the scores are tied, return None.

        :return: The team with the higher score, or None if tied.
        """
        if self.team1_score < self.team2_score:
            return self.team2
        elif self.team2_score < self.team1_score:
            return self.team1

    def get_top_goalscorer(self) -> Player:
        """
        Get the player with most scored goals in the given game.

        Return the player with the most scored goals.

        :return: The player with the most scored goals.
        """
        players = self.team1.get_players() + self.team2.get_players()
        
        return max(players, key=lambda player: player.get_goals_scored())

    def has_red_card(self, player: Player) -> bool:
        """
        Check if a player has received a red card.

        :param player: The player to check.
        :return: True if the player has a red card, False otherwise.
        """
        return player.red_cards > 0

    def get_red_carded_players(self) -> list[Player]:
        """
        Get the list of players who received red cards.

        :return: List of players with red cards.
        """
        naughty_players = []
        team_players = self.team1.get_players() + self.team2.get_players()
        for player in team_players:
            if self.has_red_card(player):
                naughty_players += [player]
        return naughty_players


if __name__ == "__main__":
    """Main for testing the functions."""
    # Initialize teams
    team1 = Team("Team A")
    team2 = Team("Team B")
    print(team1)  # Team A
    print(team2)  # Team B
    print()

    # Initialize players
    player1 = Player("Alice", 1)
    player2 = Player("Bob", 2)
    player3 = Player("Charlie", 3)
    print(player1)  # Alice (1)
    print(player3)  # Charlie (3)
    print()

    # Add players to teams
    print(team1.add_player(player1))  # True
    print(team1.add_player(player1))  # False (no duplicates allowed)
    print(team1.add_player(player2))  # True
    print(team2.add_player(player3))  # True
    print()

    # Check players in teams
    print(player1 in team1.get_players())  # True
    print(player3 in team1.get_players())  # False
    print(team1.get_players())  # [Alice (1), Bob (2)]
    print()

    # Initialize match
    match = Match(team1, team2)

    print(match.player_scored(team1, player1))  # True
    print(match.player_scored(team2, player1))  # False (wrong team)
    print(match.get_score(team1))  # 1
    print(match.get_score(team2))  # 0
    print(match.get_winner())  # Team A
