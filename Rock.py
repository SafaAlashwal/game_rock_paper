import random

game_list=["rock","scissor","paper"]

try_=6
player_one=0
playe_two=0


print(game_list)
while try_>0:
    player1=random.choice(game_list)
    player2=input("Enter on of list: ")
    print(f"{player1}:{player2}" )
    if player1=="paper":
            if player2=="rock":
                player_one+=1
                print(f"{player_one}  :  {playe_two}")
            elif player2=="scissor":
                 playe_two+=1
                 print(f"{player_one}  :  {playe_two}")
            else:
                 print(f"{player_one}  :  {playe_two} تعادل")

    elif player1=="rock":
            if player2=="paper":
                playe_two+=1
                print(f"{player_one}  :  {playe_two}")
            elif player2=="scissor":
                 player_one+=1
                 print(f"{player_one}  :  {playe_two}")
            else:
                 print(f"{player_one}  :  {playe_two} تعادل")                 
                   

    else:
            if player2=="paper":
                player_one+=1
                print(f"{player_one}  :  {playe_two}")
            elif player2=="rock":
                 playe_two+=1
                 print(f"{player_one}  :  {playe_two}")
            else:
                 print(f"{player_one}  :  {playe_two} تعادل")                 
    try_-=1
