# множественное Наследование (один ко многим)

class Geektech:
    def __init__(self, name, duration, price, direction_to_create, study):
        self.name = name
        self.duration = duration
        self.price = price
        self.direction_to_create = direction_to_create
        self.study = study

    def learn(self):
        return f'This duration can learn: {self.duration},  month'

    def __str__(self, ):
        return f'name:{self.name}\n' \
               f'duration:{self.duration}\n' \
               f'price:{self.price}\n' \
               f'direction_to_create:{self.direction_to_create}\n' \
               f'study:{self.study}\n'


Android_1 = Geektech(name='Mira', duration=8, price=12000, direction_to_create='app', study='java')


class Backend(Geektech):
    def learn(self):
        return f' This duration can learn: {self.duration}, month'

    def can(self):
        return f'This direction is{self.study} studying for web programming'

    def __str__(self):
        return super(Backend, self).__str__()


Backend_1 = Backend(name='Nurik', duration=4, price=12000, direction_to_create='web sites', study='Python, Django')


class Frontend(Geektech):
    def can_learn(self):
        return f' This duration can learn: {self.duration}, month'

    def can(self):
        return f'This direction is{self.study} studying for web programming'

    def __str__(self):
        return super(Frontend, self).__str__()


Frontend_1 = Frontend(name='Artur', duration=5, price=12000, direction_to_create='disagn for web sites',
                      study='javascript')


class Ios(Geektech):
    def can_learn(self):
        return f'This duration can learn: {self.duration}, month'

    def can(self):
        return f'This direction is{self.study} studying for web programming'

    def __str__(self):
        return super(Ios, self).__str__()


Ios_1 = Ios(name='Maks', duration=7, price=120000, direction_to_create="apps for ios", study='java')

print(Android_1)
print(Android_1.learn())
print(Backend_1)
print(Backend_1.learn)
print(Backend_1.can())
print(Frontend_1.can_learn())
print(Frontend_1.can())
print(Ios_1.can_learn())
print(Ios_1.can())


class Trees:
    def __init__(self, name, can_live, grade, price_for_kg):
        self.name = name
        self.can_live = can_live
        self.grade = grade
        self.price_for_kg = price_for_kg

    def grade1(self):
        return f'can_bear_fruit_for_years{self.can_live}\n'

    def __str__(self):
        return f" name:{self.name}\n" \
               f'can_live:{self.can_live}\n' \
               f'grade:{self.grade}\n' \
               f'price_for_kg:{self.can_live}\n' \

trees_1 = Trees(name='Persik', can_live=15, grade='Lola', price_for_kg=100)


class Applee(Trees):

    def grade1(self):
        return f'can_bear_fruit_for_years{self.can_live}\n'

    def unique(self):
       return f'continues_to_bear_fruit_in_winter {self.grade}\n'

    def __str__(self):
        return super(Applee, self).__str__()


apple_1 = Applee(name='apple', can_live=25, grade='zimeryanka', price_for_kg=100)


class Redapple(Trees):

    def grade1(self):
        return f'can_bear_fruit_for_years{can_live}\n'

    def harvest(self):
        return f'a lot of harvest {grade}\n '

    def __str__(self):
        return super(Redapple, self).__str__()


apple_2 = Redapple(name='redapple', can_live=30, grade='redapple', price_for_kg=80)


class Karlickapple(Applee, Redapple):

    def grade1(self):
        return f'can_bear_fruit_for_years{self.can_live}\n'

    def expensive(self):
        return f'harvest_is_small_but_expensive{self.grade}\n'


karlick = Karlickapple(name='apple', can_live=15, grade='karlick', price_for_kg=150)
print(karlick)
print(karlick.grade1())
print(karlick.expensive())

