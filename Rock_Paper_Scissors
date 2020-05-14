#author: Tyler Elenberger
#created: 10/20/2019

import random 

def Intro():
    print("Play a game of rock paper scissors against the CPU: ")
    print("Here's how it works: ")
    print("Enter a number between 1-3 to pick rock, paper, or scissors: ")
    print("Enter 1 for rock")
    print("Enter 2 for paper")
    print("Enter 3 for scissors")

def getInputs():
    user = int(input("\nInput your choice: "))
    while (user > 3) or (user < 1):
        print("Invaild choice! Try again!")
        user = int(input("\nInput your choice: "))
    return user

def simGame(user):
    CPU = random.randint(1,3)
    if user == 1:
        user_choice = 'Rock'
    elif user == 2:
        user_choice = 'Paper'
    else:
        user_choice = 'Scissors'
    
    print("User's choice is: ",user_choice)
    print("Now it's the CPU's turn...")
    
    while CPU == user:
        CPU = random.randint(1,3)
        
    if CPU == 1:
        CPU_choice = 'Rock'
    elif CPU == 2:
        CPU_choice = 'Paper'
    else:
        CPU_choice = 'Scissors'
        
    print("Computer's choice is: ",CPU_choice)
    
    print("\n",user_choice," vs. ",CPU_choice)
    
    if ((user == 1 and CPU == 2) or (user == 2 and CPU == 1)):
        print("Paper beats rock")
        result = 'Paper'
    elif((user == 1 and CPU == 3) or (user == 3 and CPU == 1)):
        print("Rock beats scissors")
        result = 'Rock'
    else:
        print("scissors beats paper")
        result = 'Scissors'
        
    if result == user_choice:
        print("\nYou win!!")
    else:
        print("\nCPU wins!!")
        
    return result
    
def main():
    Intro()
    user = getInputs()
    user = simGame(user)
  
main()
