d = {'a': 11, 'b': 22}


def f(a, b):
    print(a, b)





# import random
#
# print(random.randint(1,100))


# class TestContext(object):
#     test_count = 1
#
#     def __init__(self):
#         self.test_number = TestContext.test_count
#         TestContext.test_count += 1
#
#     def __enter__(self):
#         # return self.test_number
#         pass
#
#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         if exc_value is None:
#             print('Test %d passed' % self.test_number)
#         else:
#             print('Test %d failed: %s \nHERO:: %s' % (self.test_number, exc_value, exc_traceback))
#         return True
#
#
# with TestContext():
#     print("hello", t)
#     # raise Exception('fat gya')
