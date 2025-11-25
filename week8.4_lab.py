import requests

url = "https://official-joke-api.appspot.com/random_joke"
print("Calling the server")
response = requests.get(url)

print(f"Status code {response.status_code}")

print("raw Data")
print(response.text)
