while True:
  user_number=input('Give me a number 0-100 ,which computer have to guess: ')
  if user_number.isdecimal():
    user_number=int(user_number)
    if user_number>=0 and user_number<=100:
      break
    else:
      print('You have to select a number from 0 to 100')
  else:
      print('You have to enter a numeric value')

tries=0
min_number=0; max_number=100

while True:   
  comp_number=int((min_number+max_number)/2)
  tries+=1
  print('comp_number: ', comp_number)
  if comp_number==user_number:
    print('Comp, you guess a user number: %d in %d tries' %(user_number, tries))
    break
  elif comp_number<user_number:
    print('User number is bigger than: %d' %comp_number)
    min_number=comp_number+1
  else:
    print('User number is smaller than: %d' %comp_number)
    max_number=comp_number-1


print('-'*50)


import random

tries=0
min_number=0; max_number=100

while True:   
  comp_number=random.randint(min_number,max_number)
  tries+=1
  print('Dummy comp_number: ', comp_number)
  if comp_number==user_number:
    print('Dummy Comp, you guess a user number: %d in %d tries' %(user_number, tries))
    break
  elif comp_number<user_number:
    print('User number is bigger than: %d' %comp_number)
    min_number=comp_number+1
  else:
    print('User number is smaller than: %d' %comp_number)
    max_number=comp_number-1
