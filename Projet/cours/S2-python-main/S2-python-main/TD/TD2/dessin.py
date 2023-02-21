# Chargement du module tkinter
from tkinter import * # pour Python2 ce serait Tkinter
from random import randint
# Construction de la fenêtre principale «root»
root = Tk()
root.title('Mon dessin')
r = 50
d = 100
HEIGHT = 600
WDTH = 600
couleur = ""

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
    x,y = randint(50, 550),randint(50,550)
    if couleur == "":
        canvas.create_oval(x-r, y-r, x+r, y+r, fill="#00FFFF", width=0)
    else :  
        canvas.create_oval(x-r, y-r, x+r, y+r, fill=couleur, width=0)    
    

def afficheca():
    x,y = randint(0,500), randint(0,500)
    if couleur == "":
        canvas.create_rectangle(x,y,x+d,y+d, fill="red",width=0)
    else : 
        canvas.create_rectangle(x,y,x+d,y+d, fill=couleur,width=0)
    

def affichecr():
    x,y = randint(0,500), randint(0,500)
    if couleur == "":
        canvas.create_line(x,y,x+d,y+d,fill="yellow", width=10)
        canvas.create_line(x+d,y,x,y+d,fill="yellow", width=10)
    else:
        canvas.create_line(x,y,x+d,y+d,fill=couleur, width=10)
        canvas.create_line(x+d,y,x,y+d,fill=couleur, width=10)

# Construction d'un simple bouton
qb = Button(root, text='Choissir une couleur', command=choissir, background="red")
cercle = Button(root, text="Cercle", command=affichec, activeforeground="green", borderwidth=20)
carre = Button(root, text="Carré", command=afficheca, borderwidth=2, underline=0)
croix = Button(root, text="Croix", command=affichecr, anchor="se", foreground="pink3")
canvas = Canvas(root, bg="black", height=600, width=600)







# Placement du bouton dans «root»
qb.grid(row=0, column=1)
cercle.grid(row=1, column=0, padx=10)
carre.grid(row=2, column=0)
croix.grid(row=3, column=0)
canvas.grid(row=1, column=1, rowspan=3)





# Lancement de la «boucle principale»
root.mainloop()

