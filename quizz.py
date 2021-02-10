#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys, os, re, random

os.system("clear")

quizz = open("capitales.csv", "r")

pays = list()
capitales = list()
Pays = list()
Capitales = list()

for ligne in quizz.readlines():
    pays.append(ligne.split(",")[0])
    capitales.append(ligne.split(",")[1])

for ligne in pays :
    Pays.append(ligne.split(" (")[0])

for ligne in capitales :
    Capitales.append(ligne.split("\n")[0])

print(pays)
print(capitales)
print(Pays)
print(Capitales)

if int(sys.argv[2])== 1 :
    for i in range(1, int(sys.argv[1])) :
        select_pays = random.randint(0, len(Pays)-1)
        print('Quelle est la capitale de ce pays ? ' + Pays[select_pays])
        reponse = input()
        note = 0
        print(Pays[select_pays])
        if reponse.lower() == Pays[select_pays].lower() :
            print ('Bonne réponse !')
            print(reponse)
            note += 1
        else :
            print('Mauvaise réponse !')
            print(reponse)
            print(Capitales[select_pays])

if int(sys.argv[2]) == 2 :
    for i in range(1, int(sys.argv[1])) :
        select_Capitale = random.randint(0, len(Capitales)-1)
        print('Quel pays a pour capitale ? ' + Capitales[select_Capitale])
        reponse = input()
        note = 0
        if reponse.lower() == Capitales[select_Capitale].lower() :
            print ('Bonne réponse !')
            print(reponse)
            note += 1
        else :
            print('Mauvaise réponse !')
            print(reponse)
            print(Pays[select_Capitale])


##i = 0
#while i < n:
 #   print("Quelle est la capitale de ce pays ?")
  #  select_pays = random.randint(1,len(Pays))
   # print(Pays[select_pays])
    #m = input()
    #print(m)
  #  print(capitales[select_pays])
  #  if m == capitales[select_pays] :
  #      print("Bonne réponse !")
  #  else:
  #      print("Mauvaise réponse !")
  #  i=i+1

print(str(note) + "/" + sys.argv[1])
print(str((note/100)*int(sys.argv[1])) + "% de bonnes réponses")

        


