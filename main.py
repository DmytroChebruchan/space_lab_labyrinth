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
        for _ in self.labyrinth.keys():
            if cell_key in self.labyrinth.keys():

                cell_data = self.labyrinth[cell_key]

                if 'players' not in cell_data:
                    cell_data['players'] = {}

                cell_data['players'][player.name] = {
                    'name': player.name,
                    'health': player.health,
                    'items': player.items
                }

        return self.labyrinth

    # def get_players_on_cell(self, x, y):
    #     cell_key = f'x{x}_y{y}'
    #
    #     if cell_key in self.labyrinth.labyrinth_map:
    #         cell_data = self.labyrinth.labyrinth_map[cell_key]
    #
    #         # Перевіряємо, чи є ключ 'players' у вкладеному словнику
    #         players_on_cell = cell_data.get('players', {})
    #
    #         return players_on_cell
    #     else:
    #         return {}


labyrinth_instance = Labyrinth()
labyrinth_instance.generate_labyrinth()
player_instance = Player()
players_dict = player_instance.add_player()
cell_instance = Cell(labyrinth=labyrinth_instance, players=players_dict)
print(cell_instance.add_player_location(player_instance))

# cell_players = cell_instance.get_players_on_cell(1, 0)
# print(cell_players)


# class Game:
#     def __init__(self):
#         self.labyrinth_instance = Labyrinth()
#         self.player_instance = Player()

# def to_hit_with_sword(self):
#     for player in self.player_instance.players.values():
#         if 0 < player.health <= 5:
#             player.active = True
#             while player.active:
#                 if self.labyrinth_instance.


# if 0 < self.player_instance.players['objects'].get('health', 0) <= 5:
#     player = self.player_instance.players['active': True]
#
#     while players_counter <= len(players):
#         if (players[0].x == players[players_counter].x and players[0].y == players[players_counter].y) and (players[0].name != players[players_counter].name):
#             nearest_players.append(players[players_counter])
#         else:
#             players_counter += 1
#             if players_counter >= len(players):
#                 break
#
#
#         hit = input(f'''{players[].name}, you can hit {players[1].name} with your sword! It would take one
#             point of his health and your move would be finished. What would you like to do?
#             HIT to kick another player,
#             MOVE to walk away
#             ''')
#         if hit == 'HIT':
#             players[0].active = False
#             players[1].health -= 1
#             print(f'''{players[1].name}, you were kicked by {players[0].name}!
#             {players[1].health} points of health left!''')
#
#
#         return players


# game_instance = Game()
# game_instance.labyrinth_instance.generate_labyrinth()
# game_instance.labyrinth_instance.make_fire()
#
# game_instance.player_instance.add_player()

# print(game_instance.player_instance.players)
# print(game_instance.labyrinth_instance.labyrinth_map)
# print(game_instance.to_hit_with_sword())


# def to_hit_with_sword(self, players):
#     nearest_players = []
#     if len(players) > 1:
#         players_counter = 1
#
#         while players_counter <= len(players):
#             if (players[0].x == players[players_counter].x and players[0].y == players[players_counter].y) and (players[0].name != players[players_counter].name):
#                 nearest_players.append(players[players_counter])
#             else:
#                 players_counter += 1
#                 if players_counter >= len(players):
#                     break
#
#
#             hit = input(f'''{players[].name}, you can hit {players[1].name} with your sword! It would take one
#                 point of his health and your move would be finished. What would you like to do?
#                 HIT to kick another player,
#                 MOVE to walk away
#                 ''')
#             if hit == 'HIT':
#                 players[0].active = False
#                 players[1].health -= 1
#                 print(f'''{players[1].name}, you were kicked by {players[0].name}!
#                 {players[1].health} points of health left!''')
#
#
#             return players


#     def move(self, players):
#
#         """При вводе в консоль UP - изменит положение персонажа записав х + 1 , DOWN - х - 1, LEFT - у - 1,
#          RIGHT - у + 1. Перезаписывает поле location и меняет статус поля active на False."""
#
#         for player in players:
#             max_attempts = 3
#             attempts = 0
#             if player.health > 0:
#                 player.active = True
#             else:
#                 print(f'{player.name} is dead.')
#
#             while player.active:
#                 move = input(f'''
# {player.name} ,where would you like to move?
# You have {max_attempts - attempts} chances for correct input:
#     UP to move up,
#     DOWN to move down,
#     LEFT to move left,
#     RIGHT to move right
# ''')
#                 if move not in ["UP", "DOWN", "RIGHT", "LEFT"]:
#                     print(f'Wrong input, try again!')
#                     attempts += 1
#                     if attempts == max_attempts:
#                         player.active = False
#                         print("Too many wrong inputs.")
#                 else:
#                     player.active = False
#                     temporary_x = player.x
#                     temporary_y = player.y
#                     if move == "UP":
#                         temporary_y += 1
#
#                     elif move == "DOWN":
#                         temporary_y -= 1
#
#                     elif move == "RIGHT":
#                         temporary_x += 1
#
#                     elif move == "LEFT":
#                         temporary_x -= 1
#
#                     for labyrinth_instance in labyrinth_instances:
#                         if temporary_x == labyrinth_instance.x and temporary_y == labyrinth_instance.y:
#                             player.x, player.y = temporary_x, temporary_y
#                             print(f'{player.name} moved!')
#                             break
#                     else:
#                         print('Wrong vector!')
#                         player.health -= 1
#                         print(f'{player.name} health lost! {player.health} left.')
#
#         return [(player.x, player.y) for player in players]
#
#     def take_damage(self, players, labyrinth_instances):
#
#         """Здесь будет сниматся очки health, если герой получит урон от стены или огня. Выведет сообщение о
#         причине снятия баллов здоровья и колличества снятых баллов"""
#
#         for player in players:
#
#             for labyrinth_instance in labyrinth_instances:
#                 if labyrinth_instance.objects is not None and 'fire' in labyrinth_instance.objects and player.x == labyrinth_instance.x and player.y == labyrinth_instance.y:
#
#                     player.health -= 1
#                     print(f'Player {player.name} received damage from fire. Health: {player.health}')
#                     break
#
#         return players
#

#
#     def play(self):
#         while any(player.health > 0 for player in all_players):
#             self.make_fire()
#             self.move(all_players)
#             self.take_damage(all_players, labyrinth_instances)
#             self.remove_fire()
#         print("Game over!")
#
#
# if __name__ == "__main__":
#     game_instance = Game()
#     game_instance.play()

# def take_health(self):
#     """Сработает при попадании на клетку с сердечком, добавив баллы health и отняв 1 от значения поля heart.
#     Выведет сообщение о востановлении здоровья."""
#     pass
#
# def condition(self):
#     """Выводит соббщения о поражении при ходе на предыдущую клетку, если значение поля health = 0, и при встрече с
#     без ключа. Выводит сообщение о победе при достиженни голема, когда key для игрока в статусе True."""
#
#     pass
