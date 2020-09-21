class Team:
    counter = 0

    def __init__(self, name, country, capacity, power):
        Team.counter += 1
        self.id = Team.counter
        self.name = name
        self.country = country
        self.arena_capacity = capacity
        self.power = power
        self.points = 0
        self.wins = 0
        self.losses = 0
        self.plus_points = 0
        self.minus_points = 0
        self.results = []

    '''List of tuples that has the following format 
    (opponent team, home/away, home points, away points, W/L)'''

    def add_result(self, result):
        self.results += [result]

    def print_team_results(self):
        print(f"-------- {self.name} ----------")
        print(f"{self.wins} wins, {self.losses} losses")
        for round, game in enumerate(self.results):
            print(f"{round + 1} {game[4]} {game[1]} {game[0].name} {game[2]} - {game[3]}")

    def __str__(self):
        string = f"Team id: {self.id}, "
        string += f"Team: {self.name}, "
        string += f"Country: {self.country.upper()}, "
        string += f"Arena Capacity: {self.arena_capacity}, "
        string += f"Power Ranking: {self.power}. "

        return string

    def __gt__(self, other):
        if self.points > other.points:
            return True
        if self.points == other.points:
            if (self.plus_points - self.minus_points) > (other.plus_points - other.minus_points):
                return True

