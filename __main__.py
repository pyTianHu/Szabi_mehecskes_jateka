import pygame as pg
from sys import exit

from random import randint


pg.init()
screen = pg.display.set_mode((800,600))
welcome_caption = pg.display.set_caption('Szabika méhecskés játéka')
clock = pg.time.Clock()

font = pg.font.Font(None,50)

sky_surface = pg.image.load('pics/landscape.png').convert()
ground_surface = pg.image.load('pics/ground.png').convert()
#katica_surface = pg.image.load('pics/katica.png')

bee_x_pos = 100
bee_y_pos = 100

bee_surface = pg.image.load('pics/mehecske.png').convert_alpha()
bee_rect = bee_surface.get_rect(topleft = (bee_x_pos, bee_y_pos))

bee_surface_2 = pg.image.load('pics/mehecske2.png').convert_alpha()
bee_rect_2 = bee_surface_2.get_rect(topleft = (bee_x_pos, bee_y_pos))

flower_surface = pg.image.load('pics/flower.png').convert_alpha()
flower_rect = flower_surface.get_rect(topleft = (randint(50,750), randint(50,550)))

big_flower_surface = pg.image.load('pics/bigflower.png').convert_alpha()
big_flower_surface.set_colorkey('White')
big_flower_rect = big_flower_surface.get_rect(topleft = (randint(50,750), randint(50,550)))

current_bee = True
collided = False
score = 0

is_bigflower = False

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,495))

    if is_bigflower:
        screen.blit(big_flower_surface,big_flower_rect)
    else: 
        screen.blit(flower_surface,flower_rect)
    

    bee_rect.left += 2
    bee_rect_2.left +=2
    if bee_rect.left > 800:
        bee_rect.left = -100
        bee_rect_2.left = -100
    
    key_pressed = pg.key.get_pressed()
    if key_pressed[pg.K_UP]:
        bee_rect.top -=1
        bee_rect_2.top -=1
    if key_pressed[pg.K_DOWN]:
        bee_rect.top +=1
        bee_rect_2.top +=1
    if key_pressed[pg.K_RIGHT]:
        bee_rect.left +=1
        bee_rect_2.left +=1

    if current_bee == True:
        actual_bee = bee_surface
        actual_bee_rect = bee_rect
        current_bee = False
    elif current_bee == False:
        actual_bee = bee_surface_2
        actual_bee_rect = bee_rect_2
        current_bee = True

    screen.blit(actual_bee,actual_bee_rect)

    if actual_bee_rect.colliderect(big_flower_rect if is_bigflower else flower_rect) and not collided:
        collided = True
        
        if is_bigflower:
            score += 2
        else:
            score += 1
            
        if randint(0,10) < 4:
            is_bigflower = True
            big_flower_rect = big_flower_surface.get_rect(topleft = (randint(50,750), randint(50,450)))
            screen.blit(big_flower_surface,big_flower_rect)
        else:
            is_bigflower = False
            flower_rect = flower_surface.get_rect(topleft = (randint(50,750), randint(50,450)))
            screen.blit(flower_surface,flower_rect)
        
        

    if not actual_bee_rect.colliderect(flower_rect) and collided:
        collided = False

    counter_text = font.render(f'Pontszám: {score}', True, 'BLACK')
    screen.blit(counter_text, (20, 20))

    pg.display.update()
    clock.tick(30)