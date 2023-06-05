import math

from main2 import ComplexNumber


class ComplexResistance(ComplexNumber):
    def __init__(self, real, imaginary, angular_frequency):
        super().__init__(real, imaginary)
        self.resistor_resistance = self.x.imag
        self.inductance = self.x.real
        self.angular_frequency = angular_frequency

    def arg(self):
        s = math.atan(self.resistor_resistance * self.inductance / self.angular_frequency)
        return s


if __name__ == '__main__':
    print('Введите комплексное число')
    a, b = int(input()), int(input())
    print('Введите значение угловой частоты')
    c = int(input())
    result = ComplexResistance(a, b, c)
    print(result.info())
    print('Градус комплексного числа', result.arg())

    p: int = 0
