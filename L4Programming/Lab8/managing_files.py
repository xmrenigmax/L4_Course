def write_to_file(filename, content):
    with open(filename, 'w') as file:
        content_of_file = file.write(content)
        content_of_file = file.write(content)


def read_from_file(filename):
    # complete the function
    with open(filename, 'r') as file:
        content = file.read()

def append_to_file(filename, content):
    # complete the function
    with open(filename, 'a') as file:
        file.write(content)

def remove_file(filename):
   # complete the function
    import os
    os.remove(filename)
