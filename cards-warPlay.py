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
for i in range(0,len(cards)):
    if i%2==0:
       player1.append(cards[i])
    else:
       player2.append(cards[i])
else:
    print('players1 cards:', player1,sep='\n')
    print('players2 cards:', player2,sep='\n')

while len(player1)>0 and len(player2)>0:
    print('Player1 cards:', len(player1), '\tPlayer2 cards:', len(player2))
    card1=player1.pop(0)
    card2=player2.pop(0)
    print('card1:', card1['Power'], '\tvs\tcard2:', card2['Power'])
    if card1['Power']>card2['Power']:
        player1.append(card1)
        player1.append(card2)
    elif card1['Power']<card2['Power']:
        player2.append(card2)
        player2.append(card1)
    else:
        player1.append(card1)
        player2.append(card2)
else:
    if len(player1):
        print('Player1 Won!!!'.center(50))    
    else:
        print('Player2 Won!!!'.center(50))   
        
    
