# https://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python/
# NOTE :: WHEN WE PACK MULTIPLE VALUE in *args THEY ARE STORED AS TUPLE.


# A Python program to demonstrate packing of
# dictionary items using **
def fun(**kwargs):
    # kwargs is a dict
    print(type(kwargs))

    # Printing dictionary items
    for key in kwargs:
        print("%s = %s" % (key, kwargs[key]))


# Driver code
fun(name="geeks", ID="101", language="Python")


# # A sample program to demonstrate unpacking of
# # dictionary items using **
# def fun(a, b, c):
#     print(a, b, c)
#
#
# # A call with unpacking of dictionary
# d = {'a': 2, 'c': 10, 'b': 4}
# fun(**d)


# # A Python program to demonstrate use
# # of packing
#
# # This function uses packing to sum
# # unknown number of arguments
# def mySum(*args):
#     print(args)
#     sum = 0
#     for i in range(0, len(args)):
#         sum = sum + args[i]
#     return sum
#
# # Driver code
# print(mySum(1, 2, 3, 4, 5))
# print(mySum(10, 20))


# # A sample function that takes 4 arguments
# # and prints the,
# def fun(a, b, c, d):
#     print(a, b, c, d)
#
#
# # Driver Code
# my_list = [1, 2, 3, 4]
#
# # Unpacking list into four arguments
# fun(*my_list)


# # A Python program to demonstrate need
# # of packing and unpacking
#
# # A sample function that takes 4 arguments
# # and prints them.
# def fun(a, b, c, d):
#     print(a, b, c, d)
#
#
# # Driver Code
# my_list = [1, 2, 3, 4]
#
# # This doesn't work
# fun(my_list)
