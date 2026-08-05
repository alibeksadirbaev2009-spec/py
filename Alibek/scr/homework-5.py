import math
from abc import ABC, abstractmethod

class GeometricForm(ABC):

    @abstractmethod
    def area(self):
        return "Area"
    
    @abstractmethod
    def perimetr(self):
        return "Perimetr"

class Triangle(GeometricForm):
    def __init__(self, a: int | float, b: int | float, c: int | float) -> None:
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

    def perimetr(self) -> float | int:
        return self.__a + self.__b + self.__c
    
    def area(self) -> float | int:
        p = self.perimetr() / 2
        return math.sqrt(p * (p - self.__a) * (p - self.__b) * (p - self.__c))

class Square(GeometricForm):
    def __init__(self, a: int | float, b: int | float, c: int | float, d: int | float) -> None:
        if not isinstance(a, (int, float)):
            raise TypeError("Ta'repleri int yamasa float boliwi kerek")
        if a < 0 or b < 0 or c < 0 or d < 0:
            raise ValueError("Ta'rep 0 den u'lken boliwi kerek")
        if not (a == c and b == d):
            raise ValueError("Qarama qarsi ta'repleri ten' boliwi kerek")
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d

    def area(self) -> float | int:
        return self.__a * self.__b

    def perimetr(self) -> float | int:
        return self.__a + self.__b + self.__c +self.__d

form1 = Triangle(10, 10, 12)
form2 = Square(10, 12, 10, 12)
print("Perimeter triangle:", round(form1.perimetr(), 2))
print("Area triangle:", round(form1.area(), 2))
print("Perimetr square:", round(form2.perimetr(), 2))
print("Area square:", round(form2.area(), 2))    

# 2
# class instance method, @classmethod, @staticmethod  qalegen bir misal jaratiw erkin tema an'sat emes

class Car:
    brand = "BMW"

    def __init__(self, model):
        self.__model = model

    def show_model(self):
        print(self.__model)

    @classmethod
    def show_brand(cls):
        print(cls.brand)

    @staticmethod
    def miles_to_km(miles):
        return miles * 1.609


c = Car("M")

print("Model:")
c.show_model()

print("Brand:")
Car.show_brand()

print("Miles to km:", Car.miles_to_km(10))



class Person:
    count = 0
    people = []

    def __init__(self, name):
        self.__name = name
        Person.count += 1
        Person.people.append(name)

    def say_hello(self):
        print(f"Hi, my name is {self.__name}")

    @classmethod
    def show_count(cls):
        print(f"Ja'mi adamlar: {cls.count}")

    @classmethod
    def show_people(cls):
        print("Adamlar royxati:", cls.people)

    @staticmethod
    def is_adult(age):
        return age >= 18

p1 = Person("Ali")
p2 = Person("Vali")
p3 = Person("Muxammadali")

p1.say_hello()
p2.say_hello()

Person.show_count()
Person.show_people()

print("Is Ali adult?", Person.is_adult(17))
print("Is Vali adult?", Person.is_adult(20)) 
