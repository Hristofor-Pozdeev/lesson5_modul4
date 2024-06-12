# Этот код создает игру пинг-понг для 2 игроков на Python с использованием библиотеки Pygame.
# Игроки управляют ракетками с помощью клавиш "W", "S" для первого игрока и стрелок вверх и вниз для второго игрока.
# Мяч никогда не улетает за пределы экрана, а выигрывает игрок, который чаще касался мяча.

import pygame
import random

# Инициализация Pygame
pygame.init()

# Установка размеров экрана
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пинг-понг")

# Цвета
WHITE = (255, 255, 255)

# Константы
PAD_WIDTH, PAD_HEIGHT = 10, 100
BALL_RADIUS = 10
PAD_SPEED = 5
BALL_SPEED = 4

# Класс для создания ракеток
class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, PAD_WIDTH, PAD_HEIGHT)

    def draw(self, win):
        pygame.draw.rect(win, WHITE, self.rect)

# Класс для создания мяча
class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, BALL_RADIUS, BALL_RADIUS)
        self.direction = random.choice([(1, 1), (-1, 1), (1, -1), (-1, -1)])

    def draw(self, win):
        pygame.draw.circle(win, WHITE, (self.x, self.y), BALL_RADIUS)

    def move(self):
        self.x += self.direction[0] * BALL_SPEED
        self.y += self.direction[1] * BALL_SPEED
        self.rect = pygame.Rect(self.x, self.y, BALL_RADIUS, BALL_RADIUS)

# Функция для обновления экрана
def redraw_window(paddle1, paddle2, ball):
    win.fill((0, 0, 0))
    paddle1.draw(win)
    paddle2.draw(win)
    ball.draw(win)
    pygame.display.update()

# Функция для проверки столкновения мяча с ракеткой
def check_collision(paddle, ball):
    return paddle.rect.colliderect(ball.rect)

# Функция для определения победителя
def check_winner(score1, score2):
    if score1 > score2:
        return "Игрок 1"
    elif score2 > score1:
        return "Игрок 2"
    else:
        return "Ничья"

# Создание ракеток
paddle1 = Paddle(50, HEIGHT // 2 - PAD_HEIGHT // 2)
paddle2 = Paddle(WIDTH - 50 - PAD_WIDTH, HEIGHT // 2 - PAD_HEIGHT // 2)

# Создание мяча
ball = Ball(WIDTH // 2, HEIGHT // 2)

# Переменные для подсчета очков
score1 = 0
score2 = 0

# Цикл игры
run = True
clock = pygame.time.Clock()
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # Управление первой ракеткой
    if keys[pygame.K_w] and paddle1.y > 0:
        paddle1.y -= PAD_SPEED
    if keys[pygame.K_s] and paddle1.y < HEIGHT - PAD_HEIGHT:
        paddle1.y += PAD_SPEED

    # Управление второй ракеткой
    if keys[pygame.K_UP] and paddle2.y > 0:
        paddle2.y -= PAD_SPEED
    if keys[pygame.K_DOWN] and paddle2.y < HEIGHT - PAD_HEIGHT:
        paddle2.y += PAD_SPEED

    # Движение мяча
    ball.move()

    # Проверка столкновения мяча с ракетками
    if check_collision(paddle1, ball):
        ball.direction = (-ball.direction[0], ball.direction[1])
    if check_collision(paddle2, ball):
        ball.direction = (-ball.direction[0], ball.direction[1])

    # Проверка выхода мяча за пределы экрана
    if ball.y - BALL_RADIUS <= 0 or ball.y + BALL_RADIUS >= HEIGHT:
        ball.direction = (ball.direction[0], -ball.direction[1])

    # Проверка победителя
    if ball.x - BALL_RADIUS <= 0:
        score2 += 1
        ball = Ball(WIDTH // 2, HEIGHT // 2)
    if ball.x + BALL_RADIUS >= WIDTH:
        score1 += 1
        ball = Ball(WIDTH // 2, HEIGHT // 2)

    # Обновление позиции ракеток
    paddle1.rect.y = paddle1.y
    paddle2.rect.y = paddle2.y

    # Обновление экрана
    redraw_window(paddle1, paddle2, ball)

# Вывод победителя
print(f"Победил {check_winner(score1, score2)}")

pygame.quit()
