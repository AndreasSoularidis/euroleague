from team import Team
from game import Game


class Euroleague:
    def __init__(self, season):
        self.season = season
        self.teams = []
        self.program = []
        self.play_off_program = []
        self.final_four_teams = []
        self.final_four_program = []
        self.champion = None

    def read_data(self):
        try:
            with open("teams.txt", encoding="UTF-8") as file:
                for line in file:
                    team = line.strip()
                    team_details = team.split(",")
                    new_team = Team(team_details[0].strip(), team_details[1].strip(), int(team_details[2]),
                                    int(team_details[3]))
                    self.teams.append(new_team)
        except FileNotFoundError:
            print("File not Found")

    def round_robin(self):
        teams = [team for team in self.teams]
        middle = len(teams) // 2
        for round in range(len(teams) - 1):
            games_of_round = []
            for i in range(middle):
                if round % 2 == 0:
                    game = Game(teams[i], teams[-(i + 1)])
                else:
                    game = Game(teams[-(i + 1)], teams[i])
                games_of_round.append(game)
            self.program.append(games_of_round)
            last_element = teams[len(teams) - 1]
            for i in range(-1, -18, -1):
                teams[i] = teams[i - 1]
            teams[1] = last_element

    def print_program(self):
        for round, games in enumerate(self.program):
            print(f"Round {round + 1}")
            for game in games:
                print(f"{game.home.name} vs {game.away.name}")

    def print_results(self):
        for round, games in enumerate(self.program):
            print(f"Round {round + 1}")
            for game in games:
                print(f"{game.home.name} vs {game.away.name} \t{game.home_points} {game.away_points}")

    def calculate_results(self):
        for round in self.program:
            for game in round:
                game.calculate_score("Regular Season")

    def calculate_ranking(self):
        self.teams.sort(reverse=True)
        print(f"{'Group Regular Season':<25}{'W':>12}{'L':>12}{'PTS+':>13}{'PTS-':>12}{'+/-':>12}")
        print(f"{85 * '-'}")
        for index, team in enumerate(self.teams):
            print(
                f"{team.name:<25}{team.wins:>12}{team.losses:>12}{team.plus_points:>12}{team.minus_points:>12}{(team.plus_points - team.minus_points):>12}")
            if index == 7:
                print(f"{85 * '-'}")

    def calculate_play_off_program(self):
        second_team = 7
        for i in range(4):
            game = Game(self.teams[i], self.teams[second_team])
            second_team -= 1
            self.play_off_program += [game]

        print(f"\nPlay Offs Season {self.season}")
        print(f"{40 * '-'}")
        for game in self.play_off_program:
            print(f"{game.home.name} vs {game.away.name}")


    def calculate_play_off_games(self):
        for game in self.play_off_program:
            advantage_team = game.home
            disadvantage_team = game.away
            advantage_team_wins = 0
            disadvantage_team_wins = 0
            game_number = 0
            while True:
                if advantage_team_wins == 3:
                    self.final_four_teams.append(advantage_team)
                    break
                if disadvantage_team_wins == 3:
                    self.final_four_teams.append(disadvantage_team)
                    break
                game_number += 1
                if game_number == 3 or game_number == 5:
                    game.home, game.away = game.away, game.home
                winner = game.calculate_score("Play offs")
                if winner.name == advantage_team.name:
                    advantage_team_wins += 1
                else:
                    disadvantage_team_wins += 1



    def print_play_off_results(self):
        for game in self.play_off_program:
            for team_game in game.home.results:
                if team_game[5] == "Play offs":
                    if team_game[1] == "vs":
                        print(f"{game.home.name} vs {team_game[0].name} {team_game[2]} - {team_game[3]}")
                    else:
                        print(f"{team_game[0].name} vs {game.home.name} {team_game[2]} - {team_game[3]}")
            print(f"{40 * '-'}")


    def calculate_final_four_program(self):
        semi_final_1 = Game(self.final_four_teams[0], self.final_four_teams[3])
        semi_final_2 = Game(self.final_four_teams[1], self.final_four_teams[2])
        self.final_four_program.append(semi_final_1)
        self.final_four_program.append(semi_final_2)


    def calculate_final_four_games(self):
        g_final = []
        s_final = []
        print("Semi Finals")
        print(f"{40 * '-'}")
        for game in self.final_four_program:
            winner = game.calculate_score("final-4")
            g_final.append(winner)
            print(f"{game.home.name} vs {game.home.results[-1][0].name} {game.home.results[-1][2]} - {game.home.results[-1][3]}")
        for team in self.final_four_teams:
            if team not in g_final:
                s_final.append(team)

        print("Small Final")
        print(f"{40 * '-'}")
        small_final = Game(s_final[0], s_final[1])
        small_final.calculate_score("final-4")
        print(f"{small_final.home.name} vs {small_final.home.results[-1][0].name} {small_final.home.results[-1][2]} - {small_final.home.results[-1][3]}")
        print(f"{40 * '-'}")
        print("Final")
        print(f"{40 * '-'}")
        final = Game(g_final[0], g_final[1])
        self.champion = final.calculate_score("final-4")
        print(f"{final.home.name} vs {final.home.results[-1][0].name} {final.home.results[-1][2]} - {final.home.results[-1][3]}")
        print(f"{40 * '*'}")
        print(f"{self.champion.name} is the Euroleague champion in the {self.season} season")
        print(f"{40 * '*'}")