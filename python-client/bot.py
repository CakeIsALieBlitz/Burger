from random import choice
from game import Game
from PathFinding import PathFinding


class Bot:
    pass


class RandomBot(Bot):
    def move(self, state):
        game = Game(state)

        target = game.customers_locs

        return __getDirection(self, target, game)

    def __getDirection(self, target, game):
        start = "(" + game.myHero.pos[0] + "," + game.myHero.pos[1] + ")"
        target = "(" + target[0] + "," + target[1] + ")"
        return PathFinding.getPath(game.board.tiles, game.board.size, start, target)

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
