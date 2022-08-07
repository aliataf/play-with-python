class Alpha:

    def __init__(self):
        self._a = 2.  # Protected member ‘a’
        self.__b = 7.  # Private member ‘b’

""" a = Alpha()
print(a._Alpha__b) """

class MyClass:
    a = 5

    def hello(self):
        print('Hello World')

""" myc = MyClass()
print(myc.a)
print(myc.hello()) """

class House:
    num_rooms = 5
    bathrooms = 2
    def cost_evaluation(self):
        print(self.num_rooms)
        pass
""" house = House()
print(house.num_rooms)
print(House.num_rooms)
House.num_rooms = 7
print(house.num_rooms)
print(House.num_rooms) """

class Recipe:
    def __init__(self, dish, items, time) -> None:
        self.dish = dish
        self.items = items
        self.time = time
    
    def contents(self):
        print("The {} has {} and takes {} min to prepare".format(self.dish, self.items, self.time))
recipe = Recipe("Pizza", ['Tomato', 'Cheese', 'Dough'], 15)
recipe.contents()