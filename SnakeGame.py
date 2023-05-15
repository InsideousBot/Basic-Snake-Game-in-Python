import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Set screen dimensions and create the screen
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Set colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set game speed
clock = pygame.time.Clock()
SPEED = 10

snake_pos = [[100, 50], [90, 50], [80, 50]]
snake_speed = [10, 0]

food_pos = [random.randrange(1, WIDTH//10) * 10, random.randrange(1, HEIGHT//10) * 10]
food_spawn = True

def game_over():
    font = pygame.font.SysFont("monospace", 35)
    text = font.render("Game Over! Press Q to Quit", True, WHITE)
    screen.blit(text, (WIDTH // 2 - 200, HEIGHT // 2))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        keys = pygame.key.get_pressed()
        for key in keys:
            if keys[pygame.K_UP]:
                snake_speed = [0, -10]
            if keys[pygame.K_DOWN]:
                snake_speed = [0, 10]
            if keys[pygame.K_LEFT]:
                snake_speed = [-10, 0]
            if keys[pygame.K_RIGHT]:
                snake_speed = [10, 0]

    snake_pos[0][0] += snake_speed[0]
    snake_pos[0][1] += snake_speed[1]

    # Game Over conditions
    if snake_pos[0][0] < 0 or snake_pos[0][0] >= WIDTH or snake_pos[0][1] < 0 or snake_pos[0][1] >= HEIGHT:
        game_over()
    for block in snake_pos[1:]:
        if snake_pos[0] == block:
            game_over()

    screen.fill((0, 0, 0))

    for pos in snake_pos:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

    if not food_spawn:
        food_pos = [random.randrange(1, WIDTH // 10) * 10, random.randrange(1, HEIGHT // 10) * 10]
    food_spawn = False

    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    if snake_pos[0] == food_pos:
        food_spawn = True
        snake_pos.append([0, 0])

    snake_pos = [snake_pos[0]] + [[pos[0] + spd[0], pos[1] + spd[1]] for pos, spd in zip(snake_pos[1:], snake_speed)]

    pygame.display.flip()
    clock.tick(SPEED)
