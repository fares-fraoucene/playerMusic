import pygame

pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height ))
pause = False
play = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 


