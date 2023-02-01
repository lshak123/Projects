#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pygame

class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load("./data/player.png")
        self.image = pygame.transform.scale(self.image,(64,64))
        self.image_in = pygame.image.load("./data/player_in.png")   # 무적상태 반짝거림을 주기위한 이미지
        self.image_in = pygame.transform.scale(self.image_in,(64,64))
        self.pos =[x,y]
        self.to = [0,0]
        self.angle = 0
        # 미션 1: 효과음 발생을 위해 boom.wav를 다운 받은 후 soindObj에 저장
        self.soundObj = pygame.mixer.Sound('./data/boom.wav')
        
        self.boom_image = pygame.image.load('./data/boom.png') # 미션 2: 그림을 나타내기 위해 boom.png를 boom_image변수에 저장
        self.boom_image = pygame.transform.scale(self.boom_image,(128,128)) # 비행기 사이즈와 동일하면 너무 작아서 128,128로 크기를 맞춰준다.
        
        self.boom_show = False # 폭발 그림을 나타내야할 때를 알려주기 위한 부분
        self.boom_show_time = 0 # 폭발 그림을 얼마나 나타낼 지 시간을 알려주기 위한 부분.
        
        self.life = 100 # life를 100으로 지정
        self.invincible = False # 무적이 될 때를 알려주기 위한 부분
        self.invincible_time = 0 #무적 지속시간 설정을 하기위한 부분

        
    def goto(self, x, y):
        self.to[0] += x
        self.to[1] += y
        
    def update(self, dt, screen):
        width, height = screen.get_size()
        phw = self.image.get_width()/2
        phh = self.image.get_height()/2
        self.pos[0] = self.pos[0] + dt * self.to[0]
        self.pos[1] = self.pos[1] + dt * self.to[1]
        self.pos[0] = min(max(self.pos[0], phw), width- phw)
        self.pos[1] = min(max(self.pos[1], phh), height- phh)
#       if self.pos[0] < 0:
#           self.pos[0] = 0
#       if self.pos[0] > width - player_half_width:
#           self.pos[0] = width - player_half_width
#       if self.pos[1] < 0:
#           self.pos[1] = 0
#       if self.pos[1] > height - player_half_height:
#           self.pos[1] = height -player_half_height
        self.boom_show_time -= dt
        if self.boom_show_time < 0:
            self.boom_show = False
        
        self.invincible_time -= dt
        if self.invincible_time < 0:
            self.invincible = False
        
    def draw(self, screen):
        if self.to == [0,-1]: self.angle =0
        elif self.to == [-1,-1]: self.angle =45
        elif self.to == [-1,0]: self.angle =90
        elif self.to == [-1,1]: self.angle =135
        elif self.to == [0,1]: self.angle =180
        elif self.to == [1,1]: self.angle =-135
        elif self.to == [1,0]: self.angle =-90
        elif self.to == [1,-1]: self.angle =-45
        
       
        if self.boom_show:
            rotated = pygame.transform.rotate(self.boom_image, 0)
            calib_pos = (self.pos[0] - rotated.get_width()/2,
                         self.pos[1] - rotated.get_height()/2)
            screen.blit(rotated, calib_pos)
        else:
            if self.invincible:
                if self.invincible_time%100%2 == 0:
                    rotated = pygame.transform.rotate(self.image_in, self.angle)
                    calib_pos = (self.pos[0] - rotated.get_width()/2,
                                 self.pos[1] - rotated.get_height()/2)
                    screen.blit(rotated, calib_pos)
            else:
                rotated = pygame.transform.rotate(self.image, self.angle)
                calib_pos = (self.pos[0] - rotated.get_width()/2,
                             self.pos[1] - rotated.get_height()/2)
                screen.blit(rotated, calib_pos)
            
    def hit(self,damage): # 맞았을 때 반응하기 위한 hit 함수 생성
        if not self.invincible:
            self.soundObj.play() # 맞았을 때 폭발음을 발생 시킨다.
            self.boom_show = True # 맞았을 때 폭발 그림을 나타낸다.
            self.boom_show_time = 300 # 300만큼 폭발 그림을 나타낸다.
            self.life -= damage
            self.invincible = True
            self.invincible_time = 1300 # 무적시간 1300

        return bool(self.life <= 0)