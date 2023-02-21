import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400

if __name__ == '__main__':
    root = tk.Tk()

    canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

    # Début de votre code
    x0 = 100
    x1 = CANVAS_WIDTH - 100
    y = CANVAS_HEIGHT / 2
    canvas.create_oval(300 - 50, 100 + 50, 300 + 50, 100 - 50)
    canvas.create_oval(300 - 50, 300 + 50, 300 + 50, 300 - 50)
    canvas.create_oval((x0 + x1) / 2 - 50, y + 50, (x0 + x1) / 2 + 50, y - 50)
    canvas.create_line(300,100,300,300)
    # Fin de votre code

    canvas.grid(row=0, column=0)
    root.mainloop()
