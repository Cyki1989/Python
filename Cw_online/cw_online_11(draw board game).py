def draw_board_game(board_game_size):
    rows=int(board_game_size.split('x')[0])
    columns=int(board_game_size.split('x')[1])
    for i in range(0,rows):
        print(' ---'*columns)
        print('|   '*columns+'|')
    print(' ---'*columns)

##board_game_size=input('Give me a board game size')
draw_board_game('10x20')

