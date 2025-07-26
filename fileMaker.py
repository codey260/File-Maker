import os

path = os.path.dirname(os.path.abspath(__file__))
filename = input("Enter Your File Name: ").strip()
mode = input("Enter Your Mode: write(w), append(a), read(r), rename(cn): ").lower().strip()

full_path = os.path.join(path, filename)

if mode in ("w", "write"):
    with open(full_path, "w") as file:
        userInput = input("What Do You Want To Write In Your File:\n> ")
        file.write(userInput)
        print(" Wrote in the file successfully.")

elif mode in ("r", "read"):
    try:
        with open(full_path, "r") as file:
            print(" File content:\n")
            print(file.read())
            print(" File read successfully.")
    except FileNotFoundError:
        print(" File not found.")

elif mode in ("a", "append"):
    with open(full_path, "a") as file:
        userInput = input("What Do You Want To Append In Your File:\n> ")
        file.write(userInput)
        print(" Appended to the file successfully.")

elif mode in ("cn", "rename", "change name"):
    new_name = input("Enter new file name (with extension): ").strip()
    new_path = os.path.join(path, new_name)
    try:
        os.rename(full_path, new_path)
        print(f" File renamed to {new_name}")
    except FileNotFoundError:
        print("Original file not found.")
    except Exception as e:
        print(f" Error: {e}")

else:
    print(f" Invalid mode: {mode}")

input("🔚 Press Enter To Exit...")
