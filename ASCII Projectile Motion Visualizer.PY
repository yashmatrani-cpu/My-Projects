##we have to take print out after whole project is completed
import math
import time
import random
import sympy 
u = int(input('enter initial velocity:'))
theta = int(input('enter angle of projection:'))
theta2 = math.radians(theta)
g = 9.8
T = (2 * u * math.sin(theta2)) / g
H = ((u * math.sin(theta2)) ** 2) / (2 * g)
R = (u ** 2 * math.sin(2 * theta2)) / g
print(f"time of flight is {T} seconds,range is {R} metres and maximum height is {H} metres")
ROWS = 20
COLS = 80
grid = [[' ' for i in range(COLS)] for i in range(ROWS)]
scale_x = COLS/R
scale_y = ROWS/H
step = R/100
x = 0
while x<=R:
    y = x * math.tan(theta2) - (g * x**2) / (2 * u**2 * math.cos(theta2)**2)
    if y<0 :
        break##if ball touches ground
    col = int(x*scale_x)
    row = ROWS-1-int(y*scale_y)
    if 0<=row<ROWS and 0<=col<COLS:
        grid[row][col] = '*'
    x+=step  
for row in grid:
    print(''.join(row))
print(f"\nRange: {R:.2f} m | Max Height: {H:.2f} m | Time: {T:.2f} s")    

    


