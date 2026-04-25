correct_username = "admin"
correct_password = "admin123"
attempts=0
max_attempts=3
while attempts < max_attempts:
    username=input("Enter username: ")
    password=input("Enter password: ")
    if username == correct_username and password == correct_password:
        print("Login successful.")
        break
    else:
        attempts += 1
        print("Invalid credentials. Attempts left:",max_attempts - attempts)
if attempts == max_attempts:
    print("Account locked due to 3 failed login_v2 attempts.")
