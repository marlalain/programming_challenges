#!/bin/python3
# Made by Paulo Elienay II

# imports
import random
# vars
# defs


def user_choice(choice):
    if choice == 'yes' or choice == 'y':
        return True
    else:
        return False


def create_password(size, upper, letters, numbers, special_chars):
    print("Creating your password...")
    password_array = []

    while len(password_array) != size:
        rand = random.choice(['letters', 'numbers', 'special_chars'])
        if rand == 'letters' and letters:
            if upper:
                if random.randint(0, 1) == 0:
                    password_array.append(chr(random.randint(65, 90)))
                else:
                    password_array.append(chr(random.randint(97, 122)))
            else:
                password_array.append(chr(random.randint(97, 122)))
        elif rand == 'numbers' and numbers:
            password_array.append(chr(random.randint(48, 57)))
        elif rand == 'special_chars' and special_chars:
            password_array.append(chr(random.randint(33, 46)))
    return ''.join(password_array)


# main
def main():
    password = 'ERROR'
    # default options
    pwd_size = 10
    pwd_letters = True
    pwd_upper = True
    pwd_numbers = True
    pwd_special_chars = False

    print('Password Generator!')
    print(f'The default size of a password is {pwd_size}. ')
    if user_choice(input("Do you want to change this? [yes/no] ")):
        pwd_size = int(input("Set the new password size: "))

    # letters
    if pwd_letters:
        print('By default the program uses letters in passwords.')
        if user_choice(input("Change this? [yes/no] ")):
            pwd_letters = False
    else:
        print("By default the program don't uses letters in passwords. ")
        if user_choice(input("Change this? [yes/no] ")):
            pwd_letters = True

    # letters
    if pwd_upper:
        print("By default the program uses uppercase in passwords.")
        if user_choice(input("Change this? [yes/no] ")):
            pwd_upper = False
    else:
        print("By default the program don't uses uppercase in passwords.")
        if user_choice(input("Change this? [yes/no] ")):
            pwd_upper = True

    # numbers
    if pwd_numbers:
        print("By default the program uses numbers in passwords.")
        if user_choice(input("Change this? [yes/no] ")):
            pwd_numbers = False
    else:
        print("By default the program don't uses numbers in passwords.")
        if user_choice(input("Change this? [yes/no] ")):
            pwd_numbers = True

    # special characters
    if pwd_special_chars:
        print("By default the program uses special chars in passwords.")
        if user_choice(input("Change this? [yes/no] ")):
            pwd_special_chars = False
    else:
        print("By default the program don't uses special chars in passwords. ")
        if user_choice(input("Change this? [yes/no] ")):
            pwd_special_chars = True

    password = create_password(
        pwd_size, pwd_upper, pwd_letters, pwd_numbers, pwd_special_chars)
    print(f"Your new password is {password}")


if __name__ == '__main__':
    main()
