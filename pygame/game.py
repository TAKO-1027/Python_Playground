# framework
import pygame
import time
import random


class Point:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def copy(self):
        return Point(row=self.row, col=self.col)


# init window
pygame.init()
W = 800
H = 600
ROW = 30
COL = 40
size = (W, H)
CELL_WIDTH = W/COL
CELL_HEIGHT = H/ROW
window = pygame.display.set_mode(size)
pygame.display.set_caption('TAKO_Snake')

bg_color = (255, 255, 255)
head = Point(row=ROW//2, col=COL//2)
head_color = (123, 0, 218)
body_color = (128, 128, 128)
food = Point(random.randint(0, ROW-1), random.randint(0, COL-1))
food_color = (0, 228, 23)

snake_body = [
    Point(row=head.row, col=head.col+1),
    Point(row=head.row, col=head.col+2),
    Point(row=head.row, col=head.col+2)
]


direct = "left"


def plot(point, color):
    left = point.col*CELL_WIDTH
    top = point.row*CELL_HEIGHT
    pygame.draw.rect(window, color, (left, top, CELL_WIDTH, CELL_HEIGHT))


def food_gen():
    while 1:
        pos = Point(random.randint(0, ROW-1), random.randint(0, COL-1))

        is_coll = False

        if head.row == pos.row and head.col == pos.col:
            is_coll = True

        for body in snake_body:
            if body.row == pos.row and body.col == pos.col:
                is_coll = True
                break

        if not is_coll:
            break
    return pos

# game loop
quit_game = False
clock = pygame.time.Clock()
# set fps
clock.tick(10)

while not quit_game:
    # event list
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True
        elif event.type == pygame.KEYDOWN:
            if event.key == 273 or event.key == 119:
                if direct == "left" or direct == "right":
                    direct = "up"
            elif event.key == 274 or event.key == 115:
                if direct == "left" or direct == "right":
                    direct = "down"
            elif event.key == 276 or event.key == 97:
                if direct == "up" or direct == "down":
                    direct = "left"
            elif event.key == 275 or event.key == 100:
                if direct == "up" or direct == "down":
                    direct = "right"

    if direct == 'up':
        head.row -= 1
    elif direct == 'down':
        head.row += 1
    elif direct == 'left':
        head.col -= 1
    elif direct == 'right':
        head.col += 1

    dead = False
    if head.col < 0 or head.row < 0 or head.col >= COL or head.row >= ROW:
        dead = True

    for body in snake_body:
        if head.col == body.col and head.row == body.row:
            dead = True
            break

    if dead:
        print("Busted")
        quit_game = True

    eat = head.row == food.row and head.col == food.col

    if eat:
        food = food_gen()

    snake_body.insert(0, head.copy())
    if not eat:
        snake_body.pop()


    #
    pygame.draw.rect(window, (255, 255, 255), (0, 0, W, H))

    # plot snake
    for body in snake_body:
        plot(body, body_color)
    plot(head, head_color)
    plot(food, food_color)

    #
    pygame.display.flip()


