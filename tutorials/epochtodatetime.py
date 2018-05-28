import os, time

# curr = time.time()
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(curr)))

DIR = "C:\\"
t = {}
for dirName in os.listdir(DIR):
    if os.path.isdir(os.path.join(DIR, dirName)):
        t[str(
            time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getctime(os.path.join(DIR, dirName)))))] = dirName

for key in sorted(t.keys(), reverse=True):
    print("%s : %s" % (key, t[key]))
