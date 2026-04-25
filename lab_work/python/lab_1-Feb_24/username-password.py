username = input("Enter username: ")
password = input("Enter password: ")
if len(username) < 5:
    print("Invalid Username: Must be at least 5 characters long.")
elif not username.isalnum():
    print("Invalid Username: Only letters and numbers allowed.")
elif len(password) < 8:
    print("Invalid Password: Must be at least 8 characters long.")
else:
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        else:
            has_special = True
    if has_upper and has_lower and has_digit and has_special:
        print("Username and Password are Valid.")
    else:
        print("Invalid Password: Must contain uppercase, lowercase, digit, and special character.")