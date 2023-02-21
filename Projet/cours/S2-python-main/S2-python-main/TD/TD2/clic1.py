import tkinter as tk

def c_pixel(event):
    posx = event.x
    posy = event.y
    canvas.create_rectangle(posx,posy,posx,posy, fill="red", width=0)

root = tk.Tk()
canvas = tk.Canvas(root, bg="black", height=500, width=500)
canvas.pack()
canvas.bind('<Button>', c_pixel)
root.mainloop()