                                                 #Creating tic-tac-toe game
gameboard = ["-","-","-",
           "-","-","-",
           "-","-","-"]
currentplayer = "X"
game = True
win = None


def display(board):
    print(gameboard[0]+"|"+gameboard[1]+"|"+gameboard[2])
    print("______")
    print(gameboard[3]+"|"+gameboard[4]+"|"+gameboard[5])
    print("______")
    print(gameboard[6]+"|"+gameboard[7]+"|"+gameboard[8])

def value():
    choice=int(input(f"Enter the position of {currentplayer}"))
    if choice<=9 and choice>=1 and gameboard[choice-1]=="-":
        gameboard[choice-1] =currentplayer
    else:
        print("invalid")


def switchuser():
    global currentplayer
    if currentplayer=='X':
        currentplayer="O"
    else:
        currentplayer='X'


def checkwin():
    global win
    if (gameboard[0]==gameboard[1]==gameboard[2] and gameboard[0]!='-') :
        win=gameboard[0]
        return 1


    elif gameboard[3]==gameboard[4]==gameboard[5] and gameboard[3]!='-':
        win=gameboard[3]
        return 1


    elif gameboard[6] == gameboard[8] == gameboard[7] and gameboard[6] != '-':
        win=gameboard[6]
        return 1


def checktie():
    global game
    if '-' not in gameboard:
        print("Match tie")
        game=False
def winner():
    if checkwin():
        print(f"The winner is {win}")


while(game):
    display(gameboard)
    value()
    winner()
    checktie()
    switchuser()

#End of the Code

#run


