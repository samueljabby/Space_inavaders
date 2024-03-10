import pygame
from laser import Laser
class Player(pygame.sprite.Sprite):
    def __init__(self,pos,screen_constraint) :
        super().__init__()
        self.image=pygame.image.load("graphics/player.png").convert_alpha()
        self.rect=self.image.get_rect(midbottom=pos)
        self.speed=5
        self.player_constraint=screen_constraint
        self.ready=True
        self.laser_time=0
        self.laser_cooldown=600

        self.lasers=pygame.sprite.Group()
    def get_input(self):
        keys=pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x+=self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x-=self.speed
        if keys[pygame.K_SPACE] and self.ready:
            self.shoot_laser()
            self.ready=False
            self.laser_time=pygame.time.get_ticks()
        
    def recharge(self):
        if not self.ready:
            current_time=pygame.time.get_ticks()#this one notes the time game jab se chalu hua ciuz its benn called repeatly
            if current_time -self.laser_time>=self.laser_cooldown:
                self.ready=True

    def constraint(self):
        if self.rect.right>=self.player_constraint:
            self.rect.right=self.player_constraint
        if self.rect.left<=0:
            self.rect.left=0
    def shoot_laser(self):
        self.lasers.add(Laser(self.rect.center,8,self.rect.bottom))  #the laser pos is given as the centet of the player rect

    def update(self):
        self.get_input()
        self.constraint()
        self.recharge()
        self.lasers.update()    #here we are caliing the update method from lasers group  jiske class ka instance humne bana lia hai
        