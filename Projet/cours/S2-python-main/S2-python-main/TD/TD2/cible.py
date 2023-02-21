import tkinter as tk
height, couleur = 800, ["blue","green","black", "yellow", "magenta", "red"]
root = tk.Tk()
canvas = tk.Canvas(root, height=height, width=height, bg="black")
for i in range(0, height//2, 10):
    canvas.create_oval(i,i,height-i,height-i, fill=couleur[(i//10)%6], width=0)
canvas.pack()
root.resizable(False,False)
root.mainloop()