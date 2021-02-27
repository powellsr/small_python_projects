from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print(" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# Everything from here on should be in your for loop
# don't forget to properly indent!
turns = int(input("Enter number of turns: "))
while turns > 24 or turns < 1:#This loop objects to strange no.s of turns imputed
  printi("Well that's just absurd...")
  turns = int(input("Enter a REASONABLE number of turns: "))
  
for turn in range(turns):
  print("Turn", turn + 1)  #this prints turn number, one more than turn index, since indices start at 0. This syntax must concentrate strings and values
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print("Congratulations! You sank my battleship!")
    break # "break" command breaks a loop (the for loop that governs turns). Here it is nested under the win conditional, so if the game is won, the loop ends. 
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print("Oops, that's not even in the ocean. The Admiral's on the phone. He wants to discharge you...")
    elif board[guess_row][guess_col] == "X":
      print("You guessed that one already.")
      #turn - 1 (This is an attempt to decrement turns, as this shouldn't count) (Consider applying this to shouts outside the board, too)
    else:
      print("You missed my battleship!")
      board[guess_row][guess_col] = "X"
    if turn == (turns - 1): #This executes after the last turn, regardless of reason for miss, at end of loop
      print("Game Over")
    print_board(board)
  # print turn + 1 here
