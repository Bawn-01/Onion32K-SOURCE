from cmath import inf
import pygame, sys, time

from menus import *

pygame.init()

width, height = 700, 500

screen = pygame.display.set_mode((width, height))

white = 255, 255,255

pygame.mixer.music.load(r'music/MAINMENU.ogg')
pygame.mixer.music.play(-1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    menus(screen)


    pygame.display.flip()
    pygame.display.update()
