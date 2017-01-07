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
        self.pathFinder = PathFinding()

    def move(self, state):
        game = Game(state)

        client_target = game.customers_locs.pop()
        hero_pos = game.myHero.pos

        return self.__getDirection(game, client_target, hero_pos)

    def __getDirection(self, game, target, start):
        theMap =game.state['game']['board']
        size = game.board.size
        return self.pathFinder.getPath(theMap,size, start, target)

class SimpleBot(Bot):
    def __init__(self):
        self.isFirstTime = True
        self.pathFinder = PathFinding()

    def move(self, state):
        game = Game(state)

        if (self.isFirstTime):
            self.isFirstTime = False
            self.customer = 0
            self.target = self.trouverFritte(game)
            self.nbFries = game.myHero.nbFrittes
            self.nbBurger = game.myHero.nbBurger
            self.bump = False

        print(self.isAdjacent(game.myHero.pos, self.target))

        if self.isAdjacent(game.myHero.pos, self.target):
            if self.bump:
                self.bump = False
                if game.myHero.nbFrittes < game.customers[self.customer].french_fries:
                    self.target = self.trouverFritte(game)
                elif game.myHero.nbBurger < game.customers[self.customer].burger:
                    self.target = self.trouverBurger(game)
                else:
                    self.target = game.customers[self.customer].pos
            else:
                self.bump = True

        return self.__getDirection(game, self.target, game.myHero.pos)

    def isAdjacent(self, pos1, pos2):
        pos1 = list(pos1)
        pos2 = list(pos2)
        print(pos1)
        print(pos2)
        if pos1[0] == pos2[0]:
            if abs(pos1[1] - pos2[1]) == 1:
                return True
        elif pos1[1] == pos2[1]:
            if abs(pos1[0] - pos2[0]) == 1:
                return True
        return False

    def __getDirection(self, game, target, start):
        theMap = game.state['game']['board']
        size = game.board.size
        return self.pathFinder.getPath(theMap, size, start, target)

    def trouverFritte(self, game):
        return choice(list(game.fries_locs.keys()))

    def trouverBurger(self, game):
        return choice(list(game.burger_locs.keys()))

class Target:
    def __init__(self, pos, type):
        self.pos = pos
        self.type = type


class IntelligentBot(Bot):
    def move(self, state):
        game = Game(state)
        dirs = ['Stay', 'North', 'South', 'East', 'West']
        return choice(dirs)

    def getClientPosition(self):
        print("GetClient")

    def getFriesPosition(self):
        print("GetFries")

    def getBurgerPosition(self):
        print("GetBurger")

    def getDirections(self):
        print("GetDirection")
