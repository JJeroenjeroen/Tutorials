import random

class Animal:
    """This class will include attributes of a given Animal"""

    #Contructor
    def __init__(self, growth_rate, food_need, water_need, name):

        #Set initial attributes for the class
        #The underscores in front of the attributes indicate that the attributes are private
        #(can't be altered from outside the class)

        self._weight = 3
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._food_need = food_need
        self._water_need = water_need
        self._status = "Baby"
        self._type = "Generic animal"
        self._name = "Name"


    def needs(self):

        #Return a dictionary containing the food and water needs
        return {'Daily food need': self._water_need,'Daily water need': self._water_need}

    def report(self):
        # Return a dictionary containing the type, status, growth and days growing
        return {'name': self._name,
                'type': self._type,
                'status': self._status,
                'growth': self._weight,
                'days growing': self._days_growing}

    def _update_status(self):
        #Method that updates the status depending on the animal's growth
        if self._weight > 30:
            self._status = "Old"
        elif self._weight> 20:
            self._status = "Mature"
        elif self._weight > 10:
            self._status = "Adolescent"
        elif self._weight > 3:
            self._status = "Young"
        elif self._weight == 3:
            self._status = "Baby"


    def grow(self, food, water):
        #Define a function that tells how the animal is growing depending on the food and water it receives
        if food >= self._food_need and water >= self._water_need:
            self._weight += self._growth_rate

        #increment days growing
        self._days_growing += 1
        self._update_status()

def auto_grow(animal, days):
    #grow the animal
    for day in (range(days)):
        food = random.randint(1,10)
        water = random.randint(1, 10)
        animal.grow(food, water)

def manual_grow(animal):
    #get the food and water values from the user
    valid = False
    while not valid:
        try:
            food = int(input("Please enter a food value (1-10):"))
            if 1 <= food <= 10:
                valid = True
            else:
                print("Value entered not valid - Please enter a value between 1 and 10:")
        except ValueError:
            print("Value entered not valid - Please enter a value between 1 and 10:")

    #now for water
    valid = False
    while not valid:
        try:
            water = int(input("Please enter a water value (1-10):"))
            if 1 <= water <= 10:
                valid = True
            else:
                print("Value entered not valid - Please enter a value between 1 and 10:")
        except ValueError:
            print("Value entered not valid - Please enter a value between 1 and 10:")

    #grow the animal
    animal.grow(food, water)


def display_menu():
    print("1. Grow manually over 1 day")
    print("2. Grow automatically over 30 days")
    print("3. Report status")
    print("0. Exit test program")
    print()
    print("please select an option from the above menu")

def get_menu_choice():
    option_valid = False
    while not option_valid:
        try:
            choice = int(input("Option selected: "))
            if 0 <= choice <= 3:
                option_valid = True
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")
    return choice

def manage_animal(animal):
    print("This is the animal management program")
    print()
    noexit = True

    while noexit:
        display_menu()
        option = get_menu_choice()
        print()
        if option == 1:
            manual_grow(animal)
            print()
        elif option == 2:
            auto_grow(animal, 30)
            print()
        elif option == 3:
            print(animal.report())
            print()
        elif option == 0:
            noexit = False
            print()
    print("Thank you for using the animal management program")



def main():
    #instantiate the class
    new_animal = Animal(1,4,3)
    manage_animal(new_animal)


if __name__ == "__main__":
    main()
