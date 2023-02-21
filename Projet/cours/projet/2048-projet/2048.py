import numpy as np
from random import randint
from tkinter import *
import couleur as c
import numpy as np
height = 400
width = height
compteur = 0
tmpo = []
grid = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
    ]

def gui():
    canvas.delete("all")
    for i in range(0,400,100):
        for j in range(0,400,100):
            if grid[j//100][i//100] != 0 : 
                canvas.create_rectangle(i,j,i+100,j+100,fill=c.BACKGROUND[grid[j//100][i//100]],width=0)
                canvas.create_text(i+50,j+50, text=grid[j//100][i//100], fill=c.TEXT_COLOR[grid[j//100][i//100]], width=20)
    for p in range(0,400,100):
        canvas.create_line(p,0,p,400, fill="#808080",width=3)
        canvas.create_line(0,p,400,p,fill="#808080", width=3)
def stack():
    global grid
    for o in range(3):
        for i in range(4):
            for j in range(1,4):
                if grid[i][-j] == 0:
                    grid[i][-j] = grid[i][-j-1]
                    grid[i][-j-1] = 0

def reset_grid():
    global grid, res
    grid = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
    ]
    random()
    random()
    gui()
    res = 0
res = 0
def random():
    global res
    while True : 
        res += 1
        x,y = randint(0, 3),randint(0, 3)
        if grid[x][y] == 0 :
            grid[x][y] = 2**randint(1, 2)
            break
        if res == 1000:
            print("you lose")
            reset_grid()
            break

def combine():
    global grid
    for o in range(1):
        for i in range(4):
            for j in range(1,4):
                if grid[i][-j] == grid[i][-j-1]:
                    grid[i][-j] *= 2
                    grid[i][-j-1] = 0

def reverse():
    global grid
    for i in range(4):
        for j in range(2):
            tmp = grid[i][j]
            grid[i][j] = grid[i][-j-1]
            grid[i][-j-1] = tmp

def transpose():
    global grid
    L = [[],[],[],[]]
    for i in range(4):
        for j in range(4):
            L[i].append(grid[j][i])
    grid = L

def rigth():
    global grid
    tmpo = []
    for z in range(4):
        tmpo.append([grid[z][0],grid[z][1],grid[z][2],grid[z][3]])
    stack()
    combine()
    stack()
    gui()
    if tmpo == grid :
        return None
    random()
    gui()

def left():
    global grid
    tmpo = []
    for z in range(4):
        tmpo.append([grid[z][0],grid[z][1],grid[z][2],grid[z][3]])
    reverse()
    stack()
    combine()
    stack()
    reverse()
    gui()
    print(tmpo)
    print(grid)
    print(tmpo == grid)
    if tmpo == grid :
        return None
    random()
    gui()
    
def up():
    global grid
    tmpo = []
    for z in range(4):
        tmpo.append([grid[z][0],grid[z][1],grid[z][2],grid[z][3]])
    transpose()
    reverse()
    stack()
    combine()
    stack()
    reverse()
    transpose()
    gui()
    if tmpo == grid :
        return None
    random()
    gui()

def down():
    global grid
    tmpo = []
    for z in range(4):
        tmpo.append([grid[z][0],grid[z][1],grid[z][2],grid[z][3]])
    transpose()
    stack()
    combine()
    stack()
    transpose()
    gui()
    if tmpo == grid :
        return None
    random()
    gui()

def game_over():
    test = []
    for z in range(4):
        test.append([grid[z][0],grid[z][1],grid[z][2],grid[z][3]])
    

def appui_z(event):
    up()

def appui_s(event):
    down()

def appui_q(event):
    left()

def appui_d(event):
    rigth()
root = Tk()
root.title("2048")
b_reset = Button(root,text="Reset", command=reset_grid)
b_right = Button(root, text="→", command=rigth)
b_left = Button(root, text="←", command=left)
b_up = Button(root,text="↑",command=up)
b_down = Button(root,text="↓",command=down)
canvas = Canvas(root,bg="#AFACAC", height=height, width=width)

b_reset.grid(row=0, column=0, ipady=5, ipadx=10, pady=10)
b_right.grid(row=2, column=3)
b_left.grid(row=2, column=1)
b_up.grid(row=1, column=2)
b_down.grid(row=3,column=2)
canvas.grid(row=1,column=0, rowspan=999)
root.bind('<KeyPress-z>', appui_z)
root.bind('<KeyPress-s>', appui_s)
root.bind('<KeyPress-q>', appui_q)
root.bind('<KeyPress-d>', appui_d)
random()
random()
gui()
root.mainloop()
