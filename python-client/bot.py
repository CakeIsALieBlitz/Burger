from random import choice
from game import Game


class Bot:
    pass


class RandomBot(Bot):
    def move(self, state):
        game = Game(state)
        dirs = ['Stay', 'North', 'South', 'East', 'West']
        return choice(dirs)

class IntelligentBot(Bot):
    def move(self, state):
        game = Game(state)
        dirs = ['Stay', 'North', 'South', 'East', 'West']
        game.board.passable
        return choice(dirs)

    def getClientPosition(self):
        print("GetClient")

    def getFriesPosition(self):
        print("GetFries")

    def getBurgerPosition(self):
        print("GetBurger")

    def getDirections(self):
        print("GetDirection")
