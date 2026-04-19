import requests

target = input("Enter Target Address: ")
wordlist = ["Login", "Account", "Password", "Admin", "Logout", "anything", "test", "localhost", "local", "web", "signin", "signup", "cake"]

print(f"Scanning Target Address: {target}\n")
found = 0

for word in wordlist:
    url = f"{target}/{word}"
    try:
        respone = requests.get(url, timeout=5)
        if respone.status_code == 200:
            print(f"FOUND {url}")
            found = found + 1
        else:
            print(f"{respone.status_code}: {url}")
    except Exception as e:
        print(f"[ERORR] {url}")

print(f"\nScan Complete. {found} pages found.")