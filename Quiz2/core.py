class Pet:
    def __init__(self, name, age ,type, color, numberOfPets, price = 50000):
        self.__name = name
        self.__age = age
        self.__type = type
        self.__color = color
        self.__numberOfPets = numberOfPets
        self.__price = price

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getType(self):
        return self.__type

    def getColor(self):
        return self.__color

    def getNumberOfPets(self):
        return self.__numberOfPets

    def setName(self, name):
        self.__name = name

    def setAge(self,age):
        self.__age = age

    def setType(self, type):
        self.__type = type

    def setColor(self,color):
        self.__color = color

    def setNumberOfPets(self, numberOfPets):
        self.__numberOfPets = numberOfPets

    def getPrice(self):
        return self.__price

    def setPrice(self, price):
        self.__price = price
