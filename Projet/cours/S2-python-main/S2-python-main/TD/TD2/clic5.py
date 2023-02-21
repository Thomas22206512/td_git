import tkinter as tk

cercle = []
compteur = 0

def clic(event):
    global compteur, cercle
    compteur += 1
    if compteur <= 8 :
        canvas.create_oval(event.x-50,event.y-50,event.x+50,event.y+50, fill="red", width=0)
        cercle.append([event.x,event.y])
    if compteur == 9 :
        canvas.delete('all')
        for i in range(8):
            canvas.create_oval(cercle[i][0]-50, cercle[i][1]-50, cercle[i][0]+50, cercle[i][1]+50, fill="yellow", width=0)
        canvas.create_oval(event.x-50,event.y-50,event.x+50,event.y+50, fill="yellow", width=0)
    if compteur == 10:
        canvas.delete('all')
        compteur = 0
        cercle = []

root = tk.Tk()
canvas = tk.Canvas(root, bg="black", height=500, width=500)
canvas.pack()
canvas.bind('<Button>', clic)
root.mainloop()