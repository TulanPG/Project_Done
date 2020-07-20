import pygame
import sys
import random
from pygame.locals import *  # udostępnienie nazw metod z locals

# TODO:
# 1) przesuwanie kulki tylko jak nic nie przeszkadza
# 2) linia przesunięcia kulki
# 3) dzwięki
#4) menu

BLACK = (0, 0, 0)

red = pygame.image.load("red.png")
aqua = pygame.image.load("aqua.png")
green = pygame.image.load("green.png")
grey = pygame.image.load("grey.png")
pink = pygame.image.load("pink.png")
yellow = pygame.image.load("yellow.png")
blue = pygame.image.load("blue.png")
color_list = [0, red, aqua, green, grey, pink, yellow, blue]

#Can be changed 5-10
COL = 9
ROW = 9

SQUARESIZE = 55
width = COL * SQUARESIZE
height = ROW * SQUARESIZE

play_board = [[0 for x in range(COL)] for y in range(ROW)]
play_board_light = [[0 for x in range(COL)] for y in range(ROW)]
where_next = []
balls_list = []

ball_miss_after_refutation = 0
score = 0

clicklocations = []
clicklocations_light = []


class Board(object):
    """
    Plansza do gry. Odpowiada za rysowanie okna gry.
    """

    def __init__(self, width, height):
        """
        Konstruktor planszy do gry. Przygotowuje okienko gry.

        :param width: szerokość w pikselach
        :param height: wysokość w pikselach
        """

        self.surface = pygame.display.set_mode((width, height), 0, 32)
        pygame.display.set_caption('Kulki vol.2 by Tulan')

    def draw(self, *args):
        """
        Rysuje okno gry

        :param args: lista obiektów do narysowania
        """

        self.background = (85, 153, 204)
        self.surface.fill(self.background)
        self.draw_base_ball()
        self.draw_board()
        self.draw_ball_on_board()
        self.draw_score()
        for drawable in args:
            drawable.draw_on(self.surface)

        # dopiero w tym miejscu następuje fatyczne rysowanie
        # w oknie gry, wcześniej tylko ustalaliśmy co i jak ma zostać narysowane

    def draw_board(self):
        background_board = (153, 204, 238)
        pygame.draw.rect(self.surface, background_board, (0, SQUARESIZE*2, width, height))
        for i in range(1, (COL+1)):
            pos = int(width / COL * i)
            # Horizontal
            pygame.draw.line(self.surface, self.background, (0, pos + SQUARESIZE), (width, pos + SQUARESIZE), 2)
            # Vertical line
            pygame.draw.line(self.surface, self.background, (pos, SQUARESIZE*2), (pos, width + SQUARESIZE*2), 2)

    def draw_score(self):
        ## DODAC WYNIK
        global score
        board_score = "Wynik: "
        self.draw_text(board_score + str(score), center=(SQUARESIZE*2, SQUARESIZE), color=BLACK)

    def draw_text(self, text, center, color=(180, 180, 180)):
        """
        Rysuje wskazany tekst we wskazanym miejscu
        """
        pygame.font.init()
        font_path = pygame.font.match_font('arial')
        font = pygame.font.Font(font_path, 48)

        text = font.render(text, True, color)
        rect = text.get_rect()
        rect.center = center
        self.surface.blit(text, rect)

    def lighting(self, location):
        poleX = location[0][0]
        poleY = location[0][1]
        if play_board[poleX][poleY] != 0 and play_board[poleX][poleY] < 10:
            play_board_light[poleX][poleY] = 1

    def end_lighting(self, location, count=0):

        poleX = location[0][0]
        poleY = location[0][1]

        if count == 1:
            play_board_light[poleX][poleY] = 0

        clicklocations_light.insert(0, (poleX, poleY))

        if len(clicklocations_light) == 2:
            if clicklocations_light[0][0] != clicklocations_light[1][0] and clicklocations_light[0][1] != \
                    clicklocations_light[1][1]:
                play_board_light[clicklocations_light[1][0]][clicklocations_light[1][1]] = 0

        if len(clicklocations_light) == 2:
            clicklocations_light.pop(1)

    def draw_ball_on_board(self):
        for i in range(0, COL):
            for j in range(0, COL):

                x = j * SQUARESIZE + (SQUARESIZE/2)
                y = i * SQUARESIZE + (SQUARESIZE*2) + (SQUARESIZE/2)

                # Light

                for k in range(1, (COL-1)):
                    if play_board_light[i][j] == 1:
                        pygame.draw.rect(self.surface, (255, 255, 255), (int(x - ((SQUARESIZE-3)/2)), int(y - ((SQUARESIZE-3)/2)), SQUARESIZE-3, SQUARESIZE-3))

                # Balls

                for k in range(1, (COL-1)):
                    if play_board[i][j] == k:
                        self.surface.blit(pygame.transform.scale(color_list[k], (SQUARESIZE, SQUARESIZE)), (int(x - ((SQUARESIZE-2)/2)), int(y - ((SQUARESIZE-2)/2))))
                for k in range(11, 18):
                    if play_board[i][j] == k:
                        k = k - 10
                        self.surface.blit(pygame.transform.scale(color_list[k], (int(SQUARESIZE*0.4), int(SQUARESIZE*0.4))), (int(x - (SQUARESIZE*0.2)), int(y - (SQUARESIZE*0.2))) )

    def draw_base_ball(self):
        # Wstawia wizualnie kulki na pozycję poglądową
        for k in range(0, 3):
            width_ball = balls_list[k][0]
            height_ball = balls_list[k][1]
            chose_color = balls_list[k][2]
            self.surface.blit(pygame.transform.scale(color_list[chose_color], (SQUARESIZE, SQUARESIZE)), (int(width_ball), int(height_ball)))


class Ball(object):

    def __init__(self):
        """
        Konstruktor planszy do gry. Przygotowuje okienko gry.

        :param width: szerokość w pikselach
        :param height: wysokość w pikselach
        """

    def insert_board_3_ball(self):
        # Wstawia kulki na tablice
        for _ in range(0, 3):
            poleX = where_next[_][0]
            poleY = where_next[_][1]
            ball_color = where_next[_][2]
            while play_board[poleX][poleY] != 0 and play_board[poleX][poleY] < 10:
                poleX = random.randint(0, (COL-1))
                poleY = random.randint(0, (COL-1))
            if play_board[poleX][poleY] == 0 or play_board[poleX][poleY] > 10:
                play_board[poleX][poleY] = ball_color
        ball_miss_after_refutation = 0
        self.insert_base_ball()

    def insert_board_3_ball_visual(self):
        # Pokazuje, małe kulki, gdzie się wstawią
        for _ in range(0, 3):
            poleX = random.randint(0, (COL-1))
            poleY = random.randint(0, (COL-1))
            while play_board[poleX][poleY] != 0:
                poleX = random.randint(0, (COL-1))
                poleY = random.randint(0, (COL-1))
            if play_board[poleX][poleY] == 0:
                where_next.insert(0, [poleX, poleY, balls_list[_][2]])
                play_board[poleX][poleY] = (balls_list[_][2] + 10)

    def insert_base_ball(self):
        # Dodaje 3 kulki do listy, wkłąda je na pozycję bazową (pokazową) -> draw base ball je pokazuje
        for _ in range(8*SQUARESIZE, 5*SQUARESIZE, -SQUARESIZE):
            balls_list.insert(0, (_, int(SQUARESIZE*0.6), random.randint(1, 7)))

        self.insert_board_3_ball_visual()

    def smash_the_balls(self):


        global play_board
        global ball_miss_after_refutation
        global score
        win_board_local = []
        poz = []

        for wining_No in range(1, 8):
            for Column in range(COL):
                if play_board[Column].count(wining_No) >= 5:
                    for place_in_line in range(ROW):
                        if play_board[Column][place_in_line] == wining_No:
                            win_board_local.insert(0, 1)
                            poz.insert(0, (Column, place_in_line))
                            if len(win_board_local) == play_board[Column].count(wining_No):
                                for xx in range((play_board[Column].count(wining_No))):
                                    play_board[poz[xx][0]][poz[xx][1]] = 0
                                    score += 1
                                ball_miss_after_refutation = 1

                        else:
                            win_board_local = []
                            poz = []

        Pole_vertical = list(map(list, zip(*play_board)))
        for wining_No in range(1, 8):
            for Column in range(COL):
                if Pole_vertical[Column].count(wining_No) >= 5:
                    for place_in_line in range(ROW):
                        if Pole_vertical[Column][place_in_line] == wining_No:
                            win_board_local.insert(0, 1)
                            poz.insert(0, (Column, place_in_line))
                            if len(win_board_local) == Pole_vertical[Column].count(wining_No):
                                for xx in range((Pole_vertical[Column].count(wining_No))):
                                    Pole_vertical[poz[xx][0]][poz[xx][1]] = 0
                                    score += 1
                                a = list(map(list, zip(*Pole_vertical)))
                                ball_miss_after_refutation = 1
                                play_board = a

                        else:
                            win_board_local = []
                            poz = []
        ##########TODO: MAKE IT 5+ in row
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
                        ball_miss_after_refutation = 1
                        score += 5

            for poleX in range(0, 5):
                for poleY in range(0, 5):
                    if play_board[poleX][poleY] == i and play_board[poleX + 1][poleY + 1] == i and play_board[poleX + 2][
                        poleY + 2] == i and play_board[poleX + 3][poleY + 3] == i and play_board[poleX + 4][poleY + 4] == i:
                        play_board[poleX][poleY] = 0
                        play_board[poleX + 1][poleY + 1] = 0
                        play_board[poleX + 2][poleY + 2] = 0
                        play_board[poleX + 3][poleY + 3] = 0
                        play_board[poleX + 4][poleY + 4] = 0
                        ball_miss_after_refutation = 1
                        score += 5

    def ball_move(self, clicklocations):
        global ball_miss_after_refutation
        poleX1 = clicklocations[0][0]
        poleY1 = clicklocations[0][1]
        poleX2 = clicklocations[1][0]
        poleY2 = clicklocations[1][1]
        a = play_board[poleX1][poleY1]
        play_board[poleX1][poleY1] = 0
        play_board[poleX2][poleY2] = a
        Board.end_lighting(self, clicklocations, 1)
        Ball.smash_the_balls(self)
        if ball_miss_after_refutation == 0:
            Ball.insert_board_3_ball(self)
        if ball_miss_after_refutation == 1:
            ball_miss_after_refutation = 0


class Kulki(object):
    """
    Łączy wszystkie elementy gry w całość.
    """

    def __init__(self, width, height):
        """
        Przygotowanie ustawień gry
        :param width: szerokość planszy mierzona liczbą komórek
        :param height: wysokość planszy mierzona liczbą komórek
        :param cell_size: bok komórki w pikselach
        """
        pygame.init()

        self.Ball = Ball()
        self.board = Board(width, SQUARESIZE*2 + height)
        # zegar którego użyjemy do kontrolowania szybkości rysowania
        # kolejnych klatek gry
        self.fps_clock = pygame.time.Clock()

    def run(self):
        """
        Główna pętla gry
        """
        strting_balls = 1
        while not self.handle_events():
            # działaj w pętli do momentu otrzymania sygnału do wyjścia

            if strting_balls == 1:
                self.Ball.insert_base_ball()
                strting_balls += 1
            self.board.draw()

            self.fps_clock.tick(30)
            pygame.display.flip()

    def handle_events(self):
        """
        Obsługa zdarzeń systemowych, tutaj zinterpretujemy np. ruchy myszką

        :return True jeżeli pygame przekazał zdarzenie wyjścia z gry
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return True

            if event.type == MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos
                if mouseY > SQUARESIZE*2:
                    if event.button == 1:
                        poleX = (int((mouseY - (SQUARESIZE*2)) / SQUARESIZE))
                        poleY = int(mouseX / SQUARESIZE)
                        if clicklocations == []:
                            self.Ball.insert_board_3_ball()

                        if play_board[poleX][poleY] != 0 and play_board[poleX][poleY] < 10:

                            clicklocations.insert(0, (poleX, poleY))

                            if len(clicklocations) > 1:
                                clicklocations.pop(1)

                            self.board.lighting(clicklocations)
                            self.board.end_lighting(clicklocations)

                        if play_board[poleX][poleY] == 0 or play_board[poleX][poleY] > 10:

                            clicklocations.insert(1, (poleX, poleY))

                            if len(clicklocations) > 1 and play_board[clicklocations[0][0]][clicklocations[0][1]] != 0:
                                self.Ball.ball_move(clicklocations)

                            if len(clicklocations) == 3:
                                clicklocations.pop(2)

                        # print("Tablica:", clicklocations)

                        pygame.display.update()


# Ta część powinna być zawsze na końcu modułu (ten plik jest modułem)
# chcemy uruchomić naszą grę dopiero po tym jak wszystkie klasy zostaną zadeklarowane
if __name__ == "__main__":
    game = Kulki(width, height)
    game.run()
