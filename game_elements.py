import json
import random


class Labyrinth:
    def __init__(self, labyrinth_map: dict = None):
        self.labyrinth_map = labyrinth_map or {}

    def generate_labyrinth(self) -> dict:
        # Генерирует лабиринт из файла 'labyrinth.json'
        with open("labyrinth.json", "r") as json_file:
            data = json.load(json_file)
            self.labyrinth_map.update(data)
        return self.labyrinth_map

    def make_fire(self):
        # Генерирует в 5-ти случайных ячейках пламя
        fire_counter = 0
        while fire_counter < 4:
            random_key = random.choice(list(self.labyrinth_map.keys()))
            current_cell = self.labyrinth_map[random_key]
            if current_cell.get("special") is None:
                current_cell["objects"] = {"fire": 1}
                fire_counter += 1

        return self.labyrinth_map

    def remove_fire(self):
        # Удаляет пламя из ячеек в конце круга
        for key, cell in self.labyrinth_map.items():
            if cell["objects"] == {"fire": 1}:
                del cell["objects"]

        return self.labyrinth_map


class Cell:
    def __init__(self, labyrinth: Labyrinth, players: dict = None):
        self.labyrinth = labyrinth.labyrinth_map
        self.players = players or {}

    def add_player_location(self):
        # Добавляет игрока в ячейку лабиринта и удаляет его, после того как игрок переходит на другую ячейку
        for player in self.players.values():
            cell_key = f"x{player.location[0]}_y{player.location[1]}"
            if cell_key in self.labyrinth:
                for _ in self.labyrinth.values():
                    if (
                        player.name in _
                        and player.location[0] != _["x"]
                        and player.location[1] == _["y"]
                    ):
                        del _[player.name]
                    elif (
                        player.location[0] == _["x"]
                        and player.location[1] == _["y"]
                    ):
                        if self.labyrinth[cell_key]:
                            self.labyrinth[cell_key][player.name] = {
                                "name": player.name,
                                "location": player.location,
                                "health": player.health,
                                "items": player.items,
                                "active": player.active,
                            }

        return self.labyrinth

    def __str__(self):
        return f"LABYRINTH:{self.labyrinth}\nPLAYERS:{self.players}"


class Player:
    def __init__(
        self,
        name: str = "",
        x: int = 0,
        y: int = 0,
        active: bool = False,
        health: int = 5,
        items: dict = None,
        players: dict = None,
    ):
        self.name = name
        self.active = active
        self.location = [x, y]
        self.health = health
        self.items = items
        self.players = players or {}

    def add_player(self):
        # Добавляет игроков в игру
        quantity = input("How many players? ")
        if quantity.isdigit():
            quantity = int(quantity)
            for _ in range(quantity):
                name = input("Enter your name: ")
                self.players[name] = Player(name=name)
        else:
            print("Invalid! Enter correct number of players")

        return self.players
