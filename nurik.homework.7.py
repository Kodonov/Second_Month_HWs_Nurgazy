class Algorithm:
    def __init__(self):
        self.integer = [5, 1, 30, 10, 330,3,53,6,4,6,36,2,3,5,4,456,568,58,12,234,43,23,235,5]


    def bubble_sort(self):

        swapped = False

        for x in range(len(self.integer) -1, 0, -1):
             for o in range(x):
                 if self.integer[o] > self.integer[o + 1]:
                     self.integer[o], self.integer[o + 1] = self.integer[o + 1], self.integer[o]
                     swapped = True
             if swapped:
                swapped = False

             else:

                break

        return  self.integer

    def porteshin(self, lst):
        if len(lst) <= 1:
            return lst
        else:
            g = lst[0]
            left = list(filter(lambda x: x < g, lst))
            center = [x for x in self.integer if x == g]
            right = list(filter(lambda x: x > g, lst))
            return self.porteshin(left) + center + self.porteshin(right)

    def quick_sort(self):

        if len(self.integer) <= 1:
            return self.integer
        else:
            g = self.integer[0]
            left = list(filter(lambda x: x < g, self.integer))
            center = [x for x in self.integer if x == g]
            right = list(filter(lambda x: x > g, self.integer))
            return self.porteshin(left) + center + self.porteshin(right)


juki = Algorithm()
print(juki.bubble_sort())
print(juki.quick_sort())



class Light:
    def __init__(self):
        self.numbers = 343

    def palindrome_str(self):
     if self.numbers <= 0:
            return False
     qwe = 1
     for i in range(len(str(self.numbers))):
        if str(self.numbers)[i] != str(self.numbers)[len(str(self.numbers)) - qwe]:
            return False
        qwe += 1
        return True


kolobok = Light()
print(kolobok.palindrome_str())

