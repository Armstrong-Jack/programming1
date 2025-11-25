#This simulates data we might get from a User API
fake_api_data = {
    "status": "success",
    "total_results": 2,
    "users": [
        {"id": 1, "name": "John", "contact": {"email": "john@test.com"}},
        {"id": 2, "name": "Jane", "contact": {"email": "jane@test.com"}}
    ]
}
# HINT:
# 1. Access the "users" list first: fake_api_data["users"]
# 2. Access the second item (index 1): ... [1]
# 3. Access the "contact" dictionary: ... ["contact"]
# 4. Access the "email" key: ... ["email"]

while True:
    try:
        entered_id = int(input("what user are you trying to access?(Numbers ONLY!)"))
        break
    except ValueError:
        print("Incorrect input")

if entered_id == 1:
    data = fake_api_data["users"]
    email = data[0]
    email1 = email["contact"]
    email2 = email1["email"]
    print(email2)



elif entered_id == 2:
    data = fake_api_data["users"]
    email = data[1]
    email1 = email["contact"]
    email2 = email1["email"]
    print(email2)
else:
    "incorrect input"