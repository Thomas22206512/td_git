# Chargement du module tkinter
import tkinter as tk
from random import randint

# Construction de la fenêtre principale «root»
root = tk.Tk()
root.title('Mon dessin')
# Def des variables et constante
r = 50
d = 100
couleur = ""
objets = [] 

# Construction des diff fonctions
def choissir():
    global couleur
    liste = ["white","black", "red", "green", "blue", "cyan", "yellow"]
    couleur = input("choisissez une couleur : ")
    res = 0
    for i in liste :
        if couleur != i:
            res += 1
    if res == 7:
        couleur = "blue"

def affichec():
    global objets
    x,y = randint(50, 550),randint(50,550)
    if couleur == "":
        cercle = canvas.create_oval(x-r, y-r, x+r, y+r, fill="#00FFFF", width=0)
        objets.append(cercle)
    else :  
        cercle = canvas.create_oval(x-r, y-r, x+r, y+r, fill=couleur, width=0)
        objets.append(cercle)
    
def afficheca():
    x,y = randint(0,500), randint(0,500)
    if couleur == "":
        carre = canvas.create_rectangle(x,y,x+d,y+d, fill="red",width=0)
        objets.append(carre)
    else : 
        carre = canvas.create_rectangle(x,y,x+d,y+d, fill=couleur,width=0)
        objets.append(carre)
    

def affichecr():
    x,y = randint(0,500), randint(0,500)
    if couleur == "":
        croix = canvas.create_line(x,y,x+d,y+d,fill="yellow", width=10)
        croix_2 = canvas.create_line(x+d,y,x,y+d,fill="yellow", width=10)
        objets.append(croix)
        objets.append(croix_2)
    else:
        croix = canvas.create_line(x,y,x+d,y+d,fill=couleur, width=10)
        croix_2 = canvas.create_line(x+d,y,x,y+d,fill=couleur, width=10)
        objets.append(croix)
        objets.append(croix_2)

def undo():
    global objets
    if len(objets)>=1 :
        if canvas.type(objets[-1]) == "line" : 
            canvas.delete(objets[-1])
            objets.pop()
        canvas.delete(objets[-1])
        objets.pop()
    else : print("Vous n'avez plus rien a sup")

# Construction des widgets
qb = tk.Button(root, text='Choissir une couleur', command=choissir, background="red")
cercle = tk.Button(root, text="Cercle", command=affichec)
carre = tk.Button(root, text="Carré", command=afficheca)
croix = tk.Button(root, text="Croix", command=affichecr)
b_undo = tk.Button(root, text="Undo", command = undo)
canvas = tk.Canvas(root, bg="black", height=600, width=600)

# Placement des widgets dans la grille
qb.grid(row=0, column=1)
cercle.grid(row=1, column=0, padx=10)
carre.grid(row=2, column=0)
croix.grid(row=3, column=0)
canvas.grid(row=1, column=1, rowspan=3)
b_undo.grid(row=0, column=0)

# Lancement de la «boucle principale»
root.mainloop()

