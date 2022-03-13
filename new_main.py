# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 23:07:52 2022

@author: Manzaca
"""

import time
import sys
import math
from graphics import *
from map_gen import gen_map



print("\n\n\n\n\n\n\n\n\n\n\n")
print('###   PROGRAM Fiona A1.2 - Open Release   ###')
print('\n')
print('Press 1 to enable ray tracing draw (WILL SEVERELY LOWER THE PERFORMANCE)')
print('Press 0 to disable ray tracing draw')
print('\n\n')
print('Use default values? (Y/N): ')
default = input()
if default == 'Y':
    
    
    MAP_SIZE = 10
    MAP_DENS = 30
    accuracy = 5
    framerate = 0
    WIN_SIDE = 600
    player_fov_deg = 80

else:
    
    print('Select map size (recommend lower than 25): ')
    MAP_SIZE = int(input())
    print('Select map density (recommend lower than 40): ')
    MAP_DENS = int(input())
    
    print('set Performance Metrics? (Y/N): ')
    default = input()
    if default == 'Y':
        print('Accuracy (recomend higher than 2 and lower than 7): ')
        accuracy = int(input())
        print('Speed (Higher is faster, recommend 100, set 0 to max speed): ')
        framerate = int(input())
    else:
        accuracy = 5
        framerate = 0
        
        
    print('set Complex values? (Y/N): ')
    default = input()
    if default == 'Y':
        print('Select Window side lenght (in pixels): ')
        WIN_SIDE = int(input())
        print('Player FOV (in deg): ')
        player_fov_deg = int(input())
        
        
        
    else:
        WIN_SIDE = 600
        player_fov_deg = 80


gen_map(MAP_SIZE,MAP_DENS)

# Global Constants

MAP = ''
cake_x = 1
cake_y = 1
player_x = MAP_SIZE - 2
player_y = MAP_SIZE - 2
player_angle = math.pi
view = True


    # Calculate FOV in Radians
player_fov = player_fov_deg/(180/math.pi)

imortal = False
counts = 0
counts2 = 0


# PERFORMANCE METRICS

rotation_speed = math.pi * 0.01
check_fq = 60




# Global Variables

up = False
left = False
right = False
bingo = False
ray_view = False
check_count = 0
do_check = True
homing = False
stuck = False
stored_x = 0
stored_y = 0
old_x = ''
old_y = ''
switch = True
count1 = 0
count3 = 0
steps = 2 * math.pi /rotation_speed




# Window Creation


win = GraphWin("Fiona - Alpha 1.1 ", WIN_SIDE, WIN_SIDE)




# MAP

    # open and manage MAP file
with open('map.txt','r') as file:
    file_first_line = file.readline()

    # check map size

MAP_SIZE = len(file_first_line) - 1

    # add file lines to MAP
count = 0
while count < MAP_SIZE:
    with open('map.txt','r') as file:
        content = file.readlines()
        MAP = MAP + content[count]
    count += 1

    # replace line breaks    
MAP = MAP.replace("\n","") 
   
    # Calculate square side (pixels)
SQUARE_SIDE = WIN_SIDE//MAP_SIZE

    # Calculate initial player position
player_x = player_x * SQUARE_SIDE + SQUARE_SIDE/2
player_y = player_y * SQUARE_SIDE + SQUARE_SIDE/2


for row in range(MAP_SIZE):
    for col in range(MAP_SIZE):
        
        #calculate map string index
            
        index = row * MAP_SIZE + col
        
        if MAP[index] == '#':
            map_square=Rectangle(Point(col*SQUARE_SIDE, row*SQUARE_SIDE),Point(col*SQUARE_SIDE + SQUARE_SIDE, row*SQUARE_SIDE + SQUARE_SIDE))
            map_square.setFill("grey")
            map_square.draw(win)

    # Calculate player radius
    
    player_radius = 0.15 * WIN_SIDE / MAP_SIZE
            
cake=Circle(Point(cake_x * SQUARE_SIDE + SQUARE_SIDE/2 ,cake_y * SQUARE_SIDE + SQUARE_SIDE/2 ), player_radius)
cake.setFill("red")
cake.draw(win)

player=Circle(Point(player_x ,player_y ), player_radius)
player.setFill("green")
player.draw(win)

def death():
    if not imortal == True:
        time.sleep(0)
        win.close()
        sys.exit(0)

def move_player():
    
    global do_check
    global player_x
    global player_y
    global player_angle
    global up
    global left
    global right
    global ray_view
    
    pressed = win.checkKey()
    if pressed == "c":
        do_check = True
    if pressed == "0":
        ray_view = False
    if pressed == "1":
        ray_view = True
    if pressed == "2":
        view = True
    if pressed == "3":
        print('herereeeeeeeeeeee')
        view = False
    
    
    
    if pressed == "Left" or left == True:
        player_angle += rotation_speed
    if pressed == "Right" or right == True:
        player_angle -= rotation_speed
    
    if pressed == "Up" or up == True:
        player_x = player_x + 2 * math.sin(player_angle)
        player_y = player_y + 2 * math.cos(player_angle)
        player.move(2*math.sin(player_angle),2*math.cos(player_angle))
        
    up = False
    left = False
    right = False
    
  
def rt():
    
    global bingo 
    
    
    
    rt.cake_col = False
    rt.ray_colision = False
    rt.ray_f_x = player_x
    rt.ray_f_y = player_y
    rt.ray_1_x = player_x
    rt.ray_1_y = player_y
    rt.ray_2_x = player_x
    rt.ray_2_y = player_y
    rt.ray_f_x_col = 0
    rt.ray_f_y_col = 0
    rt.ray_1_x_col = 0
    rt.ray_1_y_col = 0
    rt.ray_2_x_col = 0
    rt.ray_2_y_col = 0
    rt.ray_1l_x = player_x
    rt.ray_1l_y = player_y
    rt.ray_2l_x = player_x
    rt.ray_2l_y = player_y
    rt.ray_1l_x_col = 0
    rt.ray_1l_y_col = 0
    rt.ray_2l_x_col = 0
    rt.ray_2l_y_col = 0
    
    while rt.ray_colision == False:
        
        rt.ray_f_x = rt.ray_f_x + accuracy * math.sin(player_angle)
        rt.ray_f_y = rt.ray_f_y +  accuracy * math.cos(player_angle)
        rt.ray_1_x = rt.ray_1_x + accuracy * math.sin(player_angle + player_fov/2)
        rt.ray_1_y = rt.ray_1_y +  accuracy * math.cos(player_angle + player_fov/2)
        rt.ray_2_x = rt.ray_2_x + accuracy * math.sin(player_angle - player_fov/2)
        rt.ray_2_y = rt.ray_2_y + accuracy * math.cos(player_angle - player_fov/2)
        rt.ray_1l_x = rt.ray_1l_x + accuracy * math.sin(player_angle + math.pi/2)
        rt.ray_1l_y = rt.ray_1l_y +  accuracy * math.cos(player_angle + math.pi/2)
        rt.ray_2l_x = rt.ray_2l_x + accuracy * math.sin(player_angle - math.pi/2)
        rt.ray_2l_y = rt.ray_2l_y + accuracy * math.cos(player_angle - math.pi/2)
        
      
    
        if rt.ray_f_x_col == 0:
            
            if  (math.sqrt( ( ( (cake_x * SQUARE_SIDE + SQUARE_SIDE/2) - rt.ray_f_x ) ** 2) + ( ( (cake_y * SQUARE_SIDE + SQUARE_SIDE/2) - rt.ray_f_y ) ** 2)  )) <=   player_radius:
                rt.ray_f_x_col = rt.ray_f_x
                rt.ray_f_y_col = rt.ray_f_y
                rt.cake_col = True
                bingo = True
                
                
    
    
        if rt.ray_1_x_col == 0:
            
            if  (math.sqrt( ( ( (cake_x * SQUARE_SIDE + SQUARE_SIDE/2) - rt.ray_1_x ) ** 2) + ( ( (cake_y * SQUARE_SIDE + SQUARE_SIDE/2) - rt.ray_1_y ) ** 2)  )) <=   player_radius:
                rt.ray_1_x_col = rt.ray_1_x
                rt.ray_1_y_col = rt.ray_1_y
                rt.cake_col = True
          
        if rt.ray_1l_x_col == 0:
            
            if  (math.sqrt( ( ( (cake_x * SQUARE_SIDE + SQUARE_SIDE/2) - rt.ray_1l_x ) ** 2) + ( ( (cake_y * SQUARE_SIDE + SQUARE_SIDE/2) - rt.ray_1l_y ) ** 2)  )) <=   player_radius:
                rt.ray_1l_x_col = rt.ray_1l_x
                rt.ray_1l_y_col = rt.ray_1l_y
                rt.cake_col = True
            
        if rt.ray_2_x_col == 0:
            
            if  (math.sqrt( ( ( (cake_x * SQUARE_SIDE + SQUARE_SIDE/2) - rt.ray_2_x ) ** 2) + ( ( (cake_y * SQUARE_SIDE + SQUARE_SIDE/2) - rt.ray_2_y ) ** 2)  )) <=   player_radius:
                rt.ray_2_x_col = rt.ray_2_x
                rt.ray_2_y_col = rt.ray_2_y
                rt.cake_col = True
          
        if rt.ray_2l_x_col == 0:
            
            if  (math.sqrt( ( ( (cake_x * SQUARE_SIDE + SQUARE_SIDE/2) - rt.ray_2l_x ) ** 2) + ( ( (cake_y * SQUARE_SIDE + SQUARE_SIDE/2) - rt.ray_2l_y ) ** 2)  )) <=   player_radius:
                rt.ray_2l_x_col = rt.ray_2l_x
                rt.ray_2l_y_col = rt.ray_2l_y
                rt.cake_col = True
                
           
            
        for row in range(MAP_SIZE):
            for col in range(MAP_SIZE):
        
                #calculate map string index
                
                index = row * MAP_SIZE + col
                if MAP[index] == '#':
                    
                    if rt.ray_f_x_col == 0:
                        if rt.ray_f_x >= col*SQUARE_SIDE:
                            if rt.ray_f_x <= (col*SQUARE_SIDE + SQUARE_SIDE):
                                if rt.ray_f_y >= row*SQUARE_SIDE:
                                    if rt.ray_f_y <= (row*SQUARE_SIDE + SQUARE_SIDE):
                                        rt.ray_f_x_col = rt.ray_f_x
                                        rt.ray_f_y_col = rt.ray_f_y
            
                index = row * MAP_SIZE + col
                if MAP[index] == '#':
                    
                    if rt.ray_1_x_col == 0:
                        if rt.ray_1_x >= col*SQUARE_SIDE:
                            if rt.ray_1_x <= (col*SQUARE_SIDE + SQUARE_SIDE):
                                if rt.ray_1_y >= row*SQUARE_SIDE:
                                    if rt.ray_1_y <= (row*SQUARE_SIDE + SQUARE_SIDE):
                                        rt.ray_1_x_col = rt.ray_1_x
                                        rt.ray_1_y_col = rt.ray_1_y
                                        
                                        
                index = row * MAP_SIZE + col
                if MAP[index] == '#':
                    if rt.ray_2_x_col == 0:
                        if rt.ray_2_x >= col*SQUARE_SIDE:
                            if rt.ray_2_x <= (col*SQUARE_SIDE + SQUARE_SIDE):
                                if rt.ray_2_y >= row*SQUARE_SIDE:
                                    if rt.ray_2_y <= (row*SQUARE_SIDE + SQUARE_SIDE):
                                        rt.ray_2_x_col = rt.ray_2_x
                                        rt.ray_2_y_col = rt.ray_2_y
                                        
                    if rt.ray_1l_x_col == 0:
                        if rt.ray_1l_x >= col*SQUARE_SIDE:
                            if rt.ray_1l_x <= (col*SQUARE_SIDE + SQUARE_SIDE):
                                if rt.ray_1l_y >= row*SQUARE_SIDE:
                                    if rt.ray_1l_y <= (row*SQUARE_SIDE + SQUARE_SIDE):
                                        rt.ray_1l_x_col = rt.ray_1l_x
                                        rt.ray_1l_y_col = rt.ray_1l_y                                        
                          
                    if rt.ray_2l_x_col == 0:
                        if rt.ray_2l_x >= col*SQUARE_SIDE:
                            if rt.ray_2l_x <= (col*SQUARE_SIDE + SQUARE_SIDE):
                                if rt.ray_2l_y >= row*SQUARE_SIDE:
                                    if rt.ray_2l_y <= (row*SQUARE_SIDE + SQUARE_SIDE):
                                        rt.ray_2l_x_col = rt.ray_2l_x
                                        rt.ray_2l_y_col = rt.ray_2l_y                
                          
                            
        if not rt.ray_1_x_col == 0:
            if not rt.ray_2_x_col == 0:
                if not rt.ray_1l_x_col == 0:
                    if not rt.ray_2l_x_col == 0:
                        if not rt.ray_f_x_col == 0:
                            rt.ray_colision = True
                        
                            if ray_view == True:
                                
                                col = Circle(Point(rt.ray_f_x_col,rt.ray_f_y_col,), player_radius/3)
                                col.setFill("red")
                                col.draw(win)
                            
                                col = Circle(Point(rt.ray_1_x_col,rt.ray_1_y_col,), player_radius/3)
                                col.setFill("red")
                                col.draw(win)
                            
                                col = Circle(Point(rt.ray_2_x_col,rt.ray_2_y_col,), player_radius/3)
                                col.setFill("red")
                                col.draw(win)
                            
                                col = Circle(Point(rt.ray_1l_x_col,rt.ray_1l_y_col,), player_radius/3)
                                col.setFill("red")
                                col.draw(win)
                            
                                col = Circle(Point(rt.ray_2l_x_col,rt.ray_2l_y_col,), player_radius/3)
                                col.setFill("red")
                                col.draw(win)
                        
                    
    
    
    
   
    
    
    # Distance Calculator

        #ray 1 (clockwize)
    rt.distance_1 = math.sqrt((player_x - rt.ray_1l_x_col) * (player_x - rt.ray_1l_x_col) + (player_y - rt.ray_1l_y_col) * (player_y - rt.ray_1l_y_col)) 
    
        #ray 2 (clockwize)
    rt.distance_2 = math.sqrt((player_x - rt.ray_1_x_col) * (player_x - rt.ray_1_x_col) + (player_y - rt.ray_1_y_col) * (player_y - rt.ray_1_y_col))
    
        #ray 3 (clockwize)
    rt.distance_3 = math.sqrt((player_x - rt.ray_2_x_col) * (player_x - rt.ray_2_x_col) + (player_y - rt.ray_2_y_col) * (player_y - rt.ray_2_y_col))
    
        #ray 4 (clockwize)
    rt.distance_4 = math.sqrt((player_x - rt.ray_2l_x_col) * (player_x - rt.ray_2l_x_col) + (player_y - rt.ray_2l_y_col) * (player_y - rt.ray_2l_y_col))
    
        #ray f (clockwize)
    rt.distance_f = math.sqrt((player_x - rt.ray_f_x_col) * (player_x - rt.ray_f_x_col) + (player_y - rt.ray_f_y_col) * (player_y - rt.ray_f_y_col))
    
    
    # Death detection
        
    if rt.distance_1 <= player_radius+2:
        death()
        
    if rt.distance_2 <= player_radius+2:
        death()
        
    if rt.distance_3 <= player_radius+2:
        death()
        
    if rt.distance_4 <= player_radius+2:
        death()  
  
    
  
def logic():
    
    
    global check_count
    global up
    global left
    global right
    global old_x
    global old_y
    global count1
    global count3
    
    global homing
    global bingo
    global stuck
    global do_check
  
    
    if int(rt.distance_2) == int(rt.distance_3):
        if int(rt.distance_1) == int(rt.distance_4):
            stuck = True
    
    
    if rt.distance_f >= 4 * player_radius:
        up = True
    
    if rt.distance_3 >= rt.distance_2:
        right = True
        left = False
    else:
        
        right = False
        left = True
    
    if int(rt.distance_3) == int(rt.distance_2):
        if rt.distance_1 >= rt.distance_4:
            left = True
            right = False
        else:
            right = True
            left = False
    
    
    count1 += 1
    if count1 == check_fq:
        do_check = True
        count1 = 0
    
    
    
    
    
    
    
    if do_check == True:
        if count3 <= steps - 1:
            
            if bingo == True:
                up = True
                right= False
                left = False
                homing = True
                stuck = False
            else:
                count3 += 1
                right = True
                up = False
                left = False
            
            
        else:
            
            count3 = 0
            do_check = False
    
    
    
    
    
    
    # SAFETY
    
    if rt.distance_2 <= 1.50 *(player_radius / (math.sin(player_fov/2))):
        up = False
        stuck = True
        homing = False
        bingo = False
        
    if rt.distance_3 <= 1.50 *(player_radius / (math.sin(player_fov/2))):
        up = False
        stuck = True
        homing = False
        bingo = False
    
    if rt.distance_f <= 1.50 * player_radius:
        up = False
        stuck = True
        homing = False
        bingo = False
    
    
    # Stuck detection
    
    if do_check == False:
        
        if old_x == player_x and old_y == player_y:
            stuck = True
        else:
            stuck = False
    old_x = player_x
    old_y = player_y
    
        
    
    
    
    # Stuck (Not dangerous)
    
    if stuck == True:

        right = True
        left = False
    
    # Check (Not dangerous)
    
    
    
    
while True:
    
    
    move_player()
    rt()
    logic()

    

   
    
        
    if counts == 30:
            
            
        counts = 0
        print('\n','\n','\n','\n','\n','\n','\n','\n','\n','\n','\n','\n','\n','\n','\n','\n','\n','\n','\n','\n','\n','\n','\n','\n','\n')
        print('Player: X:',player_x,'  Y:',player_y,'Angle: ',player_angle)
        print('\n','Distance_1:',rt.distance_1,'\n','Distance_2:',rt.distance_2,'\n','Distance_3:',rt.distance_3,'\n','Distance_4:',rt.distance_4,'\n','Distance_f:',rt.distance_f)
        if do_check == True:
            print(' Checking: Yes')
        else:
            print(' Checking: No')
        if bingo == True:
            print(' Bingo: Yes')
        else:
            print(' Bingo: No')
        if homing == True:
            print(' Homing: Yes')
        else:
            print(' Homing: No')
        if stuck == True:
            print(' Stuck: Yes')
        else:
            print(' Stuck: No')
        
    counts +=1
        
        
        
    if not framerate == 0:
        time.sleep(1/framerate)
    

time.sleep(5)
win.close()








