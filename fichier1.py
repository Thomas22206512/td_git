#Ce code ne sert a rien mais c'est jolie
from tkinter import *
WIDTH = 500
HEIGHT = 500

def new_game():
    global grid, turn
    canvas.delete('abc')
    canvas.configure(bg='#000000')
    grid = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
        ]
    turn = 'X'

def click(event):
    global turn
    x, y = event.x, event.y
    x, y = int((x/WIDTH)*3), int((y/HEIGHT)*3)
    if grid[y][x] == ' ':
        grid[y][x] = turn
    else:
        return
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    
    canvas.create_text((x+0.5)/3*WIDTH, (y+0.5)/3*HEIGHT, text=turn, font=('consolas', 50), fill='#FFFFFF', tag='abc')

    if check_win():
        canvas.configure(bg='#FF0000')

def check_win():
    form = ('XXX','OOO')
    for y in range(3):
        var = ''
        for x in range(3):
            var += grid[y][x]
        if var in form:
            return True
    for x in range(3):
        var = ''
        for y in range(3):
            var += grid[y][x]
        if var in form:
            return True

    if grid[0][0] + grid[1][1] + grid[2][2] in form:
        return True
    
    if grid[0][2] + grid[1][1] + grid[2][0] in form:
        return True
    
    return False


root = Tk()

button = Button(root, text='Nouvelle partie', command=new_game)
button.pack()
canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg='#000000')
canvas.pack()

for i in range(1,3):
    canvas.create_line((1/3)*i*WIDTH, 0, (1/3)*i*WIDTH, HEIGHT, fill='#FFFFFF', width=4)
    canvas.create_line(0, (1/3)*i*HEIGHT, WIDTH, (1/3)*i*HEIGHT, fill='#FFFFFF', width=4)

new_game()

root.bind('<Button-1>', click)
root.resizable(False,False)
root.mainloop()