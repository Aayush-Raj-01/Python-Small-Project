import random

choices = ["rock","paper","scissors"]

print("**************************************")
print("WELCOME TO ROCK PAPER SCISSOR GAME")



going = "y"
comppoint = 0
userpoint = 0

while going == "y":
    compchoice = random.randint(0,2)

    compchoice = choices[compchoice]
    print('''    Rock = 0
    Paper = 1
    Scissors = 2 ''')
    userchoice = input("TYPE YOUR CHOICE = ")
    userchoice = int(userchoice)
    userchoice = choices[userchoice]
    if(userchoice == compchoice):
        print("Draw")
    else:
        userWin = True
        if(userchoice == "rock"):
            userWin = True if compchoice == "scisspprs" else False
        elif(userchoice == "paper"):
            userWin = True if compchoice == "rock" else False
        else:
            userWin = True if compchoice == "paper" else False
        if(userWin):
            print("YOUR WON")
            userpoint +=1
        else:
            print("YOU LOSE")
            comppoint +=1
    print(f"************YOUR POINT = {userpoint} COMPUTER POINT = {comppoint}************")
    print("DO YOU WANNA PLAY AGIN ?")
    going = input("Type y for YES and n for NO = ")

print("*************FINAL POINTS ARE *************")    
print(f"YOUR POINTS = {userpoint} COMPUTER POINT = {comppoint}")
if (userpoint >> comppoint):
    print("YOU HAVE HIGH POINTS THAN COMPUTER")
else:
    print("COMPUTER HAVE HIGHER POINTS THAN YOU")
    
