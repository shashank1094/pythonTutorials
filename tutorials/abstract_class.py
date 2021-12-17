from abc import ABC, abstractmethod


class AbstractClassExample(ABC):

    @abstractmethod
    def do_something(self):
        print("Some implementation!")


class AnotherSubclass(AbstractClassExample):
    def do_something(self):
        super().do_something()
        print("The enrichment from AnotherSubclass")


# a1 = AbstractClassExample()
# a1.do_something()
x = AnotherSubclass()
x.do_something()

# from abc import ABC, abstractmethod
#
#
# class PMixin(ABC):
#
#     @property
#     @abstractmethod
#     def progressbar_step(self):
#         raise NotImplementedError
#
#
# class B(PMixin):
#     def progressbar_step(self):
#         print("defined")
#
#
# # class B:
# #     def not_progressbar_step(self):
# #         print("defined")
#
#
# class C(B, PMixin):
#     pass
#
#
# c1 = C()
