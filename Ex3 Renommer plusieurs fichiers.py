# importez os
# # allez dans le dossier Ex3 Videos
# # avec la boucle for, passez à travers chacun des dossiers de os.listdir()
# #     utilisez os.path.splitext pour obtenir le filename et l'extension
# #     utilisez split sur le filename pour obtenir le titre, le cours et le numéro du cours
# #     utilisez strip pour enlever les espaces qui pourraient rester pour le titre et le numéro
# #     en plus utilisez zfill pour remplir le numéro de sorte que 1 deviendra 01
# #     recréez le nouveau nom de fichier#   utliser os.rename pour renommer le fichier
import os

os.chdir('C:\\Users\\2157216\\Downloads\\R03 Exercices Depart V3\\Ex3 Videos')
nom_final = []

for fichier in os.listdir():
    nom = os.path.splitext(fichier)
    nom_separe = nom[0].split('_')
    for info in nom_separe:
        info_strip = info.strip()
        nom_final.append(info_strip)
    print('mp4')