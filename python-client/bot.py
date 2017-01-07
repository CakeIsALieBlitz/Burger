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
            self.customer = game.customers[0]
            self.target = game.myHero.pos

        if game.myHero.pos == self.target :
            if game.myHero.nbFrittes < self.customer.french_fries :
                self.target = self.trouverFritte(game)
            elif game.myHero.nbBurger < self.customer.burger :
                self.target = self.trouverBurger(game)
            else:
                self.target = self.customer.pos

            return self.__getDirection(game, self.target, game.myHero.pos)

    def __getDirection(self, game, target, start):
        theMap = game.state['game']['board']
        size = game.board.size
        return self.pathFinder.getPath(theMap, size, start, target)

    def trouverFritte(self, game):
        key = choice(game.fries_locs.keys())
        print(game.fries_locs[key])
        return game.fries_locs.pop(key)

    def trouverBurger(self, game):
        return game.burger_locs.pop()


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
