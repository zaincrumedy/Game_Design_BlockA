#Zain
#10/25

import pygame as py, os, random, time
py.init()
BLACK=(255,255,255)
WHITE=(0,0,0)
PURPLE=(150,0,150)
WIDTH = 800
HEIGHT = 800
messages=['Start Game','Screen Size','Background Colors','Object color','Sound On/Off']
win=py.display.set_mode((WIDTH,HEIGHT))
py.display.set_caption("Setting Window")
#TITLE_FONT= py.font.SysFont(name,size,bold=false, italic= false)
TITLE_FONT= py.font.SysFont('comicsans', 30, italic=True)
SUBTITLE_FONT= py.font.SysFont('comicsans', 30, italic=True)
xbox=25
wbox=25
square=py.Rect(10,10, wbox, xbox)

def display_message(message):
    py.time.delay(100)
    text=TITLE_FONT.render(message,1, BLACK )
    win.blit(text, (WIDTH/2-text.get_width()/2, 30) )
    py.display.update()
    py.time.delay(10)

def displaySub(subTitle,ysub):
    py.time.delay(100)
    text=SUBTITLE_FONT.render(subTitle,1, BLACK )
    win.blit(text, (10, ysub ))
    py.display.update()
    py.time.delay(10)


def display_Menu():
    x=70
    y=190
    square.x=x
    square.y=y
    for i in range(0, len(messages)):
        word= messages[i]
        py.draw.rect(win, PURPLE, square)
        text=TITLE_FONT.render(word,10, BLACK)
        win.blit(text, (x+wbox+10, y))
        py.display.flip()
        py.time.delay(100)
        y += 100
        square.y=y

win.fill(WHITE)
display_message('Settings')
py.time.delay(200)
display_Menu()
run=True
while run:
    for eve in py.event.get():
        if eve.type == py.QUIT:
            run=False
    if eve.type==py.MOUSEBUTTONDOWN:
        mouse_pressed=py.mouse.get_pressed()
        if mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1] >=190 and mouse_pos
        win.fill(WHITE)
        display_Title("Screen Size", WIDTH/2-text)
            mouse_pos=py.mouse.get_pos()

            if py.Rect.collidepoint(square, mouse_pressed):
                win.fill
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

    print(py.mouse.get_pos())
    
py.quit()