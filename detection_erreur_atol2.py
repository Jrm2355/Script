# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 11:19:40 2017

@author: jyon et Lorita
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 09:13:40 2017

@author: jyon
"""

 ### VARIABLES ###
 
#variable pour stocker la ligne lu via readline
line = ""
#variable qui stocke l'id de la classe étudiée
id_on_process = ""

#Liste des espèces pour contrôler leur présence pour chaque class
especes = ['"SolePresent"^^xsd:string', '"ZebraFishPresent"^^xsd:string', '"CarpPresent"^^xsd:string', '"CattlePresent"^^xsd:string', '"ChickenPresent"^^xsd:string', '"CodPresent"^^xsd:string', '"DuckPresent"^^xsd:string', '"GoatPresent"^^xsd:string', '"GoosePresent"^^xsd:string', '"HorsePresent"^^xsd:string', '"MousePresent"^^xsd:string', '"PigPresent"^^xsd:string', '"QuailPresent"^^xsd:string', '"RabbitPresent"^^xsd:string', '"SalmonPresent"^^xsd:string', '"SeaBassPresent"^^xsd:string', '"SeaBreamPresent"^^xsd:string', '"SheepPresent"^^xsd:string', '"TilapiaPresent"^^xsd:string', '"TroutPresent"^^xsd:string', '"TurkeyPresent"^^xsd:string', '"SoleAbsent"^^xsd:string', '"ZebraFishAbsent"^^xsd:string', '"CarpAbsent"^^xsd:string', '"CattleAbsent"^^xsd:string', '"ChickenAbsent"^^xsd:string', '"CodAbsent"^^xsd:string', '"DuckAbsent"^^xsd:string', '"GoatAbsent"^^xsd:string', '"GooseAbsent"^^xsd:string', '"HorseAbsent"^^xsd:string', '"MouseAbsent"^^xsd:string', '"PigAbsent"^^xsd:string', '"QuailAbsent"^^xsd:string', '"RabbitAbsent"^^xsd:string', '"SalmonAbsent"^^xsd:string', '"SeaBassAbsent"^^xsd:string', '"SeaBreamAbsent"^^xsd:string', '"SheepAbsent"^^xsd:string', '"TilapiaAbsent"^^xsd:string', '"TroutAbsent"^^xsd:string', '"TurkeyAbsent"^^xsd:string']

#Liste pour le contrôle des espèces par class
espece_presente = ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]

#Liste des résultats
id_error = []
espece_error = []



### Fonction

def controle_espece(liste_espece):
    result_list = [] # liste de résultat
    for liste in liste_espece:
        temp_list = [] # liste pour stocker les espèces absentes puis l'ajouter dans result_list
        for espece in liste:
            if "Sol" in espece[1:4]:
                temp_list.append("Sole")
            if "Zeb" in espece[1:4]:
                temp_list.append("Zebrafish")
            if "Car" in espece[1:4]:
                temp_list.append("Carpe")            
            if "Cat" in espece[1:4]:
                temp_list.append("Cattle")            
            if "Chi" in espece[1:4]:
                temp_list.append("Chicken")
            if "Cod" in espece[1:4]:
                temp_list.append("Cod")
            if "Duc" in espece[1:4]:
                temp_list.append("Duck")
            if "Goa" in espece[1:4]:
                temp_list.append("Goat")
            if "Goo" in espece[1:4]:
                temp_list.append("Goose")                
            if "Hor" in espece[1:4]:
                temp_list.append("Horse")                
            if "Mou" in espece[1:4]:
                temp_list.append("Mouse")                
            if "Pig" in espece[1:4]:
                temp_list.append("Pig")
            if "Qua" in espece[1:4]:
                temp_list.append("Quail")
            if "Rab" in espece[1:4]:
                temp_list.append("Rabbit")
            if "Sal" in espece[1:4]:
                temp_list.append("Salmon")
            if "Seabr" in espece[1:6]:
                temp_list.append("Seabass")
            if "Seabr" in espece[1:6]:
                temp_list.append("Seabream")
            if "She" in espece[1:4]:
                temp_list.append("Sheep")
            if "Til" in espece[1:4]:
                temp_list.append("Tilapia")
            if "Tro" in espece[1:4]:
                temp_list.append("Trout")
            if "Tur" in espece[1:4]:
                temp_list.append("Turkey")
        temp_list_result = []
        if "Sole" not in temp_list:
            temp_list_result.append("Sole")
        if "Zebrafish" not in temp_list:
            temp_list_result.append("Zebrafish")
        if "Carp" not in temp_list:
            temp_list_result.append("Carp")                
        if "Cod" not in temp_list:
            temp_list_result.append("Cod")
        if "Salmon" not in temp_list:
            temp_list_result.append("Salmon")
        if "Seabass" not in temp_list:
            temp_list_result.append("Seabass")
        if "Seabream" not in temp_list:
            temp_list_result.append("Seabream")
        if "Tilapia" not in temp_list:
            temp_list_result.append("Tilapia")
        if "Trout" not in temp_list:
            temp_list_result.append("Trout")                              
        if "Cattle" not in temp_list:
            temp_list_result.append("Cattle")               
        if "Goat" not in temp_list:
            temp_list_result.append("Goat")               
        if "Horse" not in temp_list:
            temp_list_result.append("Horse")               
        if "Mousse" not in temp_list:
            temp_list_result.append("Mousse")
        if "Pig" not in temp_list:
            temp_list_result.append("Pig")
        if "Rabbit" not in temp_list:
            temp_list_result.append("Rabbit")
        if "Sheep" not in temp_list:
            temp_list_result.append("Sheep")
        if "Chicken" not in temp_list:
            temp_list_result.append("Chicken")                
        if "Duck" not in temp_list:
            temp_list_result.append("Duck")                
        if "Goose" not in temp_list:
            temp_list_result.append("Goose")                
        if "Quail" not in temp_list:
            temp_list_result.append("Quail")                
        if "Turkey" not in temp_list:
            temp_list_result.append("Turkey")
        result_list.append(temp_list_result)   
    return result_list
   
             
### MAIN

#lecture du fichier texte
with open ("C:/Users/jyon/Documents/Ontology/ahol/atol_turtle_v2.owl", "r", encoding='utf-8') as aholFile:
    
#Boucle pour lire le fichier, arrêt = dernière ligne
    while line != "###  Generated by the OWL API (version 4.2.6.20160910-2108) https://github.com/owlcs/owlapi":
        
#méthode pour lire la ligne puis la découpé en fonction des espaces
        line =  aholFile.readline() 
        line_split = line.split(" ")

#passe les lignes de structures du fichiers qui n'ont qu'un élément        
        if len(line_split) == 1:
            continue
        
#identifie s'il s'agit du début d'une classe, si OUI note son URI dans id_on_process     
        if line_split[2][:23] == 'http://opendata.inra.fr':
            
#vérification que toutes les especes sont renseignées pour l'id en cours               
            if len(espece_presente) != 21:
                id_error.append(id_on_process)   
                espece_error.append(espece_presente)
                
            id_on_process = line_split[2]
            espece_presente = []  #initialisation de la liste utilisée pour le controle des especes présentes 
        
#vérifie la présence des informations Present/Absent pour la classe en cours
        for espece in especes :
            if espece in line_split:
                espece_presente.append(espece)

#resultat pour le dernier id comme on est dans la boucle quand il sort, il n'écrit pas ses résultats                
if len(espece_presente) != 21:
   id_error.append(id_on_process)   
   espece_error.append(espece_presente)                

espece_error2 = controle_espece(espece_error)
   
with open ("C:/Users/jyon/Documents/travail/script/resultat_erreur_atol.txt", "w", encoding='utf-8') as result_file:
    i = 0
    while i < len(id_error) :
        result_file.write("\n"+str(id_error[i]))
        result_file.write("espèces non renseignées : "+str(espece_error2[i])+"\n")
        i += 1        
