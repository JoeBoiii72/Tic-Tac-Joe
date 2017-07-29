import random



#initialize player tokens and winning combinations for algorithm.
player = input("o or x: ")
win_combos = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]

make3combos = [(0,1,2),(1,2,0),(1,0,2),(3,4,5),(5,3,4),(5,4,3),(6,7,8),(8,6,7),(8,7,6),(0,3,6),(6,0,3),(6,3,0),(1,4,7),(7,1,4),(7,4,1),(2,5,8),(8,2,5),(8,5,2),(2,4,6),(6,2,4),(6,4,2),(0,4,8),(8,0,4),(8,4,0)]

winner = False

if player == "x":
    
    botplayer = "o"
else:
    botplayer = "x"

    
print("You are" , player, " and the bot is" , botplayer)



board = ["","","",    "","","",     "","",""] #this is the board.

print(board[0],board[1],board[2])  # Here is where we show the user the board in an attractive format.
print("- - -")
print(board[3],board[4],board[5])
print("- - -")
print(board[6],board[7],board[8])


def PlayersGo():
    position = int(input("where to go (0 - 8)"))
    while board[position] == botplayer or board[position] == player:
        
        position = int(input("where to go (0 - 8)"))
    board[position] = player

    
    print(board[0],board[1],board[2])
    print("- - -")
    print(board[3],board[4],board[5])
    print("- - -")
    print(board[6],board[7],board[8])

    
    input("Press enter to see the bots go")
    return board;


#The so called AI

def CPU_MakeWin():
    for i in make3combos:
        if board[i[0]] == botplayer and board[i[1]] == botplayer and board[i[2]] == "":
            board[i[2]] = botplayer
            
            return board;
        
    print("cant make win")
    CPU_PreventLoss()
            

def CPU_PreventLoss():
    for i in make3combos:
        if board[i[0]] == player and board[i[1]] == player and board[i[2]] == "":
            board[i[2]] = botplayer
            return board;
    
    print("cant prevent loss")
    CPU_Middle()
            

def CPU_Middle():
    if board[4] == "":
        board[4] = botplayer
        return board;
    else:
        print("middle not avabliable")
        CPU_Random()
    

def CPU_Random():
    position = random.randint(0, 8)
    while board[position] == player or board[position] == botplayer:
        position = random.randint(0, 8)
    board[position] = botplayer
    

    
    return board;



    

#Code for AI ends here




while "" in board :
    PlayersGo()
    CPU_MakeWin()
    print(board[0],board[1],board[2])
    print("- - -")
    print(board[3],board[4],board[5])
    print("- - -")
    print(board[6],board[7],board[8])
    
    
    for i in win_combos :
        if board[i[0]] == "x" and board[i[1]] == "x" and board[i[2]] == "x":
            print("x wins")
            winner = 1
        if board[i[0]] == "o" and board[i[1]] == "o" and board[i[2]] == "o":
            print("o wins")
            winner = 1
    if winner == 1:
        while "" in board:
            board.remove("")

        print(board)
        print("Game is over")
