import pygame,sys
from player import Player

pygame.init()

class Game:
    def __init__(self):
        player_sprite=Player((300,600),screen_width)
        self.player=pygame.sprite.GroupSingle(player_sprite)

    def run(self):
        self.player.sprite.lasers.draw(screen)   #i think sprite is liye cuz self.player ek group hai uske andar ek sprite hai ya group hai hai jisko draw karn a hai   
        self.player.draw(screen)
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