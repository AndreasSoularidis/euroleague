from team import Team
from league import Euroleague


def main():
    league = Euroleague("2020/2021")
    league.read_data()
    league.round_robin()
    print(f"Euroleauge Program Season {league.season}")
    league.print_program()
    while True:
        choice = input("Press 1 to see the results ")
        if not choice.isdigit():
            print("Give an acceptable value please")
            continue
        choice = int(choice)
        if choice != 1:
            print("Give an acceptable value please")
            continue
        break
    league.calculate_results()
    print("\n 1st Round Results\n")
    league.print_results()
    print("\n Final Ranking\n")
    league.calculate_ranking()

    league.calculate_play_off_program()
    print(f"{40 * '-'}")
    print(f"Play off {league.season} results")
    print(f"{40 * '-'}")
    league.calculate_play_off_games()
    league.print_play_off_results()
    print("Final 4")
    print(f"{40 * '-'}")
    league.calculate_final_four_program()
    league.calculate_final_four_games()


if __name__ == '__main__':
    main()
