from random import randint
from time import time
start_time=time()
a=randint(1,100)
print(a)
while True:
    user_guess = int(input("Please enter your guess: "))
    if user_guess<a:
        print("Your guess is lower than the number")
    elif user_guess>a:
        print("Your guess is greater than the number")
    else:
        end_time = time()
        print("You guess the number correctly in " + str(end_time - start_time) + " seconds")
        break