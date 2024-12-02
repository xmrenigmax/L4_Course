import csv

def create_csv(filename, data):
    with open(filename, mode="w", newline="") as file:
        write = csv.writer(file)
        write.writerows(data)

def read_csv(filename):
   with open(filename, "r") as file:
      read = csv.reader(file)
      for row in read:
         print(row)

def append_to_csv(filename, data):
    with open(filename, "a") as file:
      append = csv.writer(file)
      append.writerows(data)
       



