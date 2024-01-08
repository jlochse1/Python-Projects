import random
import string
import bcrypt 

print("Welcome to the Small Wave password generator!")

username = input("Please enter the email/username of the password you are using.")

word_length = int(input("Please enter the length of your password."))

components = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choices(components, k=word_length)).encode('utf-8')

hashed = bcrypt.hashpw(password, bcrypt.gensalt( 12 ))

print("Your password is" + password.decode())

f = open("passwords.txt", "a")
f.write("User: " + username + " | " + "Hashed Password: " + hashed.decode() + "\n")
f.write(" -------------------------------------------------------------------------------------------- ")

s = open("shadow.txt", "a")
s.write("User: " + username + " | " + "Plaintext Password: " + password.decode() + "\n")
s.write(" -------------------------------------------------------------------------------------------- ")
