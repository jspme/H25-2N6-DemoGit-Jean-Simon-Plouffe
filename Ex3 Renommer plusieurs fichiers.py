# importez os
# # allez dans le dossier Ex3 Videos
# # avec la boucle for, passez à travers chacun des dossiers de os.listdir()
# #     utilisez os.path.splitext pour obtenir le filename et l'extension
# #     utilisez split sur le filename pour obtenir le titre, le cours et le numéro du cours
# #     utilisez strip pour enlever les espaces qui pourraient rester pour le titre et le numéro
# #     en plus utilisez zfill pour remplir le numéro de sorte que 1 deviendra 01
# #     recréez le nouveau nom de fichier#   utliser os.rename pour renommer le fichier
import os

os.chdir(os.path.dirname(__file__)) 
os.chdir("Ex3 Videos")

for fichier in os.listdir():
    nom = os.path.splitext(fichier)
    nom_separe = nom[0].split('_')
    nom_separe[0] = nom_separe[0].strip()
    nom_separe[2] = nom_separe[2].strip()
    nom_separe[2] = nom_separe[2].strip('#')
    nom_separe[2] = nom_separe[2].zfill(2)
    nom_final = nom_separe[0] + nom_separe[1] + nom_separe[2] + '.mp4'
    os.rename(fichier,nom_final)