import tkinter as tk
from random import randint
# Construction des constante et variable
HEIGHT = 500
WIDTH = HEIGHT
grid = [[b for b in range(1,10)] for a in range(9)]
posx = False
posy = False
liste = ["1","2","3","4","5","6","7","8","9"]
l_region = [
    [False,False,False],
    [False,False,False],
    [False,False,False]
    ]
# Construction des fonctions

def gui():
    for a in range(9):
        for b in range(9):
            canvas.create_text((a/9)*HEIGHT +(1/18)*HEIGHT,(b/9)*WIDTH + (1/18)*WIDTH, text=grid[b][a], fill="white", width=1)
            # tk.Label(canvas, text=grid[b][a]).place(x=(a/9)*HEIGHT +(1/18)*HEIGHT,y=(b/9)*WIDTH + (1/18)*WIDTH)
    # affiche le cadrillage
    for i in range (3):
        canvas.create_line((i/3)*HEIGHT,0,(i/3)*HEIGHT,WIDTH, fill="white", width=5)
        canvas.create_line(0,(i/3)*WIDTH,HEIGHT,(i/3)*WIDTH, fill="white", width=5)
    for i in range(9):
        canvas.create_line((i/9)*HEIGHT,0,(i/9)*HEIGHT,WIDTH, fill="white", width=1)
        canvas.create_line(0,(i/9)*WIDTH,HEIGHT,(i/9)*WIDTH, fill="white", width=1) 

def gui_aide():
    pass

# def key_pressed(event):
#     return ”Key Pressed:”+event.char

def position(event):
    global grid, posx, posy
    posx = event.x
    posy = event.y

def modif(event):
    global liste
    if posx == False :
        return None
    else:
        if event.char in liste:
            print(event.char, type(event.char))
            grid[int(posy/(HEIGHT//9))][int(posx/(HEIGHT//9))] = event.char
            canvas.delete('all')
            gui_region()
            gui()
            
def region():
    global liste
    for i in range(3):
        for j in range(3):
            for a in range(3):
                for b in range(3):
                    if grid[a+i*3][b+j*3] in liste :
                        liste.remove(grid[a+i*3][b+j*3])
                    if len(liste) == 0 :
                        l_region[i][j] = True
            print(liste)
            print(l_region)
            liste = ["1","2","3","4","5","6","7","8","9"]
            print(liste)

def gui_region():
    region()
    for a in range(3):
        for b in range(3):
            if l_region[a][b] == False :
                canvas.create_rectangle((1/3)*a,(1/3)*b,(1/3)*a+(1/3)*HEIGHT,(1/3)*b+(1/3)*HEIGHT, fill="red")
            if l_region[a][b] == True :
                canvas.create_rectangle((1/3)*a,(1/3)*b,(1/3)*a+(1/3)*HEIGHT,(1/3)*b+(1/3)*HEIGHT, fill="green")

# Construction de la fenêtre principale
root = tk.Tk()

# Construction du canvas
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="black")
canvas.pack()
canvas.bind('<Button>', position)
root.bind("<Key>",modif)

# Lancement de la boucle principale

gui()
root.mainloop()