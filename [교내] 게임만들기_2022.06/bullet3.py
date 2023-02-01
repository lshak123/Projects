#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pygame

class Bullet3:
    def __init__(self, x, y, to_x, to_y):
        self.pos = [x, y]
        self.to = [to_x, to_y]
        self.radius = 11
        self.color = (190, 0, 0)
        self.damage = 30
        
    def update_and_draw(self, dt, screen):
        width, height = screen.get_size()
        self.pos[0] = (self.pos[0] + self.to[0] * dt) % width
        self.pos[1] = (self.pos[1] + self.to[1] * dt) % height
        pygame.draw.circle(screen, self.color, self.pos, self.radius)

