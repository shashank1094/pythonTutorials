# https://www.python-course.eu/python3_slots.php


class student:
    """Here goes the description for the class."""

    # __slots__ = ("__name",)
    def __init__(self, temp_name):
        self.name = temp_name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if type(name) != str:
            self.__name = None
        else:
            self.__name = name


s1 = student("shashank")
print(s1.name)

print("DICT OF OBJECT :: ", s1.__dict__)
print("DICT OF CLASS :: ", student.__dict__)
print("DIR OF OBJECT :: ", dir(s1))
print("DIR OF CLASS :: ", dir(student))

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