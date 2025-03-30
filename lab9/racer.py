# Импорт библиотек
import pygame, sys
from pygame.locals import *
import random, time
pygame.init()
# FPS
FPS = 60
FramePerSec = pygame.time.Clock()
# Определение цветов
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# Переменные программы
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 3
SCORE = 0
COINS = 0
# Настройки шрифтов
font = pygame.font.SysFont("Verdana", 20)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
# Загрузка фона
background = pygame.image.load("AnimatedStreet.png")
background_y = 0  # Переменная для анимации дороги
# Загрузка звуков
pygame.mixer.music.load("background.wav")
pygame.mixer.music.play(-1)  # Бесконечное воспроизведение фоновой музыки
dead_sound = pygame.mixer.Sound("crash.wav")  # Звук аварии
# Создание окна
screen = pygame.display.set_mode((400, 600))
screen.fill(WHITE)
pygame.display.set_caption("Racer")
# Класс врага
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
# Класс монеты
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        if self.rect.top > 0 and pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if self.rect.bottom < SCREEN_HEIGHT and pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
# Создание спрайтов
P1 = Player()
E1 = Enemy()
C1 = Coin()
# Группы спрайтов
enemies = pygame.sprite.Group()
enemies.add(E1)
coinss = pygame.sprite.Group()
coinss.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
# Добавление нового пользовательского события
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
# Основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.1
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Проверка столкновения игрока с врагом
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.music.stop()
        dead_sound.play()  # Воспроизведение звука аварии
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Прокрутка фона (движение дороги)
    background_y += SPEED
    if background_y >= SCREEN_HEIGHT:
        background_y = 0
    screen.blit(background, (0, background_y - SCREEN_HEIGHT))
    screen.blit(background, (0, background_y))
    # Отображение очков
    scores = font_small.render("SCORE: " + str(SCORE), True, BLACK)
    screen.blit(scores, (10, 10))
    # Отображение количества монет
    coins = font_small.render("COINS: " + str(COINS), True, BLACK)
    screen.blit(coins, (SCREEN_WIDTH - 120, 10))
    # Движение и перерисовка всех спрайтов
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()
    # Проверка сбора монеты
    if pygame.sprite.spritecollideany(P1, coinss):
        COINS += 1
        C1.rect.top = 0
        C1.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    pygame.display.update()
    FramePerSec.tick(FPS)
