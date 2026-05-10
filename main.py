import time

correct_username = "admin"
correct_password = "admin123"

attempts = 3

while attempts > 0:

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == correct_username and password == correct_password:
        print("\nLogin Successful")
        break

    else:
        attempts -= 1
        print("\nLogin Failed")
        
        if attempts > 0:
            print(f"Attempts Left: {attempts}")

if attempts == 0:
    print("\nToo many failed attempts")
    print("\nAccess Blocked for 10 seconds")
    time.sleep(10)