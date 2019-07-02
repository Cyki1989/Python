import random
min=1
max=6
dice=[]
for i in range(5):
    dice.append(random.randint(min,max))
else:
    dice.sort()
    print(dice)

from random import*
passwordLenght=randint(0,8)+4
password=[]
for i in range(passwordLenght):
    if not i:
        password.append(chr(choice([randint(32,47),randint(58,64),\
                        randint(91,96),randint(123,126)])))
    elif i==1:
        password.append(chr(randint(48,57)))
    elif i==2:
        password.append(chr(randint(65,90)))
    elif i==3:
        password.append(chr(randint(97,122)))
    else:
        password.append(chr(randint(32,126)))
else:
    shuffle(password)
    password=''.join(password)
    print(password)    
