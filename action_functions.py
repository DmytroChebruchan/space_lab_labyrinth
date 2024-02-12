from constants import DIRECTIONS


def to_hit_players(cell_instance, player_instance):
    try_counter = 3

    if len(cell_instance.players.keys()) > 1:
        for player_name, player_info in cell_instance.players.items():
            if player_info.active is True:
                current_player = player_instance.players[player_name]
                current_player.active = True
                other_player = []

                while try_counter != 0:
                    for _ in cell_instance.labyrinth.values():
                        for name, value in _.items():
                            if (
                                name in cell_instance.players.keys()
                                and name != current_player.name
                            ):
                                other_player.append(name)

                    other_player = ", ".join(other_player)

                    hit = input(
                        f"""
You can hit {other_player} for 1 damage and finish your move, or skip hit and move to another cell.
If you want to hit player - enter player`s name.
If you want to move - enter MOVE.
"""
                    )
                    if hit == "MOVE":
                        move(cell_instance, player_instance)
                    elif hit in other_player:
                        cell_instance.players[hit].health -= 1
                        cell_instance.players[
                            current_player.name
                        ].active = False
                        print(
                            f"{cell_instance.players[hit].name} was damaged! {cell_instance.players[hit].health} health points left."
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


def move(cell_instance, player_instance):
    """При вводе в консоль
    UP - изменит положение персонажа записав х + 1 ,
    DOWN - х - 1,
    LEFT - у - 1,
    RIGHT - у + 1.
    Перезаписывает поле location и меняет статус поля active на False.
    """

    for player_name, player_info in cell_instance.players.items():
        if player_info.active is True:
            current_player = player_instance.players[player_name]
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


def game_loop(cell_instance, player_instance):
    while len(cell_instance.players.items()) > 0:
        for player_name, player_info in cell_instance.players.items():
            current_player = player_instance.players[player_name]
            current_player.active = True

            if player_info.active is True and player_info.health > 0:
                print(f"{player_info.name} is active!")
                to_hit_players(cell_instance, player_instance)
                if cell_instance.players[player_name] is False:
                    print(f"{player_info.name}")

                # current_player.active = False
            else:
                print(
                    f"{player_info.name} has {player_info.health} points of health. Game over!"
                )
                del cell_instance.players[player_name]
            # current_player.active = False


def move_instructions_text(attempts, max_attempts, player_name):
    users_move = input(
        f"""
{player_name} ,where would you like to move?
You have {max_attempts - attempts} chances for correct input:
UP to move up,
DOWN to move down,
LEFT to move left,
RIGHT to move right
"""
    )
    return users_move