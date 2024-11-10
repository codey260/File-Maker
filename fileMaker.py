# Declaring Variables
path = input("Enter Your Path: ")  # Path Input From User
filename = input("Enter Your File Name: ")  # File Name Input From User
mode = input("Enter Your Mode write(w), append(a), read(r), create(x): ").lower(
).strip()  # Mode Input From User
myFile = open(f"{path}\\{filename}", f"{mode}")  # File Variable

# Functions

# Write Function


def write():

    print("What Do You Want To Write In Your File: ")
    userInput = input("Enter Here: ")

    myFile.write(userInput)
    print("Wrote In The File Succesfully")

# Read Function


def read():

    print("Reading File.......")
    print(myFile.read())

    print("File Read Succesfully")

# Append Function


def append():

    print("What Do You Want To Append In Your File: ")
    userInput = input("Enter Here: ")

    myFile.write(userInput)


# If Conditions


# If Write Mode Is Selected
if mode == "w" or mode == "write":

    write()

# If Read Mode Is Selected
elif mode == "r" or mode == "read":

    read()

# If Append Mode Is Selected
elif mode == "a" or mode == "append":

    append()

# If None Of These Modes Are Chosed
else:

    print(f"Enter A Valid Mode Not This {mode}")

input("Press Enter To Exit: ")