import csv
from managing_files import *
from csv_files import create_csv, read_csv, append_to_csv

if __name__ == "__main__":

    pass  # remove
    content_of_files = "This is my text file \n"

    write_to_file("my_file.txt", content_of_files)
    print("File created and written to successfully.")
    append_to_file("my_file.txt", content_of_files)
    print("File appended successfully.")
    content = read_from_file("my_file.txt")
    print(content)
    #from managing_files import remove_file
    #remove_file("my_file.txt")

    content = [["Name", "age","grade"], ["John", "23", "A"], ["Jane", "22", "B"], ["Doe", "21", "C"], ["Smith", "20", "D"]]
    create_csv("my_csv.csv", content)
    print("CSV file created successfully.")
    read_csv("my_csv.csv")
    #append_to_csv("my_csv.csv", content)




    