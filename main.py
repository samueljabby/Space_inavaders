import pygame,sys
from player import Player
import obstacle

pygame.init()

class Game:
    def __init__(self): 
        player_sprite=Player((300,600),screen_width)
        self.player=pygame.sprite.GroupSingle(player_sprite)

        #obstacle_setup
        self.shape=obstacle.shape
        self.block_size=6
        self.blocks=pygame.sprite.Group()
        self.obstacle_amount=4
        self.obstacle_x_pos=[num*(screen_width/self.obstacle_amount) for num in range(self.obstacle_amount)]
        self.create_mulyiple_obstacle(*self.obstacle_x_pos,x_start=50,y_start=480)   #this meanis evertime the class is initiated ot will call the method

              
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
            

    def run(self):
        self.player.sprite.lasers.draw(screen)   #i think sprite is liye cuz self.player ek group hai uske andar ek sprite hai ya group hai hai jisko draw karn a hai   
        self.player.draw(screen)
        self.blocks.draw(screen)
        self.player.update()

screen_width=600
screen_height=600
screen=pygame.display.set_mode((screen_width,screen_height))
clock=pygame.time.Clock()

game=Game()

if __name__=='__main__':
  while True:
      for event in pygame.event.get():
          if event.type==pygame.QUIT:
              pygame.quit()
              sys.exit()
  
      screen.fill('black')
      game.run()
  
      pygame.display.update()
      clock.tick(60)