class Foo(object):
    def __new__(cls, *args, **kwargs):
        print("Creating Instance", cls, args, kwargs, sep=" ==>> ")
        instance = super().__new__(cls)
        return instance

    def __init__(self, a=2, b=3):
        self.a = a
        self.b = b

    def bar(self):
        pass


i = Foo(5, 6)
print(dir(i), i.__dict__, sep='\n\n')

# class UpperAttrMetaclass(type):
#
#     def __new__(upperattr_metaclass, future_class_name,
#                 future_class_parents, future_class_attr):
#         print("hi")
#         uppercase_attr = {}
#         for name, val in future_class_attr.items():
#             if not name.startswith('__'):
#                 uppercase_attr[name.upper()] = val
#             else:
#                 uppercase_attr[name] = val
#
#         # reuse the type.__new__ method
#         # this is basic OOP, nothing magic in there
#         return super().__new__(upperattr_metaclass, future_class_name,
#                             future_class_parents, uppercase_attr)
#
#
# class A(metaclass=UpperAttrMetaclass):
#     def f1(self):
#         pass
#
#
# a1 = A()
# a1.F1()

# def upper_attr(future_class_name, future_class_parents, future_class_attr):
#     """
#       Return a class object, with the list of its attribute turned
#       into uppercase.
#     """
#
#     # pick up any attribute that doesn't start with '__' and uppercase it
#     uppercase_attr = {}
#     for name, val in future_class_attr.items():
#         if not name.startswith('__'):
#             uppercase_attr[name.upper()] = val
#         else:
#             uppercase_attr[name] = val
#
#     # let `type` do the class creation
#     return type(future_class_name, future_class_parents, uppercase_attr)
#
#
# class Foo(metaclass=upper_attr):
#     bar = 'bip'
#
#
# print(hasattr(Foo, 'bar'))
# # Out: False
# print(hasattr(Foo, 'BAR'))
# # Out: True
#
# f = Foo()
# print(f.BAR)
# # Out: 'bip'
# print(dir(Foo))
