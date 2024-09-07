import pygame
import random
import time

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Поймай  снежинку")
icon = pygame.image.load("img/content_7.jpg")
pygame.display.set_icon(icon)

target_image = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

font = pygame.font.Font(None, 36)
score = 0
game_time = 30

def show_start_screen():
    screen.fill((0, 0, 0))
    title_text = font.render("Добро пожаловать в Игру Поймай снежинку!", True, (255, 255, 255))
    instruction_text = font.render("Нажмите любую клавишу для начала", True, (255, 255, 255))
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 3))
    screen.blit(instruction_text, (SCREEN_WIDTH // 2 - instruction_text.get_width() // 2, SCREEN_HEIGHT // 2))
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN:
                waiting = False
                return True

def show_game_over_screen(score):
    screen.fill((0, 0, 0))
    game_over_text = font.render("Игра окончена!", True, (255, 255, 255))
    score_text = font.render(f"Ваш счет: {score}", True, (255, 255, 255))
    restart_text = font.render("Нажмите любую клавишу для выхода", True, (255, 255, 255))
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 3))
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2))
    screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 1.5))
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                waiting = False
                pygame.quit()
                return

running = show_start_screen()
if not running:
    exit()

# Создаем список для хранения мишеней
targets = [{
    'x': random.randint(0, SCREEN_WIDTH - target_width),
    'y': random.randint(0, SCREEN_HEIGHT - target_height),
    'speed_x': 0.5,
    'speed_y': 0.5
}]

start_time = time.time()

while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for target in targets:
                if target['x'] < mouse_x < target['x'] + target_width and target['y'] < mouse_y < target['y'] + target_height:
                    score += 1
                    new_target = {
                        'x': random.randint(0, SCREEN_WIDTH - target_width),
                        'y': random.randint(0, SCREEN_HEIGHT - target_height),
                        'speed_x': 0.5,
                        'speed_y': 0.5
                    }
                    targets.append(new_target)
                    target['x'] = random.randint(0, SCREEN_WIDTH - target_width)
                    target['y'] = random.randint(0, SCREEN_HEIGHT - target_height)

    for target in targets:
        target['x'] += target['speed_x']
        target['y'] += target['speed_y']

        if target['x'] <= 0 or target['x'] >= SCREEN_WIDTH - target_width:
            target['speed_x'] = -target['speed_x']
        if target['y'] <= 0 or target['y'] >= SCREEN_HEIGHT - target_height:
            target['speed_y'] = -target['speed_y']

    elapsed_time = time.time() - start_time
    remaining_time = max(0, game_time - int(elapsed_time))

    if remaining_time == 0:
        running = False

    score_text = font.render(f"Счет: {score}", True, (255, 255, 255))
    time_text = font.render(f"Время: {remaining_time}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(time_text, (10, 50))

    for target in targets:
        screen.blit(target_image, (target['x'], target['y']))

    pygame.display.update()

show_game_over_screen(score)