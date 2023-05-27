from game import Game


def play():
    game = Game()
    # The variable that controls whether any condition that ends the game has been met
    is_game = True
    # Asks for user input to check if it's a player vs player game or playes vs AI
    number_players = int(input('Are there 1 or 2 players? '))
    if number_players == 1:
        print('Playing vs AI... 🤖\n')

    while is_game:
        game.update_board()
        # Checks if there are 2 human players
        if number_players == 2:
            is_game = game.moves_available()
            game.new_turn()
        # Or if there's only 1 human player vs an AI
        elif number_players == 1:
            # If the active player is human
            if game.player == 1:
                is_game = game.moves_available()
                game.new_turn()
            # If the active player is an AI
            elif game.player == 2:
                is_game = game.moves_available()
                game.ai_turn()
        # Catches an invalid input
        else:
            print('Number of players invalid. Please, choose 1 or 2 for the number of players.')
        # Checks if there's a winner
        is_game = game.winner_check()

        # Changes the active player for the next turn
        if game.player == 1:
            game.player = 2
        elif game.player == 2:
            game.player = 1

    # If the game is finished, a new game can be initialized if the player chooses so
    new_game = input('Do you want to start a new game? ').lower()
    if new_game == 'yes' or new_game == 'y':
        play()
    elif new_game == 'no' or new_game == 'n':
        print('GGs')
    else:
        print('Input not recognized. Please, reply with "yes" or "no".')


# Starts the game
play()
