import sys

"""
Prompts user to input a name and password.
If password is validated, a welcome message is printed. Otherwise user is prompted to retry.
"""
def validate_credentials():
    print("[Password validator]")
    name = input("\tname: ")
    try:
        while True:
            password = input("\tpassword: ")

            print()
            if password == "erisology":
                print(f"Login successful. Welcome aboard, {name}!")
                break
            else:
                print("Invalid password, please try again.")
    except KeyboardInterrupt:
        sys.exit(1)

if __name__ == "__main__":
    validate_credentials()