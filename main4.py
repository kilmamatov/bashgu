import math
from main2 import ComplexNumber


class ComplexResistance(ComplexNumber):
    def __init__(self, real, imaginary):
        super().__init__(real, imaginary)
        self.angular_frequency = math.sqrt(self.x.real / self.x.imag)

    def value(self):
        s = abs(math.sqrt(self.x.real**2 + self.x.imag**2))
        return s

    def info(self):
        return f'Действительная часть = {self.x.real}\n' \
               f'Мнимая часть = {self.x.imag}\n' \
               f'Угловая частота = {self.angular_frequency}'


if __name__ == '__main__':
    print('Введите комплексное число')
    a, b = int(input()), int(input())
    result = ComplexResistance(a, b)
    print(result.info())
    print('Градус комплексного числа', result.value())

