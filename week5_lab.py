
def option(name, choice_ending1, choice_ending2, choices1 , choices2):
    print(name)
    choice = input(f"Do you go {choices1} or {choices2}")

    if choice == choices1:
        print(choice_ending1)
        return 1

    elif choice == choices2:
        print(choice_ending2)
        return 2

    else:
        print("wrong value entered you lose")

name = "you are in a dark forest. you see two paths"
choices1 = "left"
choices2 = "right"
choice_ending1 = "you walk down the left path and find a river"
choice_ending2 ="you walk down the right path and encounter a spleeping bear"


if option(name, choice_ending1, choice_ending2, choices1 , choices2) == 1:
    name = "Do you 'swim' accross or 'follow' the rivewr bank"
    choices1 = "swim"
    choices2 = "follow"
    choice_ending1 ="you are tired from swimmming and rest. YOU WIN!!!"
    choice_ending2 ="you follow the river bank and find a hidden cave. YOU WIN!"
    option(name, choice_ending1, choice_ending2, choices1 , choices2)

elif option(name, choice_ending1, choice_ending2, choices1 , choices2) == 2:
    name ="do you 'tiptoe' past or 'run' away"
    choices1 ="tiptoe"
    choices2 ="run"
    choice_ending1 ="you successfully sneak past the bear. you win!"
    choice_ending2 ="you trip while runing and the bear wakes up. you lose"
    option(name, choice_ending1, choice_ending2, choices1 , choices2)
