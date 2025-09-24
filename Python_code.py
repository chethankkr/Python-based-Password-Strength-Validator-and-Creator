
""" A strong password must:
    - Have at least 8 characters
    - Contain at least one digit
    - Contain at least one uppercase letter
    - Contain at least one special character
"""
print("Your password should contain a minimum of 8 characters, at least one capital letter, at least one special character, and at least one number.")

def password_creator():
    """
        Prompt the user to create a password and validate it.

        Keeps asking the user to re-enter a password until the password
        is considered strong by `password_strength`.
    """
    password=str(input("Enter your password: "))
    while not (password_strength(password)):
        print("please create stronger password.")
        password=str(input("Enter New password: "))
    print("password set successfully.",end='')

 ## Check if a given password is strong.   
def password_strength(password):
    l=len(password)
    num=False
    upper=False
    special=False
    for i in password:
        if i.isdigit():
            num=True
    for i in password:
        if i.isupper():
            upper=True
    for i in password:
        if not i.isalnum():
            special=True
    if ((l>7)and num and upper and special):
        return True
    else:
        return False         
password_creator()