x = "xtop"
y = "ytop"


def func():
    x = "xlocal"
    y = "ylocal"
    print("INSIDE func() LOCALS :: ", locals(), "GLOBALS :: ", globals(), "\n\n")

    class C:
        print("INSIDE C LOCALS :: ", locals(), "GLOBALS :: ", globals(), "\n\n")
        print(x)  # xlocal  of course
        print(y)  # ytop  why? I guess output may be 'ylocal' or '1'
        y = 1
        print(y)  # 1  of course


print("INSIDE maindir() LOCALS :: ", locals(), "GLOBALS :: ", globals(), "\n\n")
func()

# class A:
#     def __init__(self):
#         print("hello")
#
#
# a = A()
