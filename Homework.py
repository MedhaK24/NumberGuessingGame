import random 
import os
os.system('clear')
number = random.randint(1,10)
chances=3
while(chances>0):
    guess=int(input('Choose a random number form 1 to 10 :'))
    if(guess==number):
        print("You've got the correct number!")
        break
    else:
        print('Incorrect guess, try again.')
    chances=chances-1
if(chances==0):
    print('You have no chances left. The correct answer is', number)