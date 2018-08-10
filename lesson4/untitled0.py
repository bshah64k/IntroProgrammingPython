# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 14:35:39 2018

@author: bshah
"""
###stamps=int(input("How many stamps do you want?"))
###print ("I want",stamps,"stamps")
##stamps=stamps * .44
##print ("your total cost is",stamps,"dollars")


stamp=int(input("How many stamps do you need? "))
print("I need",stamp)
cost = stamp * 44
cents = cost % 100
dollars =(cost - cents) / 100
print("your total is $", dollars, "and ", cents, "cents")