import pygame
import pygame.gfxdraw
import sys
import math
import time
import serial

white = (255, 255, 255)
blue = (0, 0, 128)
black = (0, 0, 0)


pygame.init()
size_x = 800
size_y = 480
screen = pygame.display.set_mode((800, 480))
#bg_surface = pygame.image.load('').convert()
clock = pygame.time.Clock()

menu_var = 0
total_menus = 3
velocity_deg = 140


while True:
    for event in pygame.event.get():
        accel = False
        brake = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if menu_var == 3:
                    menu_var = 0
                else:
                    menu_var = menu_var + 1
            if event.key == pygame.K_LEFT:
                if menu_var == 0:
                    menu_var = 3
                else:
                    menu_var = menu_var - 1
            if  event.key == pygame.K_UP:
                accel = True
                velocity_deg = velocity_deg + 1

            if event.key == pygame.K_DOWN:
                accel = False
                brake = True
                velocity_deg = velocity_deg - 1


        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if menu_var == 0:
        screen.fill(white)
        pygame.gfxdraw.aacircle(screen, 200, 280, 100, blue)
        pygame.gfxdraw.aacircle(screen, 200, 280, 10, blue)
        pygame.gfxdraw.aacircle(screen, 600, 280, 100, blue)
        pygame.gfxdraw.line(screen, 0, 350, 800, 350, blue)
        pygame.gfxdraw.pie(screen, 200, 280, 90, int(velocity_deg), int(velocity_deg), blue)



    if menu_var == 1:
        screen.fill((128,0,0))
        pygame.gfxdraw.aacircle(screen, 200, 280, 100, blue)
        pygame.gfxdraw.aacircle(screen, 200, 280, 10, blue)
        pygame.gfxdraw.aacircle(screen, 600, 280, 100, blue)
        pygame.gfxdraw.line(screen, 0, 350, 800, 350, blue)
        pygame.gfxdraw.pie(screen, 200, 280, 90, int(velocity_deg), int(velocity_deg), blue)


    pygame.display.update()
    clock.tick(120)


