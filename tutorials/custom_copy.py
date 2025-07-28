from copy import copy, deepcopy
class A:
    def __init__(self):
        print('init')
        self.v = 10
        self.z = [2,3,4]
    def __copy__(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        return result
    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, deepcopy(v, memo))
        return result
    def __str__(self):
        return str(self.v) + str(self.z)



a1 = A()
a1.v = 12
a1.z.append(5)
print(a1)
a2 = copy(a1)
print(a2)
a1.z.append(6)
a2.z.append(7)
print(a2)

a3 = deepcopy(a1)
a1.z.append(9)
print(a1)
a3.z.append(10)
print(a3)