import turtle
import random as r
import math as m
import numpy as np

length = int(input('Enter the length of plot you prefer: ')) # Takes an input to build a 2D plot of size lengthxlength
turtle.speed("fastest")  

def find_area(l, pos, p_index, length): # finding area using heron's formula
    
    # for i in range(len(l)):
    a = m.hypot(l[p_index+1][0] - pos[0], l[p_index+1][1] - pos[1]) # finding the distance between points pos and l[p_index+1]
    b = m.hypot(l[p_index+length][0] - l[p_index+1][0], l[p_index+length][1] - l[p_index+1][1]) # finding the distance between points l[p_index+length] and l[p_index+1]
    c = m.hypot(l[p_index+length][0] - pos[0], l[p_index+length][1] - pos[1]) # finding the distance between points l[p_index+length] and pos

    s = (a+b+c)/2 #semi perimeter of triangle

    area = int(m.sqrt(s * (s - a) * (s - b) * (s - c))) # heron's formula

    x = m.hypot(l[p_index+1][0] - l[p_index+length+1][0], l[p_index+1][1] - l[p_index+length+1][1]) 
    y = m.hypot(l[p_index+length][0] - l[p_index+length+1][0], l[p_index+length][1] - l[p_index+length+1][1]) 

    s2 = (x+b+y)/2 # b is same for adjacent triangles

    area2 = int(m.sqrt(s2 * (s2 - x) * (s2 - b) * (s2 - y))) # the area of the second triangle 

    return area, area2 

def cal_ar(l, pos, index, length, area_l, colorcode_array): # function to assign colour to the corresponding area of triangle
    area, area2 = find_area(l, pos, index, length)
    for a in range(len(area_l)):
        if area == area_l[a]:
            ar = int(colorcode_array[a])
        if area2 == area_l[a]:
            ar2 = int(colorcode_array[a])
    return ar, ar2

l = [] # list for storing positions of the points
# range is taken between -length//2 and length//2 in order to plot the 2D diagram in the middle of the axis.
for i in range(-length//2, length//2): # row representation of the given number of dots
    for j in range(-length//2, length//2): # column representation of the given number of dots
        turtle.penup()
        ref = r.randint(50, 55)
        ref2 = r.randint(50, 53)
        if j%2 == 0 or j == 0: # To shift the even numbered rows 
            if i%2 != 0: # to shift the even numbered columns
                turtle.setpos((i+0.6)*ref, (j+0.3)*ref)
                l.append(turtle.position())
            else:
                turtle.setpos((i+1)*ref, (j)*ref)
                l.append(turtle.position())
        else:
            if i%2 != 0:
                turtle.setpos((i)*ref2, (j+0.3)*ref2)
                l.append(turtle.position())
            else:
                turtle.setpos((i)*ref2, (j)*ref2)
                l.append(turtle.position())
        
        #turtle.dot(5)

area_l =[] # list of areas of the triiangles
for o in range(len(l)):
    if o < (len(l)-length-1):
        area, area2 = (find_area(l, l[o], o, length))
        area_l.append(area)
        area_l.append(area2)
area_l = sorted(area_l)

colorcode_array = np.linspace(80, 255, len(area_l)) # array to select corresponding colors for areas from rgb (80, 80, 80) -> (255, 255, 255)

for h in range(len(l)):
    if h < (len(l)-length-1):
        ar, ar2 = cal_ar(l, l[h], (h), length, area_l, colorcode_array)
    turtle.colormode(255)
    turtle.fillcolor((ar, ar, ar)) 
    turtle.goto(l[h])
    turtle.pendown()
    turtle.begin_fill()
    for k in range(1, length+1):
        if h == ((length*k)-1): # to avoid the intersecting line as the turtle goes to the next column
            turtle.penup()
            turtle.end_fill()
            continue
    if h < (len(l)-1):
        turtle.goto(l[h+1])
    if h < (len(l)-length-1): # draw a line towards the point after length steps 
        turtle.goto(l[h+length])
        turtle.goto(l[h]) 
        turtle.end_fill()
        turtle.fillcolor((ar2, ar2, ar2)) # from here it is drawing second triangle or the triangle in the odd indices of the list area_l
        turtle.goto(l[h+1])
        turtle.begin_fill()
        for s in range(1, length+1):
            if h == ((length*s)-1): # to avoid the intersecting line as the turtle goes to the next column
                turtle.penup()
                turtle.end_fill()
                continue
        turtle.goto(l[h+length+1])
        turtle.goto(l[h+length])
        turtle.goto(l[h+1])
        turtle.penup()
        turtle.end_fill()

screen = turtle.getscreen()
screen.mainloop()

