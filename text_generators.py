def move_instructions_text(attempts, max_attempts, player_name):
    return input(
        f"""{player_name} ,where would you like to move?
        You have {max_attempts - attempts} chances for correct input:
        UP to move up,
        DOWN to move down,
        LEFT to move left,
        RIGHT to move right
        """)


def users_move_collector(other_player):
    return input(
        f"""
    You can hit {other_player} for 1 damage and finish your move, or skip hit and move to another cell.
    If you want to hit player - enter player`s name.
    If you want to move - enter MOVE.
    """
    )
