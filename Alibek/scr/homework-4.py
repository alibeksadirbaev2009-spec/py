# # geo abc class eki //  area, perimetr metodi
# # miyras figuralar ozgeriwshiler incaptsuliyatsiya sirtan ozgertilmewi

from abc import ABC, abstractmethod
import math


class geometry(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Triangle(geometry):
    def __init__(self, a , b, c) -> None:
        if not isinstance(a, (int, 
float)) or not isinstance(b, (int, 
float)) or not isinstance(c, (int, float)):
            raise TypeError("Ta'repleri int yamasa float boliwi kerek")
        
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Ta'repleri 0 den u'lken boliwi kerek")
        
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("U'shmu'yish bola almaydi")
        self.__a = a
        self.__b = b
        self.__c = c

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def get_c(self):
        return self.__c

    def perimeter(self):
        return self.__a + self.__b + self.__c
    
    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.__a) * (p - self.__b) * (p - self.__c))

t = Triangle(3, 4, 5)
print("Perimeter triangle:", round(t.perimeter(), 1))
print("Area triangle:", round(t.area(), 1))


class square(geometry):
    def __init__(self, a) -> None:
        if not isinstance(a, (int, float)):
            raise TypeError("Ta'repleri int yamasa float boliwi kerek")
        if a <= 0:
            raise ValueError("Ta'rep 0 den u'lken boliwi kerek")
        
        self.__a = a

    def get_a(self):    
        return self.__a

    def perimeter(self):
        return 4 * self.__a 
    
    def area(self):
        return self.__a ** 2
    
k = square(10)
print("Perimetr square:", k.perimeter())
print("Area square:", k.area())    


class circle(geometry):
    def __init__(self, r: float) -> None:
        if not isinstance(r, (int, float)):
            raise TypeError("Radius int yamasa float boliwi kerek")

        if r <= 0:
            raise ValueError("Radius 0 den u'lken boliwi kerek")

        self.__r = r  

    def get_r(self):
        return self.__r

    def perimeter(self):
        return 2 * math.pi * self.__r     # P = 2πr

    def area(self):
        return math.pi * self.__r ** 2   # C = π * r **2
    
l = circle(11)
print("Perimetr circle:", round(l.perimeter(), 2))
print("Area circle:", round(l.area(), 2))