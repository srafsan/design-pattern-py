class Celsius:
    def __init__(self, temparature=0):
        self.set_temparature(temparature)

    def to_fahrenheit(self):
        return (self._temparature * 1.8) + 32

    def get_temparature(self):
        print("Getting temperature...")
        return self._temparature

    def set_temparature(self, value):
        print("Setting temperature...")
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible")
        self._temparature = value

    # Creating a property object
    temparature = property(get_temparature, set_temparature)

human = Celsius(37)

print(human.temparature)
print(human.to_fahrenheit())
human.temparature = -300