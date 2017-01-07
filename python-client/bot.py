from random import choice
from game import Game
from PathFinding import PathFinding


class Bot:
    pass

class BasicBot(Bot):
    def move(self, state):
        game = Game(state)
        dirs = ['Stay', 'North', 'South', 'East', 'West']
        return choice(dirs)

class RandomBot(Bot):

    def __init__(self):
        self.targets = []

    def move(self, state):
        game = Game(state)

        if (len(self.targets) == 0):
            self.targets = list(game.customers_locs)
            self.target = self.targets[0]

        return self.__getDirection(self.target, game)

    def __getDirection(self, target, game):
        start = "(" + game.myHero.pos[0] + "," + game.myHero.pos[1] + ")"
        target = "(" + target[0] + "," + target[1] + ")"
        return PathFinding.getPath(game.board.tiles, game.board.size, start, target)

class SimpleBot(Bot):
    def __init__(self):
        self.isFirstTime = True

    def move(self, state):
        game = Game(state)

        if (self.isFirstTime):
            self.isFirstTime = False
            self.custommer = game.custommers[0]
            self.target = game.myHero.pos

        if(game.myHero.pos == self.target):
            if(game.myHero.nbFrittes < self.custommer.french_fries):
                self.target = self.trouverFritte(game)
            elif(game.myHero.nbBurger < self.custommer.burger):
                self.target = self.trouverBurger(game)
            else:
                self.target = self.custommer.pos

        return self.__getDirection(self.target, game)

    def trouverFritte(self, game):
        return choice(game.fries_locs)

    def trouverBurger(self, game):
        return choice(game.burger_locs)

    def __getDirection(self, target, game):
        return 'North'


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
