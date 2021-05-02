# functions
# project 98

def swapFileData():
    file1 = input("What is the name of your first file? ")
    file2 = input("What is the name of your second file? ")
    with open(file1, "r") as x:
        dataA = x.read()
    with open(file2, "r") as x:
        dataB = x.read()
    with open(file1, "w") as x:
        x.write(dataB)
    with open(file2, "w") as x:
        x.write(dataA)

swapFileData()