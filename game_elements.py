import json
import random

from constants import DIRECTIONS, DIRECTIONS_LIST
from text_generators import users_move_input


class Labyrinth:
    labyrinth_map = {}

    def __init__(self):
        with open("labyrinth.json", "r") as json_file:
            self.labyrinth_map = json.load(json_file)

    def make_fire(self):
        fire_counter = 0
        while fire_counter < 4:
            random_key = random.choice(list(self.labyrinth_map.keys()))
            current_cell = self.labyrinth_map[random_key]
            if current_cell.get('special') is None:
                current_cell['objects'] = {'fire': 1}
                fire_counter += 1

        return self.labyrinth_map

    def remove_fire(self):
        for key, cell in self.labyrinth_map.items():
            if cell['objects'] == {'fire': 1}:
                del cell['objects']

        return self.labyrinth_map


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
