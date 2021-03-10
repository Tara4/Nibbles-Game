import pygame
import random
import os
import leaderboard
pygame.init()   

def startScreen(window):
    black=(0,0,0)
    snake = pygame.image.load(r'C:\Users\User\Documents\GitHub\Nibbles-Game\Nibbles-Reboot\snake.png') 
    welcome = True
    while (welcome == True):
       window.fill(black)
       welcomeFont = pygame.font.SysFont("freesansbold.ttf", 70)
       startFont = pygame.font.SysFont("freesansbold.ttf", 40)
       welcomeText = welcomeFont.render("Welcome to Nibbles!", True, (255, 255, 255))
       startText = startFont.render("Press any key to start", True, (255, 255, 255))
       for event in pygame.event.get():
          if event.type == pygame.KEYDOWN:
              welcome = False
       window.blit(welcomeText,(10,100))
       window.blit(startText,(100,400))
       window.blit(snake, (-20, 200)) 
       pygame.display.flip()

def endScreen(window):
    win.fill((0, 0, 0))
    gameOverFont = pygame.font.SysFont("freesansbold.ttf", 100)
    finalScoreFont = pygame.font.SysFont("freesansbold.ttf", 40)
    gameOverText = gameOverFont.render("Game Over", True, (255, 255, 255))
    finalScoreText = finalScoreFont.render("Final Score: " + str(score), True, (255, 255, 255))
    endText = finalScoreFont.render("Press any key to exit", True, (255, 255, 255))
    win.blit(gameOverText, (55, 150))
    win.blit(finalScoreText, (150, 230))
    win.blit(endText, (100, 300))

win_height = 500
win_width = 500
win = pygame.display.set_caption("Project Nibbles")
win = pygame.display.set_mode((win_width, win_height))
x = 50
y = 50
vel = 15
direction = 4
body_x = [50, 51, 52, 53, 54]
body_y = [50, 50, 50, 50, 50]
size = 16
food_position = [random.randrange(1,50)*10,random.randrange(1,50)*10]
score = 0
count = 1
gameOver = False

name = input("Please Enter Name:")
startScreen(win)

run = True
while run == True:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT and pygame.K_UP]:
        if direction == 2:
            direction = 2
        else:
            direction = 1

    elif keys[pygame.K_RIGHT and pygame.K_UP]:
        if direction == 2:
            direction = 2
        else:
            direction = 1

    elif keys[pygame.K_LEFT and pygame.K_DOWN]:
        if direction == 1:
            direction = 1
        else:
            direction = 2

    elif keys[pygame.K_RIGHT and pygame.K_DOWN]:
        if direction == 1:
            direction = 1
        else:
            direction = 2

    else:
      if keys[pygame.K_LEFT]:
        if direction == 4:
            direction = 4
        else:
            direction = 3

      if keys[pygame.K_RIGHT]:
        if direction == 3:
            direction = 3
        else:
            direction = 4

    win.fill((0, 0, 0))

    food = pygame.draw.rect(win, (180,255,100), (food_position[0], food_position[1], 10, 10))

    if direction == 1:
      y -= vel
      body_y.insert(0,body_y[0]-size)
      body_x.insert(0,body_x[0])
      body_x.pop(len(body_x)-1)
      body_y.pop(len(body_y)-1)

    if direction == 2:
      y += vel
      body_y.insert(0,body_y[0]+size)
      body_x.insert(0,body_x[0])
      body_x.pop(len(body_x)-1)
      body_y.pop(len(body_y)-1)

    if direction == 3:
      x -= vel
      body_x.insert(0,body_x[0]-size)
      body_y.insert(0,body_y[0])
      body_x.pop(len(body_x)-1)
      body_y.pop(len(body_y)-1)

    if direction == 4:
      x += vel
      body_x.insert(0,body_x[0]+size)
      body_y.insert(0,body_y[0])
      body_x.pop(len(body_x)-1)
      body_y.pop(len(body_y)-1)
     
    for i in range(len(body_x)-1):
        snake_body =  pygame.draw.rect(win, (255, 0, 0), (body_x[i], body_y[i], size, size))
        snake_head = pygame.draw.rect(win, (0, 255, 255), (body_x[0], body_y[0], size, size)) 
        if i > 0 and body_x[i] == body_x[0] and body_y[i] == body_y[0]:
            gameOver = True
        
    food = pygame.draw.rect(win, (180,255,100), (food_position[0], food_position[1], 10, 10))

    scoreFont = pygame.font.SysFont("freesansbold.ttf", 40)
    scoreText = scoreFont.render("Score: " + str(score), True, (255, 255, 255))
    win.blit(scoreText, (0, 0))

    if snake_head.colliderect(food):
        food_position = [random.randrange(1,50)*10,random.randrange(1,50)*10] 
        score += 1
        
        if direction == 1:
           body_y.insert(0,body_y[0]-size)
           body_x.insert(0,body_x[0])

        elif direction == 2:
           body_y.insert(0,body_y[0]+size)
           body_x.insert(0,body_x[0])

        elif direction == 3:
           body_x.insert(0,body_x[0]-size)
           body_y.insert(0,body_y[0])

        elif direction == 4:
           x += vel
           body_x.insert(0,body_x[0]+size)
           body_y.insert(0,body_y[0])

    if x < 0 or x > win_width:
      gameOver = True

    if y <  0 or y > win_height:
      gameOver = True

    if gameOver == True:
      endScreen(win)
      if event.type == pygame.KEYDOWN:
          lbrd = leaderboard.Leaderboard()
          lbrd.saveFile(name, score)
          scores = lbrd.GetTop10()
          print("High Scores:")
          for i in range(len(scores)):
              print("[" + str(count) + "]", scores[i])
              count += 1
          break

    pygame.display.update()

pygame.quit()

