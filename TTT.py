from graphics import *
import random


def create_window():
    mywin = GraphWin('TTT', 500, 500)
    mywin.setCoords(0, 0, 500, 500)
    mywin.setBackground('light green')
    return mywin


def draw_grid(win):
    thick = 5
    color = 'white'
    bh = Line(Point(100, 200), Point(400, 200))
    bh.draw(win)
    bh.setWidth(thick)
    bh.setFill(color)
    th = Line(Point(100, 300), Point(400, 300))
    th.draw(win)
    th.setWidth(thick)
    th.setFill(color)
    lv = Line(Point(200, 400), Point(200, 100))
    lv.draw(win)
    lv.setWidth(thick)
    lv.setFill(color)
    rv = Line(Point(300, 400), Point(300, 100))
    rv.draw(win)
    rv.setWidth(thick)
    rv.setFill(color)


def draw_circle(win, x, y):
    c = Circle(Point(x, y), 40)
    c.draw(win)
    c.setOutline('white')
    c.setWidth(5)


def draw_cross(win, x1, y1, x2, y2):
    c1 = Line(Point(x1, y1), Point(x2, y2))
    c2 = Line(Point(x1, y2), Point(x2, y1))
    c1.draw(win)
    c2.draw(win)
    c1.setFill('white')
    c2.setFill('white')
    c1.setWidth(5)
    c2.setWidth(5)


def crosscoords(win, boxnum):
    boxlist = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    if boxnum in boxlist[0]:
        x1 = 110
        x2 = 190
        if boxnum == 1:
            y1 = 390
            y2 = 310
        elif boxnum == 4:
            y1 = 290
            y2 = 210
        else:
            y1 = 190
            y2 = 110
    elif boxnum in boxlist[1]:
        x1 = 210
        x2 = 290
        if boxnum == 2:
            y1 = 390
            y2 = 310
        elif boxnum == 5:
            y1 = 290
            y2 = 210
        else:
            y1 = 190
            y2 = 110
    elif boxnum in boxlist[2]:
        x1 = 310
        x2 = 390
        if boxnum == 3:
            y1 = 390
            y2 = 310
        elif boxnum == 6:
            y1 = 290
            y2 = 210
        else:
            y1 = 190
            y2 = 110
    draw_cross(win, x1, y1, x2, y2)


def circlecoords(win, boxnum):
    boxlist = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    x = 0
    y = 0
    if boxnum in boxlist[0]:
        x = 150
        if boxnum == 1:
            y = 350
        elif boxnum == 4:
            y = 250
        else:
            y = 150
    elif boxnum in boxlist[1]:
        x = 250
        if boxnum == 2:
            y = 350
        elif boxnum == 5:
            y = 250
        else:
            y = 150
    elif boxnum in boxlist[2]:
        x = 350
        if boxnum == 3:
            y = 350
        elif boxnum == 6:
            y = 250
        else:
            y = 150
    draw_circle(win, x, y)


def box_select(win):
    click = win.getMouse()
    # print(click)
    x = click.getX()
    # print(x)
    y = click.getY()
    if 100 < x < 200:
        if 300 < y < 400:
            return 1
        elif 200 < y < 400:
            return 4
        elif 100 < y < 200:
            return 7
    elif 200 < x < 300:
        if 300 < y < 400:
            return 2
        elif 200 < y < 400:
            return 5
        elif 100 < y < 200:
            return 8
    elif 300 < x < 400:
        if 300 < y < 400:
            return 3
        elif 200 < y < 400:
            return 6
        elif 100 < y < 200:
            return 9
    else:
        return None


def check_free(boxnum, used):
    if boxnum in used:
        return False
    else:
        return True


def circlewin(circles):
    if 1 in circles:
        if 2 in circles and 3 in circles:
            return [1, 3]
        if 4 in circles and 7 in circles:
            return [1, 7]
        if 5 in circles and 9 in circles:
            return [1, 9]
    if 2 in circles and 5 in circles and 8 in circles:
        return [2, 8]
    if 3 in circles:
        if 5 in circles and 7 in circles:
            return [3, 7]
        if 6 in circles and 9 in circles:
            return [3, 9]
    if 4 in circles:
        if 5 in circles and 6 in circles:
            return [4, 6]
    if 7 in circles and 8 in circles and 9 in circles:
        return [7, 9]
    else:
        return False


def crosswin(crosses):
    if 1 in crosses:
        if 2 in crosses and 3 in crosses:
            return [1, 3]
        if 4 in crosses and 7 in crosses:
            return [1, 7]
        if 5 in crosses and 9 in crosses:
            return [1, 9]
    if 2 in crosses and 5 in crosses and 8 in crosses:
        return [2, 8]
    if 3 in crosses:
        if 5 in crosses and 7 in crosses:
            return [3, 7]
        if 6 in crosses and 9 in crosses:
            return [3, 9]
    if 4 in crosses:
        if 5 in crosses and 6 in crosses:
            return [4, 6]
    if 7 in crosses and 8 in crosses and 9 in crosses:
        return [7, 9]
    else:
        return False


def its_a_win(circles, crosses, win):
    crwin = crosswin(crosses)
    ciwin = circlewin(circles)
    if crwin != False:
        winline(crwin, win)
        return 'cross'
    if ciwin != False:
        winline(ciwin, win)
        return 'circle'
    else:
        return False


def winline(list, win):
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    if list == [1, 3]:
        x1 = 100
        x2 = 400
        y1 = 350
        y2 = 350
    if list == [1, 7]:
        x1 = 150
        x2 = 150
        y1 = 400
        y2 = 100
    if list == [1, 9]:
        x1 = 100
        x2 = 400
        y1 = 400
        y2 = 100
    if list == [2, 8]:
        x1 = 250
        x2 = 250
        y1 = 400
        y2 = 100
    if list == [3, 7]:
        x1 = 400
        x2 = 100
        y1 = 400
        y2 = 100
    if list == [3, 9]:
        x1 = 350
        x2 = 350
        y1 = 400
        y2 = 100
    if list == [4, 6]:
        x1 = 100
        x2 = 400
        y1 = 250
        y2 = 250
    if list == [7, 9]:
        x1 = 100
        x2 = 400
        y1 = 150
        y2 = 150
    line = Line(Point(x1, y1), Point(x2, y2))
    line.draw(win)
    line.setFill('white')
    line.setWidth(10)


def score(win, crossct, circlect, tiect):
    crosswins = Text(Point(100, 450), "Crosses: " + str(crossct))
    circlewins = Text(Point(400, 450), "Circles: " + str(circlect))
    ties = Text(Point(250, 450), "Ties: " + str(tiect))
    crosswins.setFill('white')
    crosswins.setSize(20)
    circlewins.setFill('white')
    circlewins.setSize(20)
    ties.setFill('white')
    ties.setSize(20)
    crosswins.draw(win)
    circlewins.draw(win)
    ties.draw(win)


def endoptions(win):
    conttext = Text(Point(250, 20), 'Click anywhere on the screen to continue')
    conttext.draw(win)
    conttext.setFill('white')
    conttext.setSize(15)
    endbutton = Rectangle(Point(410, 60), Point(490, 20))
    endtext = Text(Point(450, 40), 'End Game')
    endbutton.draw(win)
    endbutton.setOutline('white')
    endtext.draw(win)
    endtext.setFill('white')


def players(win):
    size = 30
    color = 'white'
    onetext = Text(Point(125, 250), 'ONE PLAYER')
    twotext = Text(Point(375, 250), 'TWO PLAYERS')
    div = Line(Point(250, 500), Point(250, 0))
    onetext.setSize(size)
    twotext.setSize(size)
    onetext.setFill(color)
    twotext.setFill(color)
    div.setOutline(color)
    div.draw(win)
    div.setWidth(7)
    onetext.draw(win)
    twotext.draw(win)
    playerselect = win.getMouse()
    playerx = playerselect.getX()
    if 0 < playerx < 250:
        players = 1
    else:
        players = 2
    for object in win.items[:]:
        object.undraw()
    return players


def shape(win):
    color = 'white'
    width = 10
    div = Line(Point(250, 500), Point(250, 0))
    cross1 = Line(Point(25, 350), Point(225, 150))
    cross2 = Line(Point(25, 150), Point(225, 350))
    circle = Circle(Point(375, 250), 100)
    div.setOutline(color)
    div.draw(win)
    div.setWidth(width)
    cross1.draw(win)
    cross1.setWidth(width)
    cross2.setWidth(width)
    circle.setWidth(width)
    cross2.draw(win)
    circle.draw(win)
    cross1.setOutline(color)
    cross2.setOutline(color)
    circle.setOutline(color)
    shapeselect = win.getMouse()
    shapex = shapeselect.getX()
    if 0 < shapex < 250:
        circle = False
    else:
        circle = True
    for object in win.items[:]:
        object.undraw()
    return circle


def cpuwincheck(circles, crosses, cpucircle, used):
    if cpucircle:
        cpu = circles
        player = crosses
    else:
        cpu = crosses
        player = circles
    if 1 in cpu:
        if 2 in cpu and check_free(3, used):
            return 3
        if 3 in cpu and check_free(2, used):
            return 2
        if 4 in cpu and check_free(7, used):
            return 7
        if 7 in cpu and check_free(4, used):
            return 4
        if 5 in cpu and check_free(9, used):
            return 9
        if 9 in cpu and check_free(5, used):
            return 5
    if 2 in cpu:
        if 5 in cpu and check_free(8, used):
            return 8
        if 8 in cpu and check_free(5, used):
            return 5
    if 3 in cpu:
        if 2 in cpu and check_free(1, used):
            return 1
        if 5 in cpu and check_free(7, used):
            return 7
        if 7 in cpu and check_free(5, used):
            return 5
        if 6 in cpu and check_free(9, used):
            return 9
        if 9 in cpu and check_free(6, used):
            return 6
    if 4 in cpu:
        if 5 in cpu and check_free(6, used):
            return 6
        if 6 in cpu and check_free(5, used):
            return 5
    if 5 in cpu:
        if 9 in cpu and check_free(1, used):
            return 1
        if 7 in cpu and check_free(3, used):
            return 3
        if 6 in cpu and check_free(4, used):
            return 4
        if 8 in cpu and check_free(2, used):
            return 2
        if 2 in cpu and check_free(8, used):
            return 8
    if 6 in cpu:
        if 9 in cpu and check_free(3, used):
            return 3
    if 7 in cpu:
        if 9 in cpu and check_free(8, used):
            return 8
        if 8 in cpu and check_free(9, used):
            return 9
    if 8 in cpu:
        if 9 in cpu and check_free(7, used):
            return 7
    if 1 in player:
        if 2 in player and check_free(3, used):
            return 3
        if 3 in player and check_free(2, used):
            return 2
        if 4 in player and check_free(7, used):
            return 7
        if 7 in player and check_free(4, used):
            return 4
        if 5 in player and check_free(9, used):
            return 9
        if 9 in player and check_free(5, used):
            return 5
    if 2 in player:
        if 5 in player and check_free(8, used):
            return 8
        if 8 in player and check_free(5, used):
            return 5
    if 3 in player:
        if 2 in player and check_free(1, used):
            return 1
        if 5 in player and check_free(7, used):
            return 7
        if 7 in player and check_free(5, used):
            return 5
        if 6 in player and check_free(9, used):
            return 9
        if 9 in player and check_free(6, used):
            return 6
    if 4 in player:
        if 5 in player and check_free(6, used):
            return 6
        if 6 in player and check_free(5, used):
            return 5
    if 5 in player:
        if 9 in player and check_free(1, used):
            return 1
        if 7 in player and check_free(3, used):
            return 3
        if 6 in player and check_free(4, used):
            return 4
        if 8 in player and check_free(2, used):
            return 2
        if 2 in player and check_free(8, used):
            return 8
    if 6 in player:
        if 9 in player and check_free(3, used):
            return 3
    if 7 in player:
        if 9 in player and check_free(8, used):
            return 8
        if 8 in player and check_free(9, used):
            return 9
    if 8 in player:
        if 9 in player and check_free(7, used):
            return 7


def welp(circles, crosses, cpucircle):
    pick = random.randint(0, 1)
    side = random.randint(1, 4)
    if cpucircle:
        player = crosses
        cpu = circles
    else:
        player = circles
        cpu = crosses
    if 1 in player and 9 in player:
        if side == 1:
            return 2
        elif side == 2:
            return 4
        elif side == 3:
            return 6
        else:
            return 8
    elif 3 in player and 7 in player:
        if side == 1:
            return 2
        elif side == 2:
            return 4
        elif side == 3:
            return 6
        else:
            return 8
    if 5 in player:
        if 2 in player:
            if 8 not in cpu:
                return 8
            elif 1 not in cpu or 3 not in cpu:
                if pick == 0:
                    return 1
                else:
                    return 3
        elif 4 in player:
            if 6 not in cpu:
                return 6
            elif 1 not in cpu or 7 not in cpu:
                if pick == 0:
                    return 1
                else:
                    return 7
        elif 6 in player:
            if 4 not in cpu:
                return 4
            elif 3 not in cpu or 9 not in cpu:
                if pick == 0:
                    return 3
                else:
                    return 9
        elif 8 in player:
            if 2 not in cpu:
                return 2
            elif 7 not in cpu or 9 not in cpu:
                if pick == 0:
                    return 7
                else:
                    return 9


def singleplayer(my_window):
    circlect = 0
    crossct = 0
    tiect = 0
    endgame = False
    circle = shape(my_window)
    if circle:
        cpucircle = False
        playercircle = True
    else:
        cpucircle = True
        playercircle = False
    while not endgame:
        turn = 0
        used = [0]
        circles = []
        crosses = []
        winner = False
        draw_grid(my_window)
        while turn != 9 and not winner:
            if turn % 2 == 0:
                score(my_window, crossct, circlect, tiect)
                boxnum = box_select(my_window)
                while boxnum == None:
                    boxnum = box_select(my_window)
                check = check_free(boxnum, used)
                if check:
                    used.append(boxnum)
                    if playercircle:
                        circlecoords(my_window, boxnum)
                        circles.append(boxnum)
                        turn += 1
                    elif not playercircle:
                        crosscoords(my_window, boxnum)
                        crosses.append(boxnum)
                        turn += 1
            if turn % 2 != 0 and turn != 9:
                if turn == 1:
                    if 5 in used:
                        choice = random.randint(1, 4)
                        if choice == 1:
                            boxnum = 1
                        elif choice == 2:
                            boxnum = 3
                        elif choice == 3:
                            boxnum = 7
                        else:
                            boxnum = 9
                    elif 1 in used or 3 in used or 7 in used or 9 in used:
                        boxnum = 5
                    elif 2 in used:
                        boxnum = 8
                    elif 4 in used:
                        boxnum = 6
                    elif 6 in used:
                        boxnum = 4
                    else:
                        boxnum = 2
                elif turn == 3 and welp(circles, crosses, cpucircle) != None:
                    boxnum = welp(circles, crosses, cpucircle)
                else:
                    wincheck = cpuwincheck(circles, crosses, cpucircle, used)
                    if wincheck != None:
                        boxnum = wincheck
                    else:
                        choice = random.randint(1, 9)
                        while not check_free(choice, used):
                            choice = random.randint(1, 9)
                        boxnum = choice
                if cpucircle:
                    circlecoords(my_window, boxnum)
                    circles.append(boxnum)
                    used.append(boxnum)
                    turn += 1
                else:
                    crosscoords(my_window, boxnum)
                    crosses.append(boxnum)
                    used.append(boxnum)
                    turn += 1
            winner = its_a_win(circles, crosses, my_window)
        if winner == 'cross':
            res = Text(Point(250, 50), "CROSS WINS")
            crossct += 1
        elif winner == 'circle':
            res = Text(Point(250, 50), "CIRCLE WINS")
            circlect += 1
        else:
            res = Text(Point(250, 50), "TIE")
            tiect += 1
        res.draw(my_window)
        res.setFill('white')
        res.setSize(36)
        endoptions(my_window)
        endcheck = my_window.getMouse()
        if 410 < endcheck.getX() < 490 and 30 < endcheck.getY() < 70:
            endgame = True
        for object in my_window.items[:]:
            object.undraw()
        my_window.update()
    score(my_window, crossct, circlect, tiect)
    if crossct > circlect:
        display = Text(Point(250, 250), 'CROSS WINS')
    elif circlect > crossct:
        display = Text(Point(250, 250), 'CIRCLE WINS')
    else:
        display = Text(Point(250, 250), 'TIE')
    display.draw(my_window)
    display.setFill('White')
    display.setSize(36)
    display.setStyle('bold')
    my_window.getMouse()


def main():
    circlect = 0
    crossct = 0
    tiect = 0
    endgame = False
    my_window = create_window()
    playernum = players(my_window)
    if playernum == 2:
        circle = shape(my_window)
        while not endgame:
            turn = 0
            used = [0]
            circles = []
            crosses = []
            winner = False
            draw_grid(my_window)
            while turn != 9 and not winner:
                score(my_window, crossct, circlect, tiect)
                boxnum = box_select(my_window)
                while boxnum == None:
                    boxnum = box_select(my_window)
                check = check_free(boxnum, used)
                if check:
                    used.append(boxnum)
                    if circle:
                        circlecoords(my_window, boxnum)
                        turn += 1
                        circles.append(boxnum)
                        circle = False
                    elif not circle:
                        crosscoords(my_window, boxnum)
                        turn += 1
                        crosses.append(boxnum)
                        circle = True
                    winner = its_a_win(circles, crosses, my_window)
            if winner == 'cross':
                res = Text(Point(250, 50), "CROSS WINS")
                crossct += 1
            elif winner == 'circle':
                res = Text(Point(250, 50), "CIRCLE WINS")
                circlect += 1
            else:
                res = Text(Point(250, 50), "TIE")
                tiect += 1
            res.draw(my_window)
            res.setFill('white')
            res.setSize(36)
            endoptions(my_window)
            endcheck = my_window.getMouse()
            if 410 < endcheck.getX() < 490 and 30 < endcheck.getY() < 70:
                endgame = True
            for object in my_window.items[:]:
                object.undraw()
            my_window.update()
        score(my_window, crossct, circlect, tiect)
        if crossct > circlect:
            display = Text(Point(250, 250), 'CROSS WINS')
        elif circlect > crossct:
            display = Text(Point(250, 250), 'CIRCLE WINS')
        else:
            display = Text(Point(250, 250), 'TIE')
        display.draw(my_window)
        display.setFill('White')
        display.setSize(36)
        display.setStyle('bold')
        my_window.getMouse()
    elif playernum == 1:
        singleplayer(my_window)


main()
