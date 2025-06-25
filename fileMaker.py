import os

path = os.path.dirname(os.path.abspath(__file__))
filename = input("Enter Your File Name: ").strip()
mode = input("Enter Your Mode write(w), append(a), read(r): ").lower().strip()

if mode in ("w", "write"):
    with open(f"{path}\\{filename}", "w") as file:
        print("What Do You Want To Write In Your File: ")
        userInput = input("Enter Here: ")
        file.write(userInput)
        print("Wrote In The File Succesfully.")
elif mode in ("r", "read"):
    try:
        with open(f"{path}\\{filename}", "r") as file:
            print(file.read())
            print("File Read Succesfully")
    except FileNotFoundError:
        print("File not found.")
elif mode in ("a", "append"):
    with open(f"{path}\\{filename}", "a") as file:
        print("What Do You Want To Append In Your File: ")
        userInput = input("Enter Here: ")
        file.write(userInput)
        print("Appended To The File Succesfully.")
else:
    print(f"Enter A Valid Mode Not This {mode}")
input("Press Enter To Exit: ")