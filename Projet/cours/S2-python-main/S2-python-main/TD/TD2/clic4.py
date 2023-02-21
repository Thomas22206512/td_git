import tkinter as tk

compteur = 0

def clic(event):
    global compteur
    if  200 <= event.x <= 300 and 200 <= event.y <= 300 :
        compteur += 1
        canvas.delete('all')
        if compteur % 2 == 0 :
            canvas.create_rectangle(200,200,300,300 ,fill="white", width=3)
        else :
            canvas.create_rectangle(200,200,300,300 ,fill="white", width=3)
            canvas.create_rectangle(210,210,290,290 ,fill="black", width=3)
    if compteur == 10:
        root.destroy()

root = tk.Tk()
canvas = tk.Canvas(root, bg="black", height=500, width=500)
canvas.create_rectangle(200,200,300,300 ,fill="white", width=3)
canvas.pack()
canvas.bind('<Button>', clic)
root.mainloop()