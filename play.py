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
    # TODO
    number = int(input('Please give me a number...'))
    print(f'Number you gave me: {number}')

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
    # TODO

    # switch player
    # TODO

    # One more time...
