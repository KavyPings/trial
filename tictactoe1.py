"""
print("Framework: \n"+ "1|2|3\n"+
      "4|5|6\n"+
      "7|8|9")
"""

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
winner = None
gamerun = True
current = "X"

def boardlook(board):
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-----")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-----")
    print(f"{board[6]}|{board[7]}|{board[8]}\n")

def move(board,current):
    while True:

      try:
        user_input = input(f"Player {current}, enter your move (1-9):\n")

        if user_input.strip() == '':
            print("You didn't enter anything. Try again.\n")
            continue

        position = int(user_input)-1

        if position<0 or position>8:
            print("Invalid input, try again\n")

        elif board[position] != ' ':
            print("Spot taken, try again\n")


        else:
            print("Move placed\n")
            board[position] = current
            boardlook(board)
            return


      except ValueError:
          print("Invalid input, try again\n")

def switch():
    global current
    if current == "X":
        current = "O"

    else:
        current = "X"
def checkrow(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != ' ':
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[4] != ' ':
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != ' ':
        winner = board[6]
        return True

def checkcol(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != ' ':
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != ' ':
        winner = board[6]
        return True
    elif board[2] == board[5] == board[8] and board[2] != ' ':
        winner = board[6]
        return True

def checkdiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != ' ':
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[6] != ' ':
        winner = board[6]
        return True

def checktie():
    global gamerun
    if ' ' not in board and winner == None:
        print("TIE!")
        print("Game complete")
        gamerun = False

def checkwin(board):
    global winner, gamerun
    if checkcol(board) or checkrow(board) or checkdiag(board):
        print("Winner is: "+winner)
        print("GAME COMPLETE")
        gamerun = False

boardlook(board)

while gamerun == True:
    move(board, current)
    switch()
    checkwin(board)
    checktie()
