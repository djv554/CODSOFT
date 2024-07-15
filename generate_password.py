#program to generate a password for a given length

import random
import string

def generate_pw(length):
    characters= string.ascii_letters + string.digits + string.punctuation
    first_char = random.choice(string.ascii_letters)
    rem_char = ''.join(random.sample(characters,length-1)) #for i in range(length-1))
    pw = first_char + rem_char
    return pw

def main():
    print("\nPassword Generator")
    while True:
        length=int(input("\nEnter the length of the password you want to generate:"))
        if length<=4:
            print("Length of the password should be greater than 4 characters to generate a strong password. Try again.")
            continue
        else:
            pw = generate_pw(length)
            print("\nThe generated password is:"+pw)
            break
    

main()
