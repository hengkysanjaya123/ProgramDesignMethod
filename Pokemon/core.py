class Pokemon:
    def __init__(self, name, hp, attackStat, defenseStat, moveSet , type):
        self.name = name
        self.hp = hp
        self.attackStat = attackStat
        self.defenseStat = defenseStat
        self.moveSet = moveSet
        self.type = type

    # @property
    # def nameSet(self):
    #     return self.name
    #
    # @nameSet.setter
    # def nameSet(self, value):
    #     self.name = value

    def getName(self):
        return self.name

    def getHp(self):
        return self.hp

    def getAttackStat(self):
        return self.attackStat

    def getDefenseStat(self):
        return self.defenseStat

    def getMoveSet(self):
        return self.moveSet

    def getType(self):
        return self.type

    def setName(self, name):
        self.name = name

    def setHp(self, hp):
        self.hp = hp

    def setAttackStat(self, attackStat):
        self.attackStat = attackStat

    def setDefenseSeat(self, defenseSeat):
        self.defenseStat = defenseSeat

    def setMoveSet(self, moveset):
        self.moveSet = moveset

    def powerUp(self, step = 5):
        self.hp += step
        self.attackStat += step
        self.defenseStat += step

    def setType(self, type):
        self.type = type

    def evolve(self , step = 5):
        self.moveSet += step


class Water(Pokemon):
    def __init__(self, name, hp, attackStat, defenseStat, moveSet, type, weight = 0):
        super(Water, self).__init__(name, hp, attackStat, defenseStat, moveSet  ,type)

        self.weight = weight


    def getWeight(self):
        return self.weight

    def setWeight(self, weight):
        self.weight = weight

class Fire(Pokemon):

    def __init__(self, name, hp, attackStat, defenseStat, moveSet, type, height = 0):
        super(Water, self).__init__(name, hp, attackStat, defenseStat, moveSet  ,type)

        self.height = height

    def getHeight(self):
        return self.height

    def setHeight(self, height):
        self.height = height


