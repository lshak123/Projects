#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame
from player import Player
from bullet import Bullet
from bullet2 import Bullet2
from bullet3 import Bullet3
import random as rnd
import time

def collision(obj1, obj2):
    dist = ((obj1.pos[0]-obj2.pos[0])**2 + (obj1.pos[1]-obj2.pos[1])**2)**0.5
    return dist < 20

def draw_text(txt, size, pos, color):
    font = pygame.font.Font('freesansbold.ttf',size)
    r = font.render(txt, True, color)
    screen.blit(r,pos)

scores = []

with open("scores.txt", "r") as f:
    for line in f:
        scores.append(float(line)) # scores.txt에 저장되어 있는 점수를 리스트로 저장

scores.sort(reverse = True)
    
pygame.init() # pygame모듈 초기화
WIDTH, HEIGHT = 1000, 800  # 창 크기
pygame.display.set_caption("총알 피하기") # 제목

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
FPS = 60 # fps설정

pygame.mixer.music.load('bgm.wav') #bgm설정
pygame.mixer.music.play(-1) # 반복횟수(-1은 무한반복)

bg_image = pygame.image.load('./data/bg.jpg') #배경
bg_pos_x = -100 
bg_pos_y = -100

player = Player(WIDTH/2,HEIGHT/2)



bullets = []  # 3종류 총알을 만들기위한 리스트를 생성
bullets2 = []
bullets3 = []
for i in range(1):  # 총알 넣기
    bullets.append(Bullet(0, rnd.random()*HEIGHT, rnd.random()-0.5, rnd.random()-0.5))
for i in range(1):
    bullets2.append(Bullet2(0, rnd.random()*HEIGHT, rnd.random()-0.5, rnd.random()-0.5))
for i in range(1):
    bullets3.append(Bullet3(0, rnd.random()*HEIGHT, rnd.random()-0.5, rnd.random()-0.5))

time_for_adding_bullets = 0
time_for_adding_bullets2 = 0 # 각 총알이 생성되는 시간을 다르게 하기위한 변수
time_for_adding_bullets3 = 0

start_time = time.time()

score = 0

gameover = False
running = True 
saved = False 

while running:
    
    dt = clock.tick(FPS) 
    time_for_adding_bullets += dt
    time_for_adding_bullets2 += dt
    time_for_adding_bullets3 += dt
    #이벤트 받는 부분
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.goto(-1, 0)
            elif event.key == pygame.K_RIGHT:
                player.goto(1, 0)
            elif event.key == pygame.K_UP:
                player.goto(0, -1)
            elif event.key == pygame.K_DOWN:
                player.goto(0, 1)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.goto(1, 0)
            elif event.key == pygame.K_RIGHT:
                player.goto(-1, 0)
            elif event.key == pygame.K_UP:
                player.goto(0, 1)
            elif event.key == pygame.K_DOWN:
                player.goto(0, -1)
    
    player.update(dt, screen)
    #화면 갱신
    #screen.fill((0,0,0))
    # 플레이어의 x,y좌표에 따라 배경 이동(기존의 0.01씩 이동은 너무 느려서 0.03으로)
    bg_pos_x -= dt * 0.03 * player.to[0]
    bg_pos_y -= dt * 0.03 * player.to[1]
    
    screen.blit(bg_image, (bg_pos_x,bg_pos_y))
    
    player.draw(screen)
    # 3색 불릿 추가  
    for b in bullets:
        b.update_and_draw(dt, screen)
    
    for b in bullets:
        if collision(b, player):
            if player.hit(10):    # 파란 총알은 damage 10
                gameover = True
    for b2 in bullets2:
        b2.update_and_draw(dt, screen)
    
    for b2 in bullets2:
        if collision(b2, player):
            if player.hit(20):   # 초록 총알은 damage 20
                gameover = True
    for b3 in bullets3:
        b3.update_and_draw(dt, screen)
    
    for b3 in bullets3:
        if collision(b3, player): 
            if player.hit(30):   # 빨강 총알은 damage 30
                gameover = True

    
    if gameover:
        if not saved:  # score 저장 코드
            scores.append(score)
            scores.sort(reverse = True)
            saved = True
            if len(scores) > 10:
                scores = scores[:10]
            with open("scores.txt","w") as f:
                for s in scores:
                    f.write(f"{s}\n")
        draw_text("GAME OVER", 100, (WIDTH/2 - 300, HEIGHT/2 - 300), (255,255,255))
        for i in range(0,min(10,len(scores))):
            txt = f"{i+1}. Survival Time : {scores[i]:.3f}"
            if score == scores[i]:                                                           # 스코어를 등수를 매겨서 보여준다
                draw_text(txt, 25, (WIDTH/2 - 100, HEIGHT/2 - 200 + 30*i),(200,0,0))         # 상위 10등 안에 점수가 있다면 빨간색으로 표시
            else:
                draw_text(txt, 25, (WIDTH/2 - 100, HEIGHT/2 - 200 + 30*i),(255,255,255))
    else:
        score = time.time() - start_time
        txt = f"Time:{score:.3f}, Bullets: {len(bullets)+len(bullets2)+len(bullets3)}, Life{player.life}"
        draw_text(txt,32,(10,10),(255,255,255))
        # 체력게이지를 나타내기 위한 부분 위는 체력바를 위한 사각형, 아래는 남은 체력에 대한사각형이다.
        pygame.draw.rect(screen, (0,0,0) , [750, 10 , 180 , 20 ]) 
        pygame.draw.rect(screen, (255,0,0), [750, 10, 1.8*player.life ,20])        
        # 3색 불릿 추가 속도를 다르게 해줌
        if time_for_adding_bullets > 1000:
            bullets.append(Bullet(0, rnd.random()*HEIGHT, rnd.random()-0.5, rnd.random()-0.5))
            time_for_adding_bullets -= 1000
        if time_for_adding_bullets2 > 1900:
            bullets2.append(Bullet2(0, rnd.random()*HEIGHT, rnd.random()-0.5, rnd.random()-0.5))
            time_for_adding_bullets2 -= 1900
        if time_for_adding_bullets3 > 2600:
            bullets3.append(Bullet3(0, rnd.random()*HEIGHT, rnd.random()-0.5, rnd.random()-0.5))
            time_for_adding_bullets3 -= 2600
    
    pygame.display.update() 


# In[ ]:




