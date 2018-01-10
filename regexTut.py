import re

st1 = "Hello"
st2 = """this
is
a
multi
line
hello"""

print("st1 :: " + st1)
print("st2 :: " + st2)
print()

print("Going to match st1 with ^ and $ in regex :: ")
if re.match(r"^[A-Za-z]+$", st1):
    print("Yay! its a match.")
else:
    print("Noo!")


print("Going to match st2 with ^ and $ in regex :: ")
if re.match(r"^[A-Za-z]+$", st2):
    print("Yay! its a match.")
else:
    print("Noo!")


print("Going to match st1 without ^ and $ in regex :: ")
if re.match(r"[A-Za-z]+", st1):
    print("Yay! its a match.")
else:
    print("Noo!")


print("Going to match st2 without ^ and $ in regex :: ")
if re.match(r"[A-Za-z]+", st2):
    print("Yay! its a match.")
else:
    print("Noo!")


