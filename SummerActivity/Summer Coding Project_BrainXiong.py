print('Welcome to Trivia')
print('Answer 5 questions correctly and you win!')
def question():
    c=input('what month does summer start? (answer in full lowercase) \n')
    if c=='june':
        print('Correct, next question')
        c=input('What season comes after summer? (4 letters) \n')
    else:
        print('Incorrect, Game Over')
        quit()
    if c=='fall':
        print('Correct, next question')
        c=input('Which season has the shortest amount of daylight? \n')
    else:
        print('Incorrect, Game Over')
        quit()
    if c=='winter':
        print('Correct, next question')
        c=input('What date is the sun out the longest? (Answer M/D) \n')
    else:
        print('Incorrect, Game Over')
        quit()
    if c=='7/21':
        print ('Correct, final question')
        c=input('How many days are in summer (Exact number) \n')
    else:
        print('Incorrect, Game Over')
        quit()
    if c=='93.6':
        print('no way you knew that, cheater')
        quit()
    else:
        print('Incorrect, Game Over')
        quit()
question()
