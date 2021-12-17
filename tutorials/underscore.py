# https://hackernoon.com/understanding-the-underscore-of-python-309d1a029edc

# Ignore a value when unpacking
x, _, y = (1, 2, 3) # x = 1, y = 3

# Ignore the multiple values. It is called "Extended Unpacking" which is available in only Python 3.x
x, *_, y = (1, 2, 3, 4, 5) # x = 1, y = 5

print(x, y, _)
# Ignore the index
for _ in range(10):
    # do_something()
    pass

