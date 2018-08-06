from graphics import *

Player_1 = input('Player 1 print your name: ')
color_1 = input('Player 1 pick a color: ')
Player_2 = input('Player 2 Print your name: ')
color_2 = input('Player 2 pick a color: ')
board_size = input('Please enter the board size (3-10): ')
N = int(board_size)
length = (N * 100 + 200)
win = GraphWin("Tic Tac Toe", length, length)

def board():

    play1 = Text(Point(100, 20), 'Player 1: ')
    play1.setSize(18)
    play1.draw(win)
    name1 = Text(Point(100, 50), Player_1)
    name1.setSize(22)
    name1.setTextColor(color_1)
    name1.draw(win)

    play2 = Text(Point(((N+1) * 100), 20), 'Player 2: ')
    play2.setSize(18)
    play2.draw(win)
    name2 = Text(Point(((N+1) * 100), 50), Player_2)
    name2.setSize(22)
    name2.setTextColor(color_2)
    name2.draw(win)

    import sys
    while True:
        # print lines for the tic tac toe board
        for n in range(1, N):
            pt1 = Point(((n + 1 ) * 100), 100)
            pt2 = Point(((n + 1 ) * 100), (length - 100))
            ln_vert = Line(pt1, pt2)
            ln_vert.setOutline(color_rgb(0, 0, 0))
            ln_vert.setWidth(5)
            ln_vert.draw(win)

            pt3 = Point(100, ((n + 1 ) * 100))
            pt4 = Point((length - 100),((n + 1 ) * 100))
            ln_horiz = Line(pt3, pt4)
            ln_horiz.setOutline(color_rgb(0, 0, 0))
            ln_horiz.setWidth(5)
            ln_horiz.draw(win)
        else:
            break


def tic_tac_toe():

    import sys

    grid = [0] * N
    for row in range(N):
        grid[row] = [0] * N
    print(grid)

    while True:
        #sum(map(sum, grid)) < ((N*N/2)*3)-1
        # if sum(map(sum, grid)) < ((N*N/2)*3):
        #if (N%2 == 0 and i <= (N*N)/2) or (N%2 != 0 and i < (N*N/2)):
            print('Player 1 Go!')
            Player1 = win.getMouse()
            X1_Value = Player1.getX()
            Y1_Value = Player1.getY()
            print(X1_Value, Y1_Value)

            Move1 = Text(Point(X1_Value, Y1_Value), "X")
            Move1.setSize(36)
            Move1.setTextColor(color_1)
            Move1.draw(win)

# to record where the 'X' is played and insert a 1 in that index within our matrix
            for b in range(0, N):
                for a in range(0, N):
                    if ((100 + 100 * a) < X1_Value < (200 + 100 * a)) and ((100 + 100 * b) < Y1_Value < (200 + 100 * b)):
                        grid[b].pop(a)
                        grid[b].insert(a, 1)
                        print(grid)

# to determine if the player 1 won
        # columns
            for f in range (0, N):
                col1 = []
                for e in range (0, N):
                    if grid[e][f] == 1:
                        col1.append(1)
                        print(col1)
                if col1 == ([1] * N):
                    print('Player 1 Wins!')
                    sys.exit('The game is over!')

        # rows
            for f in range (0, N):
                row1 = []
                for e in range (0, N):
                    if grid[f][e] == 1:
                        row1.append(1)
                if row1 == ([1] * N):
                    print('Player 1 Wins!')
                    sys.exit('The game is over!')

        # diagonals
            diag1 = []
            for g in range(0, N):
                if grid[g][g] == 1:
                    diag1.append(1)
                if diag1 == ([1] * N):
                    print('Player 1 Wins!')
                    sys.exit('The game is over!')

        # reverse diagonal
            rev_diag1 = []
            for g in range(0, N):
                if grid[g][N - 1 - g] == 1:
                    rev_diag1.append(1)
                if rev_diag1 == ([1] * N):
                    print('Player 1 Wins!')
                    sys.exit('The game is over!')


            if sum(map(sum, grid)) == ((N*N/2)*3)-0.5:
                break


            print('Player 2 Go!')
            Player2 = win.getMouse()
            X2_Value = Player2.getX()
            Y2_Value = Player2.getY()
            print(X2_Value, Y2_Value)

            Move2 = Text(Point(X2_Value, Y2_Value), "O")
            Move2.setSize(36)
            Move2.setTextColor(color_2)
            Move2.draw(win)



# to record where the 'O' is played and insert a 2 in that index within our matrix
            for d in range(0, N):
                for c in range(0, N):
                    if ((100 + 100 * c) < X2_Value < (200 + 100 * c)) and ((100 + 100 * d) < Y2_Value < (200 + 100 * d)):
                        grid[d].pop(c)
                        grid[d].insert(c, 2)
                        print(grid)

# to determine if the player 2 won
        # columns
            for f in range (0, N):
                col2 = []
                for e in range (0, N):
                    if grid[e][f] == 2:
                        col2.append(2)
                        print(col2)
                if col2 == ([2] * N):
                    print('Player 2 Wins!')
                    sys.exit('The game is over!')

        # rows
            for f in range (0, N):
                row2 = []
                for e in range (0, N):
                    if grid[f][e] == 2:
                        row2.append(2)
                if row2 == ([2] * N):
                    print('Player 2 Wins!')
                    sys.exit('The game is over!')


        # diagonals
            diag2 = []
            for g in range(0, N):
                if grid[g][g] == 2:
                    diag2.append(2)
                if diag2 == ([2] * N):
                    print('Player 2 Wins!')
                    sys.exit('The game is over!')

        # reverse diagonal
            rev_diag2 = []
            for g in range(0, N):
                if grid[g][N - 1 - g] == 2:
                    rev_diag2.append(2)
                if rev_diag2 == ([2] * N):
                    print('Player 2 Wins!')
                    sys.exit('The game is over!')

            if sum(map(sum, grid)) == ((N*N/2)*3):
                break

    print("Oops, it's a tie...")
    sys.exit('This game is over!')

# Determine if it's a tie
# Show on the graphics who won
# make sure they can't play more than once in a box



# to center the 'X' and 'O' in the grid
def rect():
    rectangle = []
    rect1 = Rectangle(Point(100,100), Point(200,200))
    if X1_Value and Y1_Value in rect1:
        print('True')
    else:
        print('False')




board()
tic_tac_toe()
