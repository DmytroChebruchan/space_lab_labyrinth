from game_elements import Labyrinth, Cell, Player
from action_functions import to_hit_players, game_loop


def main():
    labyrinth_instance = Labyrinth()
    labyrinth_instance.generate_labyrinth()

    player_instance = Player()
    players_dict = player_instance.add_player()

    cell_instance = Cell(labyrinth=labyrinth_instance, players=players_dict)

    cell_instance.add_player_location()
    game_loop(cell_instance, player_instance)
    to_hit_players(cell_instance, player_instance)

    cell_instance.add_player_location()


if __name__ == "__main__":
    main()
