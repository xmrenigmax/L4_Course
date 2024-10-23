import json
import xmltodict


# Display Movie XML
try:
    with open('L4Fundamentals/Lab3/movies.xml', 'r') as xml_file:
        xml_movie_data = xml_file.read()
        print(xml_movie_data)
except FileNotFoundError:
    print("Error: The file 'movies.xml' was not found.")
    
# Display Book XML
try:
    with open('L4Fundamentals/Lab3/book.xml', 'r') as xml_file:
        xml_data = xml_file.read()
        print(xml_data)
except FileNotFoundError:
    print("Error: The file 'book.xml' was not found.")

# Display Movie JSON
try:
    with open('L4Fundamentals/Lab3/movies.json', 'r') as json_file:
        json_movie_data = json.load(json_file)
        print(json.dumps(json_movie_data, indent=4))
except FileNotFoundError:
    print("Error: The file 'book.json' was not found.")

# Display Book JSON
try:
    with open('L4Fundamentals/Lab3/books.json', 'r') as json_file:
        json_data = json.load(json_file)
        print(json.dumps(json_data, indent=4))
except FileNotFoundError:
    print("Error: The file 'book.json' was not found.")


