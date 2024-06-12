import pygame
import sys

# Инициализация Pygame
pygame.init()

# Установка параметров окна
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Константы для ракеток и мяча
RACKET_WIDTH, RACKET_HEIGHT = 10, 100
BALL_RADIUS = 10
RACKET_SPEED = 5
BALL_SPEED = 5

# Класс для ракетки
class Racket:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, RACKET_WIDTH, RACKET_HEIGHT)

    def draw(self):
        pygame.draw.rect(WIN, WHITE, self.rect)

# Класс для мяча
class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, BALL_RADIUS, BALL_RADIUS)
        self.dx = BALL_SPEED
        self.dy = BALL_SPEED

    def draw(self):
        pygame.draw.ellipse(WIN, WHITE, self.rect)

# Функция для обновления экрана
def draw_window(racket1, racket2, ball):
    WIN.fill(BLACK)
    racket1.draw()
    racket2.draw()
    ball.draw()
    pygame.display.update()

# Функция для обработки движения ракеток
def move_racket(racket, direction):
    if direction == "up" and racket.y > 0:
        racket.y -= RACKET_SPEED
    elif direction == "down" and racket.y < HEIGHT - RACKET_HEIGHT:
        racket.y += RACKET_SPEED
    racket.rect.y = racket.y

# Инициализация ракеток и мяча
racket1 = Racket(20, HEIGHT / 2 - RACKET_HEIGHT / 2)
racket2 = Racket(WIDTH - 30, HEIGHT / 2 - RACKET_HEIGHT / 2)
ball = Ball(WIDTH / 2 - BALL_RADIUS / 2, HEIGHT / 2 - BALL_RADIUS / 2)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        move_racket(racket1, "up")
    if keys[pygame.K_s]:
        move_racket(racket1, "down")

    # Движение второй ракетки
    if ball.rect.y < racket2.y:
        move_racket(racket2, "up")
    elif ball.rect.y > racket2.y + RACKET_HEIGHT:
        move_racket(racket2, "down")

    # Движение мяча
    ball.rect.x += ball.dx
    ball.rect.y += ball.dy

    # Отскок мяча от верхней и нижней границы
    if ball.rect.y <= 0 or ball.rect.y >= HEIGHT - BALL_RADIUS:
        ball.dy = -ball.dy

    # Отскок мяча от ракеток
    if ball.rect.colliderect(racket1.rect) or ball.rect.colliderect(racket2.rect):
        ball.dx = -ball.dx

    # Проверка на проигрыш
    if ball.rect.x < 0 or ball.rect.x > WIDTH:
        ball = Ball(WIDTH / 2 - BALL_RADIUS / 2, HEIGHT / 2 - BALL_RADIUS / 2)

        draw_window(racket1, racket2, ball)
        clock.tick(60)