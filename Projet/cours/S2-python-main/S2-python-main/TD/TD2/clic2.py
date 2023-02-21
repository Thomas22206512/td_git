import tkinter as tk

def c_cercle(event):
    posx = event.x
    posy = event.y
    if posx > 250 :
        canvas.create_oval(posx-50,posy-50,posx+50,posy+50, fill="red", width=0)
    else : 
        canvas.create_oval(posx-50,posy-50,posx+50,posy+50, fill="blue", width=0)

root = tk.Tk()
canvas = tk.Canvas(root, bg="black", height=500, width=500)
canvas.create_line(250,0,250,500,fill="white", width=3)
canvas.pack()
canvas.bind('<Button>', c_cercle)
root.mainloop()
