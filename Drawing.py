from PIL import Image
import pygame
import glob
import os
import time
import math
import random
import sys
import threading
from pygame.locals import *

pygame.init()
pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)

screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Draw")
IMAGE_SIZE = (150,150)
playerImg = pygame.image.load('img/guy1.png')
#spriteImg = pygame.image.load('img/rundude0.png')

##                    pygame.image.load('img/rundude1.png'),
##                    pygame.image.load('img/rundude2.png'),
##                    pygame.image.load('img/rundude3.png'),
##                    pygame.image.load('img/rundude4.png'),
##                    pygame.image.load('img/rundude5.png'),
##                    pygame.image.load('img/rundude6.png'),
##                    pygame.image.load('img/rundude7.png'),
##                    pygame.image.load('img/rundude8.png')]
clock = pygame.time.Clock()
frame_index = 0



def rightplayer (x, y):
    global spriteImg
    spriteImg = pygame.image.load(f'img/rundude{int(run_index)}.png')
    spriteImg = pygame.transform.scale(spriteImg, IMAGE_SIZE)
    screen.blit(spriteImg, (x, y) )
    
def leftplayer (x, y):
    global spriteImg
    spriteImg = pygame.image.load(f'img/rundude{int(run_index)}.png')
    spriteImg = pygame.transform.scale(spriteImg, IMAGE_SIZE)
    spriteImg = pygame.transform.flip(spriteImg, True, False)
    screen.blit(spriteImg, (x, y) )
    



[os.remove(png) for png in glob.glob("*png")]
def draw():
    global frame_index
    loop = True
    while loop:
        
        press = False
        color = "white"
        cnt = 0
        ink = 0
        
        animation_speed = 0.3

        #pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    screen.fill(pygame.Color(0, 0, 0))
                    frame_index = 0
                if event.key == pygame.K_s:
                    if cnt < 10:
                        pygame.image.save(screen, f"Screenshots\screenshot " + time.strftime("%Y-%m-%d_%H%M%S") + ".png")
                        print('Captured screenshot')
                    else:
                        pygame.image.save(screen, f"Screenshots\screenshot " + time.strftime("%Y-%m-%d_%H%M%S") + ".png")
                        print('Captured screenshot')
                    cnt += 1
                if event.key == pygame.K_g:
                        frames = []
                        imgs = glob.glob("*.png")
                        for i in imgs:
                            new_frame = Image.open(i)
                            frames.append(new_frame)
     
                        # Save into a GIF file that loops forever
                        frames[0].save('animated.gif', format='GIF',
                                        append_images=frames[1:],
                                        save_all=True,
                                        duration=300, loop=0)
                        os.startfile("animated.gif")


        px, py = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed() == (1,0,0):
            pygame.draw.rect(screen, (255,255,255), (px,py,15,15))
            frame_index += animation_speed
            pygame.display.update()

            #math.ceil(ink)

        print(frame_index)
        if frame_index >= 100:
            frame_index = 0
        
        barImg = pygame.image.load(f'inkbar/load{int(frame_index)}.png')
        pygame.draw.rect(screen, (0,0,0), (20,1,100,102))
        screen.blit(barImg,(20,1))
        

        if pygame.mouse.get_pressed() == (0,0,1):
            pygame.draw.rect(screen, (0,0,0), (px,py,10,10))

        if event.type == pygame.MOUSEBUTTONUP:
            press == False
        #pygame.display.update()
        clock.tick(1000)

def play():
    running = True
    global spriteImg
    global run_index
    global run_speed
    playerX = 500  
    playerY = 500
    run_index = 0
    run_speed = 0.4
    vel = 5
    width = 1000
    height = 600

    isJump = False
    jumpCount = 9
    #clear = (0, 0, 0, 0)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #if we click the X the program ends
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            pygame.draw.rect(screen, (0,0,0), (playerX,playerY+5,150,110))
            run_index += run_speed
            #time.sleep(0.3)
            if run_index >= 8:
                run_index = 0
            spriteImg = pygame.image.load(f'img/rundude{int(run_index)}.png')
            #pygame.display.update()
            playerX += vel
            rightplayer(playerX, playerY)
            #pygame.display.update()
            
        if keys[pygame.K_LEFT]:
            pygame.draw.rect(screen, (0,0,0), (playerX,playerY+5,150,110))
            #pygame.display.update()
            run_index += run_speed
            #time.sleep(0.3)
            if run_index >= 8:
                run_index = 0
            spriteImg = pygame.image.load(f'img/rundude{int(run_index)}.png')
            playerX -= vel
            leftplayer(playerX, playerY)
            
        if not(isJump):
            if keys[pygame.K_UP]:
                pygame.draw.rect(screen, (0,0,0), (playerX,playerY+5,150,110))
                playerY -= vel
                
            if keys[pygame.K_DOWN]:
                pygame.draw.rect(screen, (0,0,0), (playerX,playerY+5,150,110))
                playerY += vel
                
            if keys[pygame.K_SPACE]:
                pygame.draw.rect(screen, (0,0,0), (playerX,playerY+5,150,110))
                isJump = True
                
        else:
            if jumpCount >= -10:
                playerY -= (jumpCount * abs(jumpCount)) * 0.25
                jumpCount -= 1
            else: 
                jumpCount = 10
                isJump = False

            
            
        pygame.display.update()


        
          
         


thread1 = threading.Thread(target=draw)
thread1.start()

thread2 = threading.Thread(target=play)
thread2.start()
