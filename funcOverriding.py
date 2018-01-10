# Function overloading in Python is not allowed, but can be achieved with default arguments in function definition.


def f():
    print("Inside f() version1.")


# First definition of the function is hidden by the second definition
def f():
    print("Inside f() version2.")


f()
