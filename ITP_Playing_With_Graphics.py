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


def point():
    for i in range(0, N**2):
        print('Player 1 Go!')
        Player1 = win.getMouse()
        X1_Value = Player1.getX()
        Y1_Value = Player1.getY()
        print(X1_Value, Y1_Value)

        Move1 = Text(Point(X1_Value, Y1_Value), "x")
        Move1.setSize(36)
        Move1.draw(win)

        print('Player 2 Go!')
        Player2 = win.getMouse()
        X2_Value = Player2.getX()
        Y2_Value = Player2.getY()
        print(X2_Value, Y2_Value)

        Move2 = Text(Point(X2_Value, Y2_Value), "o")
        Move2.setSize(36)
        Move2.draw(win)

        break
    #win.close()

def rect():
    rectangle = []
    rect1 = Rectangle(Point(100,100), Point(200,200))
    if X1_Value and Y1_Value in rect1:
        print('True')
    else:
        print('False')

# Def box():
#     boxes = []
#     for Value in range(100, length-100):
#         if (100 < X1_Value < 200) and (100 < Y1_Value < 200):
#             box1 = 0
#         elif


board()
point()
rect()


# def main():
#     win = GraphWin("My Window", 500, 500)
#     win.setBackground(color_rgb(255, 255, 255))
#
#     input_box = Entry(Point(250,250), 10)
#     input_box.draw(win)
#     txt = Text(Point(250, 280), "")
#     txt.draw(win)
#
#     while True:
#         txt.setText(input_box.getText())
#

    # pt1 = Point(250, 250)
    # pt2 = Point(350, 350)

    # rect = Rectangle(pt1, pt2)
    # rect.setOutline(color_rgb(0, 255, 255))
    # rect.setFill(color_rgb(0, 255, 255))
    # rect.draw(win)

    # text = Text(Point(250, 250), "What's Up?")
    # text.setTextColor(color_rgb(0, 255, 200)
    # text.setSize(30)
    # text.draw(win)

    # pt = Point(250, 250)
    # cir = Circle(pt, 50)
    # cir.setFill(color_rgb(100, 255, 50))
    # cir.draw(win)

    # ln = Line(pt1, pt2)
    # ln.setOutline(color_rgb(0, 255, 255))
    # ln.setWidth(5)
    # ln.draw(win)
    #
    # pt.setOutline(color_rgb(255, 0, 0))
    # pt.draw(win)
#
#     win.getMouse()
#     win.close()
#
# main()

# def line(x1, y1, x2, y2)
#     return Line(Point(x1, y1), Point(x2, y2))
#
# line(250, 250, 250, 350)
