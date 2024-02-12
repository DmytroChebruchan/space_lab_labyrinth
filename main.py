from game_elements import Labyrinth, Cell, Player
from action_functions import to_hit_players, game_loop, create_players_dict


def main():
    labyrinth_instance = Labyrinth()

    player_instance = Player()
    players_dict = create_players_dict()

    cell_instance = Cell(labyrinth=labyrinth_instance.labyrinth_map)

    cell_instance.add_player_location(players_dict)

    game_loop(cell_instance, player_instance, players_dict)
    to_hit_players(cell_instance, player_instance, players_dict)

    cell_instance.add_player_location(players_dict)


if __name__ == "__main__":
    main()
