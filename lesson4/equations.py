# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 12:52:17 2018

@author: bshah
"""
#%%
#linear eqn


def linear(a,b,c):
    
    solution = False
    for x in range(0, c,1):
                
        #print ("beginnig x loop with x = ", x)
        
        for y in range (0, c, 1):
            if ((a*x + b*y) == c):
                solution = True
                print (x,y)
                break
            #print (x, y)
            
        #end y loop
        
    #end x loop
    if (solution == False):
        print("no solution")
    
#%%
def linear3 (a,b,c,d) :
    solution = False
    for x in range (0,d,1):
        

        for y in range (0,d,1):
            
            
            for z in range (0,d,1):
                if ((a*x+b*y +c*z )== d):
                    solution = True
                    print (x,y,z)
                    break
        if (solution == False):
            print ("no solution")
#%%
def homework():
    for a in range (1,7):
        
        for b in range (1,7):
            
            for c in range (1,7):
            
                for d in range (1,7):
                
                    for e in range (1,7):
                    
                        for f in range (1,7):
                            if (a+(b-c)*d-e)*f ==75 :
                                print(a,b,c,d,e,f)
                                break


                        