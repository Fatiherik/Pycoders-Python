import random
import time
start_time=time.time()
while True:
    user_choice=input("Enter your choice (Rock/Paper/Scissor): ")
    print("User choice is: "+user_choice)
    print("Now it is computer turn...")
    while True:
        time.sleep(3)
        alternatives=["Rock","Paper","Scissor"]
        computer_choice=random.choice(alternatives)
        if user_choice!=computer_choice:
            break
    print("Computer choice is: "+computer_choice)
    print(user_choice+" V/s "+computer_choice)
    if user_choice=="Rock" and computer_choice=="Paper":
        print(computer_choice+" wins => computer wins")
    elif user_choice=="Rock" and computer_choice=="Scissor":
        print(user_choice+" wins => user wins")
    if user_choice=="Paper" and computer_choice=="Rock":
        print(user_choice+" wins => user wins")
    if user_choice=="Paper" and computer_choice=="Scissor":
        print(computer_choice+" wins => computer wins")
    if user_choice=="Scissor" and computer_choice=="Paper":
        print(user_choice+" wins => user wins")
    if user_choice=="Scissor" and computer_choice=="Rock":
        print(computer_choice+" wins => computer wins")

    again=input("Do you want to play again?: ")
    if again=="N":
        break
end_time=time.time()
print("bu oyun" +str(end_time-start_time)+ "saniye sürdü")

