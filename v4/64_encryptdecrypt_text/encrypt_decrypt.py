#!/usr/bin/env python3
# Paulo Elienay II
#
# imports
import sys, string
# vars
user_input, passcode, plaintext, output = "", "", "", ""
alpha, alphA = string.ascii_lowercase, string.ascii_uppercase
shifted, shifteD = alpha, alphA
temp_list = []
# defs
def create_key(passcode, plaintext):
    key, cycle, passlist, i = '', True, list(passcode), 0
    while cycle:
        if len(key) == len(plaintext):
            cycle = False
        else:
            if (i < len(passcode)): key += passlist[i]
            if (i == len(passcode)): i = 0
            else: i += 1
    return key
def encrypt(passcode, plaintext):
    key, passlist = create_key(passcode, plaintext), list(passcode)
    temp_list.append(alpha[-1])
    temp_list.append(alpha)
    print(temp_list)
    #return output
#def decrypt(passcode, plaintext)
# main
def main():
    print("Vigenère Encrypt/Decrypt Tool")
    user_input = input("Do you want to decrypt or encrypt? [d/e] ")
    if (user_input == "e"):
        passcode = input("What's your passphrase? ")
        plaintext = input("What's your plaintext? ")
        print(encrypt(passcode, plaintext))
    elif (user_input == "d"):
        passcode = input("What's your passphrase? ")
        plaintext = input("What's your plaintext? ")
        decrypt(passcode, plaintext)
    else:
        sys.exit()
    
if __name__ == "__main__":
    main()
