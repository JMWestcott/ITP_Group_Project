# Let's play with graphics

from graphics import *

board_size = input('Please enter the board size (3-10): ')
N = int(board_size)
length = (N * 100 + 200)

win = GraphWin("Tic Tac Toe", length, length)

def board():

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


    # clickPoint = win.getMouse()
    # keyString = win.getKey()
    # x = x.draw()
    # o = o.draw()
    # win.setCoords(0, 0, 10, 10)
    # Line1 = Line(Point(2,2), Point(2,8))

    #win.getMouse()
    #win.close()


def tic_tac_toe():

    import sys
    # import numpy as np

    grid = []
    for row in range(N):
        grid.append([])
        for column in range(N):
            grid[row].append(0)
    print(grid)

    for i in range(0, N**2):
        print('Player 1 Go!')
        Player1 = win.getMouse()
        X1_Value = Player1.getX()
        Y1_Value = Player1.getY()
        print(X1_Value, Y1_Value)

        Move1 = Text(Point(X1_Value, Y1_Value), "x")
        Move1.setSize(36)
        Move1.draw(win)

        for b in range(0, N):
            for a in range(0, N):
                if ((100 + 100 * a) < X1_Value < (200 + 100 * a)) and ((100 + 100 * b) < Y1_Value < (200 + 100 * b)):
                    grid[a].pop(a)
                    grid[a].insert(a, 1)
                    print(grid)

    # for f in range(0, N):
    #     if any([(grid[f, :] == 1).all(), (grid[;, f] == 1).all()]):
    #         print('Player 1 Wins')
    #         sys.exit('The game is over')

        for f in range(0, N):
            for e in range(0, N):
                if grid[e: ] == 1:
                    print('Player 1 Wins')
                    sys.exit('The game is over!')
                elif grid[ :e] == 1:
                    print('Player 1 Wins')
                    sys.exit('The game is over!')

        # for e in range(0, N):
        #     for f in range(0, N):
        #         if grid[f][e] == 1:
        #             print('Player 1 Wins')
        #             sys.exit('The game is over!')
        # for g in range(0, N):
        #     for h in range(0, N):
        #         if grid[h][g] == 1:
        #             print('Player 1 Wins!')
        #             sys.exit('The game is over!')



        if (grid[0][0] and grid[1][1] and grid[2][2]) == 1:
                print('Player 1 Wins!')
                sys.exit('The game is over!')

        if (grid[0][2] and grid[1][1] and grid[2][0]) == 1:
                print('Player 1 Wins!')
                sys.exit('The game is over!')

        print('Player 2 Go!')
        Player2 = win.getMouse()
        X2_Value = Player2.getX()
        Y2_Value = Player2.getY()
        print(X2_Value, Y2_Value)

        Move1 = Text(Point(X2_Value, Y2_Value), "o")
        Move1.setSize(36)
        Move1.draw(win)

        for d in range(0, N):
            for c in range(0, N):
                if ((100 + 100 * c) < X2_Value < (200 + 100 * c)) and ((100 + 100 * d) < Y2_Value < (200 + 100 * d)):
                    grid[c].pop(c)
                    grid[c].insert(c, 2)
                    print(grid)

        for code in grid[0]:

            if (grid[0][0] and grid[0][1] and grid[0][2]) == 2:
                print('Player 2 Wins!')
                sys.exit('The game is over!')

            if (grid[1][1] and grid[1][1] and grid[1][2]) == 2:
                print('Player 2 Wins!')
                sys.exit('The game is over!')

            if (grid[2][0] and grid[2][1] and grid[2][2]) == 2:
                print('Player 2 Wins!')
                sys.exit('The game is over!')

            if (grid[0][0] and grid[1][1] and grid[2][2]) == 2:
                print('Player 2 Wins!')
                sys.exit('The game is over!')

            if (grid[0][2] and grid[1][1] and grid[2][0]) == 2:
                print('Player 2 Wins!')
                sys.exit('The game is over!')

def rect():
    rectangle = []
    rect1 = Rectangle(Point(100,100), Point(200,200))
    if X1_Value and Y1_Value in rect1:
        print('True')
    else:
        print('False')


# def win_box():
#     # if these things are in the list, they win
#     if box in list:
#         if box == '11x' and box = '12x' and '13x'
#             print(Player 1 Wins!)

# Def box():
#     boxes = []
#     for Value in range(100, length-100):
#         if (100 < X1_Value < 200) and (100 < Y1_Value < 200):
#             box1 = 0
#         elif


board()
tic_tac_toe()
