"""Spaceship."""


class Crewmate:
    """Crewmate class."""

    def __init__(self, color: str, role: str, tasks: int = 10):
        """Initialize crewmate class.

        Args:
            color (str): Color of the crewmate.
            role (str): Role of the player.
            tasks (int, optional): Amount of tasks left to complete. Defaults to 10.
        """
        self.color = color.title()
        self.tasks = tasks
        self.protected = False

        if role.lower() in ["crewmate", "sheriff", "guardian angel", "altruist"]:
            self.role = role.title()
        else:
            self.role = "Crewmate"

    def __repr__(self):
        """Represent crewmate.

        Returns:
            str: The string representation of the crewmate.
        """
        return f"{self.color}, role: {self.role}, tasks left: {self.tasks}."

    def complete_task(self):
        """Complete a task.
        """
        if self.tasks > 0:
            self.tasks -= 1


class Impostor:
    """Impostor class."""

    def __init__(self, color: str):
        """Initialize the impostor class.

        Args:
            color (str): Color of the impostor.
        """
        self.color = color.title()

        self.kills = 0

    def __repr__(self):
        """Represent impostor.

        Returns:
            str: The string representation of the impostor.
        """
        return f"Impostor {self.color}, kills: {self.kills}."


class Spaceship:
    """Spaceship class."""

    def __init__(self):
        """Initialize spaceship class.
        """
        self.crewmate_list = []
        self.impostor_list = []
        self.dead_players = []
        self.player_colors = []
        self.crewmate_protected = False

    def get_crewmate_list(self):
        """Get crewmate list.

        Returns:
            list: List of crewmates.
        """
        return self.crewmate_list

    def get_impostor_list(self):
        """Get impostor list.

        Returns:
            list: List of impostors.
        """
        return self.impostor_list

    def get_dead_players(self):
        """Get dead players.

        Returns:
            list: List of dead players.
        """
        return self.dead_players

    def add_crewmate(self, crewmate: Crewmate):
        """Add crewmate to game.

        Args:
            crewmate (Crewmate): The crewmate to add.
        """
        if (crewmate not in (self.impostor_list and self.dead_players)):
            if isinstance(crewmate, Crewmate):
                if crewmate.color not in self.player_colors:
                    self.crewmate_list += [crewmate]
                    self.player_colors += [crewmate.color]

    def add_impostor(self, impostor: Impostor):
        """Add impostor to game.

        Args:
            impostor (Impostor): The impostor to add.
        """
        if (impostor not in (self.crewmate_list and self.dead_players)):
            if (len(self.impostor_list) <= 2):
                if isinstance(impostor, Impostor):
                    if impostor.color not in self.player_colors:
                        self.impostor_list += [impostor]
                        self.player_colors += [impostor.color]

    def kill_impostor(self, sheriff: Crewmate, color: str):
        """Kill an impostor.

        If the picked color was not an impostor, kill the sheriff.

        Args:
            sheriff (Crewmate): A crewmate.
            color (str): Color of the player to kill.
        """
        color = color.title()

        if (sheriff in self.crewmate_list) and (sheriff.role == "Sheriff"):
            for impostor in self.impostor_list:
                if impostor.color == color:
                    self.impostor_list.remove(impostor)
                    self.dead_players.append(impostor)
                    return

            for crewmate in self.crewmate_list:
                if crewmate.color == color:
                    self.crewmate_list.remove(sheriff)
                    self.dead_players.append(sheriff)
                    return

    def revive_crewmate(self, altruist: Crewmate, dead_crewmate: Crewmate):
        """Revive a teammate.

        The altruist can sacrifice his life to revive a dead crewmate.

        Args:
            altruist (Crewmate): Crewmate who should have the altruist role.
            dead_crewmate (Crewmate): Crewmate who should be dead.
        """
        if (altruist.role == "Altruist") and (dead_crewmate in self.dead_players) and (altruist in self.crewmate_list):
            self.crewmate_list.remove(altruist)
            self.dead_players.append(altruist)

            self.dead_players.remove(dead_crewmate)
            self.crewmate_list.append(dead_crewmate)

    def protect_crewmate(self, guardian_angel: Crewmate, crewmate_to_protect: Crewmate):
        """Protect a crewmate.

        If a guardian angel is dead, they can revive a crewmate.
        Only one crewmate can be protected at a time.

        Args:
            guardian_angel (Crewmate): Crewmate who should have the guardian angel role and be dead.
            crewmate_to_protect (Crewmate): Crewmate who should be alive.
        """
        if guardian_angel.role == "Guardian Angel":
            if guardian_angel in self.dead_players:
                if not self.crewmate_protected:
                    for crewmate in self.crewmate_list:
                        if (crewmate == crewmate_to_protect) and (not crewmate.protected):
                            crewmate_to_protect.protected = True
                            self.crewmate_protected = True
                            return

    def kill_crewmate(self, impostor: Impostor, color: str):
        """Kill a crewmate.

        If the crewmate is protected by a guardian angel, remove the protection.

        Args:
            impostor (Impostor): Impostor who should be alive.
            color (str): Color of the player to kill.
        """
        color = color.title()

        if (color in self.player_colors) and (impostor in self.impostor_list):
            for crewmate in self.crewmate_list:
                if crewmate.color == color.capitalize():
                    if crewmate.protected:
                        crewmate.protected = False
                        self.crewmate_protected = False
                        break
                    else:
                        self.crewmate_list.remove(crewmate)
                        self.dead_players.append(crewmate)
                        impostor.kills += 1
                        break

    def sort_crewmates_by_tasks(self):
        """Sort crewmates by tasks in an ascending order.

        Returns:
            list: List of crewmates.
        """
        return sorted(self.crewmate_list, key=lambda crewmate: crewmate.tasks)

    def sort_impostors_by_kills(self):
        """Sort impostors by kills in an descending order.

        Returns:
            list: List of impostors.
        """
        return sorted(self.impostor_list, key=lambda impostor: impostor.kills, reverse=True)

    def get_regular_crewmates(self):
        """Get regular crewmates.

        Returns:
            list: List of regular crewmates.
        """
        return list(filter(lambda crewmate: crewmate.role == "Crewmate", self.crewmate_list))

    def get_role_of_player(self, color: str):
        """Get role of player of the given color.

        Args:
            color (str): Color of the player.

        Returns:
            str: Role of the player.
        """
        color = color.title()
        players = self.crewmate_list + self.impostor_list + self.dead_players

        for player in players:
            if isinstance(player, Impostor) and player.color == color:
                return "Impostor"

            elif player.color == color:
                return player.role

    def get_crewmate_with_most_tasks_done(self):
        """Get the crewmate with the most tasks done.

        Returns:
            Crewmate: Crewmate object.
        """
        return min(self.crewmate_list, key=lambda crewmate: crewmate.tasks)

    def get_impostor_with_most_kills(self):
        """Get the impostor with the most kills.

        Returns:
            Impostor: Impostor object.
        """
        return max(self.impostor_list, key=lambda impostor: impostor.kills)


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
    # -> [Red, role: Crewmate, tasks left: 10., White, role: Crewmate, tasks left: 10., Yellow, role: Guardian Angel, tasks left: 4., Green, role: Altruist, tasks left: 10.]
    print(spaceship.get_crewmate_list())

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

    # Blue player already exists in Spaceship.
    spaceship.add_impostor(Impostor("Blue"))
    spaceship.add_impostor(purple)
    # No more than three impostors can be on Spaceship.
    spaceship.add_impostor(Impostor("Pink"))
    # -> [Impostor Orange, kills: 0., Impostor Black, kills: 0., Impostor Purple, kills: 0.]
    print(spaceship.get_impostor_list())
    print()

    print("The game has begun! Orange goes for the kill.")
    spaceship.kill_crewmate(orange, "yellow")
    print(orange)  # -> Impostor Orange, kills: 1.
    # You can't kill another Impostor, silly!
    spaceship.kill_crewmate(black, "purple")
    # -> [Yellow, role: Guardian Angel, tasks left: 4.]
    print(spaceship.get_dead_players())
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
    # -> [Red, role: Crewmate, tasks left: 9., White, role: Crewmate, tasks left: 10.]
    print(spaceship.sort_crewmates_by_tasks())
    # -> [Impostor Purple, kills: 2., Impostor Orange, kills: 1., Impostor Black, kills: 0.]
    print(spaceship.sort_impostors_by_kills())
    # -> [White, role: Crewmate, tasks left: 10., Red, role: Crewmate, tasks left: 9.]
    print(spaceship.get_regular_crewmates())
