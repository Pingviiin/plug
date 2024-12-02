from EX.ex13_football.football import *


def test_get_player_number():
    player = Player("John Doe", 1)
    assert player.get_player_number() == 1


def test_add_player():
    team = Team("Team A")
    player = Player("John Doe", 1)
    assert team.add_player(player) is True
    assert team.add_player(player) is False


def test_get_players_sorted():
    team = Team("Team A")
    match = Match(team, Team("Dummy Team"))
    player1 = Player("John Doe", 1)
    player2 = Player("Jane Doe", 2)
    team.add_player(player1)
    team.add_player(player2)

    match.player_scored(team, player1)
    assert team.get_players_sorted() == [player1, player2]


def test_get_player_name():
    player1 = Player("Johnson", 54)
    player2 = Player("Bob", 3)

    assert player1.get_player_name() == "Johnson"
    assert player2.get_player_name() == "Bob"


def test_remove_player():
    team = Team("Team A")
    player1 = Player("Tyrone", 2)
    player2 = Player("Big dog", 15)
    player3 = Player("Johannes", 5)
    team.add_player(player1)
    team.add_player(player2)

    team.remove_player(player1)
    assert team.remove_player(player3) == False
    assert team.get_players() == [player2]
    assert team.get_players() != [player1]


def test_get_team_name():
    team = Team("Banaanid")
    assert team.get_team_name() == "Banaanid"


def test_get_player_by_number():
    team = Team("Team Toomas")
    player1 = Player("Toomas", 5)
    player2 = Player("Peeter", 4)
    player3 = Player("Artur", 1)

    team.add_player(player1)
    team.add_player(player2)
    team.add_player(player3)

    assert team.get_player_by_number(5) == player1


def test_player_repr():
    player1 = Player("Bob", 5)
    assert repr(player1) == "Bob (5)"


def test_get_goals_scored():
    team1 = Team("Nacho")
    team2 = Team("Kebab")
    match = Match(team1, team2)
    player1 = Player("Andrus", 1)

    team1.add_player(player1)
    match.player_scored(team1, player1)

    assert player1.get_goals_scored() == 1


def test_get_red_cards():
    team1 = Team("Nacho")
    team2 = Team("Kebab")
    match = Match(team1, team2)
    player1 = Player("Andrus", 1)

    team1.add_player(player1)
    match.give_red_card(player1)

    assert player1.get_red_cards() == 1


def test_repr_team():
    team1 = Team("Summer")
    assert repr(team1) == "Summer"


def test_is_full():
    team1 = Team("Scream")
    player1 = Player("Bob1", 1)
    team1.add_player(player1)
    assert team1.is_full() == False

    for i in range(2, 13):
        player = Player(f"Player{i}", i)
        team1.add_player(player)
    assert team1.is_full() == True


def test_player_scored_player_has_red_card():
    team1 = Team("Memories")
    team2 = Team("Dreams")
    match = Match(team1, team2)
    player1 = Player("David", 22)
    player2 = Player("Pitbull", 14)

    team1.add_player(player1)
    match.give_red_card(player1)

    assert match.player_scored(team1, player1) == False

    team2.add_player(player2)
    match.give_red_card(player2)

    assert match.player_scored(team2, player2) == False


def test_player_scored_player_has_no_team():
    team1 = Team("Memories")
    team2 = Team("Dreams")
    team3 = Team("Fake")
    match = Match(team1, team2)
    player1 = Player("David", 22)

    team3.add_player(player1)

    assert match.player_scored(team3, player1) == False


def test_player_scored():
    team1 = Team("Memories")
    team2 = Team("Dreams")
    match = Match(team1, team2)
    player1 = Player("David", 22)
    player2 = Player("Pitbull", 14)

    team1.add_player(player1)
    team2.add_player(player2)

    assert match.player_scored(team1, player1) == True

    assert match.player_scored(team2, player2) == True


def test_give_red_card_player_not_in_team():
    team1 = Team("Memories")
    team2 = Team("Dreams")
    match = Match(team1, team2)
    player1 = Player("David", 22)
    player2 = Player("Pitbull", 14)

    assert match.give_red_card(player1) == False
    assert match.give_red_card(player2) == False


def test_give_red_card_player_already_has_red_card():
    team1 = Team("Memories")
    team2 = Team("Dreams")
    match = Match(team1, team2)
    player1 = Player("David", 22)
    player2 = Player("Pitbull", 14)

    match.give_red_card(player1)
    match.give_red_card(player2)

    assert match.give_red_card(player1) == False
    assert match.give_red_card(player2) == False


def test_get_score():
    team1 = Team("Memories")
    team2 = Team("Dreams")
    match = Match(team1, team2)
    player1 = Player("David", 22)
    player2 = Player("Pitbull", 14)

    team1.add_player(player1)
    team2.add_player(player2)
    match.player_scored(team1, player1)
    match.player_scored(team2, player2)

    assert match.get_score(team1) == 1
    assert match.get_score(team2) == 1


def test_get_winner():
    team1 = Team("Memories")
    team2 = Team("Dreams")
    match = Match(team1, team2)
    player1 = Player("David", 22)
    player2 = Player("Pitbull", 14)

    team1.add_player(player1)
    team2.add_player(player2)
    match.player_scored(team1, player1)
    for i in range(4):
        match.player_scored(team2, player2)

    assert match.get_winner() == team2

    for i in range(6):
        match.player_scored(team1, player1)

    assert match.get_winner() == team1


def test_get_winner_tie():
    team1 = Team("Memories")
    team2 = Team("Dreams")
    match = Match(team1, team2)
    player1 = Player("David", 22)
    player2 = Player("Pitbull", 14)

    team1.add_player(player1)
    team2.add_player(player2)
    match.player_scored(team1, player1)
    match.player_scored(team2, player2)

    assert match.get_winner() == None


def test_get_top_goalscorer():
    team1 = Team("Memories")
    team2 = Team("Dreams")
    match = Match(team1, team2)
    player1 = Player("David", 22)
    player2 = Player("Pitbull", 14)

    team1.add_player(player1)
    team2.add_player(player2)
    match.player_scored(team1, player1)
    for i in range(4):
        match.player_scored(team2, player2)

    for i in range(6):
        match.player_scored(team1, player1)

    assert match.get_top_goalscorer() == player1


def test_get_red_carded_players():
    team1 = Team("Memories")
    team2 = Team("Dreams")
    match = Match(team1, team2)
    player1 = Player("David", 22)
    player2 = Player("Pitbull", 14)

    team1.add_player(player1)
    team2.add_player(player2)

    match.give_red_card(player1)
    match.give_red_card(player2)

    assert match.get_red_carded_players() == [player1, player2]
