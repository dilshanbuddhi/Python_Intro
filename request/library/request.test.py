import requests as request


"""response = request.get("https://api.github.com/events")

if(response.status_code == 200):
    print("success")
    print(response.headers['content-type'])
    print()
    print(response.text[0:100])

else:
    print("error")"""


# Authentication example
import requests
url = 'https://httpbin.org/get'
username = 'dila'
password = '1234'
response = requests.get(url, auth=(username, password))
if response.status_code == 200:
    print("Authentication successful.")
    print(response.text)
else:
    print(f"Authentication failed with status code: {response.status_code}")
