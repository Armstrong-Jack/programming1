

while True:
    try:
        age = int(input("How old are you?(Numbers ONLY!)"))
        break
    except ValueError:
        print("Incorrect input")

if age >= 18:
    print("you are an adult")
else:
    print("you are a minor")    
