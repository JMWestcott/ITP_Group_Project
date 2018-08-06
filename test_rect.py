
from graphics import *

def box():

    N = int(input('N: '))
    win = GraphWin("Tic Tac Toe", 1000, 1000)

    for y in range(0, N):
        for x in range(0, N):
            rect = Rectangle(Point((100 + 100 * x), (100 + 100 * y )), Point((200 + 100 * x), (200 + 100 * y)))

            rect.setOutline(color_rgb(0,0,0))
            rect.draw(win)
    win.getMouse()
box()
