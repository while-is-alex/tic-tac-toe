def row_choice(player, first_row, second_row, third_row):
    """Asks for player's input to convert a row choice (string)
    into the correspondent list.
    Returns a list"""
    if player == 1:
        row = input('Player 1, you\'re "X". Choose a row (1, 2 or 3): ')
    elif player == 2:
        row = input('Player 2, you\'re "O". Choose a row (1, 2 or 3): ')

    if row == '1':
        row = first_row
        return row
    elif row == '2':
        row = second_row
        return row
    elif row == '3':
        row = third_row
        return row
    else:
        print('Please, choose a valid option.')
        return row_choice(player, first_row, second_row, third_row)


def column_choice():
    """Asks for player's input to convert a column choice (string)
    into the correspondent list index.
    Returns an integer."""
    column = input('Now, choose a column (a, b or c): ').lower()
    if column == 'a':
        index_number = 0
        return index_number
    elif column == 'b':
        index_number = 1
        return index_number
    elif column == 'c':
        index_number = 2
        return index_number
    else:
        print('Please, choose a valid option.')
        return column_choice()
