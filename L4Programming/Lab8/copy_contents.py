# copy content of one file into another

# function
def copy_contents(source, destination):
    with open(source, 'r') as file:
        content = file.read()
    with open(destination, 'w') as file:
        file.write(content)

# test
print(copy_contents("my_file.txt","file_of_data.txt")) 