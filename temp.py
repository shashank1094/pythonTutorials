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
