import pygame
import math
import random

# Poop의 가로 위치
poop_width = random.randint(1, 480)

# 초기화
pygame.init()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))

keys = [False, False, False, False]
playerpos = [100,100]

# 이미지 가져오기
player = pygame.image.load("Resources/images/dude.png")
grass = pygame.image.load("Resources/images/grass.png")
poop = pygame.image.load("Resources/images/poop.png")

# 4 - 계속 화면이 보이도록 반복해서 실행한다
while True:
    # 5 - 화면을 깨끗하게 청소한다 (R,G,B) 값 사용
    screen.fill((0,0,0))

    # 6. - 모든 요소들을 다시 그린다
    for x in range(width//grass.get_width()+1):
        for y in range(height//grass.get_height()+1):
            screen.blit(grass,(x*100,y*100))

    # 6.1 - 플레이어 포지션과 회전
    position = pygame.mouse.get_pos()
    screen.blit(player, playerpos)

     # 7. - 화면을 다시 그린다
    pygame.display.flip()

    # 8 - 게임을 종료할 준비, 종료아이콘(x)를 누르면 종료되도록 프로그램
    for event in pygame.event.get():
        # X 를 눌렀는지 검사
        if event.type==pygame.QUIT:
            # 게임종료
            pygame.quit()
            exit(0)

    if event.type == pygame.KEYDOWN:
        # if event.key==pygame.K_w:
        #     keys[0]=True
        if event.key==pygame.K_a:
            keys[1]=True
        # elif event.key==pygame.K_s:
        #     keys[2]=True
        elif event.key==pygame.K_d:
                keys[3]=True

    if event.type == pygame.KEYUP:
        # if event.key==pygame.K_w:
        #     keys[0]=False
        if event.key==pygame.K_a:
            keys[1]=False
        # elif event.key==pygame.K_s:
        #     keys[2]=False
        elif event.key==pygame.K_d:
            keys[3]=False

# 9 - 플레이어 움직이기
    # if keys[0]:
    #     playerpos[1] = playerpos[1] - 5
    if keys[2]:
        playerpos[1] = playerpos[1] + 5
    # if keys[1]:
    #     playerpos[0] = playerpos[0] - 5
    elif keys[3]:
        playerpos[0] = playerpos[0] + 5
