
from random import*
passwordLenght=randint(0,8)+4
password=[]
specialDigits=list(range(32,48))+list(range(58,65))+list(range(91,97))+list(range(123,127))
for i in range(passwordLenght):
    if not i:
        password.append(chr(choice(specialDigits)))
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
