from spaceship import Spaceship, Impostor, Crewmate


class OPSpaceship(Spaceship):
    """OPSpaceship class."""

    def __init__(self, difficulty: str):
        """Initialize OPSpaceship class."""
        super().__init__()

        if difficulty.lower() == "easy":
            self.difficulty = "easy"
        else:
            self.difficulty = "hard"

        self.ejected_players = []
        self.meeting = False
        self.votes = {}
        self.game = False
        self.reporting_player = ""
        self.winner = ""

    def add_crewmate(self, crewmate: Crewmate):
        if not self.game:
            return super().add_crewmate(crewmate)

    def add_impostor(self, impostor: Impostor):
        if not self.game:
            return super().add_impostor(impostor)

    def kill_impostor(self, sheriff: Crewmate, color: str):
        if self.game and not self.meeting:
            super().kill_impostor(sheriff, color)
            if self.check_is_game_over():
                self.reset()
                return 'Crewmates won.'

    def kill_crewmate(self, impostor: Impostor, color: str):
        if self.game and not self.meeting:
            super().kill_crewmate(impostor, color)
            if self.check_is_game_over():
                self.reset()
                return 'Impostors won.'

    def start_game(self):
        if (len(self.impostor_list) > 0) and (len(self.crewmate_list) > 1) and (len(self.crewmate_list) > len(self.impostor_list)) and not self.game:
            self.game = True

    def report_dead_body(self, reporting_player: Crewmate | Impostor, dead_body: Crewmate):
        if dead_body in self.dead_players and reporting_player in (self.crewmate_list + self.impostor_list):
            self.meeting = True

    def cast_vote(self, player: Crewmate | Impostor, target_player_color: str):
        if (player.color not in self.votes.keys()) and (player not in self.dead_players) and self.game:
            if self.meeting and target_player_color.title() in self.player_colors:
                self.votes[player.color] = target_player_color.title()

    def count_votes(self):
        counted_votes = {}
        for candidate in self.votes.values():
            if candidate in counted_votes:
                counted_votes[candidate] += 1
            else:
                counted_votes[candidate] = 1

        return counted_votes

    def end_meeting(self):
        if not self.meeting:
            return

        counted_votes = self.count_votes()

        if not counted_votes:
            self.reset_meeting()
            return "No one was ejected. (Skipped)"
        
        max_votes = max(counted_votes.values())
        most_voted_players = [key for key, value in counted_votes.items() if value == max(counted_votes.values())]
        abstainers = len(self.player_colors) - sum(counted_votes.values())

        if (abstainers == len(self.player_colors)) or (abstainers > max_votes):
            self.reset_meeting()
            return "No one was ejected. (Skipped)"

        if (len(most_voted_players) > 1) or (abstainers == max_votes):
            self.reset_meeting()
            return "No one was ejected. (Tie)"

        ejected = most_voted_players[0]
        self.ejected_players.append(ejected)

        was_impostor = any(player.color == ejected for player in self.impostor_list)
        if was_impostor:
            self.impostor_list = [player for player in self.impostor_list if player.color != ejected]
        else:
            self.crewmate_list = [player for player in self.crewmate_list if player.color != ejected]

        if self.check_is_game_over():
            winner = self.winner
            self.reset()
            return winner

        self.reset_meeting()
        if self.difficulty == "easy":
            impostor_count = len(self.impostor_list)
            if was_impostor:
                return f"{ejected} was an Impostor. {impostor_count} Impostor{'s' if impostor_count != 1 else ''} remain."
            else:
                return f"{ejected} was not an Impostor. {impostor_count} Impostor{'s' if impostor_count != 1 else ''} remain."
        else:
            return f"{ejected} was ejected."

    def reset_meeting(self):
        self.dead_players.clear()
        self.votes.clear()
        self.meeting = False

    def check_is_game_over(self):
        if len(self.impostor_list) == 0:
            self.winner = "Crewmates won."
            self.dead_players.clear()
            self.votes.clear()
            self.meeting = False
            return True

        elif (len(self.impostor_list) == len(self.crewmate_list)) and (len(self.impostor_list) < 4) and (len(self.crewmate_list) < 4):
            self.winner = "Impostors won."
            self.dead_players.clear()
            self.votes.clear()
            self.meeting = False
            return True

        else:
            return False

    def get_vote(self, color: str):
        for voter, candidate in self.votes.items():
            if voter.lower() == color.lower():
                return candidate
        else:
            return "No vote found"

    def get_ejected_players(self):
        return self.ejected_players

    def get_votes(self):
        return self.votes

    def is_meeting(self):
        return self.meeting
    
    def reset(self):
        self.ejected_players = []
        self.meeting = False
        self.votes = {}
        self.game = False
        self.reporting_player = ""
        self.winner = ""

        self.crewmate_list = []
        self.impostor_list = []
        self.dead_players = []
        self.player_colors = []
        self.crewmate_protected = False
    
def test_OP_spaceship_end_meeting_highest_votes_equals_skipped():
    # Initialize the spaceship
    spaceship = OPSpaceship(difficulty="easy")
    
    # Create players
    crewmate1 = Crewmate("Red")
    crewmate2 = Crewmate("Blue")
    impostor1 = Impostor("Green")
    
    # Add players to the spaceship
    spaceship.add_crewmate(crewmate1)
    spaceship.add_crewmate(crewmate2)
    spaceship.add_impostor(impostor1)
    
    # Start the game
    spaceship.start_game()
    assert spaceship.game, "Game should be started."
    
    # Simulate a meeting and voting
    spaceship.meeting = True
    spaceship.cast_vote(crewmate1, "Skip")  # Skip vote
    spaceship.cast_vote(crewmate2, "Green")  # Vote for impostor
    spaceship.cast_vote(impostor1, "Skip")  # Skip vote
    
    # End the meeting and check the result
    result = spaceship.end_meeting()
    assert result == "No one was ejected. (Skipped)", f"Unexpected result: {result}"
