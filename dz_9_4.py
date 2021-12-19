class Car:
    def __init__(self, name, color, speed, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


    def go(self):
        return f"{self.name} {self.color} Go!"


    def stop(self):
        return f"{self.name} {self.color} Stop!"


    def turn_right(self):
        return f"{self.name} {self.color} turned right!"


    def turn_left(self):
        return f"{self.name} {self.color} turned left!"


    def show_speed(self):
        if self.is_police is True:
            return f"Police car {self.name} rides with speed {self.speed} km/h"
        else:
            return f"{self.name} rides with speed {self.speed} km/h"


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f"{Car.show_speed(self)}. Over speed {self.speed - 60} km/h!"
        else:
            return Car.show_speed(self)


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f"{Car.show_speed(self)}. Over speed {self.speed - 40} km/h!"
        else:
            return Car.show_speed(self)


class SportCar(Car):
    def show_speed(self):
        return f"Sport car {Car.show_speed(self)}"


class PoliceCar(Car):
    def show_speed(self):
        if self.is_police is True:
            return Car.show_speed(self)
        else:
            return Car.show_speed(self)


toyota = WorkCar('Toyota', 'white', 60, False)
print(toyota.go())
print(toyota.turn_right())
print(toyota.turn_left())
print(toyota.show_speed())
print(toyota.stop(), end="\n\n")

opel = TownCar('Opel', 'royal blue', 70, False)
print(opel.go())
print(opel.turn_right())
print(opel.turn_left())
print(opel.show_speed())
print(opel.stop(), end="\n\n")

mercedes = PoliceCar('Mercedes', 'black', 100, True)
print(mercedes.go())
print(mercedes.turn_right())
print(mercedes.turn_left())
print(mercedes.show_speed())
print(mercedes.stop(), end="\n\n")