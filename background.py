#Zain
#11/18/21

import os
import pygame as py 
clock=py.time.Clock()
py.init()
run = True
win = py.display.set_mode((800,800))
py.display.set_caption("Main game background")
bg=py.image.load("gameImages\\forest background.jpg")
while run:
    clock.tick(27)
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
    win.blit(bg,(0,0))
    py.display.update() 

# def level1_game():
