import random

class TimeDesk:
    def __init__(self, seconds):
        self.seconds = seconds

    def time_2(self):
        min = self.seconds // 60
        self.seconds -= 60*min

        hours = self.seconds // 3600
        self.seconds -= 3600*hours

        day = self.seconds // 86400
        self.seconds -= 86400*day

        general_resultat = (f'day: {day}, hours: {hours} min: {min}, seconds: {self.seconds}')
        return general_resultat


time_1 = TimeDesk(80)
print(time_1.time_2())


class Flowers:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    @property
    def general(self):
        flowers = self.name + '' + self.color
        return  flowers

    @general.setter
    def genearal(self, flowers):
        self.name, self.color = flowers.split()

    @general.deleter
    def general(self):
        self.name = None
        print('Name delete')

    def __str__(self):
        return f'flowers: {self.name}  {self.color}'

    @staticmethod
    def for_all(age):
        if age > 0:
            return True
        else:
            return False

flowers1 = Flowers(name='Roza', color='white')
print(flowers1)
print(flowers1.general)

flowers1.name = 'romashka'
print(flowers1.general)

del flowers1.general
print(flowers1.general)

print(flowers1.for_all(67))




