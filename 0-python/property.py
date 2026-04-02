class Celsius:
    def __init__(self, temparature=0):
        self.temparature = temparature

    def to_fahrenheit(self):
        return (self._temparature * 1.8) + 32

    @property
    def temparature(self):
        print("Getting temperature...")
        return self._temparature

    @temparature.setter
    def temparature(self, value):
        print("Setting temperature...")
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible")
        self._temparature = value

human = Celsius(37)
print(human.temparature)
print(human.to_fahrenheit())

try:
    human.temparature = -300
except ValueError as e:
    print(e)