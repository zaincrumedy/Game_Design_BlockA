#Zain
#10/25

import pygame as py, os, random, time
py.init()
BLACK=(255,255,255)
WIDTH = 800
HEIGHT = 800
win=py.display.set_mode((WIDTH,HEIGHT))
py.display.set_caption("Setting Window")
#TITLE_FONT= py.font.SysFont(name,size,bold=false, italic= false)
TITLE_FONT= py.font.SysFont('comicsans', 40, italic=True)
def display_message(message):
    py.time.delay(100)
    text=TITLE_FONT.render(message,1, BLACK )
    win.blit(text, (WIDTH/2-text.get_width()/2, HEIGHT/2-text.get_height()/2) )
    py.display.update()
    py.time.delay(10)


run=True
while run:
    for eve in py.event.get():
        if eve.type == py.QUIT:
            run=False
            py.quit()
    display_message("words")
    py.time.delay(300)
    win.fill((0,0,0))
    display_message("words")
    py.time.delay(700)
    win.fill((0,0,0))
    display_message("words")
    py.time.delay(500)
    win.fill((0,0,0))
py.quit()