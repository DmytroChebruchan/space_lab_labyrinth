import json
import random
from functools import wraps


class Labyrinth:
    def __init__(self, labyrinth_map: dict = None):
        self.labyrinth_map = labyrinth_map or {}

    def generate_labyrinth(self) -> dict:
        with open('labyrinth.json', 'r') as json_file:
            data = json.load(json_file)
            self.labyrinth_map.update(data)
        return self.labyrinth_map

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


# labyrinth_instance = Labyrinth()
# labyrinth_instance.generate_labyrinth()
# labyrinth_instance.make_fire()
#
# labyrinth_instance.remove_fire()


# print(labyrinth_instance.labyrinth_map.values())


class Player:
    def __init__(self, name: str = '', x: int = 0, y: int = 0, active: bool = False,
                 health: int = 5, items: dict = None, players: dict = None):
        self.name = name
        self.active = active
        self.location = (x, y)
        self.health = health
        self.items = items
        self.players = players or {}

    def add_player(self):
        quantity = int(input('How many players? '))
        for _ in range(quantity):
            name = input('Enter your name: ')
            self.players[name] = Player(name=name)

        return self.players


# player_instance = Player()
# players_dict = player_instance.add_player()
# for keys, values in players_dict.items():
#     print(keys, values.name, values.health, values.items)


class Cell:
    def __init__(self, labyrinth: Labyrinth, players: dict = None):

        self.labyrinth = labyrinth.labyrinth_map
        self.players = players or {}

    def add_player_location(self, player: Player):
        x, y = player.location
        cell_key = f'x{x}_y{y}'
        for player in self.players.values():
            if cell_key in self.labyrinth:
                cell_data = self.labyrinth[cell_key]

                if 'players' not in cell_data:
                    cell_data['players'] = {}

                cell_data['players'][player.name] = {
                    'name': player.name,
                    'health': player.health,
                    'items': player.items,
                    'active': player.active,
                }

        return self.labyrinth


# labyrinth_instance = Labyrinth()
# labyrinth_instance.generate_labyrinth()
# player_instance = Player()
# players_dict = player_instance.add_player()
# cell_instance = Cell(labyrinth=labyrinth_instance, players=players_dict)
# cell_instance.add_player_location(player=player_instance)
# print(cell_instance.labyrinth)

# for _, player_instance in players_dict.items():
#     print(cell_instance.add_player_location(player_instance))
# for player in cell_instance.players.items():
#     print(player)
# print(cell_instance.add_player_location(player_instance.players))


# cell_players = cell_instance.get_players_on_cell(1, 0)
# print(cell_players)


class Game:
    def __init__(self):
        self.labyrinth_instance = Labyrinth()
        self.cell_instance = Cell(labyrinth=Labyrinth(), players={})

    # def activate_player(self, player: Player):
    #     for player in player.players.values():
    #         if player.active == 0:
    #             player.active = True
    #             print(f'{player.name} is active!')
    #         if player.active == 1:
    #             break
    #
    #     return player

    def start_game(self, cell: Cell):
        not_active_players = {}
        try_counter = 3
        for player in cell.players.values():
            if not player.active:
                player.active = True
                print(f'{player.name} is active')
                while player.active:
                    for _ in cell.players.items():
                        for player_name, player_info in cell.players.items():
                            if player_info.active:
                                continue
                            else:
                                not_active_players[player_name] = player_info.name

                    not_active_player_names = ', '.join(not_active_players.values())
                    hit = input(
                        f'You can hit {not_active_player_names} for 1 damage and finish your move, or skip hit and move to another cell.'                        
                        '''
If you want to hit player - enter player`s name.
If you want to move - enter MOVE.
''')
                    if hit == 'MOVE':
                        player.active = False
                    elif hit in not_active_player_names:
                        cell.players[hit].health -= 1
                        print(f'{cell.players[hit].name} was damaged! {cell.players[hit].health} health points left.')
                        break
                    else:
                        if try_counter == 0:
                            print('You did nothing, try next time!')
                            player.active = False


                            break
                        else:
                            print(f'Wrong input, try again.{try_counter} tries left')
                            try_counter -= 1
                        break
            return cell.players, cell.labyrinth


labyrinth_instance = Labyrinth()
labyrinth_instance.generate_labyrinth()
player_instance = Player()
players_dict = player_instance.add_player()
cell_instance = Cell(labyrinth=labyrinth_instance, players=players_dict)
cell_instance.add_player_location(player=player_instance)
game_instance = Game()

print(game_instance.start_game(cell_instance))





