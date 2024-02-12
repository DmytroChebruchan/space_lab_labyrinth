import json
import random


class Labyrinth:
    def __init__(self, labyrinth_map: dict = None):
        self.labyrinth_map = labyrinth_map or {}

    def generate_labyrinth(self) -> dict:
        # Генерирует лабиринт из файла 'labyrinth.json'
        with open('labyrinth.json', 'r') as json_file:
            data = json.load(json_file)
            self.labyrinth_map.update(data)
        return self.labyrinth_map

    def make_fire(self):
        # Генерирует в 5-ти случайных ячейках пламя
        fire_counter = 0
        while fire_counter < 4:
            random_key = random.choice(list(self.labyrinth_map.keys()))
            current_cell = self.labyrinth_map[random_key]
            if current_cell.get('special') is None:
                current_cell['objects'] = {'fire': 1}
                fire_counter += 1

        return self.labyrinth_map

    def remove_fire(self):
        # Удаляет пламя из ячеек в конце круга
        for key, cell in self.labyrinth_map.items():
            if cell['objects'] == {'fire': 1}:
                del cell['objects']

        return self.labyrinth_map


class Player:
    def __init__(self, name: str = '', x: int = 0, y: int = 0, active: bool = False,
                 health: int = 5, items: dict = None, players: dict = None):
        self.name = name
        self.active = active
        self.location = [x, y]
        self.health = health
        self.items = items
        self.players = players or {}

    def add_player(self):
        # Добавляет игроков в игру
        quantity = input('How many players? ')
        if quantity.isdigit():
            quantity = int(quantity)
            for _ in range(quantity):
                name = input('Enter your name: ')
                self.players[name] = Player(name=name)
        else:
            print('Invalid! Enter correct number of players')

        return self.players


class Cell:
    def __init__(self, labyrinth: Labyrinth, players: dict = None):
        self.labyrinth = labyrinth.labyrinth_map
        self.players = players or {}

    def add_player_location(self):
        # Добавляет игрока в ячейку лабиринта и удаляет его, после того как игрок переходит на другую ячейку
        for player in cell_instance.players.values():
            cell_key = f'x{player.location[0]}_y{player.location[1]}'
            if cell_key in cell_instance.labyrinth:
                for _ in cell_instance.labyrinth.values():
                    if player.name in _ and player.location[0] != _['x'] and player.location[1] == _['y']:
                        del _[player.name]
                    elif player.location[0] == _['x'] and player.location[1] == _['y']:
                        if cell_instance.labyrinth[cell_key]:
                            labyrinth_instance.labyrinth_map[cell_key][player.name] = {
                                'name': player.name,
                                'location': player.location,
                                'health': player.health,
                                'items': player.items,
                                'active': player.active,
                            }

        return self.labyrinth

    def __str__(self):
        return f'LABYRINTH:{self.labyrinth}\nPLAYERS:{self.players}'


class Game:
    def __init__(self):
        self.cell_instance = Cell(labyrinth=Labyrinth(), players={})

    def game_loop(self):


        while len(cell_instance.players.items()) > 0:
            for player_name, player_info in cell_instance.players.items():
                current_player = player_instance.players[player_name]
                current_player.active = True

                if player_info.active is True and player_info.health > 0:
                    print(f'{player_info.name} is active!')
                    self.to_hit_players()
                    if cell_instance.players[player_name] is False:
                        print(f'{player_info.name}')



                    # current_player.active = False
                else:
                    print(f'{player_info.name} has {player_info.health} points of health. Game over!')
                    del cell_instance.players[player_name]
                # current_player.active = False

    def to_hit_players(self):

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
                                if name in cell_instance.players.keys() and name != current_player.name:
                                    other_player.append(name)

                        other_player = ', '.join(other_player)

                        hit = input(f'''
You can hit {other_player} for 1 damage and finish your move, or skip hit and move to another cell.
If you want to hit player - enter player`s name.
If you want to move - enter MOVE.
''')
                        if hit == 'MOVE':
                            game_instance.move()
                            # return self.cell_instance.players[current_player].move()
                        elif hit in other_player:
                            cell_instance.players[hit].health -= 1
                            cell_instance.players[current_player.name].active = False
                            print(
                                f'{cell_instance.players[hit].name} was damaged! {cell_instance.players[hit].health} health points left.')

                            return cell_instance

                        else:
                            try_counter -= 1
                            print(f'Wrong input, try again. {try_counter} tries left!')

                    print('You did nothing, try next time!')
                    player_info.active = False
                    break
            return cell_instance




    def move(self):

        """При вводе в консоль UP - изменит положение персонажа записав х + 1 , DOWN - х - 1, LEFT - у - 1,
         RIGHT - у + 1. Перезаписывает поле location и меняет статус поля active на False."""

        for player_name, player_info in cell_instance.players.items():
            if player_info.active is True:
                current_player = player_instance.players[player_name]
                current_player.active = True

                max_attempts = 3
                attempts = 0
                player_info.active = True
                while player_info.active:
                    move = input(f'''
{player_name} ,where would you like to move?
You have {max_attempts - attempts} chances for correct input:
UP to move up,
DOWN to move down,
LEFT to move left,
RIGHT to move right
''')
                    if move not in ["UP", "DOWN", "RIGHT", "LEFT"]:
                        print(f'Wrong input, try again!')
                        attempts += 1

                        if attempts == max_attempts:
                            player_info.active = False
                            print("Too many wrong inputs.")
                            break
                    else:
                        player_info.active = False
                        if move == "UP":
                            player_info.location[1] += 1
                        elif move == "DOWN":
                            player_info.location[1] -= 1
                        elif move == "RIGHT":
                            player_info.location[0] += 1
                        elif move == "LEFT":
                            player_info.location[0] -= 1

                    for _ in cell_instance.labyrinth.values():
                        if player_info.location[0] == _['x'] and player_info.location[1] == _['y']:
                            print(f'{player_info.name} MOVED!')
                            break

                    else:
                        print('Wrong vector!')
                        player_info.health -= 1
                        if move == "UP":
                            player_info.location[1] -= 1
                        elif move == "DOWN":
                            player_info.location[1] += 1
                        elif move == "RIGHT":
                            player_info.location[0] -= 1
                        elif move == "LEFT":
                            player_info.location[0] += 1
                        print(f'{player_info.name} health lost! {player_info.health} left.')

            return cell_instance


if __name__ == '__main__':
    labyrinth_instance = Labyrinth()
    labyrinth_instance.generate_labyrinth()

    player_instance = Player()
    players_dict = player_instance.add_player()

    cell_instance = Cell(labyrinth=labyrinth_instance, players=players_dict)

    game_instance = Game()
    cell_instance.add_player_location()

    game_instance.game_loop()
    game_instance.to_hit_players()


    cell_instance.add_player_location()
