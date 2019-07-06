##import random
##
##numbers=set(range(1,50))
##luckyNumbers=[]
##print(numbers)
##while len(luckyNumbers)<6:
##    drawnNumber=random.choice(list(numbers))
##    print(drawnNumber)
##    luckyNumbers.append(drawnNumber)
##    numbers.remove(drawnNumber)
##else:
##    print(luckyNumbers)
##    print(numbers)

import random

numbers=set(range(1,50))
luckyNumbers=[]
while len(luckyNumbers)<6:
    drawnNumber=random.choice(list(numbers))
    luckyNumbers.append(drawnNumber)
    numbers.remove(drawnNumber)
else:
    print(luckyNumbers)

