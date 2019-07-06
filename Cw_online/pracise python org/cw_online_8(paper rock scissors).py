player1_score=0
player2_score=0


def compareValues(value1,value2):
    global player1_score; global player2_score
    
    if value1==value2:
        print('Tie, neither player get score!'.center(50))
        print(f' Player1:Player2 {player1_score}:{player2_score}'.center(50))
    elif (value1=='R' and value2=='S') or (value1=='S' and value2=='R'):
        print ('Rock won!'.center(51))
        if value1=='R':
            player1_score+=1
            print('Player 1 get score!'.center(52))
            print(f' Player1:Player2 {player1_score}:{player2_score}'.center(50))
        else:
            player2_score+=1
            print('Player 2 get score!'.center(52))
            print(f' Player1:Player2 {player1_score}:{player2_score}'.center(50))
    elif (value1=='S' and value2=='P') or (value1=='P' and value2=='S'):
        print ('Scissors won!'.center(51))
        if value1=='S':
            player1_score+=1
            print('Player 1 get score!'.center(52))
            print(f' Player1:Player2 {player1_score}:{player2_score}'.center(50))
        else:
            player2_score+=1
            print('Player 2 get score!'.center(52))
            print(f' Player1:Player2 {player1_score}:{player2_score}'.center(50))
    else:
        print ('Paper won!'.center(51))
        if value1=='P':
            player1_score+=1
            print('Player 1 get score!'.center(52))
            print(f' Player1:Player2 {player1_score}:{player2_score}'.center(50))
        else:
            player2_score+=1
            print('Player 2 get score!'.center(52))
            print(f' Player1:Player2 {player1_score}:{player2_score}'.center(50))
    print('-'*50,'\n')

while player1_score<3 and player2_score<3:
    players_chooses={'player1_choose' : '', 'player2_choose': ''}                   
    for k in players_chooses.keys():
        while True:
            try:
                v=input(f'{k}: Rock(R) or Paper(P) or Scissors(S) : ').upper()
                if v not in('RPS'):
                    raise Exception 
                players_chooses[k]=v
                break
            except Exception:
                print('Wrong Value, Select R or P or S one more time')
    else:
        print('\n','-'*50,'\n',players_chooses)
        compareValues(*players_chooses.values())
else:
    if player1_score==3:
        print(f'GameOver Player 1 won: {player1_score} : {player2_score} !!!'.center(50))
    else:
        print(f'GameOver Player 2 won: {player2_score} : {player1_score} !!!'.center(50))

        

    
