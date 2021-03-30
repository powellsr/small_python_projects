from random import randint

def get_board():
  board = []
  size = int(input("Enter a length / width for the board size: "))
  while (size < 5 or size > 15):
    print("Enter a valid size for the board. Integers between 5 and 15 (inclusive) are accepted.")
    size = int(input("Size of board (integer between 5 and 15: "))
  for x in range(0, size):
    board.append(["O"] * size)
  return board

def print_board(board):
  for row in board:
    print(" ".join(row))

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

def get_user_guess():
  guess_row = int(input("Guess Row: ")) - 1
  guess_col = int(input("Guess Col: ")) - 1
  return [guess_row, guess_col]

def check_guess(user_guess, board):
  if user_guess[0] == ship_row and user_guess[1] == ship_col:
    board[user_guess[0]][user_guess[1]] = '#'
    print("Congratulations! You sank my battleship!")
    print_board(board)
    return False 
  else:
    if user_guess[0] not in range(5) or \
      user_guess[1] not in range(5):
      print("Oops, that's not even in the ocean. The Admiral's on the phone. He wants to discharge you...")
    elif board[user_guess[0]][user_guess[1]] == "X":
      print("You guessed that one already.")
      #turn - 1 (This is an attempt to decrement turns, as this shouldn't count) (Consider applying this to shouts outside the board, too)
    else:
      print("You missed my battleship!")
      board[user_guess[0]][user_guess[1]] = "X"
    if turn == (turns - 1): #This executes after the last turn, regardless of reason for miss, at end of loop
      print("Out of turns!\n\n\tGame Over")
      return False
    
def get_number_turns():
  turns = int(input("Enter number of turns: "))
  while turns > 24 or turns < 1:#This loop objects to strange no.s of turns imputed
    print("Well that's just absurd...")
    turns = int(input("Enter a REASONABLE number of turns: "))
  return turns


# Set up game variables
board = get_board()

ship_row = random_row(board)
ship_col = random_col(board)

turns = get_number_turns()

print_board(board)

# Game loop
for turn in range(turns):
  print("Turn " + str(turn + 1))  #this prints turn number, one more than turn index, since indices start at 0. This syntax must concentrate strings and values

  user_guess = get_user_guess() # get user guess

  game_continutes = check_guess(user_guess, board)

  print_board(board)
  # print turn + 1 here
