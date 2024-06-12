import pygame
import sys

# Инициализация Pygame
pygame.init()

# Установка параметров экрана
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# Класс для создания ракетки
class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 100)

    def draw(self):
        pygame.draw.rect(WIN, WHITE, self.rect)

    def move(self, vel):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= vel
        if keys[pygame.K_DOWN] and self.rect.y < HEIGHT - 100:
            self.rect.y += vel


# Класс для создания мяча
class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 10)
        self.vel_x = 7
        self.vel_y = 7

    def draw(self):
        pygame.draw.ellipse(WIN, WHITE, self.rect)

    def move(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Отскок от верхней и нижней стенок
        if self.rect.y <= 0 or self.rect.y >= HEIGHT - 10:
            self.vel_y = -self.vel_y


# Функция для обработки столкновения мяча с ракеткой
def check_collision(ball, paddle):
    if ball.rect.colliderect(paddle.rect):
        ball.vel_x = -ball.vel_x


# Инициализация ракетки и мяча
paddle = Paddle(20, HEIGHT // 2 - 50)
ball = Ball(WIDTH // 2, HEIGHT // 2)


# Основной цикл игры
def main():
    clock = pygame.time.Clock()
    paddle_vel = 5

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        WIN.fill(BLACK)

        paddle.draw()
        ball.draw()

        paddle.move(paddle_vel)
        ball.move()

        check_collision(ball, paddle)

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
    