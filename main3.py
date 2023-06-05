import math
from main1 import RightTriangle


class DescendantB(RightTriangle):
    def __init__(self, first_cathetus, second_cathetus):
        super().__init__(first_cathetus, second_cathetus)
        self.beta = math.pi - self.alpha_tangent()

    def diff_between_beta_and_alpha(self):
        diff = abs(self.beta - self.alpha_tangent())
        return diff


if __name__ == '__main__':
    a = float(input('Введите первый катет: '))
    b = float(input('Введите второй катет: '))
    result = DescendantB(a, b)
    print(result.info())
    print(result.alpha_tangent())
    print(result.beta)
    print(result.diff_between_beta_and_alpha())
