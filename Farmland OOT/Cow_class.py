from Animal_class import *

class Cow(Animal):
    """A cow class"""

    def __init__(self, name):
        #call the parent class constructor with default values for a Cow
        #growth rate = 1; Food need = 3 water need = 6, name = "No name"
        super().__init__(1,3,6, "No name")
        self._type = "Cow"
        self._name = name

    #override grow method for subclass
    def grow(self, food, water):
        if food >= self._food_need and water >= self._water_need:
            if (self._status == "Baby") and (food > self._food_need):
                self._weight += (self._growth_rate * 1.7)
            elif (self._status == "Young") and (food > self._food_need):
                self._weight += (self._growth_rate * 1.5)
            elif (self._status == "Mature") and (food > self._food_need):
                self._weight += (self._growth_rate * 1.25)
            else:
                self._weight += self._growth_rate
        #increment days growing
        self._days_growing += 1
        #update the status
        self._update_status()



def main():
    #create a new potato crop
    cow_animal = Cow("John")
    print(cow_animal.report())
    #manually grow the crop
    manual_grow(cow_animal)
    print(cow_animal.report())

if __name__ == "__main__":
    main()





