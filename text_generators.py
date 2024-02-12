def users_move_input(attempts, player_name):
    return input(
        f"""Player {player_name} where would you like to move?\n
You have {attempts} chances for correct input:
- UP to move up,
- DOWN to move down,
- LEFT to move left,
- RIGHT to move right\n"""
    )


def users_action_input(other_players):
    players_list_string = ", ".join([player.name for player in other_players])
    return input(
        f"""You can hit some one or move to another cell of the 
labyrinth.
If you want to hit player - enter player`s name from below list
- {players_list_string}.
If you want to move - enter MOVE.\n"""
    )
