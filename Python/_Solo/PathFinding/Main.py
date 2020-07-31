import pygame as py
import time
import sys
import Algorithm_visual

white = (230, 230, 230)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 200, 0)
blue = (50, 50, 200)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
bright_blue = (0, 0, 255)
icon_32pix = py.image.load("tulan_logo2.png")

py.init()
screen = py.display.set_mode((800, 600), py.RESIZABLE)

py.display.set_icon(icon_32pix)
py.display.set_caption("PathFinder by Tulan")

hugetext = py.font.Font('freesansbold.ttf', 115)
largetext = py.font.Font('freesansbold.ttf', 70)
mediumtext = py.font.Font('freesansbold.ttf', 40)
smalltext = py.font.Font('freesansbold.ttf', 20)
minitext = py.font.Font('freesansbold.ttf', 15)

intro = True

setting_board = ["Chose board", "Please chose Algorithm"]




def intro_menu():
    global intro
    while intro:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                quit()
                sys.exit()
            if event.type == py.VIDEORESIZE:
                width = event.w
                height = event.h
                py.display.set_mode((width, height), py.RESIZABLE)
        screen.fill(white)

        TextSurf, TextRect = text_objects("PathFinder", hugetext)
        TextRect.center = (400, 100)
        screen.blit(TextSurf, TextRect)

        TextSurf2, TextRect2 = text_objects("by Tulan", largetext)
        TextRect2.center = (600, 200)
        screen.blit(TextSurf2, TextRect2)

        TextSurf3, TextRect3 = text_objects("visualization", mediumtext)
        TextRect3.center = (300, 200)
        screen.blit(TextSurf3, TextRect3)

        textSurf0, textRect0 = text_objects("My GitHub: TulanPG", smalltext)
        textRect0.center = (650, 590)
        screen.blit(textSurf0, textRect0)

        button("START SETTING", 100, 520, 200, 50, green, bright_green, "setting")
        button("QUIT", 600, 520, 100, 50, red, bright_red, "quit")
        button("INSTRUCTION", 350, 520, 200, 50, blue, bright_blue, "intro")
        py.display.update()
        py.time.Clock().tick(30)


def text_objects(text, font):
    textsurface = font.render(text, True, black)
    return textsurface, textsurface.get_rect()


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = py.mouse.get_pos()
    click = py.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        py.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action is not None:
            global intro

            # Starting button
            if action == "setting":
                intro = False
                setting_menu()

            elif action == "intro":
                intro = False
                instruction_menu()

            elif action == "quit":
                py.quit()
                quit()
                sys.exit()

            elif action == "start":
                Algorithm_visual.main(screen,600, setting_board)

            # Setting button
            elif action == "10x10":
                setting_board[0] = 10
            elif action == "20x20":
                setting_board[0] = 20
            elif action == "30x30":
                setting_board[0] = 30
            elif action == "50x50":
                setting_board[0] = 50

            elif action == "Dijkstra's":
                setting_board[1] = "Dijkstra's"
            elif action == "A* Search":
                setting_board[1] = "A* Search"
            elif action == "Greedy BFS":
                setting_board[1] = "Greedy BFS"
            elif action == "Swarm":
                setting_board[1] = "Swarm"
            elif action == "Depth-first":
                setting_board[1] = "Depth-first"
            elif action == "Breadth-first":
                setting_board[1] = "Breadth-first"
            elif action == "Bidirectional":
                setting_board[1] = "Bidirectional"
            elif action == "Convergent":
                setting_board[1] = "Convergent"


    else:
        py.draw.rect(screen, ic, (x, y, w, h))
    textsurf, textrect = text_objects(msg, smalltext)
    textrect.center = (int(x + (w / 2)), int(y + (h / 2)))
    screen.blit(textsurf, textrect)


def instruction_menu():
    instruction = True
    while instruction:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                quit()
                sys.exit()
            if event.type == py.VIDEORESIZE:
                width = event.w
                height = event.h
                py.display.set_mode((width, height), py.RESIZABLE)
        screen.fill(white)
        # screen.blit(instruction_background,(0,0))
        x_text = 30
        TextSurf, TextRect = text_objects("INSTRUCTION", mediumtext)
        TextRect.center = (400, 60)
        textSurf, textRect = text_objects("This is pathfinding visualisation made by Tulan as CV project,", smalltext)
        textRect.center = (350, 100)
        textSurf1, textRect1 = text_objects("it will give you visualisation of 8'th algorithm:", smalltext)
        textRect1.center = (350, 140)
        textSurf2, textRect2 = text_objects("Dijkstra's: the father of pathfinding algorithms; "
                                            "guarantees the shortest path", minitext)
        textRect2 = (x_text, 180)
        textSurf3, textRect3 = text_objects(
            "A* Search: arguably the best pathfinding algorithm; "
            "uses heuristics to guarantee the shortest path", minitext)
        # much faster than Dijkstra's Algorithm
        textRect3 = (x_text, 210)
        textSurf4, textRect4 = text_objects(
            "Greedy Best-first Search: a faster, more heuristic-heavy ver. of A*; "
            "DOESN'T guarantee the shortest path", minitext)
        textRect4 = (x_text, 240)
        textSurf5, textRect5 = text_objects(
            "Swarm: a mixture of Dijkstra's and A*; DOESN'T guarantee the shortest-path", minitext)
        textRect5 = (x_text, 270)
        textSurf6, textRect6 = text_objects(
            "Convergent Swarm: the faster, more heuristic-heavy ver. of Swarm; "
            "DOESN'T guarantee the shortest path", minitext)
        textRect6 = (x_text, 300)
        textSurf7, textRect7 = text_objects(
            "Bidirectional Swarm: Swarm from both sides; DOESN'T guarantee the shortest path", minitext)
        textRect7 = (x_text, 330)
        textSurf8, textRect8 = text_objects(
            "Breath-first Search: a great algorithm; guarantees the shortest path", minitext)
        textRect8 = (x_text, 360)
        textSurf9, textRect9 = text_objects(
            "Depth-first Search: a very bad algorithm for pathfinding; DOESN'T guarantee the shortest path", minitext)
        textRect9 = (x_text, 390)

        textSurf0, textRect0 = text_objects("My GitHub: TulanPG", smalltext)
        textRect0.center = (650, 590)

        screen.blit(TextSurf, TextRect)
        screen.blit(textSurf, textRect)
        screen.blit(textSurf1, textRect1)
        screen.blit(textSurf0, textRect0)
        screen.blit(textSurf2, textRect2)
        screen.blit(textSurf3, textRect3)
        screen.blit(textSurf4, textRect4)
        screen.blit(textSurf5, textRect5)
        screen.blit(textSurf6, textRect6)
        screen.blit(textSurf7, textRect7)
        screen.blit(textSurf8, textRect8)
        screen.blit(textSurf9, textRect9)

        button("START SETTING", 550, 500, 200, 50, green, bright_green, "setting")
        py.display.update()
        py.time.Clock().tick(30)


def setting_menu():
    setting = True

    while setting:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                quit()
                sys.exit()
            if event.type == py.VIDEORESIZE:
                width = event.w
                height = event.h
                py.display.set_mode((width, height), py.RESIZABLE)
        screen.fill(white)

        TextSurf, TextRect = text_objects("SETTING'S OF ALGORITHM's", mediumtext)
        TextRect.center = (400, 60)
        screen.blit(TextSurf, TextRect)

        TextSurfB, TextRectB = text_objects("Board size:", smalltext)
        TextRectB.center = (400, 100)
        screen.blit(TextSurfB, TextRectB)

        button("HELP", 690, 20, 100, 50, blue, bright_blue, "intro")

        button("10x10", 120, 120, 135, 50, blue, bright_blue, "10x10")
        button("20x20", 270, 120, 135, 50, blue, bright_blue, "20x20")
        button("30x30", 420, 120, 135, 50, blue, bright_blue, "30x30")
        button("50x50", 570, 120, 135, 50, blue, bright_blue, "50x50")

        TextSurfA, TextRectA = text_objects("Algorithm chose:", smalltext)
        TextRectA.center = (400, 200)
        screen.blit(TextSurfA, TextRectA)

        button("Dijkstra's", 120, 220, 135, 50, blue, bright_blue, "Dijkstra's")
        button("A* Search", 270, 220, 135, 50, blue, bright_blue, "A* Search")
        button("Greedy BFS", 420, 220, 135, 50, blue, bright_blue, "Greedy BFS")
        button("Swarm", 570, 220, 135, 50, blue, bright_blue, "Swarm")

        button("Depth-first", 120, 290, 135, 50, blue, bright_blue, "Depth-first")
        button("Breadth-first", 270, 290, 135, 50, blue, bright_blue, "Breadth-first")
        button("Bidirectional", 420, 290, 135, 50, blue, bright_blue, "Bidirectional")
        button("Convergent", 570, 290, 135, 50, blue, bright_blue, "Convergent")

        TextSurfS, TextRectS = text_objects("Chosen:", smalltext)
        TextRectS.center = (400, 370)
        screen.blit(TextSurfS, TextRectS)

        TextSurfS1, TextRectS1 = text_objects("Board:", smalltext)
        TextRectS1.center = (250, 400)
        screen.blit(TextSurfS1, TextRectS1)

        TextSurfS11, TextRectS11 = text_objects((str(setting_board[0]) + " x " + str(setting_board[0])), smalltext)
        TextRectS11.center = (250, 450)
        screen.blit(TextSurfS11, TextRectS11)

        TextSurfSA, TextRectSA = text_objects("Algorithm:", smalltext)
        TextRectSA.center = (550, 400)
        screen.blit(TextSurfSA, TextRectSA)

        TextSurfSAA, TextRectSAA = text_objects((setting_board[1]), smalltext)
        TextRectSAA.center = (550, 450)
        screen.blit(TextSurfSAA, TextRectSAA)

        if setting_board[0] != "Chose board" and setting_board[1] != "Please chose Algorithm":
            button("Start if You are sure!", 120, 500, 580, 50, green, bright_green, "start")

        textSurf0, textRect0 = text_objects("My GitHub: TulanPG", smalltext)
        textRect0.center = (650, 590)
        screen.blit(textSurf0, textRect0)
        py.display.update()
        py.time.Clock().tick(30)


intro_menu()

"""
while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
        if event.type == py.VIDEORESIZE:
            width = event.w
            height = event.h
            screen = py.display.set_mode((width, height), py.RESIZABLE)
    screen.fill(white)
    py.display.update()
    py.time.Clock().tick(60)
"""
