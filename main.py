# Mason Porter: Main, Menu, Encode, Decode
# (Hussam Saadi)


def main():
    encoded_password = ""
    while True:
        selection = menu()  # Prints menu and gets menu selection

        if selection == 1:  # Encode
            encoded_password = encode()  # Asks user for input, returns encoded password

        if selection == 2:  # Decode
            decode(encoded_password)  # Takes encoded password, decodes and prints

        if selection == 3:  # Quit
            break  # Ends the program


def encode():
    original_password = input("Please enter your password to encode: ")
    encoded_password = ""
    for item in original_password:
        item = int(item)
        item += 3
        if item > 9:
            item -= 10
        item = str(item)
        encoded_password += item
    print("Your password has been encoded and stored!")
    print("")
    return encoded_password


def decode(encoded_password):
    decoded_password = ""
    for item in encoded_password:
        item = int(item)
        item -= 3
        if item < 0:
            item += 10
        item = str(item)
        decoded_password += item
    print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
    print("")


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
