users = {
    "admin":"adminmaster123",
    "guest":"guest123"
}
try:
    username = input("Enter your username: ")
    if username in users:
        password = input("Enter your password: ")
        if password != users[username]:
            print("Invalid password")
        else:
            print("Login successful")
            with open("Logs.txt", "a") as f:
                f.write(f" logged in {username}:{password}\n")
    else:
            print("Invalid username")
            with open("Logs.txt", "a") as f:
                f.write(f" invalid username {username}\n")

except NameError:
    print(f"an error occured")

