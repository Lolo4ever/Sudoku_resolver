#!/c/Python/python.exe
# -*-coding:utf-8 -*
from random import *




#prend une ligne aleatoire dans le fichier 'fichier'
#attention: la premiere ligne est une excepetion du fait du \n
def lire_fichier_sudoku(fichier,ligne):
    with open(fichier,'r') as mon_fichier:
        texte=mon_fichier.read()
        nombres = list()
        if ligne==1:
            for i in range(81):
                nombres.append(texte[i])
        else:
            for i in range(82*(ligne-1),82*(ligne-1)+81):
                nombres.append(texte[i])
        return nombres



#saisir dans input la grille sudoku
def saisir_sudoku():   
    try:
        n=input("veuillez mettre 81 chiffres ")
        nombres=int(n)
    except ValueError : #si se n'est pas un int
        print("saisir des CHIFFRES entre 0 et 9...")
    else: 
        if len(n)!=81: #si ce n'est pas la bonne dimension
            raise Exception("pas le bon nombre de chiffres")       
        else:
            return nombres



#transforme une liste de 81 int en une grille sudoku( liste de lsite de int )
def liste_to_grille(nombres):
    grille = [ [int for i in range(9)] for j in range(9) ]
    for ligne in range(9):
        for colonne in range(9):
            grille[ligne][colonne]=int(nombres[ligne*9+colonne])
    return grille



#print la grille comme demandé
def afficher_sudoku(grille):
    print("-------------")
    for ligne in range(9):
        for colonne in range(9):
            #en fonction de la colonne printer '|'
            if colonne == 0:
                print("|"+str(grille[ligne][colonne]),end='')
            elif colonne in (2,5):
                print(str(grille[ligne][colonne])+"|",end='')
            elif colonne == 8:
                print(str(grille[ligne][colonne])+"|")
                if ligne in(2,5,8):
                    print("-------------")
            else:
                print(str(grille[ligne][colonne]),end='')




#teste si une grille est valide, en parcourant toute la grille
#return un boolean (True si valide)
def est_valide(grille):
    res=True

    #si une ligne a plus de une fois le meme chiffre, ou si il y a un 0
    #revoie false
    for ligne in range(9):
        for i in range(1,10):
            if grille[ligne].count(i) != 1 or grille[ligne].count(0) >0:
                res=False
   
    #meme chose mais avec colonne
    #cette fois ci, la liste des chifffres d'une colonne serons sauvegardé dans temp()
    temp=list()       
    for colonne in range(9):
        for ligne in range(9):
            temp.append(grille[ligne][colonne])
        for i in range(1,10):
            if temp.count(i) != 1:
                res=False
        temp=[]

    #pour les zones, en fonction de quelle zone on esst, le range de la boucle for change
    for zone in range(9):
        if(zone in(0,1,2)):
            limite_colonne=3*zone
            limite_ligne=0
        elif(zone in(3,4,5)):
            limite_colonne=3*(zone-3)
            limite_ligne=3
        else:
            limite_colonne=3*(zone-6)
            limite_ligne=6

        for ligne in range(limite_ligne,3+limite_ligne):
            for colonne in range(limite_colonne,3+limite_colonne):
                temp.append(grille[ligne][colonne])
        for i in range(1,10):
            if temp.count(i) != 1:
                res=False
        temp=[]

    return res




#definition qui chercher, pour une case donnée, dans quelle zone elle est
def quelle_zone(ligne,colonne):
    if ligne<3 and colonne<3:
        res=0
    elif ligne<3 and colonne<6:
        res=1
    elif ligne<3 and colonne<9:
        res=2
    elif ligne<6 and colonne<3:
        res=3
    elif ligne<6 and colonne<6:
        res=4
    elif ligne<6 and colonne<9:
        res=5
    elif ligne<9 and colonne<3:
        res=6
    elif ligne<9 and colonne<6:
        res=7
    else:
        res=8
    return res



#M est un tableau 3D qui dit, pour chaque possibilité de numero dans une case,
#si on peut ou pas se mettre
def remplie_M(grille):
    M = [ [ [0 for i in range(9)] for j in range(9)] for k in range(9) ] 
    for ligne in range(9):
        for colonne in range(9):
            k=grille[ligne][colonne]
            if k != 0:
                #d'abord on verifie les colonnes et les lignes et la propres case
                for i in range(9): 
                    M[ligne][i][k-1]=1
                    M[i][colonne][k-1]=1
                    M[ligne][colonne][i]=1
                
                #ensuite on regarde les zones
                zone=quelle_zone(ligne,colonne)
                if(zone in(0,1,2)):
                    limite_colonne=3*zone
                    limite_ligne=0
                elif(zone in(3,4,5)):
                    limite_colonne=3*(zone-3)
                    limite_ligne=3
                else:
                    limite_colonne=3*(zone-6)
                    limite_ligne=6
                for li in range(limite_ligne,3+limite_ligne):
                    for co in range(limite_colonne,3+limite_colonne):
                        M[li][co][k-1]=1
    return M



#resolution de maniere simple de la grille
#si dans M il y a une seule possibilité, on met le chiffre
def remplie_grille(grille):
    while not est_valide(grille):  
        M=remplie_M(grille)
        a_change=False
        for ligne in range(9):
            for colonne in range(9):
                if M[ligne][colonne].count(0)==1:
                    chiffre=M[ligne][colonne].index(0)+1
                    grille[ligne][colonne]=chiffre
                    a_change=True
        #il toure en boucle si la grille n'est pas simple
        #on decide de break si il n'a plus rien a changer
        if not a_change:
            break       
    return grille


#comme la methode copy() marche pas pour une double liste
#on creer nous meme la methode
#on copie la grille case par case
def copier(grille):
    res=[[int for i in range(9)] for j in range(9)]
    for ligne in range(9):
        for colonne in range(9):
            res[ligne][colonne]=grille[ligne][colonne]
    return res

def copier(grille, l):
    res=[[int for i in range(9)] for j in range(9)]
    for colonne in range(9):
        res[l][colonne]=grille[l][colonne]
    return res

def copier(grille,l,c):
    res=[[int for i in range(9)] for j in range(9)]
        res[l][c]=grille[l][c]
    return res



#test si la grille peut etre resolue de maniere simple
#vu que la methode remplie_grille modifie la grille en parametre
#on fait une copie avant
def est_resolvable(a):
    b=copier(a)
    remplie_grille(b)
    res=est_valide(b)
    return res


#methode qui resoud grille meme complexe
#on va parcourir la grille et la ou on a le choix enrte seulement 2 chiffre
#on esseye un et on test est_resolvable
#si non, on enregistre la grille dans une liste 'memoire' (copies()) et on esseye
#le deuxieme chiffre et on continue avec ce deuxieme chiffre
#
#une fois qu'il a parcourue toute les cases et esseyer de mettre des chiffre
#on reapelle la methode avec une grille dans la liste memoire, ainsi de suite
#
#PROBLEME: solution recursive qui prend beaucoup trop de temp, plusieurs minutes meme
#il faudrais chercher une solution non recursive, en utilisant la vrai logique sudoku
copies=list()
res=[[]]
def resoudre(grille,conteur):
#un conteur qui est incrementé a chaque passage de la definition
    global res
    #pour pouvoir return la grille, il faut une variable globale
    if not est_valide(grille):
        grille_copie=copier(grille)
        for ligne in range(9):
            for colonne in range(9):                 
                M=remplie_M(grille_copie)
                if M[ligne][colonne].count(0)==2:
                    chiffre=M[ligne][colonne].index(0)+1
                    grille_copie[ligne][colonne]=chiffre
                    copies.append(copier(grille_copie))
                    if not est_resolvable(grille_copie):
                        chiffre=M[ligne][colonne].index(0,chiffre)+1
                        grille_copie[ligne][colonne]=chiffre
                    if est_resolvable(grille_copie):
                    #si notre grille est resolvable, on est la dedans
                        remplie_grille(grille_copie)
                        res=copier(grille_copie)
                        return res
        conteur +=1
        resoudre(copies[conteur],conteur)
    return res



#prend une grille remplie en parametre et on enleve aléatoirement environ 
# un quart des chiffre
def partielle(grille):
    grille_copie=copier(grille)
    for ligne in range(9):
        for colonne in range(9):
            r=int(random()*4)
            if r==0:
                grille_copie[ligne][colonne]=0
    return grille_copie




if __name__ == "__main__":
    #---------------------interactif-------------------------
    print("bonjour, que souhaitez vous? (tapez le numero correspondant)")
    print("1/ Afficher une grille sudoku")
    print("2/ Resoudre partiellement votre grille")
    print("3/ Resoudre totalement votre grille")
    print("4/ saisir une grille sudoku")
    print("0/ Quitter")
    n='c'
    grille_principale=[[int for i in range(9)]for j in range(9)]
    grille_complete=[[int for i in range(9)]for j in range(9)]
    while n != '0':
        n=input(" :: ")
        if n == '1':
            ligne=int(random()*245 + 1)
            grille_principale=liste_to_grille(lire_fichier_sudoku('sudoku.txt',ligne))
            print("grille numero: "+str(ligne))
            afficher_sudoku(grille_principale)
            grille_complete=resoudre(grille_principale,-1)
        elif n =='2':
            print("grille partielle : ")
            part=partielle(grille_complete)
            afficher_sudoku(part)
        elif n=='3':
            print("grille_complete")
            afficher_sudoku(grille_complete)
        elif n=='4':
            grille_principale=liste_to_grille(saisir_sudoku())
            grille_complete=resoudre(grille_principale,-1)







    




