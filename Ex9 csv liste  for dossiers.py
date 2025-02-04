import os                             # N'enlevez pas ces lignes.
os.chdir(os.path.dirname(__file__))   # Elles permettent de se positionner dans le répertoire de ce script

# Importez csv
import csv

 

# Vous utiliserez encore le fichier "Ex7 Lan Party.csv"
# 
#         Vous voulez créer un dossier par Lan Party
#         Et pour chaque Lan Party, créez des sous-dossier pour chaque jeu
#                   (On y mettra éventuellement la liste des participants du Lan qui veulent jouer à ce jeu)
#         ATTENTION: Pour le nom de chaque jeu: changez le ':' pour un '_' et gardez juste les 20 premiers caractères

#         Si besoin, des instructions détaillées sont données plus bas
os.chdir("csvs")

liste_de_jeu = []

with open("Ex7 Lan Party.csv") as fichier_lu:
    reader = csv.reader(fichier_lu,delimiter=';')
    next(reader)
    for line in reader:
        liste_de_jeu.append(line)
for ligne in liste_de_jeu:
    os.mkdir(ligne[0])
    os.chdir(ligne[0])
    jeux = ligne[1:]
    for jeu in jeux:
        if ':' in jeu:
            jeu = jeu.replace(':','_')
        jeu_final = jeu[:20]
        os.mkdir(jeu_final)
    os.chdir('..')
print("fin")















# INSTRUCTIONS DÉTAILLÉES
#      Commencez par créer une liste des différents jeux vide
#      Ouvrez le fichier 'Ex4 Lan Party.csv' en lecture
#      utilisez csv.reader pour lire le fichier avec le bon delimiter
#      Sautez la première ligne de l'entête
#      Faites une boucle pour passer à travers chacune des lignes 
#      Créez un dossier pour le nom du Lan Party
#      Déplacez vous dans ce dossier
#      Utilisez le slicing pour garder uniquement les 3 jeux
#      Faites une boucle pour passer à travers chacun des jeux
#      Pour le nom de chaque jeu: changez le ':' pour un '_' et gardez juste les 20 premiers caractères
#      Créez un dossier pour le jeu avec le nouveau nom de jeu
#      Revenez au dossier parent

            


