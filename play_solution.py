columns_number = 3
row_0 = ['-', '-', '-']
row_1 = ['-', '-', '-']
row_2 = ['-', '-', '-']

rows = [row_0, row_1, row_2]
current_player = 'X'
winner = None


while winner is None:

    # print board
    for row in rows:
        print(row)

    # player move
    print(f'Player {current_player} turn.')
    row_selected = int(input('Select row number (0-2)'))
    column_selected = int(input('Select column number (0-2)'))

    rows[row_selected][column_selected] = current_player

    # check winner by row
    for row in rows:
        if all(sign == current_player for sign in row):
            print(f'Player {current_player} is a winner!')
            winner = current_player

    # check winner by column:
    for index in range(columns_number):
        column = [
            row_0[index],
            row_1[index],
            row_2[index]
        ]
        if all(sign == current_player for sign in column):
            print(f'Player {current_player} is a winner!')
            winner = current_player

    # check_winner_by_cross
    cross_1 = [
        row_0[0],
        row_1[1],
        row_2[2]
    ]
    cross_2 = [
        row_0[2],
        row_1[1],
        row_2[0]
    ]
    if all(sign == current_player for sign in cross_1):
        print(f'Player {current_player} is a winner!')
        winner = current_player

    if all(sign == current_player for sign in cross_2):
        print(f'Player {current_player} is a winner!')
        winner = current_player

    # switch player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'

    # One more time...
