import random


roll = random.randint(1,6)

while True:
    players = int(input("Enter the number of players (2-4): "))
    if 2<= players <= 4:
        break
    else:
        print("Invalid, try again")

print(players)

max_score = 50
player_scores = [0 for _ in range(players)]


while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nPlayer",player_idx + 1,"turn has just started!!\n")
        print("Your Total score is:",player_scores[player_idx], "\n")
        current_score = 0
        while True:
            should_roll = input("Would you like to roll (y)?")
            if should_roll.lower() != "y":
                break

            roll = random.randint(1,6)
            if roll == 1:
                print("You rolled a 1!, Turn done!")
                current_score = 0
                break
            else:
                current_score += roll
                print(f"You rolled a {roll}")
            
            print("Your score is :",current_score )

        player_scores[player_idx] += current_score
        print("Your Total score is :",player_scores[player_idx])


max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number",winning_idx + 1 , "is the winning PLAYER CONGRATS!!!\n","MAXIMUM SCORE IS :",max_score)