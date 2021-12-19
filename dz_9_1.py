from time import sleep

class TrafficLight:
    __color = " "

    def running(self, color):
        self.__color = color


light = TrafficLight()
light.running("  ")
print(f"\033[31m\033[41m {light._TrafficLight__color}", end='')
sleep(7)
print(f"\r\033[0m {light._TrafficLight__color}", end='')
print(f"\033[33m\033[43m {light._TrafficLight__color}", end='')
sleep(2)
print(f"\r\033[0m {light._TrafficLight__color}", end='')
print(f"\033[0m {light._TrafficLight__color}", end='')
print(f"\033[32m\033[42m {light._TrafficLight__color}", end='')
sleep(7)
print(f"\r\033[0m {light._TrafficLight__color}", end='')
print(f"\033[33m\033[43m {light._TrafficLight__color}", end='')
sleep(2)
print(f"\r\033[0m {light._TrafficLight__color}", end='')
print(f"\r\033[31m\033[41m {light._TrafficLight__color}", end='')