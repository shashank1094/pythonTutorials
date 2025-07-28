import shlex

command = "grep -i 'hello world' file.txt"
tokens = shlex.split(command)

print("Command:", tokens[0])
print("Arguments:", tokens[1:])
print("Arguments:", tokens)

command = "ls -l | grep 'example is full'"
command_tokens = shlex.split(command)

print(command_tokens)