colors = ['Hearts','Diamonds','Clubs','Spades']

figures = ['Ace','King','Queen','Jack','10','9']
                 
cards=[]

for i in colors:
    for j in figures:
       cards.append('%s %s' % (str(i),str(j)))
else:
    print('all cards:')
    print(cards)

import random
random.shuffle(cards)
print('shullfed cards:')
print(cards)
player1=[]
player2=[]
for i in range(0,len(cards)):
    if i%2==0:
       player1.append(cards[i])
    else:
       player2.append(cards[i])
else:
    print('players1 cards:', player1,sep='\n')
    print('players2 cards:', player2,sep='\n')


player1=cards[0:int(len(cards)/2)]
player2=cards[int(len(cards)/2):int(len(cards))]

print('player1 cards:', player1,sep='\n')
print('player2 cards:', player2,sep='\n')
