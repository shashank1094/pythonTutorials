# dir(<module>) lists all the variables/functions/classes that are import via that module.
import re

print("--main--", dir())
print()
print("dir(re)", dir(re), sep=" =====>>> ", end="...")
