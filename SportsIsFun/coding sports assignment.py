import random
def power_of_shot():
    x=random.randint(1,10)
    n=1
    for z in range(0,3):
        p=int(input('Choose the Power of your shot 1-10 \n'))
        if x==p:
            print('You scored!')
            quit()
        else:
            print('You missed, Try Again')
    print('you missed all 3 shots')
    quit()
power_of_shot()