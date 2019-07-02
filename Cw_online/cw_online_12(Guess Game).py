import random
secret_number=random.randint(1,9)
tries=0

while True:
    user_number=input('Guess a secret number (1-9) or write exit to end game: ')
    if user_number=='exit':
        print('GG')
        break
    elif user_number in '1 2 3 4 5 6 7 8 9'.split(' '):
        user_number=int(user_number)
        tries+=1
        if secret_number==user_number:
            print('You guess a secret number: %d in %d tries' %(secret_number, tries))
            break
        elif secret_number>user_number:
            print('Secret number is bigger than: %d' %user_number)
        elif secret_number<user_number:
            print('Secret number is smaller than: %d' %user_number)
    else:
        print('You have to select a number from 1 to 9')
