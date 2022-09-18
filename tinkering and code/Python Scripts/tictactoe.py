import random

random_coin_toss = (random.randint(1, 2))


class e:
    def __repr__(self):
        return "   "


class Board():


    def __init__(self):
        self.main_board = [e() ,e(), e(), e(), e(), e(), e(), e(), e()]
    def board(self):
        print("{}  | {}  | {}".format(self.main_board[0],self.main_board[1],self.main_board[2]))
        print('-----------------------')
        print("{}  | {}  | {}".format(self.main_board[3], self.main_board[4],self.main_board[5]))
        print('-----------------------')
        print("{}  | {}  | {}".format(self.main_board[6],self.main_board[7], self.main_board[8]))
        print("======================")

    def output_board(self, input_string):

        X_input = input()
        if X_input == 'row1_1':
            self.main_board[0] = input_string
            self.board()

        elif X_input == 'row1_2':
            self.main_board[1] = input_string
            self.board()
        # AI()
        elif X_input == 'row1_3':
            self.main_board[2] = input_string
            self.board()
        #  AI()
        elif X_input == 'row2_1':
            self.main_board[3] = input_string
            self.board()
        #  AI()
        elif X_input == 'row2_2':
            self.main_board[4] = input_string
            board.board()
        #  AI()
        elif X_input == 'row2_3':
            self.main_board[5] = input_string
            self.board()
        #  AI()
        elif X_input == 'row3_1':
            self.main_board[6] = input_string
            self.board()
        #  AI()
        elif X_input == 'row3_2':
            self.main_board[7] = input_string
            self.board()
        #  AI()
        elif X_input == 'row3_3':
           self.main_board[8] = input_string
           self.board()
        #  board()
        else:
            print("WRONG INPUT LOSER XD")
            self.board()

    def X_Win(self):
     if self.main_board[0] == 'X':
        print("WINNER WINNER CHICKEN DINNER")
     elif self.main_board[3] and self.main_board[4] and self.main_board[5] == 'X':
        print("WINNER WINNER CHICKEN DINNER")
     elif self.main_board and self.main_board== [e(), e(), e(), e(), e(), e(), 'X','X', 'X']:
        print("WINNER WINNER CHICKEN DINNER")
     elif self.main_board == ['X', e(), e(), 'X', e(), e(), 'X', e(), e()]:
        print("WINNER WINNER CHICKEN DINNER")
     elif self.main_board == [e(), 'X', e(), e(), 'X', e(), e(), 'X', e()]:
        print("WINNER WINNER CHICKEN DINNER")
     elif self.main_board == [e(), e(), 'X' ,e(), e(), 'X', e(), e(), 'X']:
        print("WINNER WINNER CHICKEN DINNER")
     elif self.main_board == ['X', e(), e(), e(), 'X', e(), e(), e(), 'X']:
        print("WINNER WINNER CHICKEN DINNER")
     elif self.main_board == [e(), e(), 'X', e(), 'X', e(), 'X', e(), e()]:i

    def Y_Win(self):
      if self.main_board == ['Y', 'Y', 'Y', e(),e(), e(), e(),e(), e()]:
        print("WINNER WINNER CHICKEN DINNER")
      elif  self.main_board == [e(), e(), e(), 'Y', 'Y', 'Y', e(), e(), e()]:
        print("WINNER WINNER CHICKEN DINNER")
      elif self.main_board == [e(), e(), e(), e(), e(), e(), 'Y','Y', 'Y']:
        print("WINNER WINNER CHICKEN DINNER")
      elif self.main_board == ['Y', e(), e(), 'Y', e(), e(), 'Y', e(), e()]:
        print("WINNER WINNER CHICKEN DINNER")
      elif self.main_board == [e(), 'Y', e(), e(), 'Y', e(), e(), 'Y', e()]:
        print("WINNER WINNER CHICKEN DINNER")
      elif self.main_board == [e(), e(), 'Y' ,e(), e(), 'Y', e(), e(), 'Y']:
        print("WINNER WINNER CHICKEN DINNER")
      elif self.main_board == ['Y', e(), e(), e(), 'Y', e(), e(), e(), 'Y']:
        print("WINNER WINNER CHICKEN DINNER")
      elif  self.main_board == [e(), e(), 'Y', e(), 'Y', e(), 'Y', e(), e()]:
        print("WINNER WINNER CHICKEN DINNER")

class Node():
    def __init__(self, value):
      self.value=value
      self.children = []

    def add_child(self, obj):
     self.children.append(obj)




board = Board()
random_coin_toss = (random.randint(1, 2))





def X_Turn():
    board.X_Win()
    board.output_board('X')
    print(board.main_board)
def Y_turn():

    board.Y_Win()
    board.output_board('Y')
def gameplay():
    switch = None
    board.board()
    turn = 0
    if random_coin_toss == 1:
        print("X goes first!!")
        X_Turn()
        switch = 0
    elif random_coin_toss == 2:
        print("O goes first!")
        Y_turn()
        switch = 1

    while turn <= 9:
        if switch == 1:
            X_Turn()
            turn += 1
            switch = 0
        elif switch == 0:
            Y_turn()
            turn += 1
            switch = 1


gameplay()
