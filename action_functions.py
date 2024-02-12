from game_elements import Player, Try
from text_generators import users_action_input


def players_turn(player, labyrinth, players_list):
    try_counter = Try(total_tries=3)

    while try_counter.num != 0:
        other_players = [p for p in players_list if p != player]
        users_input = users_action_input(other_players)

        if users_input == "MOVE":
            player.move_player(labyrinth, other_players)
            return

        players_names = [p.name for p in players_list]
        if users_input in players_names:
            target_player = [player for player in players_list if player.name
                             == users_input][0]
            player.punch(target_player)
            return

        print(f"Wrong input, try again. {try_counter.num} tries left!")
        try_counter.decrease_try_number()

    print("You did nothing, try next time!")


def game_loop(labyrinth, players_list):
    if len(players_list) == 1:
        print(f"Player {players_list[0].name} won! Game is over.")
        return

    # round
    for player in players_list:
        print(f"###\nPlayer {player.name} is active!\n###")
        players_turn(player, labyrinth, players_list)

        if player.health == 0:
            print("Game over for player ", player.name)
            players_list = [p for p in players_list if p != player]

    game_loop(labyrinth, players_list)


def create_players_dict():
    quantity = input("How many players? ")
    if not quantity.isdigit() or int(quantity) <= 1:
        print("Invalid! Enter correct number of players. 2 and more.")
        return

    players = []
    for _ in range(int(quantity)):
        name = input(f"Enter name of player {_ + 1}: ")
        players.append(Player(name=name))
    print("Players were created.\n")
    return players
