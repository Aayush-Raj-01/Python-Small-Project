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
player_scores = [0 for _ in range(len(players))]
