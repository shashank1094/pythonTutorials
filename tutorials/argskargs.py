# https://stackoverflow.com/questions/3394835/args-and-kwargs


def func(*args, **kargs):
    print("Positional arguments :")
    if args is not None:
        for arg in args:
            print(arg, end=" ")
        print("")
    print("Keywords arguments :")
    if kargs is not None:
        for i, j in kargs.items():
            print(i, ":", j, end=" ")


func(1, 2, 3, sex="male")
