class Road:
    def __init__(self, le, wi):
        self._lenght = le
        self._width = wi
        print(f"Длина полотна: {le} м.\nШирина полотна: {wi} м.")
        self.weight()

    def weight(self):
        print(f"Масса асфальта: "
                     f"{int((self._lenght * self._width * 25*100 * 5/100) / 1000)} т.")


m = Road(5000, 20)