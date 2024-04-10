# Mason Porter: Main, Menu, Encode

def main():
    while True:
        selection = menu()  # Prints menu and gets menu selection

        if selection == 1:  # Encode
            encode()

        if selection == 2:  # Decode
            decode()

        if selection == 3:  # Quit
            break  # Ends the program


def encode():
    original_password = input("Please enter your password to encode: ")
    encoded_password = ""
    for item in original_password:
        item = int(item)
        item += 3
        if item == 10:
            item = 0
        if item == 11:
            item = 1
        if item == 12:
            item = 2
        item = str(item)
        encoded_password += item
    print("Your password has been encoded and stored!")
    print("")


def decode():
    pass


def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print("")
    selection = int(input("Please enter an option: "))
    return selection


if __name__ == "__main__":
    main()
