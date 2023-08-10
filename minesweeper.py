

from graphics import *
import numpy as np
import random


def difficulty():
    win = GraphWin('Difficulty', 600, 400)
    win.setCoords(0, 0, 600, 400)
    win.setBackground('dark grey')
    easyb = Rectangle(Point(0, 300), Point(200, 0))
    easyt = Text(Point(100, 175), 'EASY')
    easyt2 = Text(Point(100, 120), '8 x 10,')
    easyt3 = Text(Point(100, 95), '10 mines')
    easyb.setFill('light gray')
    easyb.setOutline(color_rgb(190, 190, 190))
    easyb.setWidth(5)
    easyb.draw(win)
    easyt.setFill(color_rgb(140, 140, 140))
    easyt.setStyle('bold')
    easyt.setSize(25)
    easyt.draw(win)
    easyt2.setFill(color_rgb(140, 140, 140))
    easyt2.setSize(14)
    easyt2.draw(win)
    easyt3.setFill(color_rgb(140, 140, 140))
    easyt3.setSize(14)
    easyt3.draw(win)
    medb = Rectangle(Point(200, 300), Point(400, 0))
    medt = Text(Point(300, 175), 'MEDIUM')
    medt2 = Text(Point(300, 120), '11 x 17,')
    medt3 = Text(Point(300, 95), '30 mines')
    medb.setFill('light gray')
    medb.setOutline(color_rgb(190, 190, 190))
    medb.setWidth(5)
    medb.draw(win)
    medt.setFill(color_rgb(140, 140, 140))
    medt.setStyle('bold')
    medt.setSize(25)
    medt.draw(win)
    medt2.setFill(color_rgb(140, 140, 140))
    medt2.setSize(14)
    medt2.draw(win)
    medt3.setFill(color_rgb(140, 140, 140))
    medt3.setSize(14)
    medt3.draw(win)
    hardb = Rectangle(Point(400, 300), Point(600, 0))
    hardt = Text(Point(500, 175), 'HARD')
    hardt2 = Text(Point(500, 120), '16 x 28,')
    hardt3 = Text(Point(500, 95), '80 mines')
    hardb.setFill('light gray')
    hardb.setOutline(color_rgb(190, 190, 190))
    hardb.setWidth(5)
    hardb.draw(win)
    hardt.setFill(color_rgb(140, 140, 140))
    hardt.setStyle('bold')
    hardt.setSize(25)
    hardt.draw(win)
    hardt2.setFill(color_rgb(140, 140, 140))
    hardt2.setSize(14)
    hardt2.draw(win)
    hardt3.setFill(color_rgb(140, 140, 140))
    hardt3.setSize(14)
    hardt3.draw(win)
    text = Text(Point(300, 350), 'CHOOSE YOUR DIFFICULTY')
    text.setFill(color_rgb(120, 120, 120))
    text.setSize(36)
    text.setStyle('bold')
    text.draw(win)
    try:
        click = win.getMouse()
        x = click.getX()
        y = click.getY()
        while y > 300:
            click = win.getMouse()
            x = click.getX()
            y = click.getY()
        win.close()
        if x < 200:
            return 'easy'
        elif x > 400:
            return 'hard'
        return 'medium'
    except:
        return 'closed'


def minewindow(maxx, maxy):
    win = GraphWin('Minesweeper', maxx, maxy)
    win.setCoords(0, 0, maxx, maxy)
    win.setBackground('dark gray')
    return win


def drawgrid(rows, clms, maxx, maxy, win):
    top = Rectangle(Point(0, 0), Point(maxx, maxy - 50))
    top.setOutline('light gray')
    top.setFill('light gray')
    top.draw(win)
    for x in range(clms):
        v = Line(Point(50 * x, maxy - 50), Point(50 * x, 0))
        v.draw(win)
        v.setWidth(2)
        v.setFill('dark gray')
    for x in range(rows):
        h = Line(Point(0, 50 * x), Point(maxx, 50 * x))
        h.draw(win)
        h.setWidth(2)
        h.setFill('dark gray')


def start(clms, rows, maxx, maxy, minect, clear, win):
    firstmines = mines(clms, rows, minect, clear)
    try:
        drawgrid(rows, clms, maxx, maxy, win)
        topdisplay(maxx, maxy, win)
        remflags(maxx, maxy, minect, clear, win)
        click1 = select(maxx, maxy, rows, win)
        if click1 == 'exit':
            win.close()
        elif click1 == 'opt':
            options(diff, win)
        x1 = click1[0]
        y1 = click1[1]
        if firstmines[x1, y1] == 1:
            boxdata = minefix(x1, y1, clms, rows, firstmines)
        else:
            boxdata = firstmines
        state(boxdata, win, x1, y1, minect, maxx, maxy)
        display(boxdata, win, x1, y1, clms, rows)
        return boxdata
    except:
        return


def boxselect(maxx, maxy, win):
    click = win.getMouse()
    x = click.getX()
    y = click.getY()
    if maxx - 37 <= x <= maxx - 13:
        if maxy - 37 <= y <= maxy - 13:
            return 'exit'
    elif 13 <= x <= 37:
        if maxy - 37 <= y <= maxy - 13:
            return 'opt'
    x = int(x // 50)
    y = int(y // 50)
    return x, y


def array(clms, rows):
    clm = []
    row = []
    for n in range(0, rows):
        row.append(0)
    for n in range(0, clms):
        clm.append(row)
    array = np.array(clm)
    return array


def mines(clms, rows, maxmines, array):
    minefield = array
    minect = 0
    while minect != maxmines:
        x = random.randint(0, clms - 1)
        y = random.randint(0, rows - 1)
        if minefield[x, y] != 1 and adjmines(x, y, clms, rows, minefield) < 4:
            minefield[x, y] = 1
            minect += 1
    return minefield


def minefix(x, y, clms, rows, firstmines):
    fixed = False
    firstmines[x, y] = 2
    while not fixed:
        x = random.randint(0, clms - 1)
        y = random.randint(0, rows - 1)
        if firstmines[x, y] not in range(1, 3) and adjmines(x, y, clms, rows, firstmines) < 4:
            firstmines[x, y] = 1
            fixed = True
    return firstmines


def select(maxx, maxy, rows, win):
    try:
        click = boxselect(maxx, maxy, win)
        if click == 'exit':
            return 'exit'
        elif click == 'opt':
            return 'opt'
        else:
            x = click[0]
            y = click[1]
            while y > rows - 1 or type(click) == str:
                click = boxselect(maxx, maxy, win)
                click = boxselect(maxx, maxy, win)
                if click == 'exit':
                    return 'exit'
                elif click == 'opt':
                    return 'opt'
                else:
                    x = click[0]
                    y = click[1]
            return x, y
    except:
        return 'closed'


def state(boxdata, win, x, y, minect, maxx, maxy):
    keycheck = win.checkKey()
    flags = flagcheck(boxdata)
    if keycheck == 'Shift_L' and flags != minect and boxdata[x, y] != 2:
        if boxdata[x, y] == 3:
            boxdata[x, y] = 4
        elif boxdata[x, y] == 1:
            boxdata[x, y] = 5
        elif boxdata[x, y] == 5:
            boxdata[x, y] = 1
        else:
            boxdata[x, y] = 3
        remflags(maxx, maxy, minect, boxdata, win)
    elif keycheck == '':
        if boxdata[x, y] == 1:
            return 'lose'
        elif boxdata[x, y] != 3 and boxdata[x, y] != 5:
            boxdata[x, y] = 2
    return boxdata


def cover(x, y, win):
    cover = Rectangle(Point(x - 25, y - 24), Point(x + 24, y + 25))
    cover.setFill(color_rgb(190, 190, 190))
    cover.setOutline('dark gray')
    cover.draw(win)


def flagcover(x, y, win):
    cover = Rectangle(Point(x - 25, y - 24), Point(x + 24, y + 25))
    cover.setFill('light gray')
    cover.setOutline('dark gray')
    cover.draw(win)


def drawflag(x, y, win):
    pole = Line(Point(x + 1, y + 1), Point(x + 1, y - 10))
    pole.setWidth(2)
    pole.draw(win)
    base1 = Line(Point(x - 9, y - 12), Point(x + 9, y - 12))
    base1.setWidth(3.1)
    base1.draw(win)
    base2 = Line(Point(x - 5, y - 9), Point(x + 5, y - 9))
    base2.setWidth(2.5)
    base2.draw(win)
    flag = Polygon(Point(x + 1, y - 1), Point(x + 1, y + 11), Point(x - 9, y + 5))
    flag.setFill('red')
    flag.setOutline('red')
    flag.draw(win)


def num(x, y, win, mines):
    if mines == 1:
        color = 'blue'
    elif mines == 2:
        color = 'green'
    elif mines == 3:
        color = 'red'
    elif mines == 4:
        color = 'dark blue'
    elif mines == 5:
        color = 'dark red'
    else:
        color = 'black'
    cover(x, y, win)
    num = Text(Point(x, y), str(mines))
    num.setSize(23)
    num.draw(win)
    num.setTextColor(color)


def display(boxdata, win, col, row, clms, rows):
    x = 50 * col + 25
    y = 50 * row + 25
    box = boxdata[col, row]
    if box == 2:
        mines = adjmines(col, row, clms, rows, boxdata)
        if mines == 0:
            cover(x, y, win)
            zeros = zeropop(col, row, clms, rows, boxdata, win)
            adjzeros = zeros[0]
            while len(adjzeros) != 0:
                adjzeros2 = []
                for n in adjzeros:
                    c = n[0]
                    r = n[1]
                    cover(50 * c + 25, 50 * r + 25, win)
                    zeros2 = zeropop(c, r, clms, rows, boxdata, win)
                    adjzeros2 += zeros2[0]
                adjzeros = adjzeros2
        else:
            cover(x, y, win)
            num(x, y, win, mines)
    elif box == 3 or box == 5:
        drawflag(x, y, win)
    elif box == 4 or box == 1:
        flagcover(x, y, win)


def adjmines(x, y, clms, rows, boxdata):
    mines = 0
    if x == 0:
        for n in range(x, x + 2):
            if y == 0:
                for i in range(y, y + 2):
                    if boxdata[n, i] == 1 or boxdata[n, i] == 5:
                        mines += 1
            elif y == rows - 1:
                for i in range(y - 1, y + 1):
                    if boxdata[n, i] == 1 or boxdata[n, i] == 5:
                        mines += 1
            else:
                for i in range(y - 1, y + 2):
                    if boxdata[n, i] == 1 or boxdata[n, i] == 5:
                        mines += 1
    elif x == clms - 1:
        for n in range(x - 1, x + 1):
            if y == 0:
                for i in range(y, y + 2):
                    if boxdata[n, i] == 1 or boxdata[n, i] == 5:
                        mines += 1
            elif y == rows - 1:
                for i in range(y - 1, y + 1):
                    if boxdata[n, i] == 1 or boxdata[n, i] == 5:
                        mines += 1
            else:
                for i in range(y - 1, y + 2):
                    if boxdata[n, i] == 1 or boxdata[n, i] == 5:
                        mines += 1
    else:
        for n in range(x - 1, x + 2):
            if y == 0:
                for i in range(y, y + 2):
                    if boxdata[n, i] == 1 or boxdata[n, i] == 5:
                        mines += 1
            elif y == rows - 1:
                for i in range(y - 1, y + 1):
                    if boxdata[n, i] == 1 or boxdata[n, i] == 5:
                        mines += 1
            else:
                for i in range(y - 1, y + 2):
                    if boxdata[n, i] == 1 or boxdata[n, i] == 5:
                        mines += 1
    return mines


def zeropop(x, y, clms, rows, boxdata, win):
    zeros = []
    adj = []
    if x == 0:
        for n in range(x, x + 2):
            if y == 0:
                for i in range(y, y + 2):
                    if boxdata[n, i] not in range(1, 6):
                        boxdata[n, i] = 2
                        if adjmines(n, i, clms, rows, boxdata) == 0:
                            zeros.append([n, i])
                        else:
                            adj.append([n, i])
            elif y == rows - 1:
                for i in range(y - 1, y + 1):
                    if boxdata[n, i] not in range(1, 6):
                        boxdata[n, i] = 2
                        if adjmines(n, i, clms, rows, boxdata) == 0:
                            zeros.append([n, i])
                        else:
                            adj.append([n, i])
            else:
                for i in range(y - 1, y + 2):
                    if boxdata[n, i] not in range(1, 6):
                        boxdata[n, i] = 2
                        if adjmines(n, i, clms, rows, boxdata) == 0:
                            zeros.append([n, i])
                        else:
                            adj.append([n, i])
    elif x == clms - 1:
        for n in range(x - 1, x + 1):
            if y == 0:
                for i in range(y, y + 2):
                    if boxdata[n, i] not in range(1, 6):
                        boxdata[n, i] = 2
                        if adjmines(n, i, clms, rows, boxdata) == 0:
                            zeros.append([n, i])
                        else:
                            adj.append([n, i])
            elif y == rows - 1:
                for i in range(y - 1, y + 1):
                    if boxdata[n, i] not in range(1, 6):
                        boxdata[n, i] = 2
                        if adjmines(n, i, clms, rows, boxdata) == 0:
                            zeros.append([n, i])
                        else:
                            adj.append([n, i])
            else:
                for i in range(y - 1, y + 2):
                    if boxdata[n, i] not in range(1, 6):
                        boxdata[n, i] = 2
                        if adjmines(n, i, clms, rows, boxdata) == 0:
                            zeros.append([n, i])
                        else:
                            adj.append([n, i])
    else:
        for n in range(x - 1, x + 2):
            if y == 0:
                for i in range(y, y + 2):
                    if boxdata[n, i] not in range(1, 6):
                        boxdata[n, i] = 2
                        if adjmines(n, i, clms, rows, boxdata) == 0:
                            zeros.append([n, i])
                        else:
                            adj.append([n, i])
            elif y == rows - 1:
                for i in range(y - 1, y + 1):
                    if boxdata[n, i] not in range(1, 6):
                        boxdata[n, i] = 2
                        if adjmines(n, i, clms, rows, boxdata) == 0:
                            zeros.append([n, i])
                        else:
                            adj.append([n, i])
            else:
                for i in range(y - 1, y + 2):
                    if boxdata[n, i] not in range(1, 6):
                        boxdata[n, i] = 2
                        if adjmines(n, i, clms, rows, boxdata) == 0:
                            zeros.append([n, i])
                        else:
                            adj.append([n, i])
    for n in adj:
        c = n[0]
        r = n[1]
        cx = 50 * c + 25
        ry = 50 * r + 25
        minepop = adjmines(c, r, clms, rows, boxdata)
        cover(cx, ry, win)
        num(cx, ry, win, minepop)
    return zeros, boxdata


def loss(boxdata, maxx, maxy, win):
    try:
        x = -25
        for col in boxdata:
            x += 50
            y = -25
            for box in col:
                y += 50
                if box == 1 or box == 5:
                    flagcover(x, y, win)
                    mine = Circle(Point(x, y), 14)
                    mine.setFill('black')
                    mine.setOutline('dark gray')
                    mine.setWidth(5)
                    mine.draw(win)
                if box == 3:
                    cover = Rectangle(Point(x - 25, y - 24), Point(x + 24, y + 25))
                    cover.setFill(color_rgb(232, 199, 194))
                    cover.setOutline('dark gray')
                    cover.draw(win)
                    drawflag(x, y, win)
        win.getMouse()
        for graphic in win.items[::-1]:
            graphic.undraw()
        text = Text(Point(maxx / 2, maxy / 2), 'YOU LOSE')
        text.setSize(34)
        text.setFill(color_rgb(120, 120, 120))
        text.setStyle('bold')
        text.draw(win)
        win.getMouse()
        text.undraw()
    except:
        return


def wincheck(boxdata):
    unused = False
    mines = False
    for col in boxdata:
        for box in col:
            if box == 0 or box == 3 or box == 4:
                unused = True
            elif box == 1:
                mines = True
    if not mines or not unused:
        return True
    return False


def winner(boxdata, maxx, maxy, win):
    try:
        x = -25
        for col in boxdata:
            x += 50
            y = -25
            for box in col:
                y += 50
                if box == 1 or box == 5:
                    ran1 = random.randint(0, 255)
                    ran2 = random.randint(0, 255)
                    ran3 = random.randint(0, 255)
                    flagcover(x, y, win)
                    mine = Circle(Point(x, y), 14)
                    mine.setFill(color_rgb(ran1, ran2, ran3))
                    mine.setOutline('dark gray')
                    mine.setWidth(5)
                    mine.draw(win)
        win.getMouse()
        for graphic in win.items[::-1]:
            graphic.undraw()
        text = Text(Point(maxx / 2, maxy / 2), 'YOU WIN')
        text.setSize(34)
        text.setStyle('bold')
        text.setFill(color_rgb(120, 120, 120))
        text.draw(win)
        win.getMouse()
        text.undraw()
    except:
        return


def flagcheck(boxdata):
    flags = 0
    for clm in boxdata:
        for box in clm:
            if box == 3 or box == 5:
                flags += 1
    return flags


def remflags(maxx, maxy, minect, boxdata, win):
    box = Rectangle(Point(maxx / 2 - 10, maxy), Point((maxx / 2) + 50, maxy - 48))
    box.setFill('dark gray')
    box.setOutline('dark gray')
    box.draw(win)
    flags = flagcheck(boxdata)
    text = Text(Point((maxx / 2) + 20, maxy - 25), ': ' + str(minect - flags))
    text.setSize(36)
    text.setFill(color_rgb(120, 120, 120))
    text.draw(win)


def topdisplay(maxx, maxy, win):
    x = (maxx / 2) - 20
    y = maxy - 25
    pole = Line(Point(x + 1, y + 1), Point(x + 1, y - 10))
    pole.setWidth(2)
    pole.draw(win)
    base1 = Line(Point(x - 9, y - 12), Point(x + 9, y - 12))
    base1.setWidth(3.1)
    base1.draw(win)
    base2 = Line(Point(x - 5, y - 9), Point(x + 5, y - 9))
    base2.setWidth(2.5)
    base2.draw(win)
    flag = Polygon(Point(x + 1, y - 1), Point(x + 1, y + 11), Point(x - 9, y + 5))
    flag.setFill('red')
    flag.setOutline('red')
    flag.draw(win)
    x1 = 13
    y1 = 37
    exit1 = Line(Point(maxx - x1, maxy - y1), Point(maxx - y1, maxy - x1))
    exit2 = Line(Point(maxx - x1, maxy - x1), Point(maxx - y1, maxy - y1))
    exit1.setOutline(color_rgb(140, 140, 140))
    exit1.setWidth(4)
    exit2.setOutline(color_rgb(140, 140, 140))
    exit2.setWidth(4)
    exit1.draw(win)
    exit2.draw(win)
    op1 = Line(Point(x1, maxy - 17), Point(y1, maxy - 17))
    op2 = Line(Point(x1, maxy - 25), Point(y1, maxy - 25))
    op3 = Line(Point(x1, maxy - 33), Point(y1, maxy - 33))
    op1.setOutline(color_rgb(140, 140, 140))
    op1.setWidth(5)
    op2.setOutline(color_rgb(140, 140, 140))
    op2.setWidth(5)
    op3.setOutline(color_rgb(140, 140, 140))
    op3.setWidth(5)
    op1.draw(win)
    op2.draw(win)
    op3.draw(win)


def options(diff, win):
    optwin = GraphWin('Options', 150, 150, autoflush=False)
    optwin.setCoords(0, 0, 150, 150)
    optwin.setBackground('dark gray')
    op1 = Rectangle(Point(0, 100), Point(150, 150))
    op2 = Rectangle(Point(0, 50), Point(150, 100))
    op1.setFill('light gray')
    op2.setFill('light gray')
    op1.setOutline(color_rgb(190, 190, 190))
    op2.setOutline(color_rgb(190, 190, 190))
    op1.setWidth(5)
    op2.setWidth(5)
    op1.draw(optwin)
    op2.draw(optwin)
    size = 16
    t1 = Text(Point(75, 125), 'Restart')
    t2 = Text(Point(75, 75), 'Change Difficulty')
    t3 = Text(Point(75, 25), 'Cancel')
    t1.setFill(color_rgb(130, 130, 130))
    t1.setSize(size)
    t1.draw(optwin)
    t2.setFill(color_rgb(130, 130, 130))
    t2.setSize(size)
    t2.draw(optwin)
    t3.setFill(color_rgb(90, 90, 90))
    t3.setSize(size)
    t3.draw(optwin)
    try:
        click = optwin.getMouse()
        y = click.getY()
        if 50 <= y <= 100:
            win.close()
            optwin.close()
            main(False)
        elif 100 <= y <= 150:
            win.close()
            optwin.close()
            main(diff)
        optwin.close()
    except:
        return


def playagain(maxx, maxy, diff, win):
    text = Text(Point(maxx / 2, maxy * 3 / 4), 'PLAY AGAIN?')
    text.setSize(34)
    text.setFill(color_rgb(120, 120, 120))
    text.setStyle('bold')
    text.draw(win)
    yes = Text(Point(maxx / 4, maxy / 4), 'YES')
    no = Text(Point(maxx * 3 / 4, maxy / 4), 'NO')
    yesbox = Rectangle(Point(0, 0), Point(maxx / 2, maxy / 2))
    nobox = Rectangle(Point(maxx / 2, 0), Point(maxx, maxy / 2))
    yes.setSize(25)
    yes.setFill(color_rgb(140, 140, 140))
    yes.setStyle('bold')
    yesbox.setFill('light gray')
    yesbox.setOutline(color_rgb(190, 190, 190))
    yesbox.setWidth(5)
    no.setSize(25)
    no.setFill(color_rgb(140, 140, 140))
    no.setStyle('bold')
    nobox.setFill('light gray')
    nobox.setOutline(color_rgb(190, 190, 190))
    nobox.setWidth(5)
    yesbox.draw(win)
    nobox.draw(win)
    no.draw(win)
    yes.draw(win)
    click = win.getMouse()
    x = click.getX()
    y = click.getY()
    if x < maxx / 2:
        win.close()
        main(diff)
    else:
        win.close()
    while y > maxy / 2:
        click = win.getMouse()
        x = click.getX()
        y = click.getY()
        if y < maxy / 2:
            if x < maxx / 2:
                main(' ')
            else:
                win.close()


def test(win, clms, rows, boxdata):
    x = -25
    for n in range(clms):
        x += 50
        y = -25
        for e in range(rows):
            y += 50
            if boxdata[n, e] == 1:
                mine = Text(Point(x, y), 'mine')
                mine.draw(win)


def main(diff):
    if diff == 'closed':
        return
    if not diff:
        diff = difficulty()
    if diff == 'easy':
        rows = 8
        clms = 10
        minect = 10
    elif diff == 'medium':
        rows = 11
        clms = 17
        minect = 30
    else:
        rows = 14
        clms = 28
        minect = 80
    maxx = clms * 50
    maxy = (rows * 50) + 50
    win = minewindow(maxx, maxy)
    clear = array(clms, rows)
    playing = True
    exit = False
    boxdata = start(clms, rows, maxx, maxy, minect, clear, win)
    try:
        # test(win, clms, rows, boxdata)
        while playing:
            click = select(maxx, maxy, rows, win)
            if click == 'exit':
                win.close()
                exit = True
                break
            elif click == 'opt':
                options(diff, win)
                continue
            elif click == 'closed':
                exit = True
                break
            x = click[0]
            y = click[1]
            check = state(boxdata, win, x, y, minect, maxx, maxy)
            if wincheck(boxdata):
                display(boxdata, win, x, y, clms, rows)
                winner(boxdata, maxx, maxy, win)
                break
            else:
                if type(check) != str:
                    display(boxdata, win, x, y, clms, rows)
                else:
                    loss(boxdata, maxx, maxy, win)
                    playing = False
        if not exit:
            playagain(maxx, maxy, diff, win)
    except:
        return


diff = difficulty()
main(diff)
