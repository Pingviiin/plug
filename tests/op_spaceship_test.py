from OP.op14_spaceship.spaceship_op import *

def test_OP_spaceship_kill_impostor_game_ends():
    # Initialize the spaceship
    sc = OPSpaceship(difficulty="easy")
    
    # Create players
    crewmate1 = Crewmate("Red", "sheriff")
    crewmate2 = Crewmate("Blue", "crewmate")
    impostor1 = Impostor("Green")
    
    # Add players to the spaceship
    sc.add_crewmate(crewmate1)
    sc.add_crewmate(crewmate2)
    sc.add_impostor(impostor1)
    
    # Start the game
    sc.start_game()
    assert sc.game, "Game should be started."
    
    # Kill the impostor
    result = sc.kill_impostor(crewmate1, impostor1.color)
    
    # Check if the game ended and crewmates won
    assert result == "Crewmates won.", "Crewmates should win when the last impostor is killed."
    assert not sc.game, "Game should end when impostors are defeated."
    
    # Validate that impostor list is empty
    assert len(sc.impostor_list) == 0, "No impostors should remain."
