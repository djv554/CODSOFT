#program to implement rock, paper, scissors game

import random

def comp_choice():
    options = ['rock', 'paper', 'scissors']
    return random.choice(options)

def game_logic(player, comp):
    if player == comp:
        return "The game is draw!"
        
    elif (player=='rock' and comp=='scissors') or (player=='scissors' and comp=='paper') or (player=='paper' and comp=='rock'):
        return "You win!"
        
    else:
        return "You lose!"
        
def main():
    player_score=0
    comp_score=0
    print("\nWelcome to rock, paper and scissors game!!")
    while True:
        player=input("\nChoose one of the options: Rock, Paper or Scissors:").lower()
        if player not in ['rock','paper','scissors']:
            print("Invalid option! Try again")
            continue
            
        comp=comp_choice()
        print(f"\nComputer's choice:{comp}\n")
    
        result = game_logic(player,comp)
        print(result)
    
        if result=="You win!":
            player_score+=1
        
        elif result=="You lose!":
            comp_score+=1
    
    
        elif result=="The game is draw!":
            player_score+=1
            comp_score+=1
        
        print(f"Player:{player_score}   Computer:{comp_score}\n")
        
        p=input("Do you want to play another round? (yes/no):").lower()
        if p!="yes":
            break
            
    print("\nThanks for playing!")
        
   
main()