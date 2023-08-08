import random
from sys import breakpointhook

print('Welcome to the guessing game!')


sports_list = ('golf', 'basketball', 'football', 'soccer', 'swimming', 'batminton', 'tennis', 'pool', 'hockey', 'boxing', 'volleyball', 'track', 'baseball', 'lacrosse', 'gymnastics', 'bowling', 'wrestling', 'fencing', 'softball')

Guess = True

def win():
  return

#Inputting a list into this isn't working so..
while Guess:
  chosen_number = random.randint(0, 20)
  if chosen_number == 1:
    chosen_sport = 'golf'
  elif chosen_number == 2:
    chosen_sport = 'basketball'
  elif chosen_number == 3:
    chosen_sport = 'football'
  elif chosen_number == 4:
    chosen_sport = 'soccer'
  elif chosen_number == 5:
    chosen_sport = 'swimming'
  elif chosen_number == 6:
    chosen_sport = 'batminton'
  elif chosen_number == 7:
    chosen_sport = 'tennis'
  elif chosen_number == 8:
    chosen_sport = 'pool'
  elif chosen_number == 9:
    chosen_sport = 'hockey'
  elif chosen_number == 10:
    chosen_sport = 'boxing'
  elif chosen_number == 11:
    chosen_sport = 'volleyball'
  elif chosen_number == 12:
    chosen_sport = 'track'
  elif chosen_number == 13:
    chosen_sport = 'baseball'
  elif chosen_number == 14:
    chosen_sport = 'lacrosse'
  elif chosen_number == 15:
    chosen_sport = 'gymnastics'
  elif chosen_number == 16:
    chosen_sport = 'bowling'
  elif chosen_number == 17:
    chosen_sport = 'wrestling'
  elif chosen_number == 18:
    chosen_sport = 'fencing'
  elif chosen_number == 19:
    chosen_sport = 'softball'
  else:
    chosen_sport = 'cricket'

  for i in range(5):  
    guess = input("Guess which sport I'm thinking of! ")
    if guess.lower == chosen_sport:
      print('Good job! You win!')
      win()
      break
    else: print('Oops! try again.')
    

  answer = input("You couldn't guess the sport! Would you like to try again? (y/n) ")
  if answer == 'y':
    continue
  elif answer == 'n':
    break
  else:
    print("Don't understand, so I'll take it as a no.")
    break

  