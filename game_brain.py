from choices import row_choice, column_choice
import random


class Game:
    def __init__(self):
        """Initializes the game by generating the lists that represent each space on the board,
         fills the board with the correspondent element from each list,
         controls the current active player and passes all that information to every method of the class."""
        self.player = 1
        self.title = '\n------- TIC-TAC-TOE -------\n'
        self.first_row = ['-', '-', '-']
        self.second_row = ["-", "-", '-']
        self.third_row = ["-", "-", '-']
        self.board = f"""       a     b     c
          |     |     
    1  {self.first_row[0]}  |  {self.first_row[1]}  |  {self.first_row[2]}  
     _____|_____|_____
          |     |     
    2  {self.second_row[0]}  |  {self.second_row[1]}  |  {self.second_row[2]}  
     _____|_____|_____
          |     |     
    3  {self.third_row[0]}  |  {self.third_row[1]}  |  {self.third_row[2]}  
          |     |     \n
---------------------------\n"""
        self.first_player_choices = []
        self.second_player_choices = []
        self.ai_choices = []

    def update_board(self):
        """Updates the board with the move from the previous turn."""
        self.board = f"""       a     b     c
          |     |     
    1  {self.first_row[0]}  |  {self.first_row[1]}  |  {self.first_row[2]}  
     _____|_____|_____
          |     |     
    2  {self.second_row[0]}  |  {self.second_row[1]}  |  {self.second_row[2]}  
     _____|_____|_____
          |     |     
    3  {self.third_row[0]}  |  {self.third_row[1]}  |  {self.third_row[2]}  
          |     |     \n
---------------------------\n"""

    def new_turn(self):
        """Initializes a new turn for a human player by processing their choice,
        checking if the space chosen is available
        and then placing the player's correspondent mark at that space."""
        print(self.title)
        print(self.board)

        # Asks for user input to choose a space on the board
        row = row_choice(self.player, self.first_row, self.second_row, self.third_row)
        index_number = column_choice()

        # Checks if the space chosen isn't already occupied
        if row[index_number] != '-':
            print('The space chosen is already occupied. Please, choose again.')
            self.new_turn()
        else:
            if self.player == 1:
                row[index_number] = 'X'
                # Adds the chosen space to the player's list of moves
                self.first_player_choices.append(row[index_number])
            elif self.player == 2:
                row[index_number] = 'O'
                # Adds the chosen space to the player's list of moves
                self.second_player_choices.append(row[index_number])

    def ai_turn(self):
        """Initializes a new AI turn by randomly choosing an available row and column."""
        print(self.title)
        print(self.board)
        print('AI\'s turn... 🤖')

        # Selects a random row (in this case, the lists for each row)
        random_row = random.choice((self.first_row, self.second_row, self.third_row))
        # if random_row == 1:
        #     random_row = first_row
        # elif random_row == 2:
        #     random_row = second_row
        # elif random_row == 3:
        #     random_row = third_row
        # Selects a random column (in this case, an index number for the lists)
        random_column = random.randint(0, 2)

        # Checks if the space chosen isn't already occupied
        if random_row[random_column] != '-':
            self.ai_turn()
        else:
            random_row[random_column] = 'O'
            # Adds the chosen space to the player's list of moves
            self.ai_choices.append(random_row[random_column])

    def winner_check(self):
        """Checks if a player has a winning combination of spaces chosen.
        If there is, it returns False, ending the game, and declares the winner.
        If there isn't, it returns True and the game continues."""
        winning_combinations = [
            [self.first_row[0], self.first_row[1], self.first_row[2]],
            [self.second_row[0], self.second_row[1], self.second_row[2]],
            [self.third_row[0], self.third_row[1], self.third_row[2]],
            [self.first_row[0], self.second_row[0], self.third_row[0]],
            [self.first_row[1], self.second_row[1], self.third_row[1]],
            [self.first_row[2], self.second_row[2], self.third_row[2]],
            [self.first_row[0], self.second_row[1], self.third_row[2]],
            [self.first_row[2], self.second_row[1], self.third_row[0]]
        ]

        # Goes through every possible winning combination
        for combination in winning_combinations:
            # Compares players' choices vs the board-spaces within the current winning combination
            first_player_matches = []
            second_player_matches = []
            ai_matches = []

            for board_space in combination:
                if board_space in self.first_player_choices:
                    first_player_matches.append(board_space)
                if board_space in self.second_player_choices:
                    second_player_matches.append(board_space)
                if board_space in self.ai_choices:
                    ai_matches.append(board_space)
            if first_player_matches == combination:
                print(self.title)
                self.update_board()
                print(self.board)
                print('Player 1 wins! ☝️')
                return False
            elif second_player_matches == combination:
                print(self.title)
                self.update_board()
                print(self.board)
                print('Player 2 wins! ✌️')
                return False
            elif ai_matches == combination:
                print(self.title)
                self.update_board()
                print(self.board)
                print('AI wins! 🤖')
                return False
        # If no match was found, the game continues
        return True

    def moves_available(self):
        """Checks if there are still spaces available on the board.
        Returns False, ending the game, if there aren't.
        Returns True if there are, allowing the next turn to go on."""
        if '-' not in self.first_row and '-' not in self.second_row and '-' not in self.third_row:
            print(self.title)
            print(self.board)
            print('It\'s a tie! 💀')
            return False

        else:
            return True
