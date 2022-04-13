#########################################
# groupe MIASHS 7
# GOREAU THELMA
# VIGNERON THOMAS
# SOW MAHMOUD
# LIMOUZIN MATTHIEU
# https://github.com/Thelma47/projet1bi
#########################################

# import des modules
import tkinter as tk
import random as rd

# variables globales
H = 600
W = 700
m = 6 #nb lignes
n = 7 #nb colonnes


# fonctions

def creation_grille():
    """créer une grille de puissance 4"""
    for i in range(m):
        for j in range(n):
            canvas.create_oval(W/n*j, H/m*i, W/n*(j+1), H/m*(i+1), fill="Dodgerblue3", outline="Dodgerblue2")
            canvas.create_oval(W/n*j+5, H/m*i+5, W/n*(j+1)-5, H/m*(i+1)-5, fill="white", outline="blue")

def choix_joueur():
    """choisit aléatoirement le premier des deux joueurs qui va jouer"""
    global premier_joueur
    prenom1 = input("prénom?")
    prenom2 = input("prénom?")
    premier_joueur = rd.choice([prenom1, prenom2])

def affiche_joueur():
    """affiche qui doit commencer"""
    choix_joueur()
    label.config(text= premier_joueur + " commence à jouer")

def gestion_clic():
    pass


######################
# programme principal
######################

# création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, height=H, width=W, bg="blue")
label = tk.Label(racine, text=" puissance 4 ", padx=20, pady=20, borderwidth=5, relief="groove", font = ("helvetica", "30")) 

# positionnement des widgets
racine.grid()
canvas.grid(rowspan=10)
label.grid(column=1,row=0)

# fonctions
creation_grille()
affiche_joueur()

# gestions clic
canvas.bind("<Button-1>", gestion_clic)

# boucle principale
racine.mainloop()




