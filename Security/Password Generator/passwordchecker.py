import string

class formatting:

    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'

def passwordChecker():
    
    ## Password Policy display (NEEDS GUI OR MORE PROFESSIONAL FORMATTING (or both)
    
    print(formatting.BOLD + "Current Organization Password Policy" + formatting.END)
    print('\t- Your password must be minimum 8 characters in length.')
    print('\t- Your password must be a maximum of 18 characters in length.')
    print('\t- Your password must contain at least an uppercase and a lowercase letter.')
    print('\t- Your password must contain at least 3 numbers.')
    print('\t- Your passworst must containt at least two special characters (@, +, $, *, ^, etc.).')
    print('\t- Your password must NOT contain a space or any symbol that provides whitepsace.')
    print('\t- Your passwost must also pass the dictionary check.')
    
    ## Requires the user to end their password (NEEDS UPDATED WITH MORE SECURE CODING STANDARDS TO PREVENT BREAKING THE CODE)
    print('\t- Please enter your password for a security check.')
    userPasswrd = input('\n Please enter your password for a security check: ').strip()
    
    ## Preliminary password check
    
    ## Length check
    if not(8 <= len(userPasswrd <= 18)):
        message = 'Invalid password, your password should have the minimum length of 8, maximum length of 18'
        print(message)
        return False
       
    ## Whitespace check
    if ' ' in userPasswrd:
        message = 'Invalid password, your password cannot contain any space(s).'
        print(message)
        return False
    
    ## Letter check
    if not any(i in string.ascii_letters for i in userPasswrd):
        message = 'Invalid password, your password must contain at least an uppercase and lowercase letter.'
        print(message)
        return False
    
    ## Number check
    if not any(i in string.digits for i in userPasswrd):
        message = "Invalid password, your password must contain at least one number."
        print(message)
        return False
    
    ## Special Characters check
    if not any(i in string.punctuation for i in userPasswrd):
        message = "Invalid password, your password must contain at least one special character."
        print(message)
        return False
    
    ## End of Preliminary Password Check, begin dictionary check
    print('\n End of preliminary password check, beginning dictionary check.')
    
    ## Uses an offline dictionary database to check. Additionally, matches user input password with the top 100,000 most commonly used passwords.
    file1 = open("dictionary.txt")
    
    c = file1.read()
    
    if userPasswrd in c:
        message = 'Password is a searchable dictionary word and therefore not secure, please choose a more secure password.'
        print(message)
        return False
    
    file1.close()
    
    print('\n End of Dictionary Check, beginning common password check.')
    file2 = open("CommonPasswrd.txt")
    
    c = file2.read()
    
    ##Common Passwords
    if userPasswrd in c:
        message = 'Password is a commonly used password and there is not secure, please choose a more secure password.'
        print(message)
        return False
    
    file2.close()

    return True

def main():
    #Create a Bool
    good = passwordChecker()

    ##Conditional statement depending on what the password Checker Returned
    if(good != True):
        print("Your password is NOT secure. Please make sure you are following the organization's password policy. This program will now close.")
        exit()
    
    else:
        print('Your password is secure, this program will now close.')
        exit()