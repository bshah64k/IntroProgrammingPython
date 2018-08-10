# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 23:05:35 2018

@author: bshah
"""

#%%

def linearEqn(a, b, c):
    
    x = 0
    y = 0  
    z = 0
    
    solution = False
    while (x < c):
        
        while (y < c):
            
            sum = a*x + b* y
            if (sum == c):
                print (" solution is (", x,",",y,")" ) 
                solution = True
                break
            
            y = y + 1
     
            
        #end of inner loop    
         
        x = x + 1
        y = 0
        #print("debug", x,y, sum, c)
    #end of outerloop    
    
    if (solution == False):
        print ("no solution")
        
        
#%%
        
def linearEqn2 (a, b, c, d):
    
    sum = 0
    solution = False
    
    for x in range(d):
        
        for y in range(d):
                        
            for z in range (d):
                
              sum = a*x + b*y + c*z
              
              if (sum == d):
                  solution = True
                  print ("solution is", x,y,z)
                  break
              
           #end of z forloop
           
        #end of y for loop
        
    #end of x for look
     
    if solution == False:
         print ("No Solution")
        
    
                