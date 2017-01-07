from random import choice
from game import Game
from PathFinding import PathFinding


class Bot:
    pass

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
        self.current_target = "fries"
        self.nbCustomer = -1

    def move(self, state):
        game = Game(state)
        if(self.isFirstTime):
            self.customer = game.customers[0]
            self.isFirstTime = False
            self.getNewTarget(game)
            self.nbBurger = game.myHero.nbBurger
            self.nbFries = game.myHero.nbFrittes
            self.calories = game.myHero.calories
        elif(self.current_target == "fries"):
            self.updateFries(game)
        elif(self.current_target == "burger"):
             self.updateBurger(game)
        else:
            self.updateClient(game)


        return self.__getDirection(game, self.target, game.myHero.pos)

    def __getDirection(self, game, target, start):
        theMap = game.state['game']['board']
        size = game.board.size
        return self.pathFinder.getPath(theMap, size, start, target)

    def updateClient(self, game):
        print("updateClient")
        if(game.myHero.nbBurger < self.nbBurger):
            self.getNewTarget(game)
        if(game.myHero.nbFrittes < self.nbFries):
            self.getNewTarget(game)
        if(self.calories < game.myHero.calories):
            print("on a un customer")
            self.getNewTarget(game)

    def updateFries(self, game):
        print("updateFries")
        if(game.myHero.nbFrittes < self.nbFries):
            print("voller")
            self.getNewTarget(game)
        elif(game.myHero.nbFrittes > self.nbFries):
            print("on a la fries")
            self.getNewTarget(game)

    def updateBurger(self, game):
        print("updateBurger")
        if(game.myHero.nbBurger < self.nbBurger):
            print("voller")
            self.getNewTarget(game)
        elif(game.myHero.nbBurger > self.nbBurger):
            print("on a le burger")
            self.getNewTarget(game)

    def getNewTarget(self, game):
        if game.myHero.nbFrittes < self.customer.french_fries :
            self.target = self.trouverFritte(game)
        elif game.myHero.nbBurger < self.customer.burger :
            self.target = self.trouverBurger(game)
        else:
            self.getNewCustomer(game)

    def getNewCustomer(self, game):
        self.nbFries = 0
        self.nbBurger =0
        self.calories = game.myHero.calories
        self.nbCustomer += 1
        self.current_target = "Client"
        self.customer = game.customers[self.nbCustomer]
        self.target = self.customer.pos


    def trouverFritte(self, game):
        self.current_target = "fries"
        return choice(list(game.fries_locs.keys()))

    def trouverBurger(self, game):
        self.current_target = "burger"
        return choice(list(game.burger_locs.keys()))


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
