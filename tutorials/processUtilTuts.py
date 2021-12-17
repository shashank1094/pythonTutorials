import psutil

for one in psutil.net_connections():
    if one[3][1] == 2000:
        print(one)

# or pythonic way

print(list(filter(lambda x: x[3][1] == 2000, psutil.net_connections())))
