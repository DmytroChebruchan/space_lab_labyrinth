import json

from constants import DIRECTIONS, DIRECTIONS_LIST
from text_generators import users_move_input


class Labyrinth:
    labyrinth_map = {}

    def __init__(self):
        with open("labyrinth.json", "r") as json_file:
            self.labyrinth_map = json.load(json_file)


class Player:
    location = [0, 0]
    health: int = 5
    items: dict = {}
    players = {}

    def __init__(self, name: str):
        self.name = name

    def move_player(self, labyrinth, other_players, attempts=3):
        if attempts == 0:
            print("Too many wrong inputs. Next player to make " "action.")
            return

        move_direction = users_move_input(attempts, self.name)

        if move_direction not in DIRECTIONS_LIST:
            print(f"Wrong input!")
            attempts -= 1
            self.move_player(labyrinth, other_players)

        dx, dy = DIRECTIONS[move_direction]
        self.location[0] += dx
        self.location[1] += dy
        print(f"Moved {move_direction} to {self.location}")

    def punch(self, target_player):
        target_player.health -= 1
        print(f"{target_player.name} was damaged!\n{target_player.health} health points left.")


class Try:
    num = 0

    def __init__(self, total_tries):
        self.num = total_tries

    def decrease_try_number(self, num=1):
        self.num = self.num - num
