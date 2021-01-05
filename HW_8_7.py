"""
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNumber:

    def __init__(self, real: float, imag: float):
        """
        :param real: - real part of a complex number
        :param imag: - imaginary part of a complex number
        """
        self.real = real
        self.imag = imag

    def __str__(self):
        return f"{self.real}+{self.imag}i"

    def __add__(self, other):
        if not isinstance(other, ComplexNumber):
            raise ValueError("Operand is not ComplexNumber")
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        if not isinstance(other, ComplexNumber):
            raise ValueError("Operand is not ComplexNumber")
        return ComplexNumber(self.real * other.real - self.imag * other.imag,
                             self.real * other.imag + self.imag * other.real)


if __name__ == '__main__':

    c1 = ComplexNumber(2, 4)
    c2 = ComplexNumber(3, 9)

    print(f"c1={c1}, c2={c2}, c1+c2={c1 + c2}, c1*c2={c1 * c2}")
