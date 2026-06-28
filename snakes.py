import pygame
import random
import math
import sys
pygame.init()
WIDTH, HEIGHT = 1200, 700
FPS = 144
HEAD_RADIUS = 12
SEGMENT_RADIUS = 10
SEGMENT_DISTANCE = 20
SNAKE_SPEED = 350
BLACK = (15, 15, 15)
GREEN = (0, 255, 120)
DARK_GREEN = (0, 180, 80)
RED = (255, 80, 80)
WHITE = (255, 255, 255)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Smooth Snake")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)
head_x = WIDTH // 2
head_y = HEIGHT // 2

direction_x = 1
direction_y = 0

segments = []

for i in range(12):
    segments.append(
        (
            head_x - i * SEGMENT_DISTANCE,
            head_y
        )
    )

food_x = random.randint(50, WIDTH - 50)
food_y = random.randint(50, HEIGHT - 50)

score = 0
running = True
while running:
    dt = clock.tick(FPS) / 1000
    # EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        direction_x, direction_y = 0, -1
    if keys[pygame.K_DOWN]:
        direction_x, direction_y = 0, 1
    if keys[pygame.K_LEFT]:
        direction_x, direction_y = -1, 0
    if keys[pygame.K_RIGHT]:
        direction_x, direction_y = 1, 0
    # MOVE HEAD
    head_x += direction_x * SNAKE_SPEED * dt
    head_y += direction_y * SNAKE_SPEED * dt
    # WALL COLLISION
    if (
        head_x < 0
        or head_x > WIDTH
        or head_y < 0
        or head_y > HEIGHT
    ):
        print("Game Over")
        print(f"Score:{score}")
        pygame.quit()
        sys.exit()

    # BODY FOLLOWING
    segments.insert(0, (head_x, head_y))

    while len(segments) > (score + 12) * 8:
        segments.pop()

    # FOOD COLLISION
    distance_food = math.hypot(
        head_x - food_x,
        head_y - food_y
    )

    if distance_food < 20:
        score += 1

        food_x = random.randint(50, WIDTH - 50)
        food_y = random.randint(50, HEIGHT - 50)

    # SELF COLLISION
    for part in segments[30::8]:
        d = math.hypot(
            head_x - part[0],
            head_y - part[1])

        if d < 12:
            print("Game Over!")
            print("Score:", score)
            pygame.quit()
            sys.exit()

    # DRAW
    screen.fill(BLACK)

    # FOOD
    pygame.draw.circle(
        screen,
        RED,
        (int(food_x), int(food_y)),
        10
    )

    # BODY
    for i in range(
        len(segments) - 1,
        0,
        -8
    ):
        x, y = segments[i]

        pygame.draw.circle(
            screen,
            DARK_GREEN,
            (int(x), int(y)),
            SEGMENT_RADIUS
        )

    # HEAD
    pygame.draw.circle(
        screen,
        GREEN,
        (int(head_x), int(head_y)),
        HEAD_RADIUS
    )

    # EYES
    pygame.draw.circle(
        screen,
        WHITE,
        (int(head_x - 4), int(head_y - 4)),
        2
    )

    pygame.draw.circle(
        screen,
        WHITE,
        (int(head_x + 4), int(head_y - 4)),
        2
    )

    # SCORE
    score_text = font.render(
        f"Score: {score}",
        True,
        WHITE
    )

    screen.blit(score_text, (15, 15))

    pygame.display.flip()

pygame.quit()