# Python quiz game


questions = ("which animal lays the largest egg?",
             "what is the name of the largest sea animal?",
                         "what is the first element that formed? ",
                         "what is the largest desert ",
                         "which planet is the coldest in the solar system?",
                         "how many teeth does a adult have?")


options = (("A.Crocodile","B.Ostrich","C.Snake","D.Chicken"),
                   ("A.Great white shark","B.lion's mane jellyfish","C.Whale shark","D.Blue whale"),
                   ("A.Helium ","B.Oxygen","C.Hydrogen","D.Oganesson"),
                   ("A.Sahara ","B.Arabian","C.Antarctic","D.Arctic"),
                   ("A.Nuptune","B.Uranus","C.saturn","D.mars"),
                   ("A.32","B.34","C.29","D.30"))


answers = ("B","D","C","C","B","A")
guesses = []
score = 0
question_num = 0


for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)


    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1


print("----------------------")
print("       RESULTS        ")
print("----------------------")


print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()


print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()


score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")