import time
import requests



try:
    URL = input("Please enter the URL you would like to inspect: ")
    response = requests.get(URL, timeout=5)
    if response.status_code == 200:
        print("URL is valid Details below")
        print(f"content type: {response.headers.get("Content-Type", 'N/A')}")
        print(response.headers.get("content-length"))
        print(response.headers.get("content-disposition"))
        print(response.headers.get("content-encoding"))
        xpowered = response.headers.get("x-powered-by")
        print(f"XPowered by {xpowered if xpowered else 'Not Disclosed'}")
        print(response.headers.get("Connection"))
        print(response.headers.get("Transfer-Encoding"))
        print(f"status code: {response.status_code}")
        print(f"headers: {response.headers}")
        print(f"response time: {response.elapsed.total_seconds()}")
    elif response.status_code == 404:
        print("ERORR CODE 404")
    else:
        print(f"somthing is wrong {response.status_code}")
except Exception as e:
    print(e)