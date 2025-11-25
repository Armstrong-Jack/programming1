import requests

url = "https://official-joke-api.appspot.com/random_joke"
print("Calling the server")
response = requests.get(url)


if response.status_code == 200:
    joke_data = response.json()

    setup=joke_data["setup"]
    punchline = joke_data["punchline"]

    print("--------------------")
    print(f"Joke {setup}")
    print(f"Answer {punchline}")
    print("--------------------")

