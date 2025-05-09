import random

def roll():
    rollup = random.randint(1,6)
    return rollup

while True:
    players = input("Enter number of player(2-4): ")
    if players.isdigit():
        players =  int(players)
        if 2 <= players <= 4:
            break
        else:
            print("ERROR! Players must be between 2-4.")
    else:
        print("Invalid Input! Please Enter number.")     
        
max_score = 30
player_score = [0 for i in range(players)]

while max(player_score) < max_score: 
    
    for player_indx in range(players):
        score = 0
        print("\n")
        for player_indx in range(players):
            print(f"Player {player_indx+1}'s score is: {player_score[player_indx]}")
        print("\n")
          
        print(f"Player {player_indx +1}'s turn has started \n{player_indx+1}'s score is: {player_score[player_indx]}")
        while True:
            choice = input("Do toy want to roll?(Yes) ")
            if choice.lower() != "yes":
                print("OK! You don't want to roll again!")
                break
            
            value = roll()
            if value == 1:
                print("You just rolled 1 and here your scores become zero!")
                score = 0
                break
            
            else:
                score +=value
                print("You rolled a: ",value)
                
                
        print("Your current score is: ",score)
        player_score[player_indx] +=   score
        print("Player" ,player_indx + 1 , "'s Score is: ",player_score[player_indx])
        
        
max_pla = max(player_score)
winning_index = player_score.index(max_pla)

print(f"Player no. {winning_index+1} has won with the score of {max_pla}")      