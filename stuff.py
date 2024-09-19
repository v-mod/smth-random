import math

# Add N here
N = 908

lastNumToCheck = round(math.sqrt(N))
correctNum=[]

print(lastNumToCheck)

for x in range(1,lastNumToCheck+1):
    sqred = x*x
    if sqred > N:
        break
    else:
        correctNum.append(sqred)

print(correctNum)