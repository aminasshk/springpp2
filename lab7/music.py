import pygame
import os
pygame.init()
playlist = []
music_folder = "C:\\Users\\HP\\Music"
allmusic = os.listdir(music_folder)
for song in allmusic:
    if song.endswith(".mp3"):
        playlist.append(os.path.join(music_folder, song))
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("I will watching u")
clock = pygame.time.Clock()
# Загрузка фона
background = pygame.image.load(os.path.join("music-elements", "background.jpg"))
# Фон для кнопок
bg = pygame.Surface((500, 200))
bg.fill((255, 255, 255))
# Шрифты
font2 = pygame.font.SysFont(None, 30)  # Шрифт для названия трека
font_title = pygame.font.SysFont(None, 50)  # Шрифт для заголовка
# Кнопки
playb = pygame.image.load(os.path.join("music-elements", "play.png"))
pausb = pygame.image.load(os.path.join("music-elements", "pause.png"))
nextb = pygame.image.load(os.path.join("music-elements", "next.png"))
prevb = pygame.image.load(os.path.join("music-elements", "back.png"))
index = 0
aplay = False
pygame.mixer.music.load(playlist[index])
pygame.mixer.music.play(1)
aplay = True
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if aplay:
                    aplay = False
                    pygame.mixer.music.pause()
                else:
                    aplay = True
                    pygame.mixer.music.unpause()
            if event.key == pygame.K_RIGHT:
                index = (index + 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()
            if event.key == pygame.K_LEFT:
                index = (index - 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()
    # Название трека
    text2 = font2.render(os.path.basename(playlist[index]), True, (20, 20, 50))
    text_width, text_height = text2.get_size()
    text_x = 155 + (500 - text_width) // 2  # Центрируем название трека
    text_y = 520  
    # Заголовок "I will watching u"
    title_text = font_title.render("I will watching u", True, (255, 255, 255))
    title_x = (800 - title_text.get_width()) // 2  # Центрируем заголовок
    title_y = 50
    screen.blit(background, (-50, 0))
    screen.blit(bg, (155, 500))
    screen.blit(text2, (text_x, text_y))
    screen.blit(title_text, (title_x, title_y)) 
    # Кнопки
    playb = pygame.transform.scale(playb, (70, 70))
    pausb = pygame.transform.scale(pausb, (70, 70))
    nextb = pygame.transform.scale(nextb, (70, 70))
    prevb = pygame.transform.scale(prevb, (75, 75))
    if aplay:
        screen.blit(pausb, (370, 590))
    else:
        screen.blit(playb, (370, 590))
    screen.blit(nextb, (460, 587))
    screen.blit(prevb, (273, 585))
    clock.tick(24)
    pygame.display.update()
