# EDM5240-devoir2
# Devoir 2

### BONJOUR, ICI JHR ###
### Mes notes et corrections sont encore précédées de trois dièses ###

#coding: utf-8

import csv

### Ci-dessous, je modifie simplement le nom du fichier pour faire rouler ton code sur mon ordi

data = "../grants.csv"
fichier2 = 'periodiques-JHR.csv'

### Très bonne solution: en effet, l'encodage des caractères est souvent source de problèmes...

ouvrir = open(data, 'r', encoding='latin-1') # Permet d'ouvrir le document grants.csv malgré le problème.
lignes = csv.reader(ouvrir)
next(lignes)

#print(lignes)

n = 0

for ligne in lignes:
	#n += 1
	if "riodiques" in ligne[-7]:
		n += 1
		print(ligne[-11][0:4],ligne,n)
		# Écrit l'année, la ligne et le numéro de ligne. Donc, devoir réglé!

### En effet!
### Excellent d'avoir tenté d'écrire un nouveau fichier avec tes résultats

### Tu y étais presque!
### Deux choses à changer

### 1. Changer le mode d'écriture de «'w'» à «'a'»
### Le mode «w» signifie «overwrite»; ça écrit une ligne, puis ça écrase la ligne précédente, ce qui fait qu'il ne reste que la dernière ligne à la fin
### Le mode «a» signifie «append»; ça ajoute chaque nouvelle ligne à ce que tu as écrit jusqu'à maintenant

		# Mais j'essaie de pousser un peu plus loin et de sauvegarder dans un nouveau fichier avec une colonne pour la date:
		filename = 'periodiques.csv'
		with open(filename, 'w') as file_object:
			file_object.write("%s, %s, %s" % (n,ligne[-11][0:4],ligne))
			#J'ai réussi à imprimer une ligne!!!! Ça imprime bizarre, mais je considère ça un succès!

### 2. La méthode que tu utilises écrit une longue ligne à la queue leu leu
### Comme on utilise «csv» pour lire un CSV, on peut utiliser «csv» pour écrire un CSV, où chaque ligne va être distincte
### Voici le code dont je me sers toujours:

		### variable_temporaire_1 = open(fichier2,"a")
		### variable_temporaire_2 = csv.writer(variable_temporaire_1)
		### variable_temporaire_2.writerow(ligne)

### Mais pour avoir tenté d'écrire un fichier, donc pour être allée plus loin que ce que le devoir vous demandait de faire, et ce, même si tu as remis ton script dans le «README»: un A+!

#---------------------------------------------------------------------------------
#Essais de solution au problème de lecture du document grants.csv: 

    	#try: 
		#print(ligne)
		#print(n)
	#except UnicodeDecodeError:
		#print("Boom boom shebang!")
"""try:
    file = open("exampleFileName", "r")
except UnicodeDecodeError:
    try:
        file = open("exampleFileName", "r", encoding="latin2")
    except: #..."""
#source: https://stackoverflow.com/questions/7935972/writing-to-a-new-directory-in-python-without-changing-directory
#---------------------------------------------------------------------------------


#---------------------------------------------------------------------------------
#Essais manqués d'écriture dans un autre fichier:

"""import StringIO
s = StringIO.StringIO(text)
with open('periodiques.csv', 'w') as f:
    try:
    	from StringIO import StringIO
    except ImportError:
    	from io import StringIO
    for line in s:
    	f.write(line)
"""

"""filename = 'periodiques.csv'
with open(filename, 'w') as file_object:
	file_object.write(ligne[-11][0:4],ligne,n)"""
		#for date in ligne:
			#print(ligne[-11])
	#for x in ligne:
		#if "riodiques" in x:
			#print(ligne)

"""dir_path = os.path.join(self.feed, self.address)  #will return 'feed/address'
os.makedirs(dir_path)                             #create directory [current_path]/feed/address
output = open(os.path.join(dir_path, file_name), 'wb')"""

#Nom du fichier: periodiques.csv

#source: file:///C:/Users/Marie/Downloads/beginners_python_cheat_sheet_pcc_all.pdf
"""filename = 'periodiques.csv'
with open(filename, 'w') as file_object:
 file_object.write("I love programming.")"""
 #Ça, ça a marché, mais seulement pour un string de texte. Je ne peux pas écrire plusieurs éléments.
 
#Source: https://stackoverflow.com/questions/36003630/write-a-python-3-list-to-csv
"""for row_index, list in enumerate(buffer):
    for column_index, string in enumerate(list):
        buffer[row_index][column_index] = buffer[row_index][column_index]

with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(buffer)
"""
#-----------------------------------------------------------------------------------------
