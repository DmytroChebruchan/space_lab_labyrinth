from constants import DIRECTIONS
from game_elements import Player
from text_generators import move_instructions_text, users_move_collector


def to_hit_players(cell_instance, player_instance, players_dict):
    try_counter = 3

    if len(players_dict.keys()) > 1:
        for player_name, player_info in players_dict.items():
            if player_info.active is True:
                current_player = players_dict[player_name]
                current_player.active = True
                other_player = []

                while try_counter != 0:
                    for _ in cell_instance.labyrinth.values():
                        for name, value in _.items():
                            if (
                                name in players_dict.keys()
                                and name != current_player.name
                            ):
                                other_player.append(name)

                    other_player = ", ".join(other_player)

                    hit = users_move_collector(other_player)

                    if hit == "MOVE":
                        move(cell_instance, players_dict)

                    elif hit in other_player:
                        players_dict[hit].health -= 1
                        players_dict[
                            current_player.name
                        ].active = False
                        print(
                            f"{players_dict[hit].name} was damaged! {players_dict[hit].health} health points left."
                        )

                        return cell_instance

                    else:
                        try_counter -= 1
                        print(
                            f"Wrong input, try again. {try_counter} tries left!"
                        )

                print("You did nothing, try next time!")
                player_info.active = False
                break
        return cell_instance


def move(cell_instance, players_dict):
    for player_name, player_info in players_dict.items():
        if player_info.active is True:
            current_player = players_dict[player_name]
            current_player.active = True

            max_attempts = 3
            attempts = 0
            player_info.active = True

            while player_info.active:
                move_direction = move_instructions_text(
                    attempts, max_attempts, player_name
                )

                if move_direction not in ["UP", "DOWN", "RIGHT", "LEFT"]:
                    print(f"Wrong input, try again!")
                    attempts += 1

                    if attempts == max_attempts:
                        player_info.active = False
                        print("Too many wrong inputs.")
                        break
                else:
                    player_info.active = False

                    if move_direction in DIRECTIONS:
                        dx, dy = DIRECTIONS[move_direction]
                        player_info.location[0] += dx
                        player_info.location[1] += dy

                for _ in cell_instance.labyrinth.values():
                    if (
                        player_info.location[0] == _["x"]
                        and player_info.location[1] == _["y"]
                    ):
                        print(f"{player_info.name} MOVED!")
                        break

                else:
                    print("Wrong vector!")
                    player_info.health -= 1
                    if move_direction == "UP":
                        player_info.location[1] -= 1
                    elif move_direction == "DOWN":
                        player_info.location[1] += 1
                    elif move_direction == "RIGHT":
                        player_info.location[0] -= 1
                    elif move_direction == "LEFT":
                        player_info.location[0] += 1
                    print(
                        f"{player_info.name} health lost! {player_info.health} left."
                    )

        return cell_instance


def game_loop(cell_instance, player_instance, players_dict):
    while len(players_dict.items()) > 0:
        for player_name, player_info in players_dict.items():
            current_player = players_dict[player_name]
            current_player.active = True

            if player_info.active is True and player_info.health > 0:
                print(f"{player_info.name} is active!")
                to_hit_players(cell_instance, player_instance, players_dict)

                if cell_instance.players[player_name] is False:
                    print(f"{player_info.name}")

                # current_player.active = False
            else:
                print(
                    f"{player_info.name} has {player_info.health} points of health. Game over!"
                )
                del cell_instance.players[player_name]


def create_players_dict():
    quantity = input("How many players? ")
    if not quantity.isdigit():
        print("Invalid! Enter correct number of players")
        return

    players = {}
    for _ in range(int(quantity)):
        name = input(f"Enter name of player {_ + 1}: ")
        players[name] = Player(name=name)

    return players
