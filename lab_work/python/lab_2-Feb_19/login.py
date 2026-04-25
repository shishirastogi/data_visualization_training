correct_username = "admin"
correct_password = "12345"
attempts=0
while attempts < 3:
    username=input("Enter username: ")
    password=input("Enter password: ")
    if username == correct_username and password == correct_password:
        print("Login Successful!")
        break
    else:
        attempts += 1
        print("Invalid credentials. Please try again.")
        print("Attempts remaining:",3 - attempts)
if attempts == 3:
    print("Account Locked. Too many failed attempts.")
