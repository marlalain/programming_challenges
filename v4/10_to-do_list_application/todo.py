#!/bin/python3
# Paulo Elienay II

# imports
import os, sys
# vars
name = ''
# defs
def clear():
    os.system('clear')
def get_profile(mode):
    return open("profile", mode)
def check_for_profile():
    return os.path.exists("./profile")
def create_profile(name):
    profile = get_profile("w")
    profile.write(name)
    profile.close()
def get_notes_list():
    return get_profile("r")
def main_menu():
    clear()
    if len(get_notes_list) > 1:
        # old
    else:
        # new
        print("No notes in the database.")
        user_input = input("Do you want to create your first note? [yes/no] ")
        if user_name == "yes":
            # create note
        else:
            print("Nothing left to do. Exiting")
            sys.exit()

def write_profile(new_profile):
    new_profile.close()
#def get_name():
#    return get_profile().readlines()[0]
# main
def main():
    print("Checking for profile...")
    if check_for_profile():
        print("A profile already exists.")
        name = get_profile().readlines()[0]
        print("Hi {}".format(name))
    else:
        print("No profile found.")
        print("Creating new profile.")
        create_profile(input("What's your name? "))
if __name__ == '__main__':
    main()
