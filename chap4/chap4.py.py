# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 20:40:18 2022

@author: Surface
"""

import math

import turtle
bob=turtle.Turtle()

def polygon (t , n , length ) :
    for i in range (n ) :
        t . fd ( length )
        t . lt ( 360/n)


def circle (t , r ) :
    circumference = 2 * math . pi * r
    n = 300
    length = circumference / n
    polygon (t , n , length )
circle(300,5)
#以上代码的堆栈图为:
    #cirlle→circumferfence=2*Π*5
    #length=10Π/300
    #ploygon→n=300,length=10Π/300
    #ploygon→t.fd(10Π/n),t.lt(360/300)
    #ploygon→t.fd(10Π/n),t.lt(360/300)...运行300次
    

import turtle
bob=turtle.Turtle()

def arc(t, r, angle):
    c = 2 * math.pi * r * angle / 360
    n = int(c / 3 + 3)
    length = c / n
    for i in range(n):
        t.fd(length)
        t.lt(angle / n)

def routine(t, s, angle):
    r = s / 2 / math.sin(angle / 2 * math.pi / 180)
    arc(t, r, angle)
    t.lt(180 - angle)
    arc(t, r, angle)
    t.lt(180 - angle)

for i in range(6):
    routine(bob,100,60)
    bob.lt(60)

for i in range(20):
    routine(bob,100,360/10)
    bob.lt(360/20)

for i in range(10):
    routine(bob,100,720/10)
    bob.lt(360/10)
    
def flowers(t,r,n,x):
    angle=360*x/n
    for i in range(n):
        routine(bob,100,360*x/n)
        bob.lt(360/n)

flowers(bob,100,10,2)

def spiral(t,a,b,theta_range,dtheat=1):
    x=a
    y=0
    dir=0
    for i in range(theta_range):
        theta=(i+1)*dtheta*math.pi/180
        r=a+b*theta
        dx=r*math.cos(theta)-x
        dy=r*math.sin(theta)-y
        dlength=math.sqrt(dx**2+dy**2)
        ddir=math.atan(dy,dx)*180/math.pi-dir
        x=x+dx
        y=y+dy
        dir=dir+ddir
        
turtle.delay(0.01)
spiral(bob,20,10,360*5)


        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
