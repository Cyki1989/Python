colors = ['Hearts','Diamonds','Clubs','Spades']

figures = [
    {'Figure':'Ace',  'Power':14},
    {'Figure':'King', 'Power':13},
    {'Figure':'Queen','Power':12},
    {'Figure':'Jack', 'Power':11},
    {'Figure':'10',   'Power':10},
    {'Figure':'9',    'Power':9}]

cards=[]

aCard={}

for i in colors:
    for j in figures:       
       aCard=j.copy()
       aCard['Color']=str(i)
       cards.append(aCard)
else:
    print('all cards:')
    print(cards)

import random
random.shuffle(cards)
print('shullfed cards:')
print(cards)
player1=[]
player2=[]
stack=[]
for i in range(0,len(cards)):
    if i%2==0:
       player1.append(cards[i])
    else:
       player2.append(cards[i])
else:
    print('players1 cards:', player1,sep='\n')
    print('players2 cards:', player2,sep='\n')

while len(player1) and len(player2):
    print('Player1 cards:', len(player1), '\tPlayer2 cards:', len(player2))
    card1=player1.pop(0)
    card2=player2.pop(0)
    stack.append(card1)
    stack.append(card2)
    print('card1:', card1['Power'], '\tvs\tcard2:', card2['Power'])
    if card1['Power']>card2['Power']:
        player1.extend(stack)
        stack.clear()
    elif card1['Power']<card2['Power']:
        player2.extend(stack)
        stack.clear()
    else:
        print('War!!!'.center(40))
        if len(player1) and len(player2):
            stack.append(player1.pop(0))
            stack.append(player2.pop(0))
else:
    if len(player1):
        print('Player1 Won!!!'.center(40))    
    else:
        print('Player2 Won!!!'.center(40))   
        
    
