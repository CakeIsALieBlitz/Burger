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
        self.updateOrder(game)
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
        print(target)
        return self.pathFinder.getPath(theMap, size, start, target)

    def updateClient(self, game):
        if(game.myHero.nbBurger < self.nbBurger):
            self.getNewTarget(game)
        if(game.myHero.nbFrittes < self.nbFries):
            self.getNewTarget(game)
        if(self.calories < game.myHero.calories):
            self.getNewTarget(game)

    def updateFries(self, game):
        if(game.myHero.nbFrittes < self.nbFries):
            self.getNewTarget(game)
        elif(game.myHero.nbFrittes > self.nbFries):
            self.getNewTarget(game)

    def updateOrder(self, game):
        if(not self.isFirstTime):
            nowOrder = game.customers[self.nbCustomer]
            if(self.customer.burger != nowOrder.burger):
                self.getNewTarget(game)
                self.customer = game.customers[self.nbCustomer]
            if(self.customer.french_fries != nowOrder.french_fries):
                self.getNewTarget(game)
                self.customer = game.customers[self.nbCustomer]

    def updateBurger(self, game):
        if(game.myHero.nbBurger < self.nbBurger):
            self.getNewTarget(game)
        elif(game.myHero.nbBurger > self.nbBurger):
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
        self.nbCustomer += 0
        self.current_target = "Client"
        self.customer = game.customers[self.nbCustomer]
        self.target = self.customer.pos


    def trouverFritte(self, game):
        self.current_target = "fries"
        return self.getNearestObjective(game.myHero, game.fries_locs, game)

    def trouverBurger(self, game):
        self.current_target = "burger"
        return self.getNearestObjective(game.myHero, game.burger_locs, game)

    def distance(self, pos1, pos2):
        x = (pos2[0] - pos1["x"])
        y = (pos2[1] - pos1["y"])
        return y, x

    def getNearestObjective(self, myHero, objective_type_locs, game):
        not_owned_objective = []

        for objective in objective_type_locs.keys():
            if objective_type_locs[objective] != myHero.id:
                not_owned_objective.append(objective)

        deltaX = 999999
        deltaY = 999999

        wantedPosition = myHero.pos
        for objective_position in not_owned_objective:
            distance_calculated = self.distance(myHero.pos, objective_position)
            if (deltaX + deltaY > distance_calculated[0] + distance_calculated[1]):
                deltaX = distance_calculated[0]
                deltaY = distance_calculated[1]
                wantedPosition = objective_position

        return wantedPosition

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
