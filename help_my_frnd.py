num = input()

digit = len(num)
n=0
sum = 0
fnum = int(num)
num = int(num)
while fnum >0:
    n = fnum % 10
    sum = sum + (n ** digit)
    fnum = fnum // 10

if num == sum:
    print("its a armstrong number")
else:
    print("Its not a aarmstring number")