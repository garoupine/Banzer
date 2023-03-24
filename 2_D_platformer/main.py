import pygame
import os
pygame.font.init()
pygame.mixer.init()

from pygame import image
from pygame import transform
from pygame.transform import rotate
from pygame.version import PygameVersion

#const variables
WIDH ,HEIGHT = 900,500
WHITE = (255,255,255)
RED = (255,0,0)
YELLOW = (255,255,0)
BLACK = (0,0,0)
FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
SPACE_SHIP_WIDH,SPACE_SHIP_HEIGHT = 50,40
#events
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2


#display_objects_init
WIN = pygame.display.set_mode((WIDH ,HEIGHT))
BORDER = pygame.Rect(WIDH//2 -5,0,10,HEIGHT)
HEALTH_FONT = pygame.font.SysFont('comicsans',40)
WINNER_FONT = pygame.font.SysFont('conicsans',100)
pygame.display.set_caption("YAY!!")
SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets','space.png')),(WIDH,HEIGHT))
YELLOW_SPACESHIP_IMAG = pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAG,(SPACE_SHIP_WIDH,SPACE_SHIP_HEIGHT )),90)
RED_SPACESHIP_IMAG = pygame.image.load(os.path.join('Assets','spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAG,(SPACE_SHIP_WIDH,SPACE_SHIP_HEIGHT )),270)


#soud_effects_init
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets','Grenade+1.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets','Gun+Silencer.mp3'))

def yellow_mouv(keys_pressed,yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: #left
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x: #right 
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: #up
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT -10: #down can be adjutsed 
        yellow.y += VEL

def red_mouv(keys_pressed,red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width: #left
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT]and red.x + VEL +red.width < WIDH: #right 
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL >0: #up
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN]and red.y + VEL +red.height < HEIGHT-10: #down
        red.y += VEL


def handle_bullets(yellow_bullets,red_bullets,yellow,red):
    for bullet in yellow_bullets:
        bullet.x +=BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDH:  
            yellow_bullets.remove(bullet)      
    for bullet in red_bullets:
        bullet.x -=BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)


def draw_window(red,yellow,red_bullets,yellow_bullets,red_hp,yellow_hp):
    #WIN.fill(WHITE)
    WIN.blit(SPACE,(0,0))
    pygame.draw.rect(WIN,BLACK,BORDER)
    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))
    WIN.blit(RED_SPACESHIP,(red.x,red.y))
    
    red_hp_text = HEALTH_FONT.render("Health: " + str(red_hp),1,WHITE)#this 1 as parameter funny 
    yellow_hp_text = HEALTH_FONT.render("Health: " + str(yellow_hp),1,WHITE)
    WIN.blit(red_hp_text,(WIDH - red_hp_text.get_width() - 10,10 ) )
    WIN.blit(yellow_hp_text,(10,10))
    for bullet in red_bullets:
        pygame.draw.rect(WIN,RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN,YELLOW, bullet)




    pygame.display.update() 
    

def draw_winner(text):
    draw_text = WINNER_FONT.render(text,1,WHITE)
    WIN.blit(draw_text,( WIDH/2 - draw_text.get_width()/2,HEIGHT/2 - draw_text.get_height()/2 ))
    pygame.display.update()
    pygame.time.delay(5000)



def main():
    red = pygame.Rect(700,300,SPACE_SHIP_WIDH,SPACE_SHIP_HEIGHT)
    yellow = pygame.Rect(100,300,SPACE_SHIP_WIDH,SPACE_SHIP_HEIGHT)
    red_bullets=[]
    yellow_bullets=[]

    red_hp = 10
    yellow_hp = 10

    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet=pygame.Rect(yellow.x + yellow.width,yellow.y + yellow.height//2 -2,10,5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
                if event.key == pygame.K_KP_0 and len(red_bullets) < MAX_BULLETS:
                    bullet=pygame.Rect(red.x,red.y + red.height//2 -2,10,5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
            if event.type == RED_HIT:
                red_hp -= 1
                BULLET_HIT_SOUND.play()
            if event.type == YELLOW_HIT:
                yellow_hp -= 1
                BULLET_HIT_SOUND.play()

        winner_text = ""
        if red_hp <= 0:
            winner_text = "Yellow Wins!"
        if yellow_hp <= 0:
            winner_text = "Red Wins!"
        if winner_text != "":
            draw_winner(winner_text)
            break#to close the game


        keys_pressed = pygame.key.get_pressed()
        yellow_mouv(keys_pressed,yellow)
        red_mouv(keys_pressed,red)
        handle_bullets(yellow_bullets,red_bullets,yellow,red)    
        draw_window(red,yellow,red_bullets,yellow_bullets,red_hp,yellow_hp)
    
    #pygame.quit()
    main()
    


if __name__ == "__main__":
    main()