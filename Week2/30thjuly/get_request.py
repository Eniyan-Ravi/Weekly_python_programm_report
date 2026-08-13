#GET request
import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print(response)
print(response.status_code)
print("")
users = response.json()
print(users[0]["name"])
for user in users:
    print(user["id"], user["name"])