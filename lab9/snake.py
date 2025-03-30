import pygame, sys, random
from pygame.locals import *
pygame.init()
# Параметры окна
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
# Начальные параметры
SPEED = 15  
SNAKE_WIDTH = 30 
INITIAL_DELAY = 100
food_size = 15  
FONT = pygame.font.Font(None, 36)
drawn = False
# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

class Snake:
    def __init__(self, x, y):
        self.body = [pygame.Rect(x, y, SNAKE_WIDTH, SNAKE_WIDTH)]
        self.food = self.generate_food()
        self.food2 = self.special_food()
        self.dx, self.dy = SPEED, 0
        self.last_level_score = 0
        self.last_dx, self.last_dy = self.dx, self.dy
        self.score = 0
        self.level = 1
        self.delay = INITIAL_DELAY
        self.weight = random.randint(1, 5)
        self.rand_color = (0, 0, self.weight*51)

    def generate_food(self):
        while True:
            # Generates food on random position
            new_rect = pygame.Rect(
                random.randint(0, WIDTH // SPEED - 1) * SPEED-1,
                random.randint(0, HEIGHT // SPEED - 1) * SPEED-1,
                food_size, food_size
            )
            # Checks if food is not created on snakes body
            if all(not segment.colliderect(new_rect) for segment in self.body):
                return new_rect
    
    def special_food(self):
        while True:    
            spec_rect = pygame.Rect(
                random.randint(0, WIDTH // SPEED - 1) * SPEED-1,
                random.randint(0, HEIGHT // SPEED - 1) * SPEED-1,
                food_size, food_size
            )
            # Проверяем, чтобы не совпадало с обычной едой
            if all(not segment.colliderect(spec_rect) for segment in self.body) and not spec_rect.colliderect(self.food):
                return spec_rect

    def update(self):
        new_head = self.body[0].copy()
        new_head.move_ip(self.dx, self.dy)
        # Checks if head didn't collided with border
        if new_head.left < 0 or new_head.right > WIDTH or new_head.top < 0 or new_head.bottom > HEIGHT:
            pygame.quit()
            sys.exit()
        # Checks if it didnt collided with itself
        if new_head in self.body:
            pygame.quit()
            sys.exit()
        self.body.insert(0, new_head)
        # Если не ел то уменьшает хвост если ел то нет
        eaten = False

        global drawn
        if new_head.colliderect(self.food2):
            self.food2 = self.special_food()
            self.score += 8
            drawn = False
            eaten = True
        if new_head.colliderect(self.food):
            self.food = self.generate_food()
            self.score += self.weight
            self.weight = random.randint(1, 5)
            self.rand_color = (0, 0, self.weight*51)
            eaten = True
        if not eaten:
            self.body.pop()
        # Уровень увеличивается каждые 3 еду
        if self.score - self.last_level_score >= 5:
            self.level += 1
            self.last_level_score = self.score  # Запоминаем, на каком счёте повысился уровень
            self.delay = max(50, self.delay - 20)
        self.last_dx, self.last_dy = self.dx, self.dy
    def change_direction(self, dx, dy):
        if (dx, dy) != (-self.last_dx, -self.last_dy):
            self.dx, self.dy = dx, dy
    def draw(self, surface):
        global drawn
        for segment in self.body:
            pygame.draw.rect(surface, RED, segment)
        pygame.draw.rect(surface, self.rand_color, self.food)
        if drawn:
            pygame.draw.rect(surface, YELLOW, self.food2)
        # Отображение счета и уровня
        score_text = FONT.render(f"Score: {self.score}  Level: {self.level}", True, BLACK)
        surface.blit(score_text, (10, 10))




# Создаем объект змейки
player = Snake(200, 200)
# New event
PERM_FOOD = pygame.USEREVENT + 1
pygame.time.set_timer(PERM_FOOD, 6000)


while True:
    pygame.time.delay(player.delay)

    for event in pygame.event.get():
        if event.type == PERM_FOOD:
            if drawn:
                drawn = False
            else:
                drawn = True
                player.food2 = player.special_food()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Управление направлением
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        player.change_direction(-SPEED, 0)
    if keys[K_RIGHT]:
        player.change_direction(SPEED, 0)
    if keys[K_UP]:
        player.change_direction(0, -SPEED)
    if keys[K_DOWN]:
        player.change_direction(0, SPEED)

    # Обновление положения змейки
    player.update()

    # Отрисовка
    screen.fill(WHITE)
    player.draw(screen)
    pygame.display.flip()

pygame.quit()
