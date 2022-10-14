import ipdb

class Animal:

    def __init__(self, color, food_type):
        print('I am init')
        self.color = color
        self.food_type = food_type

    def move(self):
        print("animal move")

    def eat(self):
        print("animal eats")
        print(f"this animal eats {self.food_type}")

    def breath(self):
        print("animal breaths")


my_animal1 = Animal('blue', 'meat')
# my_animal2 = Animal('vegetarian', 'red')

print(my_animal1)

# my_animal1.move()
# my_animal2.move()

# print(my_animal1)
# print(my_animal2)

ipdb.set_trace()