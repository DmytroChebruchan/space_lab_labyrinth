import random
from functools import wraps


class Labyrinth:
    def __init__(self, x: int, y: int, objects: dict = None):
        self.x = x
        self.y = y
        self.objects = objects


x0_y0 = Labyrinth(x=0, y=0)
x1_y0 = Labyrinth(x=1, y=0)
x1_y1 = Labyrinth(x=1, y=1)
x2_y1 = Labyrinth(x=2, y=1)
x2_y2 = Labyrinth(x=2, y=2, objects={'key': 1})
x3_y1 = Labyrinth(x=3, y=1)
x3_y0 = Labyrinth(x=3, y=0)
x4_y0 = Labyrinth(x=4, y=0)
x5_y0 = Labyrinth(x=5, y=0)
x5_y1 = Labyrinth(x=5, y=1)
x6_y1 = Labyrinth(x=6, y=1, objects={'heart': 1})
x5_y2 = Labyrinth(x=5, y=2)
x5_y3 = Labyrinth(x=5, y=3)
x4_y3 = Labyrinth(x=4, y=3, objects={'heart': 1})
x6_y3 = Labyrinth(x=6, y=3)
x7_y3 = Labyrinth(x=7, y=3, objects={'Golem': 1})

labyrinth_instances = [
    x0_y0, x1_y0, x1_y1, x2_y1, x2_y2, x3_y1, x3_y0, x4_y0, x5_y0, x5_y1, x6_y1, x5_y2, x5_y3, x4_y3, x6_y3, x7_y3]


class Player:
    def __init__(self, name: str, active: bool = False, x: int = 0, y: int = 0,
                 health: int = 5, items: dict = None):
        self.name = name
        self.active = active
        self.x = x
        self.y = y
        self.health = health
        self.items = items


def add_player():
    players = []
    quantity = int(input('How many players? '))
    for _ in range(quantity):
        name = input('Enter your name: ')
        player = Player(name)
        players.append(player)
    return players


all_players = add_player()


class Game:

    def make_fire(self):
        fire_counter = 4

        while fire_counter > 0:
            fire_index = random.randint(0, len(labyrinth_instances) - 1)
            if labyrinth_instances[fire_index].objects is None:
                labyrinth_instances[fire_index].objects = {'fire': 1}
                fire_counter -= 1
            else:
                continue
        return labyrinth_instances



    # def to_hit_with_sword(self, players):
    #
    #     """Здесь будет происходить обработка удара, в случае ввода игроком в консоль hit: active станет False после
    #      удара, если удар был сделан в момент пребывания на одной клетке с другими игроками - у них снимутся баллы
    #      health. Выведет сообщение с именами персонажей получивших урон, или сообщит о неудачной атаке"""
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

    def move(self, players):

        """При вводе в консоль UP - изменит положение персонажа записав х + 1 , DOWN - х - 1, LEFT - у - 1,
         RIGHT - у + 1. Перезаписывает поле location и меняет статус поля active на False."""

        for player in players:
            max_attempts = 3
            attempts = 0
            if player.health > 0:
                player.active = True
            else:
                print(f'{player.name} is dead.')

            while player.active:
                move = input(f'''
{player.name} ,where would you like to move?
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
                        player.active = False
                        print("Too many wrong inputs.")
                else:
                    player.active = False
                    temporary_x = player.x
                    temporary_y = player.y
                    if move == "UP":
                        temporary_y += 1

                    elif move == "DOWN":
                        temporary_y -= 1

                    elif move == "RIGHT":
                        temporary_x += 1

                    elif move == "LEFT":
                        temporary_x -= 1

                    for labyrinth_instance in labyrinth_instances:
                        if temporary_x == labyrinth_instance.x and temporary_y == labyrinth_instance.y:
                            player.x, player.y = temporary_x, temporary_y
                            print(f'{player.name} moved!')
                            break
                    else:
                        print('Wrong vector!')
                        player.health -= 1
                        print(f'{player.name} health lost! {player.health} left.')

        return [(player.x, player.y) for player in players]

    def take_damage(self, players, labyrinth_instances):

        """Здесь будет сниматся очки health, если герой получит урон от стены или огня. Выведет сообщение о
        причине снятия баллов здоровья и колличества снятых баллов"""

        for player in players:

            for labyrinth_instance in labyrinth_instances:
                if labyrinth_instance.objects is not None and 'fire' in labyrinth_instance.objects and player.x == labyrinth_instance.x and player.y == labyrinth_instance.y:

                    player.health -= 1
                    print(f'Player {player.name} received damage from fire. Health: {player.health}')
                    break

        return players

    def remove_fire(self):

        for instance in labyrinth_instances:
            if instance.objects and 'fire' in instance.objects:
                del instance.objects['fire']

        return labyrinth_instances

    def play(self):
        while any(player.health > 0 for player in all_players):
            self.make_fire()
            self.move(all_players)
            self.take_damage(all_players, labyrinth_instances)
            self.remove_fire()
        print("Game over!")


if __name__ == "__main__":
    game_instance = Game()
    game_instance.play()

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
