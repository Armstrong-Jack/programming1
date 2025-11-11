questions = ["What is 2+2?", "What is the capital of France?", "Whatkeyword defines a function?"]
answers = ["4", "Paris", "def"]
score = 0

for i in range(len(questions)):
    user_answer = input(questions[i])
    if user_answer == answers[i]:
        print("correct")
        score += 1
    else:
        print("Incorrect")
print(f"{score}/3")