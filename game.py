from team import Team
from random import seed, randrange
from datetime import datetime
seed(datetime.now())

class Game:
    def __init__(self, home, away):
        self.home = home
        self.away = away
        self.home_points = 0
        self.away_points = 0
        self.winner = None
        self.loser = None

    def _update_results(self, phase):
        self.winner.points += 2
        self.winner.wins += 1
        if self.winner == self.home:
            winner_arena = "vs"
            loser_arena = "at"
            winner_points = self.home_points
            loser_points = self.away_points
            self.winner.plus_points += winner_points
            self.winner.minus_points += loser_points
        else:
            winner_arena = "at"
            loser_arena = "vs"
            winner_points = self.away_points
            loser_points = self.home_points
            self.loser.plus_points += loser_points
            self.loser.minus_points += winner_points
        stats = (self.loser, winner_arena, self.home_points, self.away_points, "W", phase)
        self.winner.add_result(stats)

        # Update results for the team that lose
        self.loser.points += 1
        self.loser.losses += 1
        stats = (self.winner, loser_arena, self.home_points, self.away_points, "L", phase)
        self.loser.add_result(stats)

    def calculate_score(self, phase):

        self.home_points = 0
        self.away_points = 0
        '''Extra points for the home team according to arena capacity
         if play with team from another country '''
        if self.home.country != self.away.country and phase != "final-4":
            if 10000 < self.home.arena_capacity < 15.000:
                self.home_points += 3
            elif self.home.arena_capacity >= 15000:
                self.home_points += 5

        self.home_points += 50 + randrange(21) + self.home.power // 2
        self.away_points += 50 + randrange(21) + self.away.power // 2

        '''case of draw '''
        if self.home_points == self.away_points:
            extra_point = randrange(2)
            if extra_point == 0:
                self.home_points += 1
            elif extra_point == 1:
                self.away_points += 1

        if self.home_points > self.away_points:
            self.winner = self.home
            self.loser = self.away
        else:
            self.winner = self.away
            self.loser = self.home

        self._update_results(phase)

        return self.winner