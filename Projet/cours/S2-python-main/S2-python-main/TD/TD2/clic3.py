import tkinter as tk
ligne = []
def clic(event):
    ligne.append(event.x)
    ligne.append(event.y)
    if len(ligne) >= 4 :
        if ligne[0] >= 250 and ligne[2] >= 250 : 
            canvas.create_line(ligne[0],ligne[1],ligne[2],ligne[3], fill="blue")
            for i in range(4): ligne.pop()
        elif ligne[0] < 250 and ligne[2] < 250 : 
            canvas.create_line(ligne[0],ligne[1],ligne[2],ligne[3], fill="blue")
            for i in range(4): ligne.pop()
        else:
            canvas.create_line(ligne[0],ligne[1],ligne[2],ligne[3], fill="red")
            for i in range(4): ligne.pop()

root = tk.Tk()
canvas = tk.Canvas(root, bg="black", height=500, width=500)
canvas.create_line(250,0,250,500,fill="white", width=3)
canvas.pack()
canvas.bind('<Button>', clic)
root.mainloop()