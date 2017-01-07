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
        return self.getNearestObjective(game.myHero, game.fries_locs)

    def trouverBurger(self, game):
        self.current_target = "burger"
        return self.getNearestObjective(game.myHero, game.burger_locs)

    def distance(self, pos1, pos2):
        x = (pos2[0] - pos1["y"])
        y = (pos2[1] - pos1["x"])
        return y, x

    def getNearestObjective(self, myHero, objective_type_locs):
        not_owned_objective = []

        for objective in objective_type_locs.keys():
            if objective_type_locs[objective] != myHero.id:
                not_owned_objective.append(objective)

        deltaX = 999999
        deltaY = 999999

        for objective_position in not_owned_objective:
            distance_calculated = self.distance(myHero.pos, objective_position)
            if (deltaX + deltaY > distance_calculated[0] + distance_calculated[1]):
                deltaX = distance_calculated[0]
                deltaY = distance_calculated[1]
                self.wantedPosition = objective_position

        return (deltaX, deltaY)

    def getNearestCustomer(self, myHero, objective_type_locs):
        deltaX = 999999
        deltaY = 999999

        for objective_position in objective_type_locs:
            distance_calculated = self.distance(myHero.pos, objective_position)
            if (deltaX + deltaY > distance_calculated[0] + distance_calculated[1]):
                deltaX = distance_calculated[0]
                deltaY = distance_calculated[1]
                self.wantedPosition = objective_position

        return (deltaX, deltaY)