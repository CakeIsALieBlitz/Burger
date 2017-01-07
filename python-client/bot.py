from random import choice
from game import Game


class Bot:
    pass


class RandomBot(Bot):
    def move(self, state):
        game = Game(state)

        target = game.customers_locs[0]

        return __getDirection(self, target)

    def __getDirection(self, target):
        dirs = ['Stay', 'North', 'South', 'East', 'West']
        return choice(dirs)

