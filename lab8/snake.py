import pygame
from random import randint
pygame.init()
# Размеры экрана
WIDTH = 720
HEIGHT = 720
# Создаем экран
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Определение цветов
colorWHITE = (255, 255, 255)
colorGRAY = (70, 70, 70)
colorBLACK = (0, 0, 0)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorYELLOW = (255, 255, 0)
# Начальная скорость игры
FPS = 3
clock = pygame.time.Clock()
# Размер клетки
CELL = 60
# Класс точки на поле
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # Генерация случайной точки на поле, исключая стены
    @staticmethod
    def generate():
        return Point(randint(1, (WIDTH // CELL) - 2) * CELL, randint(1, (HEIGHT // CELL) - 2) * CELL)
# Класс змейки
class Snake:
    def __init__(self):
        self.body = [Point.generate()]
        self.dx = 0
        self.dy = 0
        self.alive = True
    def move(self):
        if not self.alive:
            return
        # Двигаем тело змейки
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        # Двигаем голову змейки
        head = self.body[0]
        head.x += self.dx * CELL
        head.y += self.dy * CELL
        # Проверка столкновения со стенами
        if head.x >= WIDTH - CELL or head.x < CELL or head.y >= HEIGHT - CELL or head.y < CELL:
            self.alive = False
        # Проверка на столкновение с самим собой
        for segment in self.body[1:]:
            if head.x == segment.x and head.y == segment.y:
                self.alive = False
    def check_collision(self, food):
        """Проверяет, съела ли змейка еду"""
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.body.append(Point(head.x, head.y))
            return True
        return False
    def draw(self):
        """Отрисовывает змейку"""
        if not self.alive:
            return
        pygame.draw.rect(screen, colorRED, (self.body[0].x, self.body[0].y, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x, segment.y, CELL, CELL))
# Класс еды
class Food:
    def __init__(self):
        self.pos = Point.generate()
    def draw(self):
        """Отрисовывает еду"""
        pygame.draw.rect(screen, colorGREEN, (self.pos.x, self.pos.y, CELL, CELL))
    def regenerate(self, snake):
        """Создает новую еду, избегая змейки"""
        while True:
            new_pos = Point.generate()
            if all(new_pos.x != segment.x or new_pos.y != segment.y for segment in snake.body):
                self.pos = new_pos
                break
# Функция для отрисовки сетки
def draw_grid():
    for i in range(0, HEIGHT, CELL):
        for j in range(0, WIDTH, CELL):
            pygame.draw.rect(screen, colorGRAY, (i, j, CELL, CELL), 1)
# Инициализация змейки, еды, счета и уровня
snake = Snake()
food = Food()
score = 0
level = 1
# Главный цикл игры
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.dy == 0:
                snake.dx = 0
                snake.dy = -1
            if event.key == pygame.K_DOWN and snake.dy == 0:
                snake.dx = 0
                snake.dy = 1
            if event.key == pygame.K_RIGHT and snake.dx == 0:
                snake.dx = 1
                snake.dy = 0
            if event.key == pygame.K_LEFT and snake.dx == 0:
                snake.dx = -1
                snake.dy = 0
    screen.fill(colorBLACK)
    if snake.alive:
        snake.move()
        if snake.check_collision(food):
            food.regenerate(snake)
            score += 1
            # Увеличение уровня каждые 3 очка
            if score % 3 == 0:
                level += 1
                FPS += 2  # Ускоряем игру
    else:
        font = pygame.font.SysFont("Verdana", 50)
        game_over_text = font.render("Game Over", True, colorWHITE)
        screen.blit(game_over_text, (WIDTH // 3, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.delay(2000)
        done = True
    snake.draw()
    food.draw()
    draw_grid()
    # Отображение счета и уровня
    font = pygame.font.SysFont("Verdana", 20)
    score_text = font.render(f"Score: {score}", True, colorWHITE)
    level_text = font.render(f"Level: {level}", True, colorWHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))
    pygame.display.flip()
    clock.tick(FPS)
    
pygame.quit()

