from action_functions import create_players_dict, game_loop
from game_elements import Labyrinth


def main():
    players_list = create_players_dict()
    if not players_list:
        return

    labyrinth = Labyrinth()

    game_loop(labyrinth, players_list)


if __name__ == "__main__":
    main()
