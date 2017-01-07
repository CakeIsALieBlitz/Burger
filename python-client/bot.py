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
                #self.customer = game.customers[0]
            self.customer = self.getNearestCustomer(game.myHero, game.customers, game)
            self.isFirstTime = False
            self.getNewTarget(game)
            self.nbBurger = game.myHero.nbBurger
            self.nbFries = game.myHero.nbFrittes
            self.calories = game.myHero.calories

        self.getNewTarget(game)
        return self.__getDirection(game, self.target, game.myHero.pos)

    def __getDirection(self, game, target, start):
        theMap = game.state['game']['board']
        size = game.board.size
        #print(target)
        return self.pathFinder.getPath(theMap, size, start, target)

    def getNewTarget(self, game):
        #self.customer = self.getNearestCustomer(game.myHero, game.customers, game)
        if game.myHero.nbFrittes < self.customer.french_fries :
            #print("frite")
            self.target = self.trouverFritte(game)
        elif game.myHero.nbBurger < self.customer.burger :
            #print("burger")
            self.target = self.trouverBurger(game)
        else:
            #print("customer")
            self.getNewCustomer(game)

    def getNewCustomer(self, game):
        self.customer = self.getNearestCustomer(game.myHero, game.customers, game)
        self.target = self.customer.pos


    def trouverFritte(self, game):
        self.current_target = "fries"
        return self.getNearestObjective(game.myHero, game.fries_locs)

    def trouverBurger(self, game):
        self.current_target = "burger"
        return self.getNearestObjective(game.myHero, game.burger_locs)

    def distance(self, pos1, pos2):
        x = (pos2[0] - pos1["x"])
        y = (pos2[1] - pos1["y"])
        return y, x

    def getNearestObjective(self, myHero, objective_type_locs):
        not_owned_objective = []

        # print(objective_type_locs)
        for objective in objective_type_locs.keys():
            if objective_type_locs[objective] != myHero.id:
                not_owned_objective.append(objective)
        # print(not_owned_objective)

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

    def getNearestCustomer(self, myHero, customers, game):
        deltaX = 999999
        deltaY = 999999
        wantedCustomer = customers[0]
        for i in range(0,len(customers)):
            objective_position = customers[i].pos
            distance_calculated = self.distance(myHero.pos, objective_position)
            if (deltaX + deltaY > distance_calculated[0] + distance_calculated[1]):
                deltaX = distance_calculated[0]
                deltaY = distance_calculated[1]
                wantedCustomer = customers[i]

        return wantedCustomer
