import pygame
import os
pygame.init()
# Инициализация плейлиста
playlist = []
music_folder = "C:\\Users\\HP\\Music"
allmusic = os.listdir(music_folder)
for song in allmusic:
    if song.endswith(".mp3"):
        playlist.append(os.path.join(music_folder, song))
# Окно 
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("My Playlist!")
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
play_img = pygame.image.load(os.path.join("music-elements", "play.png"))
pause_img = pygame.image.load(os.path.join("music-elements", "pause.png"))
nextb = pygame.image.load(os.path.join("music-elements", "next.png"))
prevb = pygame.image.load(os.path.join("music-elements", "back.png"))
# Переменные
index = 0
aplay = False  # Флаг, воспроизводится ли музыка
# Запуск первого трека
if playlist:
    pygame.mixer.music.load(playlist[index])
# Основной цикл
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Пауза/возобновление
                if aplay:
                    pygame.mixer.music.pause()
                    aplay = False
                else:
                    pygame.mixer.music.unpause()
                    aplay = True
            elif event.key == pygame.K_RIGHT:  # Следующий трек
                if playlist:
                    index = (index + 1) % len(playlist)
                    pygame.mixer.music.load(playlist[index])
                    pygame.mixer.music.play()
                    aplay = True
            elif event.key == pygame.K_LEFT:  # Предыдущий трек
                if playlist:
                    index = (index - 1) % len(playlist)
                    pygame.mixer.music.load(playlist[index])
                    pygame.mixer.music.play()
                    aplay = True
            elif event.key == pygame.K_s:  # Остановка трека
                pygame.mixer.music.stop()
                aplay = False
            elif event.key == pygame.K_p:  # Запуск текущего трека заново
                if playlist:
                    pygame.mixer.music.load(playlist[index])
                    pygame.mixer.music.play()
                    aplay = True
    # Название текущего трека
    track_name = os.path.basename(playlist[index]) if playlist else "No music found"
    text2 = font2.render(track_name, True, (20, 20, 50))
    text_width, text_height = text2.get_size()
    text_x = 155 + (500 - text_width) // 2  # Центрируем название трека
    text_y = 520  
    # Заголовок 
    title_text = font_title.render("My Playlist!", True, (255, 255, 255))
    title_x = (800 - title_text.get_width()) // 2  # Центрируем заголовок
    title_y = 50
    # Отображение элементов на экране
    screen.blit(background, (-50, 0))
    screen.blit(bg, (155, 500))
    screen.blit(text2, (text_x, text_y))
    screen.blit(title_text, (title_x, title_y)) 
    # Кнопки
    play_img = pygame.transform.scale(play_img, (70, 70))
    pause_img = pygame.transform.scale(pause_img, (70, 70))
    nextb = pygame.transform.scale(nextb, (70, 70))
    prevb = pygame.transform.scale(prevb, (75, 75))
    # Если музыка играет → показываем "Пауза", иначе "Воспроизведение"
    if aplay:
        screen.blit(pause_img, (370, 590))
    else:
        screen.blit(play_img, (370, 590))
    screen.blit(nextb, (460, 587))
    screen.blit(prevb, (273, 585))
    pygame.display.update()
    clock.tick(24)





