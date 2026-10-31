import pygame 
import random 
import time
pygame.init()
ballspeed_x = random.choice([-10, 10]) 
swidth = 800
sheight = 600
screen = pygame.display.set_mode((swidth,sheight))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()
#платформа
platform_x = 350
platform_y = 570
platform_speed = 10
#мяч
ball_x =400
ball_y = 150
ballspeed_y = 10
#блоки
blocks = []
def create_block():
    blocks.clear()
    for row in range(4):
        for coli in range(8):
            bx = 50 + coli * 90
            by = 50 + row * 30
            blocks.append({"x": bx,"y": by, "widht": 80, "height": 20,"visible": True})
create_block()
screen.fill((180, 40, 205))
pygame.draw.rect(screen, (0, 200, 250), (platform_x, platform_y, 225, 10))
pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), 10)
for block in blocks:
    pygame.draw.rect(screen, (0, 0, 139), (block["x"], block["y"], block["widht"], block["height"]))

pygame.display.flip()  
time.sleep(3)  
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((180,40,205))
    
    pygame.draw.rect(screen, (0,200,250), (platform_x,platform_y,225,10))
    pygame.draw.circle(screen,(255,255,255),(ball_x,ball_y) ,10)
    for block in blocks:
        if block["visible"]:
            pygame.draw.rect(screen, (0,0,139), (block["x"],block["y"],block["widht"],block["height"]))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        platform_x = platform_x -  platform_speed
    if keys[pygame.K_RIGHT]:
        platform_x = platform_x + platform_speed   
    if platform_x < 0:
        platform_x = 0
    if platform_x > 600:
        platform_x = 600
    pygame.display.flip()
    
    clock.tick(60)
    ball_y = ball_y + ballspeed_y
    ball_x = ball_x + ballspeed_x
    if ball_x <= 10 or ball_x >= 790:
        ballspeed_x = -ballspeed_x
    if ball_y <= 10 :
        ballspeed_y = -ballspeed_y
    #Отскок(хитбоксы)
    if ballspeed_y > 0:
        if platform_y <= ball_y + 10 <= platform_y + 10 and platform_x <= ball_x <= platform_x + 200:
            ballspeed_x = ((ball_x - (platform_x + 100)) / 100) * 12
            ballspeed_y = -ballspeed_y
    for block in blocks:
        if block["visible"]:
               if block["x"] <= ball_x <= block["x"] + block["widht"]:
                    if ballspeed_y > 0 and block["y"] <= ball_y + 10 <= block["y"] + 10:
                        ballspeed_y = -ballspeed_y
                        block["visible"] = False
                        break
                    elif ballspeed_y < 0 and block["y"] + block["height"] <= ball_y - 10 <= block["y"] + block["height"] + 10:
                        ballspeed_y = -ballspeed_y
                        block["visible"] = False
                        break
    #поражение
    if ball_y >= 600:
        print("Defeat")
        running = False

        