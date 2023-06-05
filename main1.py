import math


class RightTriangle:
    def __init__(self, first_cathetus, second_cathetus):
        self.first_cathetus = first_cathetus
        self.second_cathetus = second_cathetus

    def alpha_tangent(self):
        alpha = self.second_cathetus / self.first_cathetus
        return alpha

    def info(self):
        return f'Первый катет: {self.first_cathetus}\nВторой катет: {self.second_cathetus}'


if __name__ == '__main__':
    a = float(input('Введите первый катет: '))
    b = float(input('Введите второй катет: '))
    triangle = RightTriangle(a, b)
    print(f'Тангенц угла альфа = {triangle.alpha_tangent()}')
