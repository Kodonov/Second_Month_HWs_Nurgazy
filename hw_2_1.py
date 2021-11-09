# *****************************************************************************************************************************

class Employee:
    def __init__(self, name, age, gender, nationality, active):
        self.name = name
        self.age = age
        self.gender = gender
        self.nationality = nationality
        self.active = active

    def is_active(self):
        return f' {self.active}'

    def __str__(self):
        return f"name : {self.name}\n"\
               f"age : {self.age}\n" \
               f"gender : {self.gender}\n" \
               f"nationality : {self.nationality}\n" \
               f"active: {self.active}\n"


em1 = Employee("koly", 26, "male", "kyrgyz", True)
print(em1)


class Treinee(Employee):
    def __init__(self,name, age, gender, nationality, active, language, ):
        super().__init__(name, age, gender, nationality, active)
        self.language = language
        
    
    def __str__(self):
        return super(Treinee, self).__str__()+f" \nlanguage:{self.language}\n"\
                                                

trein_1= Treinee(name="andrey",
                  age=35,
                  gender="male",
                  nationality="rassian",
                  active=True,
                  language="Javasckript")                 
                  

print(trein_1.is_active())
print(trein_1)                                               

class Developer(Treinee):
    def __init__(self, name, age, gender, nationality, active,language ,lvl,an_experiance):
        super().__init__(name, age, gender, nationality,active,language)
        self.lvl = lvl
        self.an_experiance = an_experiance

    def __str__(self):
        return super(Developer, self).__str__()+ f"\nlvl:{self.lvl}\n"\
                                                f"an_experiance:{self.an_experiance}\n"
dev_1 = Developer(name='Artur',
                    age=49,
                    gender="male",
                    nationality="dagestanec",
                    active=True,
                    language="JS, Py",
                     lvl="senior",
                     an_experiance=29)
print(dev_1)
print(dev_1.is_active())

# *****************************************************************************************************************************

class User:

    def _authorization(self):
        print("You are signed in")

    def __registration(self):
        print("You are signed up")

    def __init__(self):
        self._login = "Nurgazy"
        self.__password = 1234

# *****************************************************************************************************************************

class Sniper:
    def gun(self):
        print("Sniper shooting with AWM")

class Shooter:
    def gun(self):
        print("Shooter shooting with M-416")

class Scout:
    def gun(self):
        print("Scout shooting with USP and use knife")

# *****************************************************************************************************************************

class Grand_Father:
    def drive(self):
        print("Grand father drive on crossover")

class Father(Grand_Father):
    def drive(self):
        print("father drive on  hetchbak")

class Grandson(Father):
    def drive(self):
        print("Grandson drive on  bike")     



def gig(sit):
    sit.drive()


grand_Father = Grand_Father()
gig(grand_Father)
father = Father()
gig(father)
grandson = Grandson()
gig(grandson)
