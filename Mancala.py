# Author: Andrew Garcia
# GitHub Username: And724
# Date: 11/20/2022
# Description: Program is a simple, computer version of the boardgame Mancala. There are two classes in the program:
#              the Mancala class and the Player class. The Player class is a child of the Mancala class so that a
#              player can be created by calling the create_player method in the Mancala class. The player class only has
#              two methods which are the constructor and a get_name method. The Mancala class has the majority of the
#              methods that define and control the rules of the game and allow a player to make a move. The class also
#              contains the methods to display the winner and board state.

class Mancala:
    """
    Represents Mancala object
    """
    def __init__(self):
        """
        Constructor for the Mancala class. Initializes data
        members and all data members are private.
        """

        self._game_board = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
        self._player_list = []


    def create_player(self, player_name):
        """
        Method takes a player name as a parameter and creates
        a player object using the player class.
        """

        player = Player(player_name)
        self._player_list.append(player)        # adds player object to list for use later


    def print_board(self):
        """
        Takes no parameters and returns the current
        state of the board.
        """

        # print block for player 1
        print("player 1:", self.get_player_1().get_player_name())
        print("store:", self._game_board[6])
        print(self._game_board[0:6])

        # print block for player 2
        print("player 2:", self.get_player_2().get_player_name())
        print("store:", self._game_board[13])
        print(self._game_board[7:13])
        return ""               # workaround because this method was returning None


    def get_player_1(self):
        """
        Returns player_1 object
        """
        player_1 = self._player_list[0]
        return player_1


    def get_player_2(self):
        """
        Returns player_2 object
        """
        player_2 = self._player_list[1]
        return player_2


    def return_winner(self):
        """
        Takes no parameter and checks to see if the game has ended.
        If so display the winner. If it is a tie, display that it is a tie.
        If the game is not over display so.
        """

        # initializes relevant local variables
        p1_store = self._game_board[6]
        p2_store = self._game_board[13]
        p1_name = self.get_player_1().get_player_name()
        p2_name = self.get_player_2().get_player_name()


        # checks if all pit values in player 1's board are equal to 0
        p1_list = self._game_board[0:6]
        count_p1 = 6
        for value in p1_list:
            if value == 0:
                count_p1 -= 1


        # checks if all pit values in player 2's board are equal to 0
        p2_list = self._game_board[7:13]
        count_p2 = 6
        for value in p2_list:
            if value == 0:
                count_p2 -= 1


        # If both counts are zero the end state of the game has been reached and a winner can be determined
        if count_p1 == 0 and count_p2 == 0:
            if p1_store > p2_store:
                return ''.join(("Winner is player 1:", " ", str(p1_name)))
            elif p1_store < p2_store:
                return ''.join(("Winner is player 2:", " ", str(p2_name)))
            elif p1_store == p2_store:
                return "It's a tie"
        else:
            return "Game has not ended"         # If end state not met


    def play_game(self, player_num, pit_index):
        """
        Method contains the bulk of the rules of the Mancala game. This includes
        making the actual moves of the game, checking for special case 1 and 2,
        and checking the end of the game.
        """


        # checks if the game has already ended by checking the values of each player's pit
        end_count = 12
        for val in self._game_board[0:6]:
            if val == 0:
                end_count -= 1
        for val in self._game_board[7:13]:
            if val == 0:
                end_count -= 1
        if end_count == 0:                  # If end_count == 0, all players pits are empty and the game already ended
            return "Game is ended"


        # Checks for invalid pit_index entries
        if pit_index > 6 or pit_index <= 0:
            return "Invalid number for pit index"


        # Block for Player 1 case
        if player_num == 1:
            pit_index -= 1          # Index adjustment
            seeds = self._game_board[pit_index]            # sets local variable seeds to value of pit at index
            self._game_board[pit_index] = 0                # sets value at pit_index to 0

            # Iterates for number of seeds
            for i in range(seeds):
                pit_index += 1
                # Special case 2 block: If last seeds is put into player's empty pit
                if pit_index <= 5 and pit_index != 6 and self._game_board[pit_index] == 0 and seeds == 1:
                    val = -(pit_index + 2)                              # adjacent pit calculation
                    self._game_board[6] += 1
                    self._game_board[6] += self._game_board[val]        # adds value at index val to store
                    self._game_board[val] = 0
                    break

                # Special case 1 block: If last seed is placed in store
                if seeds == 1 and pit_index == 6:
                    print("Player 1 take an extra turn")
                seeds -= 1
                self._game_board[pit_index] += 1

                if pit_index == 12:         # To skip Player 2's store and reset to Player 1's first pit
                    pit_index = 0


        # Block for Player 2 case
        if player_num == 2:
            pit_index += 6                              # index adjustment
            seeds_2 = self._game_board[pit_index]       # sets local variable seeds_2 to value of pit at index
            self._game_board[pit_index] = 0             # sets value at pit_index to 0

            # Iterates for number of seeds
            for i in range(seeds_2):
                pit_index += 1
                # Special case 2 block: If last seeds is put into player's empty pit
                if pit_index >= 7 and pit_index != 13 and self._game_board[pit_index] == 0 and seeds_2 == 1:
                    val = (12 - pit_index)                              # adjacent pit calculation
                    self._game_board[13] += 1
                    self._game_board[13] += self._game_board[val]       # adds value at index val to store
                    self._game_board[val] = 0
                    break

                # Special case 1 block: If last seed is placed in store
                if seeds_2 == 1 and pit_index == 13:
                    print("Player 2 take an extra turn")
                seeds_2 -= 1
                self._game_board[pit_index] += 1

                if pit_index == 5:          # If player 1 store is encountered; plus 1 to skip over it
                    pit_index += 1
                if pit_index == 13:         # Once end of list is reached set pit_index to -1. It will be set to 0 later
                    pit_index = -1


        # Move through if player 1 move
        if player_num == 1:
            copy_p1_list = self._game_board[0:6]
            count_p1 = 6

            # Checks if values are equal to 0 in P1 board. Decrements count_p1 if true
            for value in copy_p1_list:
                if value == 0:
                    count_p1 -= 1

            # If count_p1 is 0 this means all pits are empty
            if count_p1 == 0:
                sum = 0
                pos = 7
                player_2_lst = self._game_board[7:13]

                # Block sums the remaining seeds in P2 pits and adds to store
                for val in player_2_lst:
                    sum = sum + val
                    self._game_board[pos] = 0
                    pos += 1
                self._game_board[13] += sum
                return self._game_board


        # Move through if player 2 move
        if player_num == 2:
            copy_p2_list = self._game_board[7:13]
            count_p2 = 6

            # Checks if values are equal to 0 in P2 board. Decrements count_p2 if true
            for value in copy_p2_list:
                if value == 0:
                    count_p2 -= 1

            # If count_p2 is 0 this means all pits are empty
            if count_p2 == 0:
                sum = 0
                pos = 0
                player_1_lst = self._game_board[0:6]

                # Block sums the remaining seeds in P1 pits and adds to store
                for val in player_1_lst:
                    sum = sum + val
                    self._game_board[pos] = 0
                    pos += 1
                self._game_board[6] += sum
                return self._game_board
        return self._game_board


class Player(Mancala):
    """
    Represents player object
    """

    def __init__(self, player_name):
        """
        Initializes Player class with private data members. Overrides Mancala parent
        class to take player_name parameter.
        """
        super().__init__()
        self._player_name = player_name

    def get_player_name(self):
        """
        Returns player's name
        """
        return self._player_name
