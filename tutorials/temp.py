print("HELLO WORLD")

# class GenericMaxException(Exception):
#     """Base class for all Max layer exceptions."""
#
#     def __init__(self, *, message):
#         """
#         Constructor.
#
#         Parameters:
#             Required:
#                 message - String describing exception.
#
#             Optional:
#                 None
#         """
#
#         super().__init__()
#
#
# raise GenericMaxException(message="This is the reason.")

# a = [1, 2, 3]
#
# b = a * 3
# c = [a] * 3
# print(b, c)
# a[0] = 4
# print(b, c)


# def some_func():
#     try:
#         return 'from_try'
#     finally:
#         return 'from_finally'
#
#
# print(some_func())

# list_ = ['cat1', 'cat2', 'cat3', 'number1', 'number2', 'number3']
# # Don't name the variable "list" as it is a keyword if you can't think of anything else append a underscore at end
#
# my_dict = {}
#
# for item in list_:
#     if "cat" in item:
#         my_dict[item] = 'categorical'
#     elif "number" in item:
#         my_dict[item] = 'numerical'
#
# print(my_dict)

# def fun(a, b, c):
#     print(a, b, c)
#
#
# # A call with unpacking of dictionary
# d = {'a': 2, 'b': 4, 'c': 10}
# fun(**d)
#
#
# # A Python program to demonstrate packing of
# # dictionary items using **
# def fun(**kwargs):
#     # kwargs is a dict
#     print(type(kwargs))
#
#     # Printing dictionary items
#     for key in kwargs:
#         print("%s = %s" % (key, kwargs[key]))
# Driver code
# fun(name="geeks", ID="101", language="Python")


# import subprocess
# subprocess.call('jar tvf abc.jar ')
#
# # import os
# # os.system('jar tvf abc.jar')


# while True:
#     try:
#         1 / 0
#     except Exception:
#         raise
#     finally:
#         break  # discards the exception
#
# print('hell')  # it does print indeed


# final_dict = {'some_company_100': {'key1': 'value1',
#                                    'key2': 'value2',
#                                    'key3': 'value3',
#                                    'key4': 'value4',
#                                    'key5': 'value5',
#                                    'key6': {'key6_1': 'value6_1', 'key6_2': 'value6_2'},
#                                    'key7': 'value7'},
#               'some_company_101': {'key1': 'valuea',
#                                    'key2': 'valueb',
#                                    'key3': 'valuec',
#                                    'key4': 'valued',
#                                    'key5': 'valuee',
#                                    'key6': {'keyf_1': 'valuef_1', 'keyf_2': 'valuef_2'},
#                                    'key7': 'value7'}}
#
# for key, value in final_dict.items():
#     flag = 0
#     temp = []
#     for k, v in value.items():
#         if isinstance(v, dict):
#             temp.append(v)
#             flag = 1
#     if flag == 1:
#         for
# print(final_dict)


# def f():
#     s = "Perl"
#     print(s)
#
#
# s = "Python"
# f()
# print(s)

# def f():
#     print(s)
#     s = "Perl"
#     print(s)
# s = "Python"
# f()
# print(s)


# edibles = ["ham", "spam", "eggs", "nuts"]
# for food in edibles:
#     if food == "spam":
#         print("No more spam please!")
#         break
#     print("Great, delicious " + food)
# else:
#     print("I am so glad: No spam!")


# file = open("loggingTutLogs.txt", "r")
# lines = file.read()
# print("\n####\n".join(lines.split("\n")))


# try:
#     a = float(input("Please, give me a number : \n"))
#     print("Now your number is", a, "and its type is", type(a))
# except ValueError:
#     print("It's not possible to make a float.")


# n = int(input())
# a = [int(x) for x in input().split()]
# assert(len(a) == n)
# m1 = max(a)
# a.remove(m1)
# m2 = max(a)
# print(m1*m2)


# import requests, json
#
# username = "Dextication"
# url = f"https://minecraft-statistic.net/api/player/info/{username}/"
# response = requests.get(url)
# json_data = json.loads(response.text)
# print(json_data)
# print(json_data["data"]["total_time_play"])


# def age_group(sample_data):
#     tempAge = int(sample_data['age'])
#     if tempAge <= 21:
#         return 1
#     elif tempAge <= 30:
#         return 2
#     elif tempAge <= 40:
#         return 3
#     elif tempAge <= 50:
#         return 4
#     elif tempAge <= 60:
#         return 5
#     elif tempAge > 60:
#         return 6
#     else:
#         return 0
#
# Age_Est = sample_data.apply(age_group, axis=1)
# Age_Est.name = 'Age_Est'
# print(Age_Est)
