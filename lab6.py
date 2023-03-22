def menu():
    print("""Menu
-------------
1. Encode
2. Decode
3. Exit
    """)


def encoder(psswrd):
    encoded = ""
    for digit in psswrd:
        encoded += str((int(digit) + 3) % 10)
    return encoded


def decoder(psswrd):
    original = ""
    for digit in psswrd:
        original += str((int(digit) - 3) % 10)
    return original


def main():
    while True:
        menu()
        option = int(input("Please enter an option: "))

        if option == 1:
            psswrd = (input("Please enter your password to encode: "))
            ans = encoder(psswrd)
            print("Your password has been encoded and stored!\n")

        elif option == 2:
            print(f"The encoded password is {ans}, and the original password is {decoder(ans)}.\n")

        elif option == 3:
            break


if __name__ == "__main__":
    main()
