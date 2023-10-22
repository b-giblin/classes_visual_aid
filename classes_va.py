#  ---------------          ---------------
# |   Blueprint   |  ---->  |   Actual    |
# | for a "House" |        |    House    |
#  ---------------          ---------------


class House:
    def __init__(self, rooms):
        self.rooms = rooms

    def open_door(self):
        print("Door opened!")

    def close_door(self):
        print("Door closed!")

    def add_room(self, room):
        self.rooms.append(room) 


houseA = House(3)
houseB = House(4)
houseC = House(5)


class Car:
    def turn_on(self):
        print("Car is now on!")

    def open_doors(self):
        print("Doors are open!")

    def start_engine(self):
        print("Engine started!")