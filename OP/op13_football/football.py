"""Football OP."""


class Team:
    """Football Team class."""

    def __init__(self, name: str, attack: int, defence: int):
        """
        Initialize Team object. Team should have score count, which is initially 0.

        :param name: team's name.
        :param attack: team's attack value.
        :param defence: team's defence value.
        """""
        self.name = name
        self.attack = attack
        self.defence = defence
        self.score = 0

    def train(self) -> None:
        """
        Train the team.

        +1 to defence
        +1 to attack
        :return: None.
        """
        self.attack += 1
        self.defence += 1
        return

    def get_score(self) -> int:
        """
        Return team's score.

        :return: score.
        """
        return self.score

    def set_score(self, score: int):
        """
        Set score.

        :param score: score value.

        :return: None.
        """
        self.score = score
        return

    def get_attack(self) -> int:
        """
        Return attack value.

        :return: attack value.
        """
        return self.attack

    def get_defence(self) -> int:
        """
        Return defence value.

        :return: defence value.
        """
        return self.defence

    def get_name(self) -> str:
        """
        Get team's name.

        :return: team's name.
        """
        return self.name

    def __repr__(self):
        """Format the string of the team as: '[name]'."""
        return f"{self.name}"


class League:
    """Football League class."""

    def __init__(self, name: str, teams: list):
        """
        Initialize League object.

        :param name: league name.
        :param teams: list of teams in league.
        """
        self.name = name
        self.teams = teams
        self.scoreboard = {}

        for team in self.teams:
            self.scoreboard[team] = 0

    def add_team(self, team: Team) -> None:
        """
        Add team to league.

        A league can contain a maximum of 10 teams.
        If team gets added then it must also show up on the scoreboard.

        :param team: Team object.
        """
        if len(self.teams) < 10:
            self.teams.append(team)
            self.scoreboard[team] = 0

    def remove_team(self, team_name: str) -> None:
        """
        Remove team from league by name.

        Team should also be removed from scoreboard.

        :param team_name: Name of team to remove from league.
        """
        removed_team = None

        for team in self.teams:
            if team.name == team_name:
                removed_team = team
                break

        if removed_team is None:
            return

        self.teams.remove(removed_team)
        self.scoreboard.pop(removed_team)

    def play_games(self) -> None:
        """
        Each team should play against other team once.

        Create Game object and get the winner.
        Winner gets +1 point to league scoreboard.
        :return: None.
        """
        for i in range(len(self.teams)):
            for n in range(i + 1, len(self.teams)):
                team1 = self.teams[i]
                team2 = self.teams[n]

                game = Game(team1, team2)

                winner = game.play()

                self.scoreboard[winner] = winner.score

    def get_first_place(self) -> Team:
        """
        Get first place in the league.

        :return: team on the first place in scoreboard.
        """
        return max(self.scoreboard, key=lambda x: self.scoreboard[x])

    def get_last_place(self) -> Team:
        """
        Get last place in the league.

        :return: team on the last place in scoreboard.
        """
        return min(self.scoreboard, key=lambda x: self.scoreboard[x])

    def clear_scoreboard(self):
        """
        Clear scoreboard (for the new season).

        :return: None.
        """
        for team in self.teams:
            team.set_score(0)
        for team in self.scoreboard:
            self.scoreboard[team] = 0

    def get_name(self) -> str:
        """Return league name."""
        return self.name

    def get_teams(self) -> list:
        """Get all teams in league."""
        return self.teams

    def get_scoreboard(self) -> dict:
        """Return league scoreboard."""
        return self.scoreboard

    def __repr__(self):
        """Format the string of the league as: '[name]'."""
        return f"{self.name}"


class Game:
    """Football Game class."""

    def __init__(self, team1: Team, team2: Team):
        """Initialize Game object.

        :param team1: first team in the game.
        :param team2: second team in the game.
        """
        self.team1 = team1
        self.team2 = team2

        self.team1_points = 0
        self.team2_points = 0

    def play(self) -> object:
        """
        Simulate a game.

        The "play" function simulates a game between two teams, where each team earns points based on their attack and defence scores.
        If the scores are tied, the sum of each team's attack and defence points is considered.
        If this still does not resolve the tie, the team whose name comes first alphabetically wins.

        - The function starts by setting the points for both teams: `team1_points` and `team2_points`,
        both initialized to zero.
        - The first part checks which team has the higher attack score and awards a point to that team. If the attack
        scores are equal, it moves on to compare the defence scores.
        - Next, the teams' defence scores are compared. The team with the higher defence score is awarded a point.
        - If both teams are tied in points (e.g., 0-0 or 1-1), the sum of each team's attack and defence scores
        is calculated.
        - The team with the higher total score wins.
        - If the teams' total scores are still tied, the teams are sorted alphabetically by their names. The team that
        comes first alphabetically wins.
        - Once a winner is determined, the winner's score is updated (+1).
        - The function returns the winning team's object.

        :return: winner team object.
        """
        if self.validate_teams():
            return self.team1

        self.calculate_points()

        if self.team1_points == self.team2_points:
            winner = self.tiebreaker()

        if self.team1_points < self.team2_points:
            winner = self.team2

        elif self.team2_points < self.team1_points:
            winner = self.team1

        winner.score += 1

        return winner

    def validate_teams(self):
        """Validate teams."""
        if not self.team1.name or not self.team2.name:
            return True
        if self.team1.name == self.team2.name:
            return True

    def tiebreaker(self):
        """Break a tie."""
        if self.team1.attack + self.team1.defence < self.team2.attack + self.team2.defence:
            winner = self.team2
        elif self.team2.attack + self.team2.defence < self.team1.attack + self.team1.defence:
            winner = self.team1
        else:
            if self.team1.name < self.team2.name:
                winner = self.team1
            else:
                winner = self.team2
        return winner

    def calculate_points(self):
        """Calculate points."""
        if self.team1.attack < self.team2.attack:
            self.team2_points += 1

        elif self.team2.attack < self.team1.attack:
            self.team1_points += 1

        if self.team1.defence < self.team2.defence:
            self.team2_points += 1

        elif self.team2.defence < self.team1.defence:
            self.team1_points += 1

    def __repr__(self):
        """Format the string of the game as: '[team1] vs. [team2]'."""
        return f"{self.team1} vs. {self.team2}"
