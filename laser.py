from typing import Any
import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self,pos,speed,screen_height):
        super().__init__()
        self.image=pygame.Surface((4,20))
        self.image.fill('white')
        self.rect=self.image.get_rect( center=pos)
        self.speed=speed
        self.height_y_constraint=screen_height

    def moving_bullet(self):
        self.rect.y-=self.speed
    
    def destroy_laser(self):
        if self.rect.y<=-50 or self.rect.y>=self.height_y_constraint+50:
            self.kill()

    def update(self):
        self.moving_bullet()
        self.destroy_laser()
