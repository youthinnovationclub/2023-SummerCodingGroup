import random
trivia_questions = [
    {
        "question": "What popular outdoor game involves throwing bags filled with corn kernels?",
        "answer": "cornhole"
    },
    {
        "question": "What activity involves riding ocean waves on a board?",
        "answer": "surfing"
    },
    {
        "question": "What frozen treat is often made from fruit juice or yogurt?",
        "answer": "popsicle"
    },
    {
        "question": "What is the name of the outdoor meal where food is cooked over an open flame?",
        "answer": "barbecue"
    },
    {
        "question": "What is the sport that involves hitting a ball over a net with a racket?",
        "answer": "tennis"
    },
    {
        "question": "What is a popular sport involving hitting a ball and then running to bases?",
        "answer": "baseball"
    }
]

random.shuffle(trivia_questions)

print("Welcome to the Summer Activities Trivia Game!")
score = 0
for question in trivia_questions:
    print("\n" + question["question"])
    user_answer = input("Your Answer: ").lower()

    if user_answer == question["answer"]:
        print("Correct! You got a point.")
        score += 1
    else:
        print(f"Sorry, the correct answer is: {question['answer']}")

print("\nTrivia game finished!")
print(f"Your final score is: {score}/{len(trivia_questions)}")
