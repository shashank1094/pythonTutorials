import os
import tempfile

try:
    fd, path = tempfile.mkstemp(suffix=".txt", prefix="my_temp_", dir=os.getcwd(), text=True)
    print(f"Temporary file created: {path} with file descriptor: {fd}")

    with os.fdopen(fd, 'w') as tmpfile:
        tmpfile.write("This is a temporary file.")

    with open(path, 'r') as tmpfile:
        print(tmpfile.read())

finally:
    # os.remove(path)
    print(f"Temporary file {path} removed.")