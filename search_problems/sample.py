class Celcius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature(self):
        print("Getting Value ...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        print("Setting Value ...")
        self._temperature = value

# example usage
c = Celcius(37)
# print(c.temperature)
c.temperature = -300