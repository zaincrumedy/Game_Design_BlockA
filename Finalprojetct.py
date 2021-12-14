#Zain
#10/25

import pygame as py, os, random, time
py.init()
BLACK=(255,255,255)
WHITE=(0,0,0)
PURPLE=(150,0,150)
WIDTH = 800
HEIGHT = 800
#These are all my words that show on a selection screen like settings
bmessages=["Back"]
messages=['Instructions','Level 1','Level 2','Settings','Score Board', 'Exit']
messages2=['Screen size', 'Sound off', 'Sound on', ]
Ssmessages=['Larger', 'Smaller', ]
imessages=["Welcome! This game is simple: jumpto the top to continue"," There are some secret ways to get to the top if you know where to look","Reach the star to win","Try jumping straight up first, then left to right when completing levels", "Good Luck!"]
win=py.display.set_mode((WIDTH,HEIGHT))
py.display.set_caption("Setting Window")
#TITLE_FONT= py.font.SysFont(name,size,bold=false, italic= false)
#title font and subtitel font sizes
TITLE_FONT= py.font.SysFont('comicsans', 50, italic=True)
SUBTITLE_FONT= py.font.SysFont('comicsans', 30, italic=True)
xbox=25
wbox=25
sound=0
square=py.Rect(10,10, wbox, xbox)
clock=py.time.Clock()
py.init()
run = True
#display message is something I used for the lists above in settings
def displayscore(score):
    text=TITLE_FONT.render(score, 25, WHITE)
    win.blit(text, (WIDTH/2-text.get_width()/2, 30) )
    py.display.update()
def display_message(message):
    py.time.delay(100)
    text=TITLE_FONT.render(message,30, BLACK )
    win.blit(text, (WIDTH/2-text.get_width()/2, 30) )
    py.display.update()
    py.time.delay(10)
# Same thing for subtitles
def displaySub(subTitle,ysub):
    py.time.delay(100)
    text=SUBTITLE_FONT.render(subTitle,1, BLACK )
    win.blit(text, (10, ysub ))
    py.display.update()
    py.time.delay(10)
#This is for my back button
def display_back():
                x=660
                y=730
                square.x=x
                square.y=y
                for i in range(0,len(bmessages)):
                    word= bmessages[i]
                    py.draw.rect(win, PURPLE, square)
                    text=SUBTITLE_FONT.render(word,10, BLACK)
                    win.blit(text, (x+wbox+10, y))
                    py.display.flip()
                    
                    
                    square.y=y
x=50
y=650
guyx=x
level=1
walkCount=0
#this is my entire level 1 game
def level1_game():
    from os import X_OK
    import pygame
    #importing my global variables so that they carry over
    global x, y, walkCount, level
    pygame.init()
    win = pygame.display.set_mode((800,800))
    pygame.display.set_caption("First Game")
    #Window display size and caption
    walkRight = [pygame.image.load('gameImages\\sprite2.png'), pygame.image.load('gameImages\\sprite3.png'), pygame.image.load('gameImages\\sprite2.png'), pygame.image.load('gameImages\\sprite6.png')]
    walkLeft = [pygame.image.load('gameImages\\sprite4.png'), pygame.image.load('gameimages\\sprite5.png'), pygame.image.load('gameimages\\sprite7.png'), pygame.image.load('gameimages\\sprite4.png')]
    bg=pygame.image.load('gameImages\\forest background.jpg')
    char=pygame.image.load('gameImages\\standing1.png')
    smallplat=pygame.image.load('gameImages\\smallplatform.png')
    regplat=pygame.image.load('gameImages\\platform.png')
    midplat=pygame.image.load('gameImages\\middleplatform.png')
    #Some of my character and other image sprtes for the game
    if sound==0:
        #This plays my sound at all times, the -1 means that it will play on repeat forever
        game_sound = pygame.mixer.Sound("DK's Jungle Park - Mario Kart 64.wav")
        pygame.mixer.music.load("DK's Jungle Park - Mario Kart 64.wav")
        pygame.mixer.music.play(-1)
    star=pygame.image.load('gameImages\\star.png')
    trophy=pygame.image.load('gameImages\\trophy.png')
    podium=pygame.image.load('gameimages\\podium.jpg   ')
    #More images for the game
    x = 50
    y = 665
    width = 40
    height = 60
    vel = 30
    walkCount=0
    clock = pygame.time.Clock()
    #The clock which I made a variable because I needed clock.tick to switch the pictires of the character
    isJump = False
    jumpCount = 10
    left = False
    right = False
    level=1
    check = 0
    #Most of the game variables
    def redrawGameWindowL1():
        global walkCount, y, x, level
        #Globaling my variables again, THis is the first game window of 3
        win.blit(bg, (0,0)) 
        win.blit(regplat,(-10,725)) 
        platform=pygame.Rect(540, 630, 225,30)
        platformColor=((0,255,0))
        # pygame.draw.rect(win, platformColor, platform)
        if level==1:
            win.blit(regplat,(450,725)) 
            win.blit(midplat,(350,725))
            win.blit(smallplat,(525,610))
            win.blit(smallplat,(100,500))
            win.blit(smallplat,(525,390))
            win.blit(smallplat,(100,280))
            win.blit(smallplat,(525,170))
            #All of my platforms and background placement is above
        if y<-50:
            level=2
            #Switching to screen 2, since the objective is to move to the top of the screen its when y is less than a number off screen
        if level ==2:
            win.blit(bg, (0,0))
            #Same thing for level 2, I might not need this but I dont want to break my code so Ill leave it
            if walkCount + 1 >= 12:
                walkCount = 0 
            if left:  
                win.blit(walkLeft[walkCount//3], (x,y))
                walkCount += 1                          
            elif right:
                win.blit(walkRight[walkCount//3], (x,y))
                walkCount += 1
            else:
                win.blit(char, (x, y))
                walkCount = 0
                #All the htings above allow the character to move around. 
            pygame.display.update()  
        # if level==2:
        #     print("its working")
        #     win.blit(bg, (0,0)) 
        if walkCount + 1 >= 12:
            walkCount = 0   
        if left:  
            win.blit(walkLeft[walkCount//3], (x,y))
            walkCount += 1                          
        elif right:
            win.blit(walkRight[walkCount//3], (x,y))
            walkCount += 1
        else:
            win.blit(char, (x, y))
            walkCount = 0
            #Same things here with character moving
        pygame.display.update() 
    check=0
    #I dont think I need check anymore but I used check at some point to make sure that my cahracter moved to the needed positon when I switched screens 
    x=50
    y=650
    def redrawGameWindowL2():
        global walkCount, check, x, y, level
        #importing global variables
        # if check == 0:
        #     x=50
        #     y=650 
        win.blit(bg, (0,0)) 
        win.blit(regplat,(-10,725)) 
        platform=pygame.Rect(540, 630, 225,30)
        platformColor=((0,255,0))
        win.blit(smallplat, (550, 590))
        win.blit(smallplat, (250, 520))
        win.blit(smallplat, (550, 450))
        win.blit(smallplat, (250, 380))
        win.blit(smallplat, (550, 310))
        win.blit(smallplat, (250, 250))
        win.blit(smallplat, (550, 180))
        #All the platform stuff
        # win.blit(smallplat, (250, 110))
        # win.blit(smallplat, (550, 40))
        # pygame.draw.rect(win, platformColor, platform)
        # win.blit(regplat,(450,725)) 
        # win.blit(midplat,(350,725))
        # win.blit(smallplat,(525,610))
        # win.blit(smallplat,(100,500))
        # win.blit(smallplat,(525,390))
        # win.blit(smallplat,(100,280))
        # win.blit(smallplat,(525,170))
        # if level==1 and x<0:
        #     level+=1
        # if level==2:
        #     print("its working")
        #     win.blit(bg, (0,0)) 
        if walkCount + 1 >= 12:
            walkCount = 0    
        if left:  
            win.blit(walkLeft[walkCount//3], (x,y))
            walkCount += 1                          
        elif right:
            win.blit(walkRight[walkCount//3], (x,y))
            walkCount += 1
        else:
            win.blit(char, (x, y))
            walkCount = 0
            #Moving stuff    
        pygame.display.update() 
    def redrawGameWindowL3():
        global walkCount, check, x, y, level
        #Importing again, this is for the third window
        # if check == 0:
        #     x=50
        #     y=650 
        win.blit(bg, (0,0)) 
        win.blit(regplat,(710,725)) 
        win.blit(regplat,(-300,725)) 
        win.blit(smallplat,(300,725)) 
        win.blit(star, (25,500)) 
        platform=pygame.Rect(540, 630, 225,30)
        platformColor=((0,255,0))
        #Platform stuff
        # pygame.draw.rect(win, platformColor, platform)
        # win.blit(regplat,(450,725)) 
        # win.blit(midplat,(350,725))
        # win.blit(smallplat,(525,610))
        # win.blit(smallplat,(100,500))
        # win.blit(smallplat,(525,390))
        # win.blit(smallplat,(100,280))
        # win.blit(smallplat,(525,170))
        # if level==1 and x<0:
        #     level+=1
        # if level==2:
        #     print("its working")
        #     win.blit(bg, (0,0)) 
        if walkCount + 1 >= 12:
            walkCount = 0   
        if left:  
            win.blit(walkLeft[walkCount//3], (x,y))
            walkCount += 1                          
        elif right:
            win.blit(walkRight[walkCount//3], (x,y))
            walkCount += 1
        else:
            win.blit(char, (x, y))
            walkCount = 0
            #Moving stuff
        pygame.display.update() 
    def windisplay():
        #THis is my window that I display when you complete the game
        #it has the trophy, a stationary character, and just a few platforms
        global x, y
        win.blit(bg, (0,0)) 
        win.blit(trophy, (335,300))
        win.blit(smallplat, (290, 615))
        win.blit(char, (375,550))
        pygame.display.update() 
    winscreen=0
#variable for winscreen
    run = True
    score=0
    while run:
        clock.tick(12)
        #This is the clocktick I needed
        print(score)
        #Printing the score in the terminal
        if winscreen==1:
            print(score)
        else:
            score+=1
        mouse_pos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        #verifying that keys get pressed
        # if x <525 and x>700 and y< 560:
        #     y=675 
        if keys[pygame.K_LEFT] and x > vel: 
            x -= vel
            left = True
            right = False
            #Left movement
        elif keys[pygame.K_RIGHT] and x < 800 - vel - width:  
            x += vel
            left = False
            right = True
            #Right movemet
        else: 
            left = False
            right = False
            walkCount = 0
        if x>320 and x<500 and y < 650 and jumpCount == 10 and level ==1:
            y=665
            jump=False
        if x>20 and x<80 and y < 650 and jumpCount == 10 and level ==1:
            y=665
            jump=False
        if x>20 and x<80 and y < 650 and jumpCount == 10 and level ==2:
            y=665
            jump=False
        if level ==2 and x>400 and x<800 and y<670 and y > 660 and jumpCount == 10:
            x=50
            jump=False
        if y<0 and x<800 and x>700:
            level =3
        if x>700 and x<800 and y < 650 and jumpCount == 10 and level ==3:
            y=665
            x=780
            jump=False
        if x>0 and x<50 and y<600 and level==3:
            winscreen=1
            level=4    
            #THis activats the winscreen
        if x>50 and x < 650 and y<680 and level==3 and jumpCount==10:
            x=750
            y=665
            jump=False
        if x>20 and x<600 and y < 20 and jumpCount == 10 and level ==2:
            y=665
            jump=False
        #All of the other things above this are restrictions for when char is not on a platform
        if not(isJump):
            if keys[pygame.K_SPACE]:
                isJump = True
                left = False
                right = False
                walkCount = 0
        #code for when space key is pressed(Jumping)
        else:
            if jumpCount >= -10:
                y -= (jumpCount * abs(jumpCount)) * 0.7
                if level==1:
                    if x >525 and x < 780 and y < 560:
                        jump=False
                        jumpCount -=1
                    if x >100 and x < 350 and y <460:
                        jump=False
                        jumpCount -=1
                    if x >525 and x < 780 and y < 300:
                        jump=False
                        jumpCount -=1
                    if x >525 and x < 780 and y < 100:
                        jump=False
                        jumpCount -=1
                        #Platform retrictions for window 1
                if level==2:
                    if x >555 and x < 800 and y < 540:
                        jump=False
                        jumpCount -=1
                    if x >250 and x < 500 and y < 470:
                        jump=False
                        jumpCount -=1
                    if x >555 and x < 800 and y < 400:
                        jump=False
                        jumpCount -=1
                    if x >250 and x < 500 and y < 330:
                        jump=False
                        jumpCount -=1
                    if x >555 and x < 800 and y < 260:
                        jump=False
                        jumpCount -=1
                    if x >250 and x < 500 and y < 190:
                        jump=False
                        jumpCount -=1
                    if x >555 and x < 800 and y < 120:
                        jump=False
                        jumpCount -=1
                    if x >250 and x < 500 and y < 50:
                        jump=False
                        jumpCount -=1
                        #Platform restrictions for window 2  
                jumpCount -= 1
            else: 
                jumpCount=10
                isJump = False
        #These are all of the window screens and they correspond with the levels
        if level==1: 
            redrawGameWindowL1() 
        if level==2:
            redrawGameWindowL2()
        if level==3:
            redrawGameWindowL3()
        if winscreen==1:
            windisplay()
            py.time.delay(2000)
            pygame.quit()
    pygame.quit()
    #THis ends the game
def level2():
    #Everything is the same as before
    from os import X_OK
    import pygame
    global x, y, walkCount, level
    pygame.init()
    win = pygame.display.set_mode((800,800))
    pygame.display.set_caption("First Game")
    walkRight = [pygame.image.load('gameImages\\sprite2.png'), pygame.image.load('gameImages\\sprite3.png'), pygame.image.load('gameImages\\sprite2.png'), pygame.image.load('gameImages\\sprite6.png')]
    walkLeft = [pygame.image.load('gameImages\\sprite4.png'), pygame.image.load('gameimages\\sprite5.png'), pygame.image.load('gameimages\\sprite7.png'), pygame.image.load('gameimages\\sprite4.png')]
    bg=pygame.image.load('gameImages\\forest background.jpg')
    char=pygame.image.load('gameImages\\standing1.png')
    smallplat=pygame.image.load('gameImages\\smallplatform.png')
    regplat=pygame.image.load('gameImages\\platform.png')
    midplat=pygame.image.load('gameImages\\middleplatform.png')
    if sound==0:
        game_sound = pygame.mixer.Sound("DK's Jungle Park - Mario Kart 64.wav")
        pygame.mixer.music.load("DK's Jungle Park - Mario Kart 64.wav")
        pygame.mixer.music.play(-1)
    star=pygame.image.load('gameImages\\star.png')
    trophy=pygame.image.load('gameImages\\trophy.png')
    life=pygame.image.load('gameImages\\life.png')
    podium=pygame.image.load('gameimages\\podium.jpg   ')
    x = 50
    y = 665
    width = 40
    height = 60
    vel = 30
    walkCount=0
    clock = pygame.time.Clock()
    lifecount=3
    isJump = False
    jumpCount = 10
    left = False
    right = False
    level=1
    death=0
    check = 0
    def redrawGameWindowL1():
        global walkCount, y, x, level
        win.blit(bg, (0,0)) 
        if lifecount==3:
            win.blit(life, (50,50))
            win.blit(life, (100,50))
            win.blit(life, (150,50))
        if lifecount==2:
            win.blit(life, (50,50))
            win.blit(life, (100,50))
        if lifecount==1:
            win.blit(life, (50,50))
        #Lifecount is new, it is the code for the hearts in the top left corner, the hearts make it so that when you hit the ground you lose a life
        #Three lives lost and you lose the game   
        win.blit(regplat,(-10,725)) 
        platform=pygame.Rect(540, 630, 225,30)
        platformColor=((0,255,0))
        # pygame.draw.rect(win, platformColor, platform)
        if level==1:
            win.blit(regplat,(450,725)) 
            win.blit(midplat,(350,725))
            win.blit(smallplat,(525,610))
            win.blit(smallplat,(100,500))
            win.blit(smallplat,(525,390))
            win.blit(smallplat,(100,280))
            win.blit(smallplat,(525,170))
        if y<-50:
            level=2
        if level ==2:
            win.blit(bg, (0,0))
            if walkCount + 1 >= 12:
                walkCount = 0
            if left:  
                win.blit(walkLeft[walkCount//3], (x,y))
                walkCount += 1                          
            elif right:
                win.blit(walkRight[walkCount//3], (x,y))
                walkCount += 1
            else:
                win.blit(char, (x, y))
                walkCount = 0
            pygame.display.update() 
            #all the same as level 1
        # if level==2:
        #     print("its working")
        #     win.blit(bg, (0,0)) 
        if walkCount + 1 >= 12:
            walkCount = 0   
        if left:  
            win.blit(walkLeft[walkCount//3], (x,y))
            walkCount += 1                          
        elif right:
            win.blit(walkRight[walkCount//3], (x,y))
            walkCount += 1
        else:
            win.blit(char, (x, y))
            walkCount = 0   
        pygame.display.update() 
    check=0
    x=50
    y=650
    def deathscreen():
        win.blit(bg, (0,0))
        display_message('Game Over')
        #This is the deathscreen that shows after you lose three lives
    def redrawGameWindowL2():
        global walkCount, check, x, y, level
        # if check == 0:
        #     x=50
        #     y=650 
        win.blit(bg, (0,0)) 
        if lifecount==3:
            win.blit(life, (50,50))
            win.blit(life, (100,50))
            win.blit(life, (150,50))
        if lifecount==2:
            win.blit(life, (50,50))
            win.blit(life, (100,50))
        if lifecount==1:
            win.blit(life, (50,50))
        #Lifecount again
        win.blit(regplat,(-10,725)) 
        platform=pygame.Rect(540, 630, 225,30)
        platformColor=((0,255,0))
        win.blit(smallplat, (550, 590))
        win.blit(smallplat, (250, 520))
        win.blit(smallplat, (550, 450))
        win.blit(smallplat, (250, 380))
        win.blit(smallplat, (550, 310))
        win.blit(smallplat, (250, 250))
        win.blit(smallplat, (550, 180))
        # win.blit(smallplat, (250, 110))
        # win.blit(smallplat, (550, 40))
        # pygame.draw.rect(win, platformColor, platform)
        # win.blit(regplat,(450,725)) 
        # win.blit(midplat,(350,725))
        # win.blit(smallplat,(525,610))
        # win.blit(smallplat,(100,500))
        # win.blit(smallplat,(525,390))
        # win.blit(smallplat,(100,280))
        # win.blit(smallplat,(525,170))
        # if level==1 and x<0:
        #     level+=1
        # if level==2:
        #     print("its working")
        #     win.blit(bg, (0,0)) 
        if walkCount + 1 >= 12:
            walkCount = 0 
        if left:  
            win.blit(walkLeft[walkCount//3], (x,y))
            walkCount += 1                          
        elif right:
            win.blit(walkRight[walkCount//3], (x,y))
            walkCount += 1
        else:
            win.blit(char, (x, y))
            walkCount = 0 
        pygame.display.update() 
    def redrawGameWindowL3():
        global walkCount, check, x, y, level
        # if check == 0:
        #     x=50
        #     y=650 
        win.blit(bg, (0,0))
        if lifecount==3:
            win.blit(life, (50,50))
            win.blit(life, (100,50))
            win.blit(life, (150,50))
        if lifecount==2:
            win.blit(life, (50,50))
            win.blit(life, (100,50))
        if lifecount==1:
            win.blit(life, (50,50))
        #Lifecount
        win.blit(regplat,(710,725)) 
        win.blit(regplat,(-300,725)) 
        win.blit(smallplat,(350,725)) 
        win.blit(star, (25,500)) 
        platform=pygame.Rect(540, 630, 225,30)
        platformColor=((0,255,0))
        # pygame.draw.rect(win, platformColor, platform)
        # win.blit(regplat,(450,725)) 
        # win.blit(midplat,(350,725))
        # win.blit(smallplat,(525,610))
        # win.blit(smallplat,(100,500))
        # win.blit(smallplat,(525,390))
        # win.blit(smallplat,(100,280))
        # win.blit(smallplat,(525,170))
        # if level==1 and x<0:
        #     level+=1
        # if level==2:
        #     print("its working")
        #     win.blit(bg, (0,0)) 
        if walkCount + 1 >= 12:
            walkCount = 0   
        if left:  
            win.blit(walkLeft[walkCount//3], (x,y))
            walkCount += 1                          
        elif right:
            win.blit(walkRight[walkCount//3], (x,y))
            walkCount += 1
        else:
            win.blit(char, (x, y))
            walkCount = 0   
        pygame.display.update() 
    def windisplay():
        global x, y
        win.blit(bg, (0,0)) 
        win.blit(trophy, (335,300))
        win.blit(smallplat, (290, 615))
        win.blit(char, (375,550))
        #Windisplay again
        pygame.display.update() 
    winscreen=0
    run = True
    score=0
    while run:
        clock.tick(12)
        #This runs everything again
        print(score)
        if winscreen==1:
            print(score)
        else:
            score+=1
        mouse_pos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        # if x <525 and x>700 and y< 560:
        #     y=675 
        if keys[pygame.K_LEFT] and x > vel: 
            x -= vel
            left = True
            right = False
        elif keys[pygame.K_RIGHT] and x < 800 - vel - width:  
            x += vel
            left = False
            right = True 
        else: 
            left = False
            right = False
            walkCount = 0
        if x>320 and x<500 and y < 650 and jumpCount == 10 and level ==1:
            y=665
            jump=False
            lifecount-=1
        if x>20 and x<80 and y < 650 and jumpCount == 10 and level ==1:
            y=665
            jump=False
            lifecount-=1
        if x>20 and x<600 and y < 20 and jumpCount == 10 and level ==2:
            y=665
            jump=False
        if level ==2 and x>400 and x<800 and y<670 and y > 660 and jumpCount == 10:
            x=50
            jump=False
            lifecount-=1
        if y<0 and x<800 and x>700:
            level =3
        if x>700 and x<800 and y < 650 and jumpCount == 10 and level ==3:
            y=665
            x=780
            jump=False
            #The restrictions that dont subtract life are the ones that ensure the character spawns in the correct place
        if x>0 and x<50 and y<600 and level==3:
            winscreen=1
            level=4    
        if x>50 and x < 650 and y<680 and level==3 and jumpCount==10:
            x=750
            y=665
            jump=False
            lifecount-=1
        #restricitons that subtract the lifecounts
        if not(isJump):
            if keys[pygame.K_SPACE]:
                isJump = True
                left = False
                right = False
                walkCount = 0
        else:
            if jumpCount >= -10:
                y -= (jumpCount * abs(jumpCount)) * 0.7
                if level==1:
                    if x >525 and x < 780 and y < 560:
                        jump=False
                        jumpCount -=1
                    if x >100 and x < 350 and y <460:
                        jump=False
                        jumpCount -=1
                    if x >525 and x < 780 and y < 300:
                        jump=False
                        jumpCount -=1
                    if x >525 and x < 780 and y < 100:
                        jump=False
                        jumpCount -=1
                if level==2:
                    if x >555 and x < 800 and y < 540:
                        jump=False
                        jumpCount -=1
                    if x >250 and x < 500 and y < 470:
                        jump=False
                        jumpCount -=1
                    if x >555 and x < 800 and y < 400:
                        jump=False
                        jumpCount -=1
                    if x >250 and x < 500 and y < 330:
                        jump=False
                        jumpCount -=1
                    if x >555 and x < 800 and y < 260:
                        jump=False
                        jumpCount -=1
                    if x >250 and x < 500 and y < 190:
                        jump=False
                        jumpCount -=1
                    if x >555 and x < 800 and y < 120:
                        jump=False
                        jumpCount -=1
                    if x >250 and x < 500 and y < 50:
                        jump=False
                        jumpCount -=1
                    #retrictions
                jumpCount -= 1
            else: 
                jumpCount=10
                isJump = False
        if level==1:
            redrawGameWindowL1() 
        if level==2:
            redrawGameWindowL2()
        if level==3:
            redrawGameWindowL3()
        if winscreen==1:
            windisplay()
            py.time.delay(4000)
            pygame.quit()
        if lifecount==0:
            deathscreen()
            py.time.delay(4000)
            pygame.quit()
            #deathscreen
    pygame.quit()
#This is my menu display
def display_Menu():
    x=70
    y=190
    square.x=x
    square.y=y
    counter=1
    back=1
    for i in range(0, len(messages)):
        word= messages[i]
        py.draw.rect(win, PURPLE, square)
        text=SUBTITLE_FONT.render(word,10, BLACK)
        win.blit(text, (x+wbox+10, y))
        py.display.flip()
        py.time.delay(100)
        y += 100
        square.y=y
        py.display.set_caption("Menu Window")
        #menu window list of words that show after the purple swuare
win.fill(WHITE)
display_message('Jungle Jumpers')
#menu Title
ysub=200
py.time.delay(200)
display_Menu()

run=True
counter=1
back=1
#This is my running menu code
while run:
    clock.tick(27)
    for eve in py.event.get():
        if eve.type == py.QUIT:
            run=False
    if eve.type==py.MOUSEBUTTONDOWN:
        mouse_pressed=py.mouse.get_pressed()
        if mouse_pressed[0]:
            mouse_pos=py.mouse.get_pos()
            print(mouse_pos)
            if mouse_pos[0]>=70 and mouse_pos[0]<=95 and mouse_pos[1]>490 and mouse_pos[1]<515 and counter==1:
                win.fill(WHITE)
                display_message("Settings")
                py.display.set_caption("Setting Window")
                mouse_pos=py.mouse.get_pos()
                counter +=1
                #setting window
                x=70
                y=190
                square.x=x
                square.y=y
                for i in range(0, len(messages2)):
                    word= messages2[i]
                    py.draw.rect(win, PURPLE, square)
                    text=SUBTITLE_FONT.render(word,10, BLACK)
                    win.blit(text, (x+wbox+10, y))
                    py.display.flip()
                    py.time.delay(100)
                    y += 100
                    square.y=y
                back+=1
                x=660
                y=730
                square.x=x
                square.y=y
                for i in range(0,len(bmessages)):
                    word= bmessages[i]
                    py.draw.rect(win, PURPLE, square)
                    text=SUBTITLE_FONT.render(word,10, BLACK)
                    win.blit(text, (x+wbox+10, y))
                    py.display.flip()
                    #All the words after the purple squares in settings
                    square.y=y           
            if mouse_pos[0]>70 and mouse_pos[0]<=95 and mouse_pos[1]>685 and mouse_pos[1]<=715 and counter==1:
                win.fill(WHITE)
                display_message('Thanks for playing!')
                py.time.delay(1000)
                py.quit()
                #Exit button code 
            if mouse_pos[0]>70 and mouse_pos[0]<=95 and mouse_pos[1]>185 and mouse_pos[1]<=215 and counter==1:
                win.fill(WHITE)
                display_message('Instructions')
                py.display.set_caption("instructions window")
                x=70
                y=190
                square.x=x
                square.y=y
                #instructions window code
                for i in range(0, len(imessages)):
                    word= imessages[i]
                    py.draw.rect(win, PURPLE, square)
                    text=SUBTITLE_FONT.render(word,10, BLACK)
                    win.blit(text, (x+wbox+10, y))
                    py.display.flip()
                    py.time.delay(100)
                    y += 100
                    square.y=y
                x=660
                y=730
                square.x=x
                square.y=y
                for i in range(0,len(bmessages)):
                    word= bmessages[i]
                    py.draw.rect(win, PURPLE, square)
                    text=SUBTITLE_FONT.render(word,10, BLACK)
                    win.blit(text, (x+wbox+10, y))
                    py.display.flip()
                    #back button part
                    square.y=y
            if mouse_pos[0]>70 and mouse_pos[0]<=95 and mouse_pos[1]>185 and mouse_pos[1]<=215 and counter==2:
                win.fill(WHITE)
                display_message('Screen Size')
                py.display.set_caption("Screen Size Window")
                x=70
                y=190
                square.x=x
                square.y=y
                #Screen size window
                for i in range(0, len(Ssmessages)):
                    word= Ssmessages[i]
                    py.draw.rect(win, PURPLE, square)
                    text=SUBTITLE_FONT.render(word,10, BLACK)
                    win.blit(text, (x+wbox+10, y))
                    py.display.flip()
                    py.time.delay(100)
                    y += 100
                    square.y=y
                display_back()
                counter+=1
                back+=1
                #I realized I can use display back here
            if mouse_pos[0]>660 and mouse_pos[0]<=685 and mouse_pos[1]>730 and mouse_pos[1]<=755 and back==2:
                win.fill(WHITE)
                display_message('Jungle Jumpers')
                counter-=1
                back-=1
                display_Menu()
                #This is for the back button in settings
            if mouse_pos[0]>660 and mouse_pos[0]<=685 and mouse_pos[1]>730 and mouse_pos[1]<=755 and back==1:
                win.fill(WHITE)
                display_message('Jungle Jumpers')
                #back button on instructions
                display_Menu()
            if mouse_pos[0]>=70 and mouse_pos[0]<=95 and mouse_pos[1]>290 and mouse_pos[1]<315 and counter==1:
                level1_game()
                display_back()
                back+=1
                counter+=1
                #Level 1 game run code
            if mouse_pos[0]>=70 and mouse_pos[0]<=95 and mouse_pos[1]>390 and mouse_pos[1]<415 and counter==1:
                level2()
                display_back()
                back+=1
                counter+=1
                #Level 2 game run code
            if mouse_pos[0]>=70 and mouse_pos[0]<=95 and mouse_pos[1]>290 and mouse_pos[1]<315 and counter==2:
                sound=1
                #Sound on and off code
            if mouse_pos[0]>=70 and mouse_pos[0]<=95 and mouse_pos[1]>390 and mouse_pos[1]<415 and counter==2:
                sound=0
                #sound on and off code
            if mouse_pos[0]>660 and mouse_pos[0]<=685 and mouse_pos[1]>730 and mouse_pos[1]<=755 and back==3:
                win.fill(WHITE)
                #returning to the settings menu code
                counter-=1
                back-=1
                win.fill(WHITE)
                display_message("Settings")
                py.display.set_caption("Setting Window")
                mouse_pos=py.mouse.get_pos()
                back-=1
                x=70
                y=190
                square.x=x
                square.y=y
                for i in range(0, len(messages2)):
                    word= messages2[i]
                    py.draw.rect(win, PURPLE, square)
                    text=SUBTITLE_FONT.render(word,10, BLACK)
                    win.blit(text, (x+wbox+10, y))
                    py.display.flip()
                    py.time.delay(100)
                    y += 100
                    square.y=y
                back+=1
                x=660
                y=730
                square.x=x
                square.y=y
                for i in range(0,len(bmessages)):
                    word= bmessages[i]
                    py.draw.rect(win, PURPLE, square)
                    text=SUBTITLE_FONT.render(word,10, BLACK)
                    win.blit(text, (x+wbox+10, y))
                    py.display.flip()
                    square.y=y    
            if mouse_pos[0]>70 and mouse_pos[0]<=95 and mouse_pos[1]>190 and mouse_pos[1]<=215 and counter==3:
                WIDTH+=50
                HEIGHT+=50
                win=py.display.set_mode((WIDTH,HEIGHT))   
                display_back
                #Screen size larger code
            if mouse_pos[0]>70 and mouse_pos[0]<=95 and mouse_pos[1]>290 and mouse_pos[1]<315 and counter==3:
                WIDTH-=50
                HEIGHT-=50
                win=py.display.set_mode((WIDTH,HEIGHT))   
                display_back
            #Screen size smaller code
            # if py.Rect.collidepoint(square, mouse_pressed):
            #     win.fill
            # display_message("Start Game")
            # ysub=200
            # py.time.delay(300)
            # displaySub("Screen Size", ysub)
            # ysub+=125
            # displaySub("Background Colors", ysub)
            # py.time.delay(100)
            # ysub+=125
            # displaySub("Object color", ysub)
            # py.time.delay(100)
            # ysub+=125
            # displaySub("Sound On/Off", ysub)
