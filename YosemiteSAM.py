#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys,os,re, pprint

os.system("clear")


#Verification de la bonne utilisation de la ligne de commande
if (len(sys.argv) != 2 ) :
    error1  = "Mauvaise utilisation de la commande : " + sys.argv[0] + " fichier.sam"
    print(error1)
    exit()


#Extraction de l'extension du fichier et verification de celle-ci
ext = sys.argv[1].split(".")
extension = ext[len(ext) - 1].lower()


if(extension != "sam") : 
    error2 = sys.argv[1]+ " n'a pas le bonne extension, si vous voulez qu'il soit traité faire : nom_fichier.sam"
    print(error2)
    exit()


fichier = open(sys.argv[1],"r")

stock = {}
paireMapped = []
paireUnmapped = []
pairePartiellement = []
paireUnmappedPartiellement = []
paireMappedUnmapped = []
paireMappedPartiellement = []
UnMapped = []
PartiellementMapped = []
Nondef = []
compteur = 0
cigars = []

#Verication de la bonne ouverture du fichier
for line in fichier:  

    if line.startswith("@"):
        print("Entête du fichier \n", line)

    else :

    	# Récupération des patterns cherchés par une expression régulière qui permet de rechercher le motif prédéfini de facon récursive dans le fichier ouvert.

        patterns = line.split("\t") #section alignement du fichier mapping.sam*

        if patterns: # si les groupes du pattern sont trouvés (séparés par \s) , on les recupère chacun dans une variable
            
            clone = patterns[0]
            flag = int(patterns[1]) # "int" pour convertir le groupe le 2 en type entier
            cigar = patterns[5]
            #On stocke les reads par paire en gardant comme information leurs flag et cigar 
            #De plus un test est fait pour que les premières données soit toujours celle du 1er Read.
            if clone in stock:
            	if flag & 64 == 64 :
            		temp = []
            		temp = stock[clone]
            		stock[clone] = [flag, cigar]
            		stock[clone] += temp
            		compteur += 1
            	else :
            		stock[clone] += [flag, cigar]
            		compteur += 1
            else :
                stock[clone] = [flag, cigar]
                compteur +=1

#Vérifiaction que le read soit un non mappé
            if ( flag & 4 == 4 ) :
            	UnMapped.append(clone)

#Vérification que le read soit partiellement mappé
            #if( cigar != "100M" and cigar != "*" ) :
            #	PartiellementMapped.append(clone)

            elif (("h".lower() in cigar.lower() or ("s".lower() in cigar.lower())) or (flag & 48 == 48) or (flag & 48 == 0)) :
            	PartiellementMapped.append(clone)


#On parcours toutes les valeurs de notre dictionnaire stock pour crée mettre nos paires dans différents catégories
for key, value in stock.items():

	if ( key in UnMapped and key in PartiellementMapped ) :
		paireUnmappedPartiellement.append(key)

	elif key in UnMapped :
		if((value[0] & 4 == 4) and value[2] & 4 == 4 ) :
			paireUnmapped.append(key)
		elif key not in PartiellementMapped :
			paireMappedUnmapped.append(key)

	elif key in PartiellementMapped :
		if ( (("h".lower() in value[1].lower() or ("s".lower() in value[1].lower())) or (value[0] & 48 == 48) or (value[0] & 48 == 0) )  
			and  (("h".lower() in value[3].lower() or ("s".lower() in value[3].lower())) or (value[2] & 48 == 48) or (value[2] & 48 == 0) ) ) :
			pairePartiellement.append(key)
		elif key not in UnMapped :
			paireMappedPartiellement.append(key)

	else : 
		paireMapped.append(key)





#AFFICHAGE GENERAL DU PROGRAMME	

paireTotal = len(paireUnmappedPartiellement) + len(paireUnmapped) + len(paireMappedUnmapped) +len(pairePartiellement) + len(paireMapped) + len(paireMappedPartiellement)

print("Voici les résultats de l'analyse :")
print("Le fichier est composé :")

if compteur > 0 :
	pourcentageunmapped = (len(UnMapped)/compteur)*100
	pourcentagepartiellement = (len(PartiellementMapped)/compteur)*100
	pourcentagemapped = ((compteur-(len(PartiellementMapped) + len(UnMapped)))/compteur)*100


#Affichage de la compostion des Reads
print(str(compteur) + " Reads dont :")
print("---> " +str(len(UnMapped)) + " Reads non mappés")
print("---> " +str(len(PartiellementMapped)) + " Reads partiellement mappés")
print("---> " +str(compteur-(len(PartiellementMapped) + len(UnMapped)) ) + " Reads mappés")

print("\n")


#Affichage des poucentages
print("Les pourcentages correspondants sont :")

print("---> " + str(pourcentageunmapped) + "% de Reads non mappés")
print("---> " + str(pourcentagepartiellement) + "% de Reads partiellement mappés")
print("---> " + str(pourcentagemapped) + "% de Reads mappés")



print("\n")


#Affichage des différents paires de reads
print("Avec ces Reads " + str(paireTotal) + " paires de Reads sont faites dont : " )
print("---> " +str(len(paireUnmapped)) + " paires où les deux reads sont non mappés")
print("---> " +str(len(pairePartiellement)) + " paires où les deux reads sont partiellement mappés")
print("---> " +str(len(paireMapped)) + " paires où les deux reads sont mappés")
print("---> " +str(len(paireMappedPartiellement)) + " paires où un read est mappé et l'autre est partiellement mappé")
print("---> " +str(len(paireMappedUnmapped)) + " paires où un read est mappés et l'autre est non mappé ")
print("---> " +str(len(paireUnmappedPartiellement)) + " paires où un read est partiellement mappé et l'autre est non mappé")



print("\n")



#Demande si l'utilisaiteur veut les données des paires qui seront socket dans des fichiers
print("Afficher les paires de Reads voulues en tapant 1 sinon taper autre choses :")
print("Toutes les données seront stockées dans des fichiers")

x = input()


if x == str(1) :
	print("Vous voici dans le mode affichage des paires de Reads :")
	print("Pour afficher les paires où les deux reads sont non mappés taper 1")
	print("Pour afficher les paires où les deux reads sont partiellement mappés taper 2")
	print("Pour afficher les paires où les deux reads sont mappés taper 3")
	print("Pour afficher les paires où un read est mappé et l'autre est partiellement mappé taper 4")
	print("Pour afficher les paires où un read est mappés et l'autre est non mappé taper 5")
	print("Pour afficher les paires où un read est partiellement mappé et l'autre est non mappé taper 6")
	print("Pour sortir de ce mode taper 7")


	y = input()
	while y != str(7) :
		if(y == str(1)) :
			fichier = open("PairesReadsNonMappés.txt","a")
			fichier.write(str(paireUnmapped))
			fichier.close()
			print("Votre fichier a été crée")
		elif(y == str(2)) :
			fichier = open("PairesReadsPartiellementMappés.txt","a")
			fichier.write(str(pairePartiellement))
			fichier.close()
			print("Votre fichier a été crée")
		elif(y == str(3)) :
			fichier = open("PairesReadsMappés.txt","a")
			fichier.write(str(paireMapped))
			fichier.close()
			print("Votre fichier a été crée")
		elif(y == str(4)) :
			fichier = open("PairesReads1Mappé1Pariellement.txt","a")
			fichier.write(str(paireMappedPartiellement))
			fichier.close()
			print("Votre fichier a été crée")
		elif(y == str(5)) :
			fichier = open("PairesReads1Mappé1Nonmappé.txt","a")
			fichier.write(str(paireMappedUnmapped))
			fichier.close()
			print("Votre fichier a été crée")
		elif(y == str(6)) :
			fichier = open("PairesReads1Partiellement1Nonmappé.txt","a")
			fichier.write(str(paireUnmappedPartiellement))
			fichier.close()
			print("Votre fichier a été crée")
		y = input()

fichier.close()

