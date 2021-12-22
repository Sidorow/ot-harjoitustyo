class Player:
    def __init__(self, name):
        self.name = name
        self.drinks = 0
        self.curse = False

    def add_drink(self):
        self.drinks +=1

    def get_stats(self):
        return f"Juomia juotu: {self.drinks}"

    def __str__(self):
        return self.name
