def menu():  # menu formatted
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Exit\n")


def encoder(psswrd):
    encoded = ""  # empty string
    # for each digit in the inputted password, we add 3 to the value
    for digit in psswrd:
        encoded += str((int(digit) + 3) % 10)
    return encoded


def decoder(psswrd):
    original = ""  # empty string
    # for each digit in the inputted password, we subtract 3 from the value
    for digit in psswrd:
        original += str((int(digit) - 3) % 10)
    return original


def main():
    
    # while loop to keep main going until user breaks (option 3)
    while True:
        menu()  # print menu
        option = int(input("Please enter an option: "))

        if option == 1:
            psswrd = (input("Please enter your password to encode: "))
            ans = encoder(psswrd)  # assign to variable "ans" to refer to it in option 2
            print("Your password has been encoded and stored!\n")

        elif option == 2:
            print(f"The encoded password is {ans}, and the original password is {decoder(ans)}.\n")

        elif option == 3:
            break


if __name__ == "__main__":
    main()
