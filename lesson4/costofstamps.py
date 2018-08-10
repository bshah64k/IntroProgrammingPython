# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 14:35:39 2018

@author: bshah
"""
###stamps=int(input("How many stamps do you want?"))
###print ("I want",stamps,"stamps")
##stamps=stamps * .44
##print ("your total cost is",stamps,"dollars")


stamp=int (input("How many stamps do you need? ") )

print("I need",stamp)
cost = stamp * 44
cents = cost % 100
dollars =(cost - cents) / 100
print("your total is $", dollars, "and ", cents, "cents")
#%%

def sqrRoot(x):
    
    # Begin with an estimate of sqrroot
    
    est = x / 3
    
    xest2 = est **2 
    err = x - xest2 
    counter = 1
    while ((abs(err) > 0.5) and (counter < 1000)):
        print(est, err, counter)
        est = (est + x / est) /2
            
            
        xest2 = est**2
        err = x - xest2
        counter += 1
        
    print ("estimated square root is", est, "with an error of", err)   

#%%
def myroot(x):
    i = 1    
    guess = i **2
    while (guess<x):
        i = i+1
        guess = i **2
   ###     print (guess)
   
    print ("the square root is approx", i)
    
    
    
    
    
    
    
    
    
    
    
    
#%%
def prime(x,y):
    i=2
    prime = True
    while (prime == True) and (x> i <= y):
        
        if (x % i) == 0:
            prime = False
#        
        
        i = i + 1
        
    #if prime == True :
       # print (x, "is prime")
    #else:
     #  print (x,"is not prime")
   #
   
    return(prime)
   
   
   
   
    
    
 #%%
def oddnumbers (l,m):
    i = l
    while (i<m):
        i = i +2 
        print (i)