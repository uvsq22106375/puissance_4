#############################################
# groupe MIASHS 7
# GOREAU THELMA
# VIGNERON THOMAS
# SOW MAHMOUD
# LIMOUZIN MATTHIEU
# https://github.com/uvsq22106375/puissance_4
#############################################

# import des modules
import tkinter as tk
import random as rd

# variables globales
H = 600
W = 700 #largeur
m = 6 #nb lignes
n = 7 #nb colonnes
joueur1 = True
grille = []
fin = False
global prenom1
l_coup = []
retour = False
colonne_impossible = False


#création liste à deux dimensions
# 0 : case vide
# 1 : case avec un pion jaune
# 2 : case avec un pion rouge
for i in range(m):
    grille.append([0]*n)



# fonctions
def creation_grille():
    """créer une grille de puissance 4 avec m lignes et n colonnes"""
    #m = int(input("Nombre de lignes ?"))
    #n = int(input("Nombre de colonnes ?"))
    #W = n*100
    #H = m*100
    for i in range(m):
        for j in range(n):
            canvas.create_oval(W/n*j, H/m*i, W/n*(j+1), H/m*(i+1), fill="Dodgerblue3", outline="Dodgerblue2")
            canvas.create_oval(W/n*j+5, H/m*i+5, W/n*(j+1)-5, H/m*(i+1)-5, fill="white", outline="blue")

def choix_joueur():
    """choisit aléatoirement le premier des deux joueurs qui va jouer"""
    global premier_joueur, prenom1, prenom2, deuxieme_joueur
    prenom1 = input("prénom du joueur 1 ?")
    prenom2 = input("prénom du joueur 2 ?")
    premier_joueur = rd.choice([prenom1, prenom2])
    if premier_joueur == prenom1:
        deuxieme_joueur =prenom2
    else:
        deuxieme_joueur = prenom1

def affiche_joueur():
    """affiche qui doit commencer"""
    choix_joueur()
    label_joueur.config(text= premier_joueur + " commence à jouer")

#def paramètres():
#    nb_pions = int(input("Nombre de pions alignés nécessaire pour gagner ?"))

def trouver_colonne(clic_x):
    """retourne la colonne sur laquelle le jeton va apparaître"""
    colonne = clic_x // 100
    return colonne 

def trouver_ligne(colonne):
    """retourne la ligne sur laquelle le jeton va apparaître"""
    chgt_ligne = m-1
    for i in range(m):
        if grille[chgt_ligne][colonne] == 0 :
            ligne = chgt_ligne
        else:
            chgt_ligne -= 1
    return ligne

def gestion_clic(event):
    """affiche le jeton dans la grille si cela est possible"""
    global joueur1, fin, ligne, colonne, retour, colonne_impossible, numero_colonne
    if fin == True:
        return
    if 0<event.x<W and 0<event.y<H :
        clic_x = event.x
        colonne = trouver_colonne(clic_x)
        ligne = trouver_ligne(colonne)
        if joueur1:
            canvas.create_oval(colonne*100+5, ligne*100+5, colonne*100+100-5, ligne*100+100-5, fill ="gold")
            grille[ligne][colonne] = 1
            joueur1 = not joueur1
            if retour == True :
                retour = False     
            label_joueur.config(text= "À " + deuxieme_joueur + " de jouer")      
        else:
            canvas.create_oval(colonne*100+5, ligne*100+5, colonne*100+100-5, ligne*100+100-5, fill="red")
            grille[ligne][colonne] = 2
            joueur1 = not joueur1
            if retour == True:
                 retour = False
            label_joueur.config(text= "À " + premier_joueur + " de jouer") 
    alignement(ligne, colonne)
    dernier_coup()
    grille_pleine()


def alignement(ligne, colonne):
    """détecte alignement de 4 pions à partir du dernier pion posé"""
    global id_joueur
    id_joueur = grille[ligne][colonne]
    #vertical 
    cpt = 1 #compteur qui part de 1 et qui compte le nombre de pion de même couleur par rapport au dernier pion posé
    while (ligne + cpt < 6) and (grille[ligne+cpt][colonne] == id_joueur):
        cpt += 1
        if cpt == 4:
            fin_du_jeu()

    #horizontal (gauche et droite)
    cpt = 1
    while (colonne - cpt >= 0) and (grille[ligne][colonne - cpt] == id_joueur): #gauche
        cpt += 1
        if cpt == 4:
            fin_du_jeu()
    while (colonne + cpt < 7) and (grille[ligne][colonne + cpt] == id_joueur): #droite
        cpt += 1
        if cpt == 4:
            fin_du_jeu()

    # 2 diagonales (montante vers la droite ou la gauche)
    # montante vers la droite
    cpt = 1
    while (colonne - cpt >=0) and (ligne + cpt < 6) and (grille[ligne + cpt][colonne - cpt] == id_joueur): # bas gauche
        cpt += 1
        if cpt == 4:
            fin_du_jeu()
    while (colonne + cpt < 7) and (ligne - cpt >=0) and (grille[ligne-cpt][colonne + cpt] == id_joueur): # haut droite
        cpt += 1
        if cpt == 4:
            fin_du_jeu()
    # montante vers la gauche
    cpt = 1
    while (colonne + cpt < 7 ) and (ligne + cpt < 6) and (grille[ligne + cpt][colonne + cpt] == id_joueur): # bas droite
        cpt += 1
        if cpt == 4:
            fin_du_jeu()
    while (colonne - cpt >= 0) and (ligne - cpt >=0) and (grille[ligne-cpt][colonne - cpt] == id_joueur): # haut gauche
        cpt += 1
        if cpt == 4:
            fin_du_jeu()
        

def colonne_pleine(colonne):
    global colonne_impossible
    """vérifie si la colonne que le joueur a choisie est pleine ou non"""
    nb_col = 0
    for i in range(m):
        if grille[i][colonne] == 1 or grille[i][colonne] == 2:
            nb_col += 1
    if nb_col == m:
        colonne_impossible = True

def grille_pleine():
    global nb_pions
    """vérifie si la grille est pleine ou non"""
    nb_pions = 0
    for i in range(m):
        for j in range(n): 
           if grille[i][j] == 1 or grille[i][j] == 2:
               nb_pions += 1
    if nb_pions == n*m:
        fin_du_jeu_nul()


def fin_du_jeu():
    """affiche quel joueur à gagner et arrête le jeu"""
    global fin
    fin = True
    if id_joueur == 1:
        label_gagnant.config(text= premier_joueur + " a gagné", font="20")
    elif id_joueur == 2:
        if premier_joueur == prenom1:
            label_gagnant.config(text= prenom2 + " a gagné ", font="20")
        else:
            label_gagnant.config(text= prenom1 + " a gagné", font="20")


def fin_du_jeu_nul():
    """affiche qu'il n'y a aucun joueur et arrête le jeu"""
    global fin
    fin = True
    label_gagnant.config(text= "Il n'y a aucun gagnant", font="20")

def dernier_coup():
    """rajoute dans une liste les coordonnées du dernier coup """
    l_coup.extend([ligne, colonne])

def retour_1():
    """annule le dernier coup et change le numéro dans la grille"""
    global retour , joueur1
    grille[l_coup[-2]][l_coup[-1]] = 0
    canvas.create_oval(l_coup[-1]*100+5, l_coup[-2]*100+5, l_coup[-1]*100+100-5, l_coup[-2]*100+100-5, fill="white")
    joueur1 = not joueur1
    if joueur1:
         label_joueur.config(text= "À " + premier_joueur + " de jouer") 
    else:
         label_joueur.config(text= "À " + deuxieme_joueur + " de jouer") 
    del l_coup[-1]
    del l_coup[-1]
    retour = True

def sauvegarde():
    """ Ecrit la grille dans le fichier sauvegarde.txt """
    fic = open("sauvegarde.txt", "w")
    for i in range(m):
        fic.write(str(grille[i]) + "\n")
    fic.close() 

def charger():
    """Lit le fichier sauvegarde.txt, récupère la grille et met à jour la grille en conséquence (modifie l'affichage)"""
    grille1 = []  # liste qui contient tous les nombres de la grille
    grille2 = []  # liste qui contient les sous listes de nombres
    fic = open("sauvegarde.txt", "r")
    while True:
         ligne = fic.readline()
         if ligne == "":
             break
         for i in ligne:
             if i =="0" or i =="1" or i =="2":
                 grille1.append(int(i))
    for i in range(m):
         grille2.extend([[grille1[i] for i in range(n)]])
         for j in range(n):
             del grille1[0]
    fic.close()
    for i in range(m):
        for j in range(n):
            if grille2[i][j] == 1:  
                canvas.create_oval(j*100+5, i*100+5, j*100+100-5, i*100+100-5, fill="gold")
            elif grille2[i][j] == 2:
                canvas.create_oval(j*100+5, i*100+5, j*100+100-5, i*100+100-5, fill="red")




######################
# programme principal
######################

# création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, height=H, width=W, bg="blue")
bouton_retour = tk.Button(racine, command=retour_1, text="retour")
bouton_sauvegarde = tk.Button(racine, command=sauvegarde, text="sauvegarde")
bouton_charger = tk.Button(racine, command=charger, text="charger")
label_joueur = tk.Label(racine, text= " puissance 4 ", padx=20, pady=20, borderwidth=5, font = ("helvetica", "20")) 
label_gagnant = tk.Label(racine)

# positionnement des widgets
racine.grid()
canvas.grid(rowspan=10)
bouton_retour.grid(column=1, row=6)
bouton_sauvegarde.grid(column=1, row=7)
bouton_charger.grid(column=1, row = 8)
label_joueur.grid(column=1,row=0)
label_gagnant.grid(column=1, row=3)

# fonctions
creation_grille()
affiche_joueur()


# gestions clic
canvas.bind("<Button-1>", gestion_clic)


# boucle principale
racine.mainloop()