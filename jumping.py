#MAria Suarez
#10/20/2021
# Mouse position
# drawing rect
# moving object
# K_UP                  up arrow
# K_DOWN                down arrow
# K_RIGHT               right arrow
# K_LEFT                left arrow
import os
import pygame as py 

py.init()

win = py.display.set_mode((500,500))
py.display.set_caption("First Game")

walkRight = [py.image.load('gameImages\\R1.png'), py.image.load('gameImages\\R2.png'), py.image.load('gameImages\\R3.png'), py.image.load('gameImages\\R4.png'), py.image.load('gameImages\\R5.png'), py.image.load('gameImages\\R6.png')]
walkLeft = [py.image.load('gameImages\\L1.png'), py.image.load('gameImages\\L2.png'), py.image.load('gameImages\\L3.png'), py.image.load('gameImages\\L4.png'), py.image.load('gameImages\\L5.png'), py.image.load('gameImages\\L6.png')]
bg=py.image.load("gameImages\\bgSmaller1.jpg")
char = py.image.load('gameImages\\standing.png')
clock=py.time.Clock()
x = 50
y = 50
width = 40
height = 60
vel = 5

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0


def redrawGameWindow():
    global walkCount
    
    win.blit(bg, (0,0))  # This will draw our background image at (0,0)
    py.display.update() 
    


run = True

while run:
    clock.tick(18)

    for event in py.event.get():
        if event.type == py.QUIT:
            run = False

    keys = py.key.get_pressed()
    
    if keys[py.K_LEFT] and x > vel: 
        x -= vel

    if keys[py.K_RIGHT] and x < 500 - vel - width:  
        x += vel
        
    if not(isJump): 
        if keys[py.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False

    redrawGameWindow() 
    
    
py.quit()
WIDTH=800
HEIGHT=800
boulder=py.Rect(WIDTH-300, HEIGHT-200, 100,200)
screen=py.display.set_mode((WIDTH,HEIGHT))
#first thing
py.init()
#create window
height= 700
width = 800
colors = {'red':(150,0,0),'green':(0,200,0), 'blue':(0,0,255), 'purple':(150, 0, 150), 'white':(255,255,255), 'black':(0,0,0) }
screen=py.display.set_mode((width, height))
myColor= colors.get('purple')
# bg=py.image.load("gameimages\\bgSmaller1.jpg")
screen.blit(bg, (0,0))
py.display.set_caption("Moving Square")
py.display.flip()
#parameters to define our square
x=width/2
y=height/2
wbox=50
hbox=50
#creating out object square
square=py.Rect(x,y,wbox, hbox )
#draw object
objColor=colors.get('red')
boulderColor=colors.get('blue')
py.draw.rect(screen, objColor, square)
py.draw.rect(screen, boulderColor, boulder)
py.display.update()
#create speed to move the object on the screen
speed = 10
run=True #Variable to control the main loop
#boolean to check for jump
Jumping=False
jumpCount=10
while run:
    py.time.delay(100) #milliseconds
    for anyThing in py.event.get():
        if anyThing.type == py.QUIT:
            run =False
    keyPressed= py.key.get_pressed()
    if keyPressed[py.K_RIGHT] and square.x <WIDTH-wbox-speed:
        if square.colliderect(boulder):
            square.x-=5
        else:
            square.x += speed
    if keyPressed[py.K_LEFT] and square.x>speed-5:
        if square.colliderect(boulder):
            square.x+=5
        else:
            square.x -= speed
    if not(Jumping):
        if keyPressed[py.K_DOWN] and square.y <HEIGHT-hbox-speed:
            if square.colliderect(boulder):
                square.y-=5
            else:
                square.y += speed
    
        if keyPressed[py.K_UP] and square.y>speed-5:
            square.y -= speed
        if keyPressed[py.K_SPACE]:
            Jumping=True
    else:
        if jumpCount >=-10:
            square.y -= jumpCount* abs(jumpCount)*0.5
            jumpCount-=1
            
        else:
            jumpCount=10
            Jumping=False
    
    print(py.mouse.get_pos())
    # if(py.Rect.collidepoint(boulder, (square.x+wbox/2,square.y))):
    #     move=False
    #     square.x=square.x-wbox
    #     move=True
    screen.blit(bg,(0,0))
    py.draw.rect(screen, objColor, square)
    py.draw.rect(screen, boulderColor, boulder)
    py.display.flip()
py.quit()