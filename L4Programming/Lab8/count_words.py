# reads content of file
# counts the number of occurances of a given word
# returns the count

def count_words(filename, word):
    with open(filename, 'r') as file:
        content = file.read()
        count = content.count(word)
    return count

# Test the function
print(count_words("file_of_data.txt","the"))