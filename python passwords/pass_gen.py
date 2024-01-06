import random
import string 

print("Welcome to the Small Wave password generator!")

username = input("Please enter the email/username of the password you are using.")
word_length = int(input("Please enter the length of your password."))

components = string.ascii_letters + string.digits + string.punctuation

password = "".join(random.choices(components, k=word_length))

f = open("passwords.txt", "a")
f.write("Username: " + username + " " + "Password: " + password + "\n")
