'''
import random

secret_number=''
for i in range(0,4):
    secret_number+=str(random.randint(0,9))
print(secret_number)

print('Welcome to the Cows and Bulls Game!'.center(50))
while True:
    user_number=input('Enter a number:\n>>>> ')
    secret_number_copy=secret_number
    for i in range(0,4):
        if user_number[i]==secret_number_copy[i]:
             user_number[i]='c'
             secret_number_copy[i]='c'
    if user_number=='cccc':
        print('Congratulation, you guess a secret_number %s!'.center(50)%secret_number)
        break
    for i in range(0,4):
        if user_number[i] != 'c':
           find_index=secret_number_copy.find(user_number[i]) 
           if find_index != -1:
              user_number[i]='b'
              secret_number_copy[find_index]='b'
    print('%d cows, %d bulls'%(user_number.cout('c'),user_number.cout('b')))
'''


import random

secret_number=[]
for i in range(0,4):
    secret_number.append(str(random.randint(0,9)))
print(secret_number)

print('Welcome to the Cows and Bulls Game!'.center(50))
while True:
    user_number=list(input('Enter a number:\n>>>> '))
    secret_number_copy=secret_number.copy()
    for i in range(0,4):
        if user_number[i]==secret_number_copy[i]:
             user_number[i]='c'
             secret_number_copy[i]='c'
    if user_number==['c','c','c','c']:
        print('Congratulation, you guess a secret_number %s!'.center(50)%''.join(secret_number))
        break
    for i in range(0,4):
        if user_number[i] != 'c':
           if user_number[i] in secret_number_copy:
               find_index=secret_number_copy.index(user_number[i])
               user_number[i]='b'
               secret_number_copy[find_index]='b'
    print('%d cows, %d bulls'%(user_number.count('c'),user_number.count('b')))
