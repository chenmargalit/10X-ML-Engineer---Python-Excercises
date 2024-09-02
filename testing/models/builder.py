class Player:

    def __init__(self, builder) -> None:

        self.team = builder.team
        self.salary = builder.salary
        self.shirt_number = builder.shirt_number

    def __str__(self):
        return 'I am a player class'


class PlayerBuilder:

    def __init__(self):
        self.team = None
        self.salary = None
        self.shirt_number = None

    def set_team(self, team):

        if len(team) < 1:
            return

        self.team = team
        return self

    def set_salary(self, salary):
        self.salary = salary
        return self

    def set_shirt_number(self, shirt_number: int):
        if not isinstance(shirt_number, int):
            raise TypeError(f"Expected an int but got a {type(shirt_number).__name__}")

        self.shirt_number = shirt_number
        return self

    def build(self):
        return Player(self)

    def __str__(self):
        return 'I am a player builder class'


player_builder = PlayerBuilder()
player = player_builder.set_team('barca').set_salary(100).set_shirt_number(12).build()
print(player)

