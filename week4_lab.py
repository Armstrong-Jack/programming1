
secreat_number = 22

while true:
    guess = int(input("Guess the secreat number between 1 and 100: "))
    if guess == secreat_number:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess < secreat_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")