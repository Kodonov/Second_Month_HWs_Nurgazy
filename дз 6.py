class Algoritm:
    def example(self):
        equals = [2, 5, 7, 9, 12, 31, 25, 91]
        for_example = 56
        for first in equals:
            for second in equals:
                if first+second == for_example:
                    print([first, second])

answer = Algoritm()
answer.example()
