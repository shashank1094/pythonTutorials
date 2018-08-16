# https://www.python-course.eu/python3_slots.php


# https://stackoverflow.com/questions/5587653/inheritance-and-inner-classes-in-python
class A:
    yay = True

    class Foo:
        alice = True


class B(A):
    nay = False

    class Foo:
        bob = False


class B(A):
    nay = False

    class Foo(A.Foo):
        bob = False


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def from_petname(cls, pet_name):
#         return cls(pet_name, 10)
#
#     @staticmethod
#     def is_allowed_to_vote(age):
#         if age < 18:
#             print("Can't vote.")
#         else:
#             print("Can vote.")
#
#
# class Employee(Person):
#     def __init__(self, name, age, emp_code):
#         super().__init__(name, age)
#         self.emp_code = emp_code
#
#
# p1 = Person("Shashank", 23)
# e1 = Employee("Shashank", 23, 1234)
# print(dir(p1), dir(e1), dir(Person), dir(Employee), sep="\n\n")


# class Student:
#     """Here goes the description for the class."""
#
#     # __slots__ = ("__name",)
#     def __init__(self, temp_name):
#         self.name = temp_name
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         if type(name) != str:
#             self.__name = None
#         else:
#             self.__name = name
#
#
# s1 = Student("shashank")
# print(s1.name)
#
# print("DICT OF OBJECT :: ", s1.__dict__)
# print("DICT OF CLASS :: ", Student.__dict__)
# print("DIR OF OBJECT :: ", dir(s1))
# print("DIR OF CLASS :: ", dir(Student))

# x = "xtop"
# y = "ytop"
#
#
# def func():
#     x = "xlocal"
#     y = "ylocal"
#     print("INSIDE func() LOCALS :: ", locals(), "GLOBALS :: ", globals(), "\n\n")
#
#     class C:
#         print("INSIDE C LOCALS :: ", locals(), "GLOBALS :: ", globals(), "\n\n")
#         print(x)  # xlocal  of course
#         print(y)  # ytop  why? I guess output may be 'ylocal' or '1'
#         y = 1
#         print(y)  # 1  of course
#
#
# print("INSIDE maindir() LOCALS :: ", locals(), "GLOBALS :: ", globals(), "\n\n")
# func()

# class A:
#     def __init__(self):
#         print("hello")
#
#
# a = A()
