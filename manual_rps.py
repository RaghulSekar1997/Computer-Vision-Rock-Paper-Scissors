#%% Import libary
import random

#%% gets computer choice
def get_computer_choice():
    a = ['rock','paper','scissors']
    computer_choice = random.choice(a)
    return computer_choice
#%% gets user choice
def get_user_choice():
    user_choice = input("Rock (r), paper (p), scissors (S)")
    if user_choice == 'r':
        return "rock"
    elif user_choice == "p":
        return "papaer"
    elif user_choice == "s":
        return "scissors"
    else:
        return "invalid"
#%% gets winner
def get_winner(uc,cc):
    if uc == cc:
        return "Play again"
    elif uc == 'rock':
        if cc == 'scissors':
            return "Rock sharpens scissors: you win"
        elif cc == 'paper':
            return "Paper wraps rock: computer wins"
        else:
            return "The computer's selection could not be processed"
    elif uc == 'scissors':
        if cc == 'paper':
            return "Scissors cut paper=: you win"
        elif cc == 'rock':
            return "Rock sharpens scissors: computer wins"
        else:
            return "The computer's selection could not be processed"
    elif uc == 'paper':
        if cc == 'scissors':
            return "Scissors cut paper=: computer wins"
        elif cc == 'rock':
            return "Rock sharpens scissors: you win"
        else:
            return "The computer's selection could not be processed"
    else:
        return "Invalid Input"


#%% main function
def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    print ("Your: ", user_choice)
    print ("Computer: ",computer_choice)
    print(get_winner(user_choice,computer_choice))
#%% calls rps game
play()
