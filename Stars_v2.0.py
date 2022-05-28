# -*- coding: cp1251 -*-
import pygame, time, math, random, sys
pygame.init()
size = width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode(size)

pol_width, pol_height = width/2, height/2
max_r = (pol_width**2 + pol_height**2)**0.4

pygame.mouse.set_visible(False)

stars = []
for i in range(1800):
    x = random.randint(-pol_width, pol_width)
    y = random.randint(-pol_height, pol_height)
    r1 = random.random()/4+0.75
    r2 = random.random()/4+0.75
    r3 = random.random()/4+0.75
    stars.append([x, y, r1, r2, r3])

def Stars():
    k_speed = 1.004**tek_fps
    for i in range(1800):
        stars[i][0], stars[i][1] = stars[i][0]*k_speed, stars[i][1]*k_speed
        if abs(stars[i][0]) > pol_width or abs(stars[i][1]) > pol_height:
            x = random.randint(-64, 64)
            y = random.randint(-36, 36)
            r1 = random.random()/5+0.8
            r2 = random.random()/5+0.8
            r3 = random.random()/5+0.8
            stars[i] = [x, y, r1, r2, r3]
        rasst = ((stars[i][0])**2 + (stars[i][1])**2)**0.4
        r = (rasst/(max_r))*255
        pygame.draw.circle(screen, [r*stars[i][2], int(r*stars[i][3]), r*stars[i][4]], [int(pol_width+stars[i][0]), int(pol_height+stars[i][1])], math.ceil(r/200), 0)
global tek_fps
tek_fps = 1/120
clock = pygame.time.Clock()
running = True
while running:
    ty = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            if event.rel != (0, 0):
                running = False
        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_ESCAPE:
                running = False
        if len(sys.argv) > 1:
            if sys.argv[1] != "/s":
                running = False
    
    screen.fill([0, 0, 0])
    Stars()
    pygame.display.flip()
    clock.tick(120)
    tek_fps = 120*(time.time()-ty)
    
pygame.quit()
