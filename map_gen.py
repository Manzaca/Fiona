# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 15:02:59 2022

@author: Manzaca
"""

from random import *

# MAP GENERATOR A0 (dens in %)

def gen_map(size,dens):
    
    
    string =''
    count = 0
    f= open("MAP.txt","w+")
    
    while count <= size - 1:
        f.write('#')
        count += 1
    count = 0    
        
    f.write('\n')

    f.write('#')
    while count <= size - 3:
        f.write(' ')
        count += 1
    f.write('#')
    count = 0
    f.write('\n')
    
    
    count2 = 0
    while count2 <= size - 5:
        f.write('#')
        
        string = ''
        while count <= size - 3:
            
            if random() >= dens / 100:
                string = string + ' '
            else: 
                string = string + '#'
            count += 1
        count = 0
        f.write(string)
        f.write('#')
        
        f.write('\n')
        count2 += 1
       
        
       
    f.write('#')
    while count <= size - 3:
        f.write(' ')
        count += 1
    f.write('#')
    count = 0
    f.write('\n')
    
    
    
    
    
    count = 0
    while count <= size - 1:
        f.write('#')
        count += 1
    f.close()
    print('MAP GENERATION COMPLETE')
    

    
