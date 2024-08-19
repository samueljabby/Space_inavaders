import pygame,sys
from random import choice,randint
from player import Player
from alien import Alien,Extra
import obstacle
from laser import Laser

pygame.init()

class Game:
    def __init__(self): 
        #player setup
        player_sprite=Player((300,600),screen_width)
        self.player=pygame.sprite.GroupSingle(player_sprite)

        #obstacle_setup
        self.shape=obstacle.shape
        self.block_size=6
        self.blocks=pygame.sprite.Group()
        self.obstacle_amount=4
        self.obstacle_x_pos=[num*(screen_width/self.obstacle_amount) for num in range(self.obstacle_amount)]
        self.create_mulyiple_obstacle(*self.obstacle_x_pos,x_start=50,y_start=480)   #this meanis evertime the class is initiated ot will call the method
        #alein_setup
        self.aliens=pygame.sprite.Group()
        self.alien_setup(6,8)
        self.alein_direction=1
        self.alien_lasers=pygame.sprite.Group()
        #extra
        self.extra=pygame.sprite.GroupSingle()
        self.extra_spawn_time=randint(400,800)

    
              
    def create_obstacle(self,x_start,y_start,offset_x):
        for row_index,row in enumerate(self.shape):
          for col_index,col in enumerate(row):
              if col=="x":
                  x=col_index*self.block_size +x_start +offset_x  #if offset is absent all obstacle will overlap
                  y=row_index*self.block_size +y_start
                  block=obstacle.Block(self.block_size,(241,79,80),x,y)
                  self.blocks.add(block)
          
    def create_mulyiple_obstacle(self,*offset,x_start,y_start):
        for offset_x in offset:
            self.create_obstacle(x_start,y_start,offset_x)
            
    def alien_setup(self,rows,cols,x_distance=60,y_distance=48,x_offset=70,y_offset=100):
        for row_index,row in enumerate(range(rows)):
            for col_index,col in enumerate(range(cols)):
                x=col_index*x_distance+x_offset
                y=row_index*y_distance+y_offset

                if row_index==0:alien_sprite=Alien("yellow",x,y)
                elif 1<=row_index<=2:alien_sprite=Alien("green",x,y)
                else:alien_sprite=Alien("red",x,y)
                self.aliens.add(alien_sprite)

    def alien_pos_checker(self):
        all_alien=self.aliens.sprites()
        for alien in all_alien:
            if alien.rect.right>=screen_width:
                self.alein_direction=-1
                self.move_alien_down(2)
            if alien.rect.left<=0:
                self.alein_direction=1
                self.move_alien_down(2)

    def shoot_alien(self):
        if self.aliens:
            random_alien=choice(self.aliens.sprites())
            laser_sprite=Laser(random_alien.rect.center,-6,screen_height)
            self.alien_lasers.add(laser_sprite)

    def move_alien_down(self,distance):
        if self.aliens:
         for alien in self.aliens.sprites():
            alien.rect.y+=distance


    def extra_alien_spawn(self):
        self.extra_spawn_time-=1
        if self.extra_spawn_time<=0:
            self.extra.add(Extra(choice(["right","left"]),400))
            self.extra_spawn_time=randint(400,800)

    def run(self):
        self.player.update()
        self.aliens.update(self.alein_direction)
        self.alien_lasers.update()
        self.extra.update()
        self.alien_pos_checker()
        self.extra_alien_spawn()

        self.player.sprite.lasers.draw(screen)   #i think sprite is liye cuz self.player ek group hai uske andar ek sprite hai ya group hai hai jisko draw karn a hai   


        self.player.draw(screen)
        self.blocks.draw(screen)
        self.aliens.draw(screen)
        self.alien_lasers.draw(screen)
        self.extra.draw(screen)

screen_width=600
screen_height=600
screen=pygame.display.set_mode((screen_width,screen_height))
clock=pygame.time.Clock()
ALIENLASER=pygame.USEREVENT +1
pygame.time.set_timer(ALIENLASER,800)


game=Game()

if __name__=='__main__':
  while True:
      for event in pygame.event.get():
          if event.type==pygame.QUIT:
              pygame.quit()
              sys.exit()
          if event.type==ALIENLASER:
              game.shoot_alien()
  
      screen.fill('black')
      game.run()
  
      pygame.display.update()
      clock.tick(60)