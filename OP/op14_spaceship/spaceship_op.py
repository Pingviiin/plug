from spaceship import Spaceship, Impostor, Crewmate

class OPSpaceship(Spaceship):
    """OPSpaceship class."""
    
    def __init__(self, difficulty: str):
        """Initialize OPSpaceship class."""
        super().__init__()
        
        if difficulty.lower() == "easy":
            self.difficulty = "easy"
        else:
            self.difficulty == "hard"
        
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
            self.check_is_game_over()
        
    def kill_crewmate(self, impostor: Impostor, color: str):
        if self.game and not self.meeting:
            super().kill_crewmate(impostor, color)
            self.check_is_game_over()
        
    def start_game(self):
        if (len(self.impostor_list) > 0) and (len(self.crewmate_list) > 1) and (len(self.crewmate_list) > len(self.impostor_list)) and not self.game:
            self.game = True
    
    def report_dead_body(self, reporting_player: Crewmate | Impostor, dead_body: Crewmate):
        if dead_body in self.dead_players and reporting_player in (self.crewmate_list + self.impostor_list):
            self.meeting = True
    
    def cast_vote(self, player: Crewmate | Impostor, target_player_color: str):
        if (player.color not in self.votes.keys()) and (player not in self.dead_players):
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
            return "No one was ejected. (Skipped)"

        most_voted_players = [key for key, value in counted_votes if value == max(counted_votes.values())]
        non_voters_amount = len(self.player_colors) - len(self.votes)

        if non_voters_amount > max(counted_votes.values()):
            self.meeting = False
            return "No one was ejected. (Skipped)"

        elif len(most_voted_players) > 1 or max(counted_votes.values()) == non_voters_amount:
            self.meeting = False
            return "No one was ejected. (Tie)"
        
        elif len(most_voted_players) == 1:
            voted = most_voted_players[0]
            self.ejected_players.append(voted)
            
            if self.check_is_game_over():
                winner = self.winner
                self.__init__()
                return winner
            
            if self.difficulty == "easy":

                if voted in [impostor.color for impostor in self.get_impostor_list()]:
                    if len(self.impostor_list) > 1:
                        return f"{voted} was an Impostor. {len(self.impostor_list)} Impostors remain."
                    elif len(self.impostor_list) == 1:
                        return f"{voted} was an Impostor. {len(self.impostor_list)} Impostor remains."
                
                if voted in [crewmate.color for crewmate in self.get_crewmate_list()]:
                    if len(self.impostor_list) > 1:
                        return f"{voted} was not an Impostor. {len(self.impostor_list)} Impostors remain."
                    elif len(self.impostor_list) == 1:
                        return f"{voted} was not an Impostor. {len(self.impostor_list)} Impostor remains."

            elif self.difficulty == "hard":
                return f"{voted} was ejected."
            
    def check_is_game_over(self):
        if len(self.impostor_list) == 0:
            self.winner = "Crewmates won."
            return True
        
        elif (len(self.impostor_list) == len(self.crewmate_list)) and (len(self.impostor_list) < 4) and (len(self.crewmate_list) < 4):
            self.winner = "Impostors won."
            return True
        
        else:
            return False
        
    def get_vote(self, color: str):
        for voter, candidate in self.votes:
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
    