import math


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.x = complex(real, imaginary)

    def info(self):
        return f'Действительная часть = {self.x.real}\nМнимая часть = {self.x.imag}'

    def multiply_by_number(self, num):
        self.x *= num

    def degrees_number(self):
        arg_in_radians = math.atan2(self.x.real, self.x.imag)
        return math.degrees(arg_in_radians)

    def __del__(self):
        print("Объект удален")


if __name__ == '__main__':
    print('Введите комплексное число')
    a, b = int(input()), int(input())
    result = ComplexNumber(a, b)
    print(result.x)
    print(result.info())
    x = int(input('Введите число для получения произведение копмлексного числа: '))
    result.multiply_by_number(x)
    print(result.info())
    print('Градус комплексного числа', result.degrees_number())


