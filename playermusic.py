import pygame
from pygame import mixer
pygame.init()
width = 500
height = 600
screen = pygame.display.set_mode((width, height))
running = True
image_play_pause = pygame.image.load("image/pause-play-button.png").convert()
image_skip_right = pygame.image.load("image/skip.png").convert()
image_skip_left = pygame.image.load("image/skip.png").convert()
sound_plus = pygame.image.load("image/sound+.png")
sound_moins = pygame.image.load("image/sound-.png")
icon_size = (90, 90)
icon_play_pause = pygame.transform.scale(image_play_pause, icon_size)
icon_skip_right = pygame.transform.scale(image_skip_right, icon_size)
rotate_skip_left = pygame.transform.rotate(image_skip_left, 180)
icon_skip_left = pygame.transform.scale(rotate_skip_left, icon_size)
icon_sound_moins = pygame.transform.scale(sound_moins, icon_size)
icon_sound_plus = pygame.transform.scale(sound_plus, icon_size)
pause = False
playlist = ["music/Bambee.mp3", "music/Shinunoga.mp3", "music/The_Return.mp3"] 
current_track = 0  

def play_next_track():
    global current_track
    current_track = current_track + 1
    if current_track >= len(playlist):
        current_track = 0
    mixer.music.load(playlist[current_track])
    mixer.music.play()

def play_previous_track():
    global current_track
    current_track = current_track - 1
    if current_track < 0:
        current_track = len(playlist) - 1
    mixer.music.load(playlist[current_track])
    mixer.music.play()

def increase_volume():
    current_volume = mixer.music.get_volume()
    new_volume = min(1.0, current_volume + 0.1)
    mixer.music.set_volume(new_volume)

def decrease_volume():
    current_volume = mixer.music.get_volume()
    new_volume = max(0.0, current_volume - 0.1)
    mixer.music.set_volume(new_volume)

mixer.music.load(playlist[current_track])
mixer.music.set_volume(0.5)
mixer.music.play()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            mx, my = pygame.mouse.get_pos()
            if 199 < mx < 291 and 499 < my < 591:
                pause = not pause
                if pause:
                    mixer.music.pause()
                else:
                    mixer.music.unpause()
            elif 300 < mx < 400 and 499 < my < 591:
                play_next_track()
            elif 100 < mx < 190 and 499 < my < 591:
                play_previous_track()
            elif 400 < mx < 491 and 500 < my < 591:
                increase_volume()
            elif 0 < mx < 91 and 500 < my < 591:
                decrease_volume()   
    screen.fill((255, 255, 255))
    screen.blit(icon_skip_left, (100, 500))
    screen.blit(icon_play_pause, (200, 500))
    screen.blit(icon_skip_right, (300, 500))
    screen.blit(icon_sound_plus,(400,500))
    screen.blit(icon_sound_moins,(0,500))
    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()
