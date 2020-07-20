import pygame
import sys
import random
from pygame.locals import *  # udostępnienie nazw metod z locals
#Pomysły:
#Kulka As
#Podświetlanie, gdzie się pojawią
#inny sposób rozwalania
#więcej kulek pojawia się
#Licznik kulek

# inicjacja modułu pygame
pygame.init()

# lista opisująca stan pola gry, 0 - pole puste, 1 - gracz, 2 - komputer

BLACK = (0, 0, 0)
background = (85, 153, 204)
background_board = (153, 204, 238)
red = pygame.image.load("red.png")
aqua = pygame.image.load("aqua.png")
green = pygame.image.load("green.png")
grey = pygame.image.load("grey.png")
pink = pygame.image.load("pink.png")
yellow = pygame.image.load("yellow.png")
blue = pygame.image.load("blue.png")
color_list = [0, red, aqua, green, grey, pink, yellow, blue]
COL = 9
ROW = 9
SQUARESIZE = 50
width = COL * SQUARESIZE
height = ROW * SQUARESIZE

balls_list = []
for _ in range(400, 250, -50):
    balls_list.insert(0, (_, 30, random.randint(1, 7)))

board = pygame.display.set_mode((width, height + 100), 0, 0)
pygame.display.set_caption('Kulki by Tulan')

play_board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]]

END = False


##Do dopracowania!
def end_def():
    total_balls = 0
    for i in range(0, 8):
        for j in range(0, 8):
            if play_board[i][j] != 0:
                total_balls += 1
                if total_balls == 81:
                    End = True


def insert_base_ball():
    for _ in range(400, 250, -50):
        balls_list.insert(0, (_, 30, random.randint(1, 7)))


def draw_base_ball():
    for k in range(0, 3):
        width_ball = balls_list[k][0]
        height_ball = balls_list[k][1]
        chose_color = balls_list[k][2]
        board.blit(pygame.transform.scale(color_list[chose_color], (50, 50)), (width_ball, height_ball))


def rysuj_plansze():
    pygame.draw.rect(board, background_board, (0, 100, width, height))
    for i in range(1, 10):
        pos = int(width / 9 * i)
        # Horizontal
        pygame.draw.line(board, background, (0, pos + 50), (width, pos + 50), 2)
        # Vertical line
        pygame.draw.line(board, background, (pos, 100), (pos, width + 100), 2)


def rysuj_kulki():
    for i in range(0, 9):
        for j in range(0, 9):

            x = j * SQUARESIZE + 25
            y = i * SQUARESIZE + 100 + 25

            if play_board[i][j] == 1:
                board.blit(pygame.transform.scale(red, (50, 50)), (x - 24, y - 24))
            elif play_board[i][j] == 2:

                board.blit(pygame.transform.scale(aqua, (50, 50)), (x - 24, y - 24))
            elif play_board[i][j] == 3:

                board.blit(pygame.transform.scale(green, (50, 50)), (x - 24, y - 24))
            elif play_board[i][j] == 4:

                board.blit(pygame.transform.scale(grey, (50, 50)), (x - 24, y - 24))
            elif play_board[i][j] == 5:

                board.blit(pygame.transform.scale(pink, (50, 50)), (x - 24, y - 24))
            elif play_board[i][j] == 6:

                board.blit(pygame.transform.scale(yellow, (50, 50)), (x - 24, y - 24))
            elif play_board[i][j] == 7:

                board.blit(pygame.transform.scale(blue, (50, 50)), (x - 24, y - 24))

            elif play_board[i][j] == 10:
                pygame.draw.rect(board, (255, 255, 255), (x - 24, y - 24, 50, 50))
                board.blit(pygame.transform.scale(red, (50, 50)), (x - 24, y - 24))
            elif play_board[i][j] == 20:
                pygame.draw.rect(board, (255, 255, 255), (x - 24, y - 24, 50, 50))
                board.blit(pygame.transform.scale(aqua, (50, 50)), (x - 24, y - 24))
            elif play_board[i][j] == 30:
                pygame.draw.rect(board, (255, 255, 255), (x - 24, y - 24, 50, 50))
                board.blit(pygame.transform.scale(green, (50, 50)), (x - 24, y - 24))
            elif play_board[i][j] == 40:
                pygame.draw.rect(board, (255, 255, 255), (x - 24, y - 24, 50, 50))
                board.blit(pygame.transform.scale(grey, (50, 50)), (x - 24, y - 24))
            elif play_board[i][j] == 50:
                pygame.draw.rect(board, (255, 255, 255), (x - 24, y - 24, 50, 50))
                board.blit(pygame.transform.scale(pink, (50, 50)), (x - 24, y - 24))
            elif play_board[i][j] == 60:
                pygame.draw.rect(board, (255, 255, 255), (x - 24, y - 24, 50, 50))
                board.blit(pygame.transform.scale(yellow, (50, 50)), (x - 24, y - 24))
            elif play_board[i][j] == 70:
                pygame.draw.rect(board, (255, 255, 255), (x - 24, y - 24, 50, 50))
                board.blit(pygame.transform.scale(blue, (50, 50)), (x - 24, y - 24))


def draw_score():
    ## DODAC WYNIK
    board_score = "Wynik: "
    draw_text(board_score + str(score), center=(100, 50), color=BLACK)


def draw_text(text, center, color=(180, 180, 180)):
    """
    Rysuje wskazany tekst we wskazanym miejscu
    """
    pygame.font.init()
    font_path = pygame.font.match_font('arial')
    font = pygame.font.Font(font_path, 48)

    text = font.render(text, True, color)
    rect = text.get_rect()
    rect.center = center
    board.blit(text, rect)


def zbicie_5kulek():

    for i in range(1, 8):
        for poleX in range(0, 5):
            for poleY in range(4, 9):
                if play_board[poleX][poleY] == i and play_board[poleX + 1][poleY - 1] == i and play_board[poleX + 2][
                    poleY - 2] == i and play_board[poleX + 3][poleY - 3] == i and play_board[poleX + 4][poleY - 4] == i:
                    play_board[poleX][poleY] = 0
                    play_board[poleX + 1][poleY - 1] = 0
                    play_board[poleX + 2][poleY - 2] = 0
                    play_board[poleX + 3][poleY - 3] = 0
                    play_board[poleX + 4][poleY - 4] = 0
                    return False

        for poleX in range(0, 5):
            for poleY in range(0, 5):
                if play_board[poleX][poleY] == i and play_board[poleX + 1][poleY + 1] == i and play_board[poleX + 2][
                    poleY + 2] == i and play_board[poleX + 3][poleY + 3] == i and play_board[poleX + 4][poleY + 4] == i:
                    play_board[poleX][poleY] = 0
                    play_board[poleX + 1][poleY + 1] = 0
                    play_board[poleX + 2][poleY + 2] = 0
                    play_board[poleX + 3][poleY + 3] = 0
                    play_board[poleX + 4][poleY + 4] = 0
                    return False

            for poleY in range(0, 9):
                if play_board[poleX][poleY] == i and play_board[poleX + 1][poleY] == i and play_board[poleX + 2][
                    poleY] == i and play_board[poleX + 3][poleY] == i and play_board[poleX + 4][poleY] == i:
                    play_board[poleX][poleY] = 0
                    play_board[poleX + 1][poleY] = 0
                    play_board[poleX + 2][poleY] = 0
                    play_board[poleX + 3][poleY] = 0
                    play_board[poleX + 4][poleY] = 0
                    return False

        for poleX in range(0, 9):
            for poleY in range(0, 5):
                if play_board[poleX][poleY] == i and play_board[poleX][poleY + 1] == i and play_board[poleX][
                    poleY + 2] == i and play_board[poleX][poleY + 3] == i and play_board[poleX][poleY + 4] == i:
                    play_board[poleX][poleY] = 0
                    play_board[poleX][poleY + 1] = 0
                    play_board[poleX][poleY + 2] = 0
                    play_board[poleX][poleY + 3] = 0
                    play_board[poleX][poleY + 4] = 0
                    return False
    return True


def postaw_3kulki():
    for _ in range(0, 3):
        poleX = random.randint(0, 8)
        poleY = random.randint(0, 8)
        while play_board[poleX][poleY] != 0:
            poleX = random.randint(0, 8)
            poleY = random.randint(0, 8)
        if play_board[poleX][poleY] == 0:
            play_board[poleX][poleY] = balls_list[_][2]
    insert_base_ball()


def ball_select(clicklocations):
    poleX1 = clicklocations[0][0]
    poleY1 = clicklocations[0][1]
    if play_board[poleX1][poleY1] != 0:
        if len(clicklocations_full) == 1:
            del clicklocations_full[0]
        clicklocations_full.insert(0, (poleX1, poleY1))
        #Do dopracowania bo usuwa kulki dwa razy zaznaczone
        podsw(poleX1, poleY1)


    if play_board[poleX1][poleY1] == 0 and len(clicklocations_full) == 1:
        clicklocations_full.insert(1, (poleX1, poleY1))

        ball_move(clicklocations_full)
        koniec_pods(poleX1, poleY1)
        clicklocations_full.clear()

def podsw(poleX1, poleY1):
    if play_board[poleX1][poleY1] > 0:
        a = play_board[poleX1][poleY1]
        play_board[poleX1][poleY1] = a * 10

def koniec_pods(poleX1, poleY1):
    if play_board[poleX1][poleY1] > 0:
        a = play_board[poleX1][poleY1]
        play_board[poleX1][poleY1] = a / 10

def ball_move(clicklocations_full):
    poleX1 = clicklocations_full[0][0]
    poleY1 = clicklocations_full[0][1]
    poleX2 = clicklocations_full[1][0]
    poleY2 = clicklocations_full[1][1]
    a = play_board[poleX1][poleY1]
    play_board[poleX1][poleY1] = 0
    play_board[poleX2][poleY2] = a

    zbicie = zbicie_5kulek()
    if zbicie == True:
        postaw_3kulki()
    else:
        print("pass")

def can_move():
    pass

postaw_3kulki()
score = 0
clicklocations = []
clicklocations_full = []
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if END is False:

            for clicknumber in range(0, 1):
                if event.type == MOUSEBUTTONDOWN:
                    mouseX, mouseY = event.pos
                    if mouseY > 100:
                        if event.button == 1:
                            poleX = (int((mouseY - 100) / 50))
                            poleY = int(mouseX / 50)
                            clicklocations.insert(0, ([poleX, poleY]))
                            ball_select(clicklocations)


        if END is True:
            pygame.quit()
            quit()
            play_board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0]]
            END = False
        ##Wyświetl jakis napis i zresetuj tarczę

    end_def()

    board.fill(background)
    rysuj_plansze()
    rysuj_kulki()
    draw_base_ball()
    draw_score()
    ball_miss_after_refutation = True

    if zbicie_5kulek() == False:
        score += 1

    pygame.display.update()
