import pygame

pygame.init()
icon_32pix = pygame.image.load("tulan_logo2.png")
pygame.display.set_icon(icon_32pix)
pygame.display.set_caption("Pong by Tulan")
font = pygame.font.SysFont("freesansbold.ttf", 80)
height = 600
width = 800
screen = pygame.display.set_mode((width, height))
white = (230, 230, 230)
black = (0, 0, 0)

#padle
y_a = int(height / 2 - 50)
y_b = int(height / 2 - 50)
y_a_change = 0
y_b_change = 0
#score
score_a = 0
score_b = 0
#ball
x_ball = int(width / 2)
y_ball = int(height / 2)
x_ball_speed = 7
y_ball_speed = 7


def pong(x, y):

    global y_a, y_b
    # Padle
    y_a += y_a_change
    if y_a > 505:
        y_a = 500
    if y_a < -10:
        y_a = 0
    y_b += y_b_change
    if y_b > 505:
        y_b = 500
    if y_b < -10:
        y_b = 0

    pygame.draw.rect(screen, white, (x, y, 20, 100))


def ball():
    global score_a, score_b, x_ball, y_ball, x_ball_speed, y_ball_speed

    if int(width - 20) > x_ball > int(width - 40):
        if (y_a) < y_ball < (y_a + 100):
            x_ball_speed *= -1

    if 20 < x_ball < 40:
        if (y_b) < y_ball < (y_b + 100):
            x_ball_speed *= -1
        pass
    # Left/right
    x_ball += x_ball_speed
    if x_ball > width:
        score_a += 1
        x_ball = int(width / 2)
        y_ball = int(height / 2)
        x_ball_speed *= -1
        x_ball += (2 * x_ball_speed)

    if x_ball < 0:
        score_b += 1
        x_ball = int(width / 2)
        y_ball = int(height / 2)
        x_ball_speed *= -1
        x_ball += (2 * x_ball_speed)

    # Up/Down
    y_ball += y_ball_speed
    if y_ball > height:
        y_ball = height
        y_ball_speed *= -1
        y_ball += (2 * y_ball_speed)

    if y_ball < 0:
        y_ball = 0
        y_ball_speed *= -1
        y_ball += (2 * y_ball_speed)

    pygame.draw.circle(screen, white, (x_ball, y_ball), 10)


def score():
    score_render_a = font.render(str(score_a), 1, white)
    score_render_b = font.render(str(score_b), 1, white)
    screen.blit(score_render_a, (int(width / 4), 100))
    screen.blit(score_render_b, (int(3 * width / 4), 100))


run = True
while run:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_a_change -= 3

            if event.key == pygame.K_DOWN:
                y_a_change += 3

            if event.key == pygame.K_w:
                y_b_change -= 3

            if event.key == pygame.K_s:
                y_b_change += 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_a_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                y_b_change = 0



    #print(y_a, y_b, y_ball)
    score()
    pong(int(width - 40), int(y_a))
    pong(20, int(y_b))
    ball()
    pygame.draw.rect(screen, white, (int(width / 2), 0, 1, height))
    pygame.display.update()
    pygame.time.Clock().tick(30)
