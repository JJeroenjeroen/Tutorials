from Animal_class import *

class Sheep(Animal):
    """A sheep class"""

    def __init__(self, name):
        #call the parent class constructor with default values for a Sheep
        #name = "Shheeep" growth rate = 1.5; Food need = 3 water need = 3, name = "No name"
        super().__init__(1.5,3,3, "No name")
        self._type = "Sheep"
        self._name = name

    #override grow method for subclass
    def grow(self, food, water):
        if food >= self._food_need and water >= self._water_need:
            if (self._status == "Baby") and (food > self._food_need):
                self._weight += (self._growth_rate * 1.2)
            elif (self._status == "Young") and (food > self._food_need):
                self._weight += (self._growth_rate * 1.3)
            elif (self._status == "Mature") and (food > self._food_need):
                self._weight += (self._growth_rate * 1.2)
            else:
                self._weight += self._growth_rate
        #increment days growing
        self._days_growing += 1
        #update the status
        self._update_status()



def main():
    #create a new potato crop
    sheep_animal = Sheep()
    print(sheep_animal.report())
    #manually grow the crop
    manual_grow(cow_animal)
    print(sheep_animal.report())

if __name__ == "__main__":
    main()

