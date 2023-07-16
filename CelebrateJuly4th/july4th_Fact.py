import random
facts = ['Thomas Jefferson was the main author of the Declaration of Independence.',
         'John Hancock was the first person to sign the Declaration of Independence.',
         'Independence Day should have been celebrated on July 2, 1776.',
         'John Adams wrote a letter to his wife about how memorable Independence Day would be in American history.',
         "The 'Pennsylvania Evening Post' was the first newspaper to print the Declaration."
         'An estimated 2.5 million people lived in the nation in July 1776.',
         'Three presidents who signed the Declaration of Independence died on July 4.',
         'The Liberty Bell rings 13 times every Independence Day to honor the 13 original states.',
         'Independence Day was once celebrated on July 5.',
         'The very first 4th of July fireworks show took place in Philadelphia in 1777.',
         'Americans spend over $1 billion on fireworks every year.',
         'There are 33 places in the United States with the word “liberty” in their names.',
         'Calvin Coolidge was the only president born on the 4th of July',
         "It didn't become a federal holiday until 1870.",
         'The Declaration of Independence and the Constitution were both signed in Philadelphia.']
c = True
x = input('Happy Independce day, Do you want a random fact about Independence day?(yes/no): ')
if x.lower() == 'yes':
    print(random.choice(facts))
if x.lower() == 'no':
    print('Have a nice independece day')
    exit()
while c:
    x = input('Would you like another fact?(yes/no): ')
    if x.lower() == 'no':
        print('Have a nice independece day')
        exit()
    if x.lower() == 'yes':
        print(random.choice(facts))