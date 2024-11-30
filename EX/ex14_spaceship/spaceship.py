class Crewmate:
    def __init__(self, color: str, role: str, tasks: int = 10):
        if color[0].isupper():
            self.color = color
        
        if role.lower() in ["crewmate", "sheriff", "guardian angel", "altruist"]:
            self.role = role.capitalize()

        self.tasks = tasks
        self.protected = False

    def __repr__(self):
        return f"{self.color}, role: {self.role}, tasks left: {self.tasks}."
    
    def complete_task(self):
        if self.tasks > 0:
            self.tasks -= 1


class Impostor:
    def __init__(self, color: str):
        if color[0].isupper():
            self.color = color

        self.kills = 0
    
    def __repr__(self):
        return f"Impostor {self.color}, kills: {self.kills}."


class Spaceship():
    def __init__(self):
        self.crewmate_list = []
        self.impostor_list = []
        self.dead_players = []
        self.player_colors = []

    def get_crewmate_list(self):
        return self.crewmate_list
    
    def get_impostor_list(self):
        return self.impostor_list
    
    def get_dead_players(self):
        return self.dead_players
    
    def add_crewmate(self, crewmate: Crewmate):
        if (crewmate not in self.impostor_list and self.dead_players) and (len(self.crewmate_list) < 4) and isinstance(crewmate, Crewmate) and crewmate.color not in self.player_colors:
            self.crewmate_list += [crewmate]
            self.player_colors += [crewmate.color]

    def add_crewmate(self, impostor: Impostor):
        if (impostor not in self.crewmate_list and self.dead_players) and (len(self.impostor_list) < 4) and isinstance(impostor, Impostor) and impostor.color not in self.player_colors:
            self.crewmate_list += [impostor]
            self.player_colors += [impostor.color]

    def kill_impostor(self, sheriff: Crewmate, color: str):
        impostor_colors = list(filter(self.impostor_list, lambda impostor: impostor.self.color))
        if color in impostor_colors:
            impostor_colors.index(color)


if __name__ == "__main__":
    print("Spaceship.")

    spaceship = Spaceship()
    print(spaceship.get_dead_players())  # -> []
    print()

    print("Let's add some crewmates.")
    red = Crewmate("Red", "Crewmate")
    white = Crewmate("White", "Impostor")
    yellow = Crewmate("Yellow", "Guardian Angel", tasks=5)
    green = Crewmate("green", "Altruist")
    blue = Crewmate("BLUE", "Sheriff", tasks=0)

    print(red)  # -> Red, role: Crewmate, tasks left: 10.
    print(white)  # -> White, role: Crewmate, tasks left: 10.
    print(yellow)  # -> Yellow, role: Guardian Angel, tasks left: 5.
    print(blue)  # -> Blue, role: Sheriff, tasks left: 0.
    print()

    print("Let's make Yellow complete a task.")
    yellow.complete_task()
    print(yellow)  # ->  Yellow, role: Guardian Angel, tasks left: 4.
    print()

    print("Adding crewmates to Spaceship:")
    spaceship.add_crewmate(red)
    spaceship.add_crewmate(white)
    spaceship.add_crewmate(yellow)
    spaceship.add_crewmate(green)
    print(spaceship.get_crewmate_list())  # -> [Red, role: Crewmate, tasks left: 10., White, role: Crewmate, tasks left: 10., Yellow, role: Guardian Angel, tasks left: 4., Green, role: Altruist, tasks left: 10.]

    spaceship.add_impostor(blue)  # Blue cannot be an Impostor.
    print(spaceship.get_impostor_list())  # -> []
    spaceship.add_crewmate(blue)
    print()

    print("Now let's add impostors.")
    orange = Impostor("orANge")
    black = Impostor("black")
    purple = Impostor("Purple")
    spaceship.add_impostor(orange)
    spaceship.add_impostor(black)

    spaceship.add_impostor(Impostor("Blue"))  # Blue player already exists in Spaceship.
    spaceship.add_impostor(purple)
    spaceship.add_impostor(Impostor("Pink"))  # No more than three impostors can be on Spaceship.
    print(spaceship.get_impostor_list())  # -> [Impostor Orange, kills: 0., Impostor Black, kills: 0., Impostor Purple, kills: 0.]
    print()

    print("The game has begun! Orange goes for the kill.")
    spaceship.kill_crewmate(orange, "yellow")
    print(orange)  # -> Impostor Orange, kills: 1.
    spaceship.kill_crewmate(black, "purple")  # You can't kill another Impostor, silly!
    print(spaceship.get_dead_players())  # -> [Yellow, role: Guardian Angel, tasks left: 4.]
    print()

    print("Yellow is a Guardian angel, and can protect their allies when dead.")
    spaceship.protect_crewmate(yellow, green)
    print(green.protected)  # -> True
    spaceship.kill_crewmate(orange, "green")
    print(green in spaceship.dead_players)  # -> False
    print(green.protected)  # -> False
    print()

    print("Green revives their ally.")
    spaceship.kill_crewmate(purple, "RED")
    spaceship.revive_crewmate(green, red)
    print(red in spaceship.dead_players)  # -> False
    print()

    print("Let's check if the sorting and filtering works correctly.")

    red.complete_task()
    print(spaceship.get_role_of_player("Blue"))  # -> Sheriff
    spaceship.kill_crewmate(purple, "blue")
    print(spaceship.sort_crewmates_by_tasks())  # -> [Red, role: Crewmate, tasks left: 9., White, role: Crewmate, tasks left: 10.]
    print(spaceship.sort_impostors_by_kills())  # -> [Impostor Purple, kills: 2., Impostor Orange, kills: 1., Impostor Black, kills: 0.]
    print(spaceship.get_regular_crewmates())  # -> [White, role: Crewmate, tasks left: 10., Red, role: Crewmate, tasks left: 9.]
