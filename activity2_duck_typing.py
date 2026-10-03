class Car:
    def move(self):
        print("Car is driving on the road.")



class Person:
    def move(self):
        print("Person is walking.")


class Robot:
    def move(self):
        print("Robot is moving mechanically.")


def make_it_move(thing):
    thing.move()


car = Car()
person = Person()
robot = Robot()
things = [car, person, robot]


for thing in things:
    make_it_move(thing)