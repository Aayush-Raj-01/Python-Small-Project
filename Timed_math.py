import random
import time

OPERARTORS = ["+","-","*"]
TOTAL_PROBLRM = random.randint(3,12)

def problem():
    left = random.randint(1,50)
    right = random.randint(1,50)
    operator = random.choice(OPERARTORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)

    return expr,answer

wrong = 0
input("   Press enter to START!!")
print("---------------------------")

start_time = time.time()

for i in range(TOTAL_PROBLRM):
    expr,answer = problem()
    while True:
        guess = input("Problem #" + str(i+1)+ ":\n" + expr + "= ")
        if guess == str(answer):
            break
        else:
            wrong += 1
            print("ITS A WRONG ANSWER TRY AGIAN!!!")

end_time = time.time()

total_time = end_time - start_time
print("--------------------------------")
print("Nice Work !!! You Finshed in ",round(total_time,2),"sec")