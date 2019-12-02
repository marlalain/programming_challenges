#!/bin/python3
# Made by Paulo Elienay II

# imports
# vars
password, user_input = 'ERROR', 'ERROR'
# default options
pwd_size = 10
pwd_letters = True
pwd_numbers = True
pwd_special_chars = False
# defs
def user_choice(choice):
	if choice == 'yes' or choice == 'y' return True
	else return False
# main


def main():
  print('Password Generator!')
	if user_choice(input("The default size of a password is {pwd_size}. Do you want to change this? [yes/no]: ")):
		pwd_size = input("Set the new password size: ")

	# letters
	if pwd_letters:
		if user_choice(input("By default the program uses letters in passwords. Change this? [yes/no]")):
			pwd_letters = False
	else:
		if user_choice(input("By default the program don't uses letters in passwords. Change this? [yes/no]")):
			pwd_letters = True
	
	# numbers
	if pwd_numbers:
		if user_choice(input("By default the program uses numbers in passwords. Change this? [yes/no]")):
			pwd_numbers = False
	else:
		if user_choice(input("By default the program don't uses numbers in passwords. Change this? [yes/no]")):
			pwd_numbers = True
	
	# special characters
	if pwd_numbers:
		if user_choice(input("By default the program uses special chars in passwords. Change this? [yes/no]")):
			pwd_special_chars = False
	else:
		if user_choice(input("By default the program don't uses special chars in passwords. Change this? [yes/no]")):
			pwd_special_chars = True

	password = create_password(pwd_size, pwd_letters, pwd_numbers, pwd_special_chars)
	print("Your new password is {password}")
	print("Although not recommended, you can save your password")
	if user_choice(input("Do you want to save your password in a file? [yes/no]"))):
		save_password(password)

if __name__ == '__main__':
  main()
