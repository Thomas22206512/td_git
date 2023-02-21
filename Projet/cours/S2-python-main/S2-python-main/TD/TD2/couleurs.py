# Chargement du module tkinter et random.randint
import tkinter as tk
from random import randint

# Def des constantes
HEIGHT = 256

# Def des diff fonctions
def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def draw_pixel(i,j,color):
    canvas.create_rectangle(i,j,i,j, fill=color, width=0)

def degrade_gris():
    for i in range(0,256):
        for j in range(256):
            draw_pixel(i, j, get_color(i, i, i))

def aleatoire():
    for i in range(0,256):
        for j in range(256):
            draw_pixel(i, j, get_color(randint(0, 255), randint(0, 255), randint(0, 255)))

def degrade_2D():
    for i in range(0,256):
        for j in range(256):
            draw_pixel(i, j, get_color(i, 0,j))

# Construction de la fenêtre principale <<root>>
root = tk.Tk()

# Construction des widgets
b_aleatoire = tk.Button(root, text="Aléatoire", command=aleatoire)
degrade_gris = tk.Button(root, text="Dégrader de gris", command=degrade_gris)
degrade_2D = tk.Button(root, text="Dégrader 2D", command=degrade_2D)
canvas = tk.Canvas(root, bg="black", height=HEIGHT, width=HEIGHT)

# Placement des widgets dans la grille
b_aleatoire.grid(row=0, column=0)
degrade_2D.grid(row=2, column=0)
degrade_gris.grid(row=1, column=0)
canvas.grid(row=0,column=1, rowspan=3)

draw_pixel(HEIGHT//2,HEIGHT//2,"white")

# Lancement de la «boucle principale»
root.mainloop()