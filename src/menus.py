import pygame, time

freeplayA = pygame.image.load('images/UI_sprite_0.png')
freeplayA = pygame.transform.scale(freeplayA, (100, 50))
freeplayB = pygame.image.load('images/UI_sprite_1.png')
freeplayB = pygame.transform.scale(freeplayB, (100, 50))
menusBG = pygame.image.load('images/ONIONMENK.png')
optionsA = pygame.image.load('images/UI_sprite_2.png')
optionsA = pygame.transform.scale(optionsA, (100, 50))
optionsB = pygame.image.load('images/UI_sprite_3.png')
optionsB = pygame.transform.scale(optionsB, (100, 50))
creditsA = pygame.image.load('images/UI_sprite_4.png')
creditsA = pygame.transform.scale(creditsA, (100, 50))
creditsB = pygame.image.load('images/UI_sprite_5.png')
creditsB = pygame.transform.scale(creditsB, (100, 50))

cur_selection = 'freeplay'

def menus(screen):

    global cur_selection
    cur_sel = 1
    keys = pygame.key.get_pressed()

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        if cur_selection == 'freeplay':
            cur_selection = 'options'
            cur_sel = 2
        elif cur_selection == 'options':
            cur_selection = 'credits'
            cur_sel = 3
        elif cur_selection == 'credits':
            cur_selection = 'freeplay'
            cur_sel = 1
    elif keys[pygame.K_UP] or keys[pygame.K_w]:
        if cur_selection == 'freeplay':
            cur_sel = 3
            cur_selection = 'credits'
        elif cur_selection == 'options':
            cur_sel = 1
            cur_selection = 'freeplay'
        elif cur_selection == 'credits':
            cur_sel = 2
            cur_selection = 'options'


    time.sleep(0.1)

    screen.blit(menusBG, (0, 0))
    if cur_selection != 'freeplay':
        screen.blit(freeplayA, (0, 0))
    else: screen.blit(freeplayB, (0, 0))

    if cur_selection != 'options':
        screen.blit(optionsA, (0, 50))
    else: screen.blit(optionsB, (0, 50))

    if cur_selection != 'credits':
        screen.blit(creditsA, (0, 100))
    else: screen.blit(creditsB, (0, 100))


