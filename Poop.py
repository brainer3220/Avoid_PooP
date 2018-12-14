import pygame
import math
import random

# 초기화
pygame.init()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))

keys = [False, False, False, False]
playerpos = [100,100]

# 이미지 가져오기
player = pygame.image.load("Resources/images/dude.png")
grass = pygame.image.load("Resources/images/gtass.png")
poop = pygame.image.load("Resources/images/poop.png")

# 4 - 계속 화면이 보이도록 반복해서 실행한다
while True:
    badtimer = badtimer-1

    # 5 - 화면을 깨끗하게 청소한다 (R,G,B) 값 사용
    screen.fill((0,0,0))

    # 6. - 모든 요소들을 다시 그린다
    for x in range(width//grass.get_width()+1):
        for y in range(height//grass.get_height()+1):
            screen.blit(grass,(x*100,y*100))
    screen.blit(castle,(0,30))
    screen.blit(castle,(0,135))
    screen.blit(castle,(0,240))
    screen.blit(castle,(0,345))

     # 7. - 화면을 다시 그린다
    pygame.display.flip()

    if event.type == pygame.KEYDOWN:
        if event.key==pygame.K_w:
            keys[0]=True
        elif event.key==pygame.K_a:
            keys[1]=True
        elif event.key==pygame.K_s:
            keys[2]=True
        elif event.key==pygame.K_d:
                keys[3]=True

    if event.type == pygame.KEYUP:
        if event.key==pygame.K_w:
            keys[0]=False
        elif event.key==pygame.K_a:
            keys[1]=False
        elif event.key==pygame.K_s:
            keys[2]=False
        elif event.key==pygame.K_d:
            keys[3]=False
