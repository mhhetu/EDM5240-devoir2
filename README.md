# EDM5240-devoir2
# Devoir 2

#coding: utf-8

import csv

data = "grants.csv"

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
		# Mais j'essaie de pousser un peu plus loin et de sauvegarder dans un nouveau fichier avec une colonne pour la date:
		filename = 'periodiques.csv'
		with open(filename, 'w') as file_object:
			file_object.write("%s, %s, %s" % (n,ligne[-11][0:4],ligne))
			#J'ai réussi à imprimer une ligne!!!! Ça imprime bizarre, mais je considère ça un succès!



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
