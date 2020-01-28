board=[" " for i in range(9)]

def board_des():
    row1="|{}|{}|{}|".format(board[0],board[1],board[2]) #arranging empty spaces
    row2="|{}|{}|{}|".format(board[3],board[4],board[5])
    row3="|{}|{}|{}|".format(board[6],board[7],board[8])

    print()
    print(row1) #b[0],b[1],b[2]
    print(row2) #b[3],b[4],b[5]
    print(row3) #b[6],b[7],b[8]
    print()
    
def player_mov(icon): 
    if icon=='X':
        number=1
    elif icon=='O':
        number=2
    print("now the It is the chance of player{}".format(number))
    choice=int(input("enter your choice between(1-9)"))
    if board[choice-1]==" ":
        board[choice-1]=icon
    else:
        print()
        print("already option exists")
def is_victory(icon):
    if(board[0]==icon and board[1]==icon and board[2]==icon)or\
      (board[2]==icon and board[5]==icon and board[8]==icon)or\
      (board[8]==icon and board[7]==icon and board[6]==icon)or\
      (board[6]==icon and board[3]==icon and board[0]==icon)or\
      (board[0]==icon and board[4]==icon and board[8]==icon)or\
      (board[2]==icon and board[4]==icon and board[6]==icon)or\
      (board[1]==icon and board[4]==icon and board[7]==icon)or\
      (board[3]==icon and board[4]==icon and board[5]==icon):
        return True
    else:
        return False
    
      
      
while True:
    board_des()
    print()
    player_mov("X")
    board_des()
    if is_victory("X"):
        print("Hurray!X has won")
        break
    board_des()
    print()
    player_mov("O")
    if is_victory("O"):
        print("Hurray!O has won")
        break
   
        

