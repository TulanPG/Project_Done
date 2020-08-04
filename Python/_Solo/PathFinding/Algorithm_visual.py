import pygame
import math
import time

pygame.init()
icon_32pix = pygame.image.load("tulan_logo2.png")
WIDTH = 800
screen = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_icon(icon_32pix)
pygame.display.set_caption("PathFinder by Tulan")
Algorithm = "Dijkstra's"
total_time = ['']
total_time_end = False
start_algorythm = False
font = pygame.font.SysFont("freesansbold.ttf", 32)

RED = (255, 0, 0)
green = (0, 255, 0)
bright_green = (0, 255, 0)
BLUE = (86, 210, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == green

    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == TURQUOISE

    def reset(self):
        self.color = WHITE

    def make_start(self):
        self.color = ORANGE

    def make_closed(self):
        if self.color != ORANGE:
            self.color = RED

    def make_open(self):
        if self.color != ORANGE:
            if self.color != TURQUOISE:
                self.color = green

    def make_barrier(self):
        self.color = BLACK

    def make_end(self):

        self.color = TURQUOISE

    def make_path(self):
        if self.color != ORANGE:
            if self.color != TURQUOISE:
                self.color = PURPLE

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():  # DOWN
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():  # UP
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():  # RIGHT
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():  # LEFT
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False


def timer(starttime, totaltime=0):
    if totaltime == 0:
        timer = round((time.time() - starttime), 2)
        counting_text = font.render(str(timer), 1, (0, 0, 0))
        counting_rect = (600, 70)
        screen.blit(counting_text, counting_rect)
        pygame.display.update()
        total_time[0] = timer
    else:
        counting_text = font.render(str(totaltime), 1, (0, 0, 0))
        counting_rect = (600, 70)
        screen.blit(counting_text, counting_rect)


def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        global total_time_end
        total_time_end = True

        draw()
        print("reconstructed_path")


def make_grid(rows, width):
    board = []
    gap = width // rows
    for i in range(rows):
        board.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            board[i].append(spot)

    return board


def draw_board(screen, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(screen, BLUE, (0, i * gap + 192), (width, i * gap + 192))
        for j in range(rows):
            pygame.draw.line(screen, BLUE, ((j * gap), 192), (j * gap, width))


def text_objects(text, font):
    textsurface = font.render(text, True, BLACK)
    return textsurface, textsurface.get_rect()


def button(msg, x, y, w, h, ic, ac, action=None):
    # TODO: Podświetlenie
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action is not None:
            global Algorithm

            # Starting button
            if action == "Dijkstra's":
                Algorithm = "Dijkstra's"
            elif action == "A* Search":
                Algorithm = "A* Search"
            elif action == "Breadth-first":
                Algorithm = "Breadth-first"
            """
            elif action == "Greedy BFS":
                Algorithm = "Greedy BFS"
            elif action == "Swarm":
                Algorithm = "Swarm"
            elif action == "Depth-first":
                Algorithm = "Depth-first"
            elif action == "Bidirectional":
                Algorithm = "Bidirectional"
            elif action == "Convergent":
                Algorithm = "Convergent"
            """

    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))
    smalltext = pygame.font.Font('freesansbold.ttf', 20)
    textsurf, textrect = text_objects(msg, smalltext)
    textrect.center = (int(x + (w / 2)), int(y + (h / 2)))
    screen.blit(textsurf, textrect)


def draw(screen, grid, rows, width):
    screen.fill(WHITE)

    for row in grid:
        for spot in row:
            spot.draw(screen)

    draw_board(screen, rows, width)
    pygame.draw.rect(screen, WHITE, (0, 0, 800, 192))
    counting_text1 = font.render("For start: press SPACE", 1, (0, 0, 0))
    counting_rect1 = (550, 10)
    screen.blit(counting_text1, counting_rect1)
    counting_text2 = font.render("For restart: press 'c'", 1, (0, 0, 0))
    counting_rect2 = (550, 30)
    screen.blit(counting_text2, counting_rect2)
    counting_text = font.render("Time:", 1, (0, 0, 0))
    counting_rect = (600, 50)
    screen.blit(counting_text, counting_rect)
    counting_text3 = font.render("Algorith chosed:", 1, (0, 0, 0))
    counting_rect3 = (10, 10)
    screen.blit(counting_text3, counting_rect3)
    counting_text4 = font.render(Algorithm, 1, (0, 0, 0))
    counting_rect4 = (10, 30)
    screen.blit(counting_text4, counting_rect4)
    x = 130
    y = 40
    button("Dijkstra's", 10, 20 + y, x, y, green, bright_green, "Dijkstra's")
    button("A* Search", 10, 30 + 2 * y, x, y, green, bright_green, "A* Search")
    button("Breadth-first", 20 + x, 20 + y, x, y, green, bright_green, "Breadth-first")
    button("Depth-first", 20 + x, 30 + 2 * y, x, y, green, bright_green, "Depth-first")
    button("Swarm", 30 + 2 * x, 20 + y, x, y, green, bright_green, "Swarm")
    button("Bidirectional", 30 + 2 * x, 30 + 2 * y, x, y, green, bright_green, "Bidirectional")
    button("Convergent", 40 + 3 * x, 20 + y, x, y, green, bright_green, "Convergent")
    button("Greedy BFS", 40 + 3 * x, 30 + 2 * y, x, y, green, bright_green, "Greedy BFS")

    if total_time_end:
        timer(0, total_time[0])
    pygame.display.update()


def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col


def algorithm_Breadth_First_Search(draw, grid, start, end):
    import queue  # Only different from A* algorithm
    # Same as Dijkstra cause of construct neighbors
    tracking = queue.Queue()
    tracking.put(start)
    came_from = {}

    while not tracking.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        current = tracking.get()

        if current == end:
            # TODO: do proper reconstruct (dont want to end, cause of loop)
            reconstruct_path(came_from, end, draw)

            return True

        for neighbors in current.neighbors:
            if neighbors not in came_from:
                neighbors.make_open()
                tracking.put(neighbors)
                came_from[neighbors] = current

        if current != start:
            current.make_closed()

        timer(start_time_var)
        draw()

    return False


def algorithm_Dijkstra(draw, grid, start, end):
    # Based at TechWithTim algorithm
    import queue  # Only different from A* algorithm

    count = 0
    g_score = {spot: float("inf") for row in grid for spot in row}  # Infinity made
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.get_pos(), end.get_pos())
    came_from = {}
    open_set = queue.Queue()
    open_set.put((0, count, start))

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)

            return True

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()
        timer(start_time_var)
        draw()

        if current != start:
            current.make_closed()
    return False


def algorithm_A_STAR(draw, grid, start, end):
    # Based at TechWithTim algorithm
    from queue import PriorityQueue
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {spot: float("inf") for row in grid for spot in row}  # Infinity made
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)

            return True

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())

                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()
        timer(start_time_var)
        draw()

        if current != start:
            current.make_closed()

    return False


def main(screen, width, algorithm):
    ROWS = 50  # Normal 50
    board = make_grid(ROWS, width)

    start = None
    end = None

    run = True
    while run:
        draw(screen, board, ROWS, width)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # Top visualisation place
            for row in range(50):
                for col in range(12):
                    spot = board[row][col]
                    spot.make_barrier()

            if pygame.mouse.get_pressed()[0]:  # LEFT
                pos = pygame.mouse.get_pos()
                x_pos = pos[1]
                if x_pos > 192:
                    row, col = get_clicked_pos(pos, ROWS, width)
                    spot = board[row][col]
                    if not start and spot != end:
                        start = spot
                        start.make_start()

                    elif not end and spot != start:
                        end = spot
                        end.make_end()

                    elif spot != end and spot != start:
                        spot.make_barrier()

            elif pygame.mouse.get_pressed()[2]:  # RIGHT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = board[row][col]
                spot.reset()
                if spot == start:
                    start = None
                elif spot == end:
                    end = None
            # if start and end and start_algorythm:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:

                    global start_time_var
                    start_time_var = time.time()

                    for row in board:
                        for spot in row:
                            spot.update_neighbors(board)

                    """ 
                    TODO:
                    elif action == "Greedy BFS":
                    elif action == "Swarm":
                    elif action == "Depth-first":
                    elif action == "Bidirectional":
                    elif action == "Convergent":
                    """
                    if Algorithm == "A* Search":
                        algorithm_A_STAR(lambda: draw(screen, board, ROWS, width), board, start, end)
                    elif Algorithm == "Dijkstra's":
                        algorithm_Dijkstra(lambda: draw(screen, board, ROWS, width), board, start, end)
                    elif Algorithm == "Breadth-first":
                        algorithm_Breadth_First_Search(lambda: draw(screen, board, ROWS, width), board, start, end)

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    board = make_grid(ROWS, width)
                    total_time[0] = ''

    pygame.quit()


main(screen, WIDTH, Algorithm)
