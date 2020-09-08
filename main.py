import pygame
from plane_sprites import *
screenHeight = 700
screenWidth = 480
heroWidth = 120
heroHeight = 125
hero_rect = pygame.Rect(100, 500, heroWidth, heroHeight)
print(hero_rect.x, hero_rect.y, hero_rect.size)
pygame.init()
# 创建游戏窗口 480*700
screen = pygame.display.set_mode((screenWidth, screenHeight))
# 绘制背景图像
bg = pygame.image.load('./images/background.jpg')
screen.blit(bg, (0, 0))

# 加载我方飞机
hero = pygame.image.load('./images/me1.png')
screen.blit(hero, (200, 500))


# 敌机精灵
enemy = GameSprite('./images/enm1.png')
enemy1 = GameSprite('./images/enm1.png', 2)

# 敌机精灵组
enemy_group = pygame.sprite.Group(enemy, enemy1)

while True:
  # 捕获事件
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      print('Game Over')
      pygame.quit()
      exit()
  # 修改飞机位置
  hero_rect.y -= 1
  if hero_rect.y <= -heroHeight:
    hero_rect.y = screenHeight
  screen.blit(bg, (0, 0))
  screen.blit(hero, hero_rect)

  # 精灵组方法
  enemy_group.update()
  enemy_group.draw(screen)


  pygame.display.update()
  event = pygame.event.poll()
  if event.type == pygame.QUIT:
    pygame.quit()
    exit()