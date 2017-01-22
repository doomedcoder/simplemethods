'''
author:Srihari Unnikrishnan
Language:Python
Class name:Simple Methods
Class objective :1) To make addition,subtraction and multiply easily without having to create another function
                 2)Just for fun
Source file:main.py

'''
import math

class simplemethod:
    def square_it(self,num1):
        pow(num1,2)
    def cube(self,num1):
        pow(num1,3)
    def powerUP(self,num1,num2):
        pow(num1,num2)        
    def add(self,num1,num2):
        print num1+num2
    def subtract(self,x1,x2):
        print x1-x2
    def multiply(self,z1,z2):
        print z1*z2
newone=simplemethods() 
newone.add(2,3)
newone.subtract(5,3)
newone.multiply(5,34) 


if __name__=="__main__":
    print "This is Srihari Unnikrishnan's file !"