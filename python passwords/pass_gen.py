import random
import string
import bcrypt 

# Welcome MEssage
print("Welcome to the Small Wave password generator!")

# Username and password legnth
username = input("Please enter the email/username of the password you are using.")
word_length = int(input("Please enter the length of your password."))

# Create the components used by random
components = string.ascii_letters + string.digits + string.punctuation

# Generate a random password and convert it to bytes
password = ''.join(random.choices(components, k=word_length)).encode('utf-8')

# Hash the password with bcrypt
hashed = bcrypt.hashpw(password, bcrypt.gensalt( 12 ))

# Write the hashed password and user to the password file
f = open("passwords.txt", "a")
f.write("User: " + username + " | " + "Hashed Password: " + hashed.decode() + "\n")

# Write the plaintext password and user to the shadow file
s = open("shadow.txt", "a")
s.write("User: " + username + " | " + "Plaintext Password: " + password.decode() + "\n")

