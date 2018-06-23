import numpy as np

a = np.random.randint(low=1, high=100, size=10)
print(a)

# FILTER()
greater_than_50 = filter(lambda x: x > 50, a)
# greater_than_50_list = [x if x > 50 for x in a ] # ERROR : else expected
greater_than_50_list = [x for x in a if x > 50]
print(list(greater_than_50), greater_than_50_list)

# MAP()
greater_than_50_else_0 = map(lambda x: x if x > 50 else 0, a)
# greater_than_50_else_0_list = [x for x in a if x > 50 else 0]  # ERROR
greater_than_50_else_0_list = [x if x > 50 else 0 for x in a]
print(list(greater_than_50_else_0), greater_than_50_else_0_list)
